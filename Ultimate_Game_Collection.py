import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random
import statistics


class GameMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Menu")
        self.geometry("900x800") # Window size
        self.configure(bg="lightblue") # background colour


        self.label = tk.Label(self, text="Select a Game to Play:", font=("Eccentric Std", 30), bg="lightgrey")
        self.label.pack(pady=20)

        self.games = [
            ("Decode It", self.play_decode_it),
            ("Dice Roll", self.play_dice_roll),
            ("Jamaican Trivia", self.play_jamaican_trivia),
            ("Math Quiz", self.play_math_quiz)
        ]

        for game_name, game_func in self.games:
            button = tk.Button(self, text=game_name, command=game_func, font=("Rosewood Std Regular", 20), bg="lightgreen")
            button.pack(pady=10)

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
        messagebox.showinfo("Game Over",
                            f"Total score: {self.total_score}\nAverage score: {self.total_score / self.games_played:.2f}")
        self.master.show()


class DiceRoll(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Dice Roll")

        self.total_score = 0
        self.games_played = 0

        self.play_round()

    def play_round(self):
        try:
            num = tk.simpledialog.askinteger("Number of Dice Rolls", "Enter the number of dice rolls:")
            if num is None or num <= 0:
                return  # Exit if user cancels or provides invalid input

            rolls = [random.randint(1, 6) for _ in range(num)]
            total = sum(rolls)
            print("Dice rolls:", rolls)
            print("Total score:", total)
            self.total_score += total
            self.games_played += 1
        except ValueError as e:
            print("Invalid input:", e)

        play_again = tk.messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.play_round()
        else:
            self.show_score()

    def show_score(self):
        if self.games_played > 0:
            average_score = self.total_score / self.games_played
        else:
            average_score = 0
        tk.messagebox.showinfo("Game Over", f"Total score: {self.total_score}\nAverage score: {average_score:.2f}")
        self.master.show()
        # Game code goes here


class JamaicanTrivia(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Jamaican Trivia")

        self.score = 0
        self.questions = {
            "What is the capital of Jamaica?": ["A) Kingston", "B) Montego Bay", "C) Ocho Rios", "D) Negril"],
            "Which famous reggae musician is from Jamaica?": ["A) Bob Marley", "B) Jimmy Cliff", "C) Peter Tosh",
                                                              "D) Shaggy"],
            "What is Jamaica's national dish?": ["A) Jerk Chicken", "B) Ackee and Saltfish", "C) Curry Goat",
                                                 "D) Escovitch Fish"],
            "Which Jamaican sprinter holds the world record for the 100m dash?": ["A) Usain Bolt", "B) Asafa Powell",
                                                                                  "C) Yohan Blake",
                                                                                  "D) Shelly-Ann Fraser-Pryce"],
            "What is the currency of Jamaica?": ["A) Dollar", "B) Peso", "C) Euro", "D) Pound"]
        }

        self.play()

    def play(self):
        print("Welcome to Jamaica Trivia Quiz!")
        start_choice = messagebox.askyesno("Start Quiz", "Do you want to start the quiz?")
        if not start_choice:
            messagebox.showinfo("Goodbye!", "Goodbye!")
            self.master.show()
            return

        for question in self.questions:
            messagebox.showinfo("Question", question)
            for option in self.questions[question]:
                messagebox.showinfo("Option", option)

            user_answer = simpledialog.askstring("Enter Answer", "Enter your choice (A, B, C, or D):").upper()

            if user_answer == "A" and question == "What is the capital of Jamaica?":
                self.score += 10
            elif user_answer == "B" and (
                    question == "Which famous reggae musician is from Jamaica?" or question == "What is Jamaica's national dish?"):
                self.score += 10
            elif user_answer == "C" and question == "Which Jamaican sprinter holds the world record for the 100m dash?":
                self.score += 10
            elif user_answer == "D" and question == "What is the currency of Jamaica?":
                self.score += 10
            else:
                self.score -= 10

            messagebox.showinfo("Current Score", f"Your current score is: {self.score}")

            choice = messagebox.askyesno("Continue", "Would you like to continue?")
            if not choice:
                break

        self.display_score()

    def display_score(self):
        messagebox.showinfo("Total Score", f"Total Score: {self.score}")
        self.master.show()
        # Game code


class MathQuiz(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Math Quiz")
        self.scores = []
        self.num_questions = 0

        self.play()

    def generate_question(self):
        # Generate two random numbers for the question
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        # Prompt the user with the question
        user_answer = tk.simpledialog.askinteger("Math Quiz", f"What is the sum of {num1} and {num2}?")
        # Check if the user's answer is correct
        if user_answer is not None:
            if user_answer == num1 + num2:
                messagebox.showinfo("Correct", "Correct!")
                self.scores.append(1)
            else:
                messagebox.showinfo("Incorrect", "Incorrect!")
            self.num_questions += 1

    def play(self):
        messagebox.showinfo("Welcome", "Welcome to the Math Quiz Game!")
        while True:
            self.generate_question()
            play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
            if not play_again:
                break
        messagebox.showinfo("Game Over", f"Game Over! You answered {self.num_questions} questions.")
        self.display_scores()

    def display_scores(self):
        if self.scores:
            mean_score = statistics.mean(self.scores)
            mode_score = statistics.mode(self.scores)
            median_score = statistics.median(self.scores)
            messagebox.showinfo("Scores",
                                f"Mean Score: {mean_score}\nMode Score: {mode_score}\nMedian Score: {median_score}")
        else:
            messagebox.showinfo("Scores", "No scores recorded.")
        # Game code goes here


if __name__ == "__main__":
    app = GameMenu()
    app.mainloop()