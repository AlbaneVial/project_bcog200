import tkinter as tk
from tkinter import messagebox
import numpy as np
import os
import sys
from player import Player, play_round, turn


class TrustApp:
    def __init__(self):
        self.personnality = ["tit_for_tat", "cheater", "grudger", "cooperator"]
        self.screen_size = [1500, 1000]

        self.root = tk.Tk()
        self.root.configure(bg="white")
        self.current = None

        self.load_images()
        self.init_window()
        self.create_panels()
        self.show_panel("intro")

    def load_images(self):
        self.images = {}
        image_files = {
            "grudger": "grudger.gif",
            "cooperator": "cooporate.gif",
            "cheater": "cheater.gif",
            "tit_for_tat": "tit_for_tat.gif",
        }

        for key, filename in image_files.items():
            if not os.path.exists(filename):
                messagebox.showerror(
                    "Missing File",
                    f"Unable to load image '{filename}'.\n"
                    "Please ensure the file is present in the application directory.",
                )
                sys.exit(1)
            self.images[key] = tk.PhotoImage(file=filename)

    def init_window(self):
        self.root.title("THE EVOLUTION OF TRUST")
        self.root.geometry(f"{self.screen_size[0]}x{self.screen_size[1]}")

    def create_panels(self):
        self.panels = {}

        # i use chatgpt to fix how use method in other class, this my conversation with chatgpt:

        # self.panels["intro"] = IntroPanel(
        #     self.root,
        #     self.images,
        #     self.personnality,
        #     start_callback=self.show_panel("bot0"),
        # )
        # why this doesn't work? how to use method in other class?

        # answer from chatgpt:
        # You need to pass a function without calling it immediately. Use a lambda or a function reference like this:
        # 💡 Why this matters
        # In Python, self.show_panel("bot0") calls the function and returns its result (which is probably None), while lambda: self.show_panel("bot0") creates a function that you can call later.

        self.panels["intro"] = IntroPanel(
            self.root,
            self.images,
            self.personnality,
            start_callback=lambda: self.show_panel("bot0"),
        )

        for i, personnality_bot in enumerate(self.personnality):
            self.panels[f"bot{i}"] = BotMatchPanel(
                self.root,
                self.images,
                index=i,
                personality_bot=personnality_bot,
                next_bot_callback=lambda i=i: self.next_bot(i),
                skip_demo_callback=lambda: self.show_panel("topo"),
            )

        self.panels["topo"] = TopoPanel(
            self.root,
            self.images,
            self.personnality,
            start_callback=lambda: self.show_panel("mainplay"),
        )

        self.panels["mainplay"] = MainPlayPanel(
            self.root,
            self.images,
            self.personnality,
            self.screen_size,
        )

    def show_panel(self, name):
        if self.current is not None:
            self.current.pack_forget()
        self.current = self.panels[name]
        self.current.pack()

    def next_bot(self, i):
        i += 1
        if i < 4:
            self.show_panel(f"bot{i}")
        else:
            self.show_panel("topo")

    def run(self):
        self.root.mainloop()


class IntroPanel(tk.Frame):
    def __init__(self, root, images, personnality, start_callback):
        super().__init__(root, bg="white")
        self.images = images
        self.personnality = personnality
        self.start_callback = start_callback
        self.build()

    def build(self):
        tk.Label(
            self,
            text="Welcome to the game 'The Evolution of Trust'!",
            font=("Arial", 20),
            justify="center",
        ).grid(row=0, column=0, columnspan=4, pady=10)

        tk.Label(
            self,
            text="This game is inspired by the famous Prisoner's Dilemma.",
            font=("Arial", 15),
            justify="center",
        ).grid(row=1, column=0, columnspan=4, pady=5)

        tk.Label(
            self,
            text="In each round, you and another type of player must each choose to either COOPERATE or CHEAT.\n"
            "Your choices determine how many points each of you will receive.\n"
            "You will play against different players with different strategies.",
            font=("Arial", 15),
            justify="center",
        ).grid(row=2, column=0, columnspan=4, pady=5)

        for idx, player in enumerate(self.personnality):
            img = self.images[player]
            lbl = tk.Label(self, image=img)
            lbl.image = img
            lbl.grid(row=3, column=idx, padx=10, pady=10)

        tk.Button(
            self,
            text="Let's start the game!",
            font=("Arial", 20),
            command=self.start_callback,
        ).grid(row=4, column=1, columnspan=2, pady=20)


