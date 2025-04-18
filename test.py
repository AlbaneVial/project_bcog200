import pytest
from player import Player, play_round, turn
from trustapp import TrustApp, MainPlayPanel


def test_player_behaviors():
    cooperator = Player("cooperator")
    cheater = Player("cheater")
    grudger = Player("grudger")
    tit_for_tat = Player("tit_for_tat")

    assert cooperator.play([]) == "cooperate"
    assert cooperator.play(["cheat", "cooperate"]) == "cooperate"

    assert cheater.play([]) == "cheat"
    assert cheater.play(["cooperate"]) == "cheat"

    assert grudger.play([]) == "cooperate"
    assert grudger.play(["cooperate", "cheat"]) == "cheat"

    assert tit_for_tat.play([]) == "cooperate"
    assert tit_for_tat.play(["cheat", "cooperate"]) == "cooperate"
    assert tit_for_tat.play(["cheat"]) == "cheat"
    assert tit_for_tat.play(["cooperate", "cheat"]) == "cheat"


def test_turn_rewards():
    p1 = Player("cooperator", score=0)
    p2 = Player("cooperator", score=0)
    turn(p1, p2, reward_cooperate=2, reward_cheat=3, reward_cheated=1)
    assert p1.score == 2
    assert p2.score == 2

    p1 = Player("cooperator", score=0)
    p2 = Player("cheater", score=0)
    turn(p1, p2, reward_cooperate=2, reward_cheat=3, reward_cheated=1)
    assert p1.score == -1
    assert p2.score == 3

    p1 = Player("cheater", score=0)
    p2 = Player("cheater", score=0)
    turn(p1, p2, reward_cooperate=2, reward_cheat=3, reward_cheated=1)
    assert p1.score == 0
    assert p2.score == 0


def test_play_round_resets_history():
    p1 = Player("tit_for_tat")
    p2 = Player("cheater")
    play_round(p1, p2, nb_round=3, reward_cooperate=2, reward_cheat=3, reward_cheated=1)
    assert p1.history == []
    assert p2.history == []


def test_remove_and_replace_players(monkeypatch):
    app = TrustApp()

    test = MainPlayPanel(
        app.root,
        app.images,
        app.personnality,
        app.screen_size,
    )

    test.players = [
        Player("cooperator", score=5),
        Player("cheater", score=10),
        Player("tit_for_tat", score=15),
    ]

    # On empêche l'appel à update_canvas (Tkinter GUI)
    test.show_players = lambda: None

    test.remove_and_replace_players()

    personalities = [p.personality for p in test.players]
    scores = [p.score for p in test.players]

    assert len(test.players) == 3
    assert personalities.count("tit_for_tat") == 2  # Le meilleur a été cloné
    assert all(score > 5 for score in scores)  # Le plus faible a été retiré
