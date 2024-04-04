import tkinter as tk
from tkinter import messagebox
import random


class GameMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Menu")

        self.label = tk.Label(self, text="Select a Game to Play:")
        self.label.pack()

        self.games = [
            ("Decode It", self.play_decode_it),
            ("Dice Roll", self.play_dice_roll),
            ("Jamaican Trivia", self.play_jamaican_trivia),
            ("Math Quiz", self.play_math_quiz)
        ]

        for game_name, game_func in self.games:
            button = tk.Button(self, text=game_name, command=game_func)
            button.pack()

    def play_decode_it(self):
        self.hide()
        DecodeIt(self)

    def play_dice_roll(self):
        self.hide()
        DiceRoll(self)

    def play_jamaican_trivia(self):
        self.hide()
        JamaicanTrivia(self)

    def play_math_quiz(self):
        self.hide()
        MathQuiz(self)

    def hide(self):
        self.withdraw()


class DecodeIt(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Decode It")

        # Game code goes here


class DiceRoll(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Dice Roll")

        # Game code goes here


class JamaicanTrivia(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Jamaican Trivia")

        # Game code goes here


class MathQuiz(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Math Quiz")

        # Game code goes here


if __name__ == "__main__":
    app = GameMenu()
    app.mainloop()