class BotMatchPanel(tk.Frame):
    def __init__(
        self,
        root,
        images,
        index,
        personality_bot,
        next_bot_callback,
        skip_demo_callback,
    ):
        super().__init__(root, bg="white")
        self.images = images
        self.index = index
        self.personality_bot = personality_bot
        self.next_bot_callback = next_bot_callback
        self.skip_demo_callback = skip_demo_callback
        self.bot = Player(personality_bot, score=10)
        self.user = Player("cooperator", score=10)
        self.round = 0

        self.play_frame = tk.Frame(self, bg="white")

        self.play_frame.pack()

        self.build()

    def build(self):
        tk.Label(
            self.play_frame,
            text=f"Match vs Bot n°{self.index +1} of 4",
            font=("Arial", 20),
            justify="center",
        ).grid(row=0, column=0, columnspan=4, pady=10)

        tk.Label(
            self.play_frame,
            text="Choose your strategy: Cheat or cooperate?",
            font=("Arial", 20),
            justify="center",
        ).grid(row=2, column=0, columnspan=4, pady=10)

        image_player = tk.PhotoImage(file="player.gif")
        image_label = tk.Label(self.play_frame, image=image_player)
        image_label.image = image_player
        image_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        bot_image = self.images[self.personality_bot]
        image_label = tk.Label(self.play_frame, image=bot_image)
        image_label.image = bot_image
        image_label.grid(row=4, column=3, padx=10, pady=10)

        tk.Button(
            self.play_frame,
            text="SKIP THE MATCHES!",
            command=self.skip_demo_callback,
        ).grid(row=8, column=3, columnspan=2)

        tk.Button(
            self.play_frame,
            text="Meet the next player!",
            command=lambda: self.next_bot_callback(),
        ).grid(row=8, column=1, columnspan=2)

        tk.Button(
            self.play_frame,
            text="COOPERATE",
            bg="green",
            command=lambda: self.handle_user_choice("cooperator"),
        ).grid(row=6, column=0)

        tk.Button(
            self.play_frame,
            text="CHEAT",
            bg="red",
            command=lambda: self.handle_user_choice("cheater"),
        ).grid(row=6, column=1)

        self.update_scores()

    def update_scores(self):
        tk.Label(
            self.play_frame,
            text=f"Round n°{self.round } of 5",
            font=("Arial", 20),
            justify="center",
        ).grid(row=1, column=0, columnspan=4, pady=10)

        tk.Label(self.play_frame, text=f"You: {self.user.score}", bg="white").grid(
            row=3,
            column=0,
            columnspan=2,
        )
        tk.Label(self.play_frame, text=f"Bot: {self.bot.score}", bg="white").grid(
            row=3,
            column=3,
            columnspan=2,
        )

    def handle_user_choice(self, user_choice):
        self.user.personality = user_choice
        turn(self.bot, self.user, 2, 3, 1)

        for widget in self.play_frame.grid_slaves():
            info = widget.grid_info()
            if info["row"] == 4 and info["column"] in [1, 2]:
                widget.destroy()

        tk.Label(self.play_frame, text=self.bot.history[-1], bg="white").grid(
            row=4, column=1
        )
        tk.Label(self.play_frame, text=self.user.history[-1], bg="white").grid(
            row=4, column=2
        )
        self.round += 1
        if self.round == 5:
            self.explication_show()

        self.update_scores()

    def explication_show(self):

        for widget in self.play_frame.grid_slaves(row=6 or 7):
            widget.destroy()

        if self.bot.personality == "tit_for_tat":
            tk.Label(
                self.play_frame,
                text="This player copies your last move. Fair and balanced — but don’t betray them!",
                bg="white",
                font=("Arial", 15),
            ).grid(row=7, column=0, columnspan=4, pady=10)

        elif self.bot.personality == "cheater":
            tk.Label(
                self.play_frame,
                text="This player seems to always cheat... Trust is not in their vocabulary!",
                bg="white",
                font=("Arial", 15),
            ).grid(row=7, column=0, columnspan=4, pady=10)

        elif self.bot.personality == "grudger":
            tk.Label(
                self.play_frame,
                text="This player holds grudges! One betrayal and they never forgive.",
                bg="white",
                font=("Arial", 15),
            ).grid(row=7, column=0, columnspan=4, pady=10)

        elif self.bot.personality == "cooperator":
            tk.Label(
                self.play_frame,
                text="This player always cooperates. Too pure for this world...",
                bg="white",
                font=("Arial", 15),
            ).grid(row=7, column=0, columnspan=4, pady=10)
            for widget in self.play_frame.grid_slaves():
                info = widget.grid_info()
                if int(info["row"]) == 8 and int(info["column"]) == 1:
                    widget.destroy()


class TopoPanel(tk.Frame):
    def __init__(self, root, images, personnality, start_callback):
        super().__init__(root)
        self.images = images
        self.personnality = personnality
        self.start_callback = start_callback
        self.build()

    def build(self):
        tk.Label(self, text="Who are the players?", font=("Arial", 24), pady=20).pack()

        descriptions = {
            "cheater": "Always cheats. Doesn't care about trust or cooperation.",
            "cooperator": "Always cooperates. Believes in the goodness of others.",
            "grudger": "Cooperates until betrayed once... then never again!",
            "tit_for_tat": "Starts by cooperating, then mimics your last move. Fair, but not naive.",
        }

        for strat in self.personnality:
            player_frame = tk.Frame(self, pady=10)
            player_frame.pack()
            img = self.images[strat]
            img_label = tk.Label(player_frame, image=img)
            img_label.image = img
            img_label.pack(side="left", padx=10)

            text_label = tk.Label(
                player_frame,
                text=descriptions[strat],
                font=("Arial", 14),
                justify="left",
                wraplength=600,
            )
            text_label.pack(side="left")

        tk.Label(
            self,
            text="Now it's time to see them compete!\nYou will define the rewards and number of rounds.\nAt the end of each match, the worst player will be eliminated and replaced by a copy of the best one.",
            font=("Arial", 16),
            pady=20,
            wraplength=900,
            justify="center",
        ).pack()

        tk.Button(
            self, text="Let's go!", font=("Arial", 18), command=self.start_callback
        ).pack(pady=20)


