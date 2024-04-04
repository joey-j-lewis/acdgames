import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
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

        self.total_score = 0
        self.games_played = 0

        self.play_round()

    def choose_word(self):
        words = ["python", "home", "friend", "food", "word", "love", "time", "family", "School", "money", "health"]
        return random.choice(words)

    def decode_it(self, word):
        jumbled_word = list(word)
        random.shuffle(jumbled_word)
        return ''.join(jumbled_word)

    def play_round(self):
        word = self.choose_word()
        jumbled = self.decode_it(word)
        print("Decode It:", jumbled)

        guess = tk.simpledialog.askstring("Guess the Word", "Guess the word:")

        if guess and guess.lower() == word:
            messagebox.showinfo("Correct", "Congratulations! That's correct.")
            self.total_score += 1
            print("Point earned: 1")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, that's incorrect. The word was: {word}")

        self.games_played += 1
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.play_round()
        else:
            self.show_score()

    def show_score(self):
        messagebox.showinfo("Game Over", f"Total score: {self.total_score}\nAverage score: {self.total_score / self.games_played:.2f}")
        self.master.show()

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
