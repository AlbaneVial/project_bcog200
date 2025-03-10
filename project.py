import tkinter as tk
import sys


class player:
    def __init__(self, personality, color, score=300):
        self.personality = personality
        self.color = color
        self.score = score

    def play(self, history):
        if self.personality == "cheater":
            return "cheat"
        if self.personality == "gudger":
            if "cheat" in history:
                return "cheat"
            else:
                return "cooperate"
        if self.personality == "tit_for_tat":
            if "cheat" in history[:-1]:
                return "cheat"
            else:
                return "cooperate"
        if self.personality == "cooperator":
            return "cooperate"


class canvas:
    def __init__(self, nb_tit_for_tat=4, nb_cheater=4, nb_gudger=4, nb_cooporate=4):
        """show the canvas and update the canva"""
        pass


def enter_number():
    nb_tit_for_tat = input("nb_tit_for_tat: ")
    nb_cheater = input("nb_cheater: ")
    nb_gudger = input("nb_gudger: ")
    nb_cooperator = input("nb_cooperator: ")

    nb_match = input("nb_match: ")

    reward_cooperate = input("reward_cooperate: ")
    reward_cheat = input("reward_cheat: ")
    reward_cheated = input("reward_cheated:  -")
    return (
        nb_tit_for_tat,
        nb_cheater,
        nb_gudger,
        nb_cooperator,
        nb_match,
        reward_cooperate,
        reward_cheat,
        reward_cheated,
    )


def verification(
    nb_tit_for_tat,
    nb_cheater,
    nb_gudger,
    nb_cooporate,
    nb_match,
    reward_cooperate,
    reward_cheat,
    reward_cheated,
):
    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if (
        nb_tit_for_tat in number
        or nb_cheater in number
        or nb_gudger in number
        or nb_cooporate in number
        or nb_match in number
        or reward_cooperate in number
        or reward_cheat in number
        or reward_cheated in number
    ):
        print("____PLEASE ENTER NUMBERS_____")
        enter_number()
        sys.exit()
    return (
        int(nb_tit_for_tat),
        int(nb_cheater),
        int(nb_gudger),
        int(nb_cooporate),
        int(nb_match),
        int(reward_cooperate),
        int(reward_cheat),
        int(reward_cheated),
    )


def play_round(
    player1, player2, nb_match, reward_cheat, reward_cooperate, reward_cheated
):
    history1 = []
    history2 = []

    for i in range(nb_match):
        strategy1 = player1.play(history1)
        strategy2 = player2.play(history2)
        history1.append(strategy2)
        history2.append(strategy1)
        if strategy1 == "cooperate" and strategy2 == "cooperate":
            player1.score += reward_cooperate
            player2.score += reward_cooperate
        elif strategy1 == "cooperate" and strategy2 == "cheat":
            player1.score -= reward_cheated
            player2.score += reward_cheat
        elif strategy1 == "cheat" and strategy2 == "cooperate":
            player1.score += reward_cheat
            player2.score -= reward_cheated

        """print(
            f"Score of {player1.personality}: {player1.score}, Score of {player2.personality}: {player2.score}"
        )"""


def main():
    (
        nb_tit_for_tat,
        nb_cheater,
        nb_gudger,
        nb_cooperator,
        nb_match,
        reward_cooperate,
        reward_cheat,
        reward_cheated,
    ) = enter_number()
    (
        nb_tit_for_tat,
        nb_cheater,
        nb_gudger,
        nb_cooperator,
        nb_match,
        reward_cooperate,
        reward_cheat,
        reward_cheated,
    ) = verification(
        nb_tit_for_tat,
        nb_cheater,
        nb_gudger,
        nb_cooperator,
        nb_match,
        reward_cooperate,
        reward_cheat,
        reward_cheated,
    )
    list_tit_for_tat = [player("tit_for_tat", "red") for _ in range(nb_tit_for_tat)]
    list_cheater = [player("cheater", "blue") for _ in range(nb_cheater)]
    list_gudger = [player("gudger", "green") for _ in range(nb_gudger)]
    list_cooperator = [player("cooperator", "yellow") for _ in range(nb_cooperator)]

    total_player = nb_tit_for_tat + nb_cooperator + nb_gudger + nb_cheater
    all_players = list_tit_for_tat + list_cheater + list_gudger + list_cooperator

    while (
        nb_tit_for_tat != total_player
        or nb_cheater != total_player
        or nb_gudger != total_player
        or nb_cooperator != total_player
    ):
        for i in range(len(all_players)):
            for j in range(i + 1, len(all_players)):
                play_round(
                    all_players[i],
                    all_players[j],
                    nb_match,
                    reward_cooperate,
                    reward_cheat,
                    reward_cheated,
                )
            print(
                f"score of players {all_players[i].personality}: {all_players[i].score } "
            )

        continue_playing = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_playing != "yes":
            break


if __name__ == "__main__":
    main()