class MainPlayPanel(tk.Frame):
    def __init__(self, root, images, personnality, screen_size):
        super().__init__(root)
        self.images = images
        self.personnality = personnality
        self.screen_size = screen_size

        self.canvas_width = self.screen_size[0] - 300
        self.canvas_height = self.screen_size[1]

        self.settingframe = tk.Frame(self, height=200, width=300)
        self.settingframe.grid(row=0, column=0, sticky="n")

        self.play_frame = tk.Frame(
            self, height=self.screen_size[1], width=self.screen_size[0] - 300
        )
        self.play_frame.grid(row=0, column=1)

        self.canvas = tk.Canvas(
            self.play_frame,
            width=self.screen_size[0] - 300,
            height=self.screen_size[1],
            bg="white",
        )
        self.canvas.pack()

        self.players = []
        self.build()

    def build(self):
        tk.Label(self.settingframe, text="Match Settings", font=("Arial", 16)).grid(
            row=0, column=0, columnspan=2
        )
        self.entries = []
        labels = [
            "Tit for tat",
            "Cheater",
            "Grudger",
            "Cooperate",
            "Round",
            "Reward for cooperate",
            "Reward for cheat",
            "Reward for cheated",
        ]
        default_values = ["2", "2", "2", "2", "5", "2", "3", "1"]

        for i, (label, default) in enumerate(zip(labels, default_values)):
            tk.Label(self.settingframe, text=label).grid(row=i + 1, column=0)
            entry = tk.Entry(self.settingframe, bg="white", fg="black")
            entry.grid(row=i + 1, column=1)
            entry.insert(0, default)
            self.entries.append(entry)

        tk.Button(
            self.settingframe,
            text="Show players",
            command=self.show_players,
            font=("Arial", 12),
        ).grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

        tk.Button(
            self.settingframe,
            text="Start match",
            command=self.start_round_robin,
            font=("Arial", 12),
        ).grid(row=len(labels) + 2, column=0, columnspan=2)

    def show_players(self):
        try:
            values = [int(entry.get()) for entry in self.entries]
            (
                self.nb_tit_for_tat,
                self.nb_cheater,
                self.nb_grudger,
                self.nb_cooperate,
                self.nb_round,
                self.reward_cooperate,
                self.reward_cheat,
                self.reward_cheated,
            ) = values
        except ValueError:
            messagebox.showinfo("Error", "Please enter valid numbers for all fields.")
            return

        self.players = (
            [Player("tit_for_tat") for _ in range(self.nb_tit_for_tat)]
            + [Player("cheater") for _ in range(self.nb_cheater)]
            + [Player("grudger") for _ in range(self.nb_grudger)]
            + [Player("cooperator") for _ in range(self.nb_cooperate)]
        )
        self.total_characters = len(self.players)
        if self.total_characters == 0:
            messagebox.showinfo("Error", "No characters to display.")
            return
        elif self.total_characters > 20:
            messagebox.showinfo(
                "Error",
                "For better visibility, the number of characters must not exceed 20",
            )
            return

        self.draw_players_circle()

    def draw_players_circle(self):
        self.canvas.delete("all")

        self.canvas_width = self.screen_size[0] - 200
        self.canvas_height = self.screen_size[1]
        rayon = min(self.canvas_width, self.canvas_height) // 2 - 80
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2

        angle = np.linspace(0, 2 * np.pi, len(self.players), endpoint=False)

        for i, player in enumerate(self.players):
            x = center_x + rayon * np.cos(angle[i])
            y = center_y + rayon * np.sin(angle[i])
            img = self.images[player.personality]
            self.canvas.create_image(x, y, image=img)
            self.canvas.create_text(
                x,
                y + 70,
                text=f"Score: {player.score}",
                font=("Arial", 10),
                fill="black",
            )

    def start_round_robin(self):
        for i in range(self.total_characters):
            for j in range(i + 1, self.total_characters):
                play_round(
                    self.players[i],
                    self.players[j],
                    self.nb_round,
                    self.reward_cooperate,
                    self.reward_cheat,
                    self.reward_cheated,
                )
        self.draw_players_circle()
        self.remove_and_replace_players()

    def remove_and_replace_players(self):
        self.players.sort(key=lambda player: player.score)
        best_player = max(self.players, key=lambda player: player.score)

        self.players = self.players[1:]
        self.players.append(
            Player(
                personality=best_player.personality,
                score=best_player.score,
            )
        )
        self.draw_players_circle()
