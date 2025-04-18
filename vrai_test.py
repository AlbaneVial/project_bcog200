# display.py
import tkinter as tk
from tkinter import messagebox
import numpy as np
import os

from player import Player, play_round, turn, Strategy

# --- Utility factory functions ---


def mk_label(parent, text, row, col, **opts):
    lbl = tk.Label(parent, text=text, **opts)
    lbl.grid(row=row, column=col, padx=5, pady=5)
    return lbl


def mk_button(parent, text, cmd, row, col, **opts):
    btn = tk.Button(parent, text=text, command=cmd, **opts)
    btn.grid(row=row, column=col, padx=5, pady=5)
    return btn


# --- Panel Classes ---
class IntroPanel(tk.Frame):
    def __init__(self, master, images, start_callback):
        super().__init__(master)
        self.images = images
        self.start_callback = start_callback
        self.build()

    def build(self):
        mk_label(self, "Welcome to The Evolution of Trust!", 0, 0, font=("Arial", 20))
        # show strategy logos
        for i, strat in enumerate(Strategy):
            img = self.images[strat.value]
            lbl = tk.Label(self, image=img)
            lbl.image = img
            lbl.grid(row=1, column=i)
        mk_button(
            self,
            "Start Game",
            self.start_callback,
            2,
            0,
            columnspan=4,
            font=("Arial", 16),
        )


class BotMatchPanel(tk.Frame):
    def __init__(self, master, images, player_idx, continue_callback):
        super().__init__(master)
        self.images = images
        self.player_idx = player_idx
        self.continue_callback = continue_callback
        self.build()

    def build(self):
        mk_label(self, f"Match vs Bot #{self.player_idx+1}", 0, 0, font=("Arial", 16))
        # ... add user/bot images, buttons, score display here ...
        mk_button(self, "Next", self.continue_callback, 5, 0)


class SettingsPanel(tk.Frame):
    def __init__(self, master, start_match_callback):
        super().__init__(master)
        self.start_match_callback = start_match_callback
        self.build()

    def build(self):
        mk_label(self, "Match Settings", 0, 0, font=("Arial", 16))
        # create entries for parameters
        self.entries = {}
        labels = ["Tit for tat", "Cheater", "Grudger", "Cooperate", "Rounds"]
        defaults = [2, 2, 2, 2, 5]
        for i, (label, df) in enumerate(zip(labels, defaults)):
            mk_label(self, label, i + 1, 0)
            ent = tk.Entry(self)
            ent.insert(0, str(df))
            ent.grid(row=i + 1, column=1)
            self.entries[label] = ent
        mk_button(
            self, "Start Round Robin", self.start_match_callback, len(labels) + 2, 0
        )


class CirclePanel(tk.Frame):
    def __init__(self, master, images):
        super().__init__(master)
        self.images = images
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill="both", expand=True)

    def update(self, players):
        self.canvas.delete("all")
        n = len(players)
        angle = np.linspace(0, 2 * np.pi, n, endpoint=False)
        r = min(self.winfo_width(), self.winfo_height()) // 2 - 50
        cx, cy = self.winfo_width() // 2, self.winfo_height() // 2
        for i, p in enumerate(players):
            x = cx + r * np.cos(angle[i])
            y = cy + r * np.sin(angle[i])
            img = self.images[p.personality]
            self.canvas.create_image(x, y, image=img)
            self.canvas.create_text(x, y + 60, text=f"{p.score}")


# --- Main Application ---
class TrustApp:
    def __init__(self):
        self.root = tk.Tk()
        self.load_images()
        self.init_window()
        self.create_panels()
        self.show_panel("intro")

    def load_images(self):
        files = {s.value: f"{s.value}.gif" for s in Strategy}
        self.images = {}
        for key, fname in files.items():
            if os.path.exists(fname):
                self.images[key] = tk.PhotoImage(file=fname)
            else:
                raise FileNotFoundError(f"Image {fname} not found")

    def init_window(self):
        self.root.title("The Evolution of Trust")
        self.root.geometry("800x600")

    def create_panels(self):
        self.panels = {}
        self.panels["intro"] = IntroPanel(
            self.root, self.images, lambda: self.show_panel("bot0")
        )
        for i in range(4):
            self.panels[f"bot{i}"] = BotMatchPanel(
                self.root, self.images, i, lambda idx=i: self.next_bot(idx)
            )
        self.panels["settings"] = SettingsPanel(self.root, self.start_round_robin)
        self.panels["circle"] = CirclePanel(self.root, self.images)

    def show_panel(self, name):
        if hasattr(self, "current"):
            self.current.pack_forget()
        self.current = self.panels[name]
        self.current.pack(fill="both", expand=True)

    def next_bot(self, idx):
        next_idx = idx + 1
        if next_idx < 4:
            self.show_panel(f"bot{next_idx}")
        else:
            self.show_panel("settings")

    def start_round_robin(self):
        # read settings, build players list
        # play_round robin and update scores
        self.players = []  # build from SettingsPanel entries
        self.show_panel("circle")
        self.panels["circle"].update(self.players)

    def run(self):
        self.root.mainloop()


def main():
    app = TrustApp()
    app.run()


if __name__ == "__main__":
    main()
