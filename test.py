import tkinter as tk
from tkinter import messagebox
import numpy as np


class Display:
    def __init__(self):
        self.screen_size = [900, 600]
        self.root = tk.Tk()
        self.init_window()
        self.create_interface_frame()

    def init_window(self):
        self.root.title("THE EVOLUTION OF TRUST")
        self.root.geometry(f"{self.screen_size[0]}x{self.screen_size[1]}")

        self.play_frame = tk.Frame(self.root, height=self.screen_size[1], width=200)
        self.play_frame.grid(row=0, column=1)

        self.interface_frame = tk.Frame(
            self.root, height=100, width=self.screen_size[0] - 200
        )
        self.interface_frame.grid(row=0, column=0)

    def create_interface_frame(self):

        tk.Label(self.interface_frame, text="nb_tit_for_tat").grid(row=0)
        tk.Label(self.interface_frame, text="nb_cheater").grid(row=1)
        tk.Label(self.interface_frame, text="nb_gudger").grid(row=2)
        tk.Label(self.interface_frame, text="nb_cooporate").grid(row=3)
        tk.Label(self.interface_frame, text="nb_match").grid(row=4)
        tk.Label(self.interface_frame, text="reward_cooperate").grid(row=5)
        tk.Label(self.interface_frame, text="reward_cheat").grid(row=6)
        tk.Label(self.interface_frame, text="reward_cheated").grid(row=7)

        self.nb_tit_for_tat_entry = tk.Entry(self.interface_frame, bg="white")
        self.nb_tit_for_tat_entry.grid(row=0, column=1)
        self.nb_tit_for_tat_entry.insert(0, "2")

        self.nb_cheater_entry = tk.Entry(self.interface_frame, bg="white")
        self.nb_cheater_entry.grid(row=1, column=1)
        self.nb_cheater_entry.insert(0, "2")

        self.nb_gudger_entry = tk.Entry(self.interface_frame, bg="white")
        self.nb_gudger_entry.grid(row=2, column=1)
        self.nb_gudger_entry.insert(0, "2")

        self.nb_cooporate_entry = tk.Entry(self.interface_frame, bg="white")
        self.nb_cooporate_entry.grid(row=3, column=1)
        self.nb_cooporate_entry.insert(0, "2")

        self.nb_match_entry = tk.Entry(self.interface_frame, bg="white")
        self.nb_match_entry.grid(row=4, column=1)
        self.nb_match_entry.insert(0, "5")

        self.reward_cooperate_entry = tk.Entry(self.interface_frame, bg="white")
        self.reward_cooperate_entry.grid(row=5, column=1)
        self.reward_cooperate_entry.insert(0, "3")

        self.reward_cheat_entry = tk.Entry(self.interface_frame, bg="white")
        self.reward_cheat_entry.grid(row=6, column=1)
        self.reward_cheat_entry.insert(0, "6")

        self.reward_cheated_entry = tk.Entry(self.interface_frame, bg="white")
        self.reward_cheated_entry.grid(row=7, column=1)
        self.reward_cheated_entry.insert(0, "0")

        self.entry = [
            self.nb_tit_for_tat_entry,
            self.nb_cheater_entry,
            self.nb_gudger_entry,
            self.nb_cooporate_entry,
            self.nb_match_entry,
            self.reward_cooperate_entry,
            self.reward_cheat_entry,
            self.reward_cheated_entry,
        ]

        self.entry_num_button = tk.Button(
            self.interface_frame,
            text="Show the character",
            command=self.create_circle_of_characters,
        )
        self.entry_num_button.grid(row=8, column=0)

        self.start_step_by_step = tk.Button(
            self.interface_frame,
            text="start_step_by_step",
            command=self.play_match,
        )
        self.start_step_by_step.grid(row=9, column=0)

    def create_circle_of_characters(self):
        self.canvas_width = self.screen_size[0] - 200
        self.canvas_height = self.screen_size[1]
        self.canvas = tk.Canvas(
            self.play_frame,
            width=self.canvas_width,
            height=self.canvas_height,
            bg="white",
        )
        self.canvas.grid(row=0, column=0)

        try:
            values = [int(entry.get()) for entry in self.entry]
            (
                self.nb_tit_for_tat,
                self.nb_cheater,
                self.nb_gudger,
                self.nb_cooporate,
                self.nb_match,
                self.reward_cooperate,
                self.reward_cheat,
                self.reward_cheated,
            ) = values
        except ValueError:
            messagebox.showinfo("Error", "Please enter valid numbers for all fields.")
            return

        self.players = (
            [Player("tit_for_tat", "blue") for _ in range(self.nb_tit_for_tat)]
            + [Player("cheater", "red") for _ in range(self.nb_cheater)]
            + [Player("gudger", "yellow") for _ in range(self.nb_gudger)]
            + [Player("cooperator", "green") for _ in range(self.nb_cooporate)]
        )

        self.total_characters = len(self.players)
        if self.total_characters == 0:
            messagebox.showinfo("Error", "No characters to display.")
            return
        self.update_canvas()

    def play_match(self):

        for i in range(self.total_characters):
            print(
                f"score of player before {self.players[i].personality}: {self.players[i].score}"
            )
            for j in range(i + 1, self.total_characters):

                play_round(
                    self.players[i],
                    self.players[j],
                    self.nb_match,
                    self.reward_cooperate,
                    self.reward_cheat,
                    self.reward_cheated,
                )
            print(
                f"score of player {self.players[i].personality}: {self.players[i].score}"
            )
        self.update_canvas()
        self.remove_and_replace_players()
        print("hello")

    def remove_and_replace_players(self):
        self.players.sort(key=lambda player: player.score)

        best_player = max(self.players, key=lambda player: player.score)

        self.players = self.players[1:]
        self.players.append(
            Player(
                personality=best_player.personality,
                color=best_player.color,
                score=best_player.score,
            )
        )
        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        total_characters = len(self.players)
        angle = np.linspace(0, 2 * np.pi, total_characters, endpoint=False)
        rayon = min(self.canvas_width, self.canvas_height) // 2 - 50
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2

        for index, player in enumerate(self.players):
            x = center_x + rayon * np.cos(angle[index])
            y = center_y + rayon * np.sin(angle[index])
            player.x = x
            player.y = y

            self.canvas.create_oval(
                x - 20, y - 20, x + 20, y + 20, fill=player.color, outline="black"
            )
            self.canvas.create_text(
                x, y, text=player.personality[0], font=("Arial", 10), fill="black"
            )
            self.canvas.create_text(
                x,
                y + 25,
                text=f"Score: {player.score}",
                font=("Arial", 10),
                fill="black",
            )


class Player:
    def __init__(self, personality, color, score=300, x=0, y=0):
        self.personality = personality
        self.color = color
        self.score = score
        self.x = x
        self.y = y

    def play(self, history):
        if self.personality == "cheater":
            return "cheat"
        if self.personality == "gudger":
            return "cheat" if "cheat" in history else "cooperate"
        if self.personality == "tit_for_tat":
            return "cheat" if "cheat" in history[:-1] else "cooperate"
        if self.personality == "cooperator":
            return "cooperate"


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
        print(
            f"    après {i}ieme round entre {player1.personality} (score: {player1.score}) et {player2.personality} (score: {player2.score})"
        )


def main():
    my_display = Display()
    my_display.root.mainloop()


if __name__ == "__main__":
    main()
