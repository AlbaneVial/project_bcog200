class Player:
    """Represents a player in the Evolution of trust simulation with a personality."""

    def __init__(self, personality, score=300, x=0, y=0):
        self.personality = personality
        self.score = score
        self.history = []
        self.x = x
        self.y = y

    def play(self, history):
        """Decide next move based on own personality and opponent history."""
        if self.personality == "cheater":
            return "cheat"
        if self.personality == "grudger":
            return "cheat" if "cheat" in history else "cooperate"
        if self.personality == "tit_for_tat":
            return "cheat" if history and history[-1] == "cheat" else "cooperate"
        if self.personality == "cooperator":
            return "cooperate"


def play_round(
    player1, player2, nb_round, reward_cooperate, reward_cheat, reward_cheated
):
    """Conduct a series of rounds between two players."""
    for _ in range(nb_round):
        turn(player1, player2, reward_cooperate, reward_cheat, reward_cheated)
    player1.history = []
    player2.history = []


def turn(player1, player2, reward_cooperate, reward_cheat, reward_cheated):
    """Execute a single turn: both players choose actions and update scores."""
    strategy1 = player1.play(player1.history)
    strategy2 = player2.play(player2.history)
    player1.history.append(strategy2)
    player2.history.append(strategy1)

    if strategy1 == "cooperate" and strategy2 == "cooperate":
        player1.score += reward_cooperate
        player2.score += reward_cooperate
    elif strategy1 == "cooperate" and strategy2 == "cheat":
        player1.score -= reward_cheated
        player2.score += reward_cheat
    elif strategy1 == "cheat" and strategy2 == "cooperate":
        player1.score += reward_cheat
        player2.score -= reward_cheated
