import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import statistics


class GameMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Menu")
        self.geometry("700x500")  # Window size
        self.configure(bg="lightblue")  # background colour

        self.label = tk.Label(self, text="Select a Game to Play:", font=("Eccentric Std", 30), bg="lightgrey")
        self.label.pack(pady=20)

        self.games = [
            ("Decode It", self.play_decode_it),
            ("Dice Roll", self.play_dice_roll),
            ("Jamaican Trivia", self.play_jamaican_trivia),
            ("Math Quiz", self.play_math_quiz)
        ]

        for game_name, game_func in self.games:
            button = tk.Button(self, text=game_name, command=game_func, font=("Rosewood Std Regular", 20),
                               bg="lightgreen", fg="black", width=20)
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
        self.geometry("700x500")  # Window size
        self.configure(bg="lightblue")  # background colour
        self.total_score = 0
        self.games_played = 0
        self.play_round()

    def play_round(self):
        self.word = self.choose_word()
        self.jumbled_word = self.decode_it(self.word)

        label = tk.Label(master=self, text=f'Decode the Word: {self.jumbled_word}', font=("Arial", 16), bg="lightblue")
        label.pack(pady=10)

        entry = tk.Entry(self, font=("Arial", 14))
        entry.pack(pady=10)

        def check_guess():
            guess = entry.get().lower()
            if guess == self.word:
                self.total_score += 1
                self.update_score_label()
                messagebox.showinfo("Correct!", "Congratulations! That's correct.")
            else:
                messagebox.showerror("Incorrect!", f"Sorry, that's incorrect. The word was: {self.word}")

            self.games_played += 1

        check_button = tk.Button(self, text="Check", command=check_guess, font=("Arial", 14),
                                 bg="lightgreen", fg="black", width=10)
        check_button.pack(pady=10)

        def play_again():
            # Reset game state
            entry.delete(0, tk.END)
            self.word = self.choose_word()
            self.jumbled_word = self.decode_it(self.word)
            label.config(text=f'Decode the Word: {self.jumbled_word}')
            self.update_score_label()

        play_again_button = tk.Button(self, text="Play Again", command=play_again, font=("Arial", 14),
                                      bg="lightblue", fg="black", width=10)
        play_again_button.pack(pady=10)

        stop_playing_button = tk.Button(self, text="Stop Playing", command=self.stop_playing, font=("Arial", 14),
                                        bg="lightcoral", fg="black", width=12)
        stop_playing_button.pack(pady=10)

        # Label to display the current score
        self.score_label = tk.Label(self, text=f'Score: {self.total_score}/{self.games_played}',
                                    font=("Arial", 14), bg="lightblue")
        self.score_label.pack(pady=10)

    def update_score_label(self):
        self.score_label.config(text=f'Score: {self.total_score}/{self.games_played}')

    def stop_playing(self):
        self.master.deiconify()
        self.destroy()

    def choose_word(self):
        words = ["python", "home", "friend", "food", "word", "love", "time", "family", "School", "money", "health"]
        return random.choice(words)

    def decode_it(self, word):
        jumbled_word = list(word)
        random.shuffle(jumbled_word)
        return ''.join(jumbled_word)


class DiceRoll(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Dice Roll")
        self.geometry("700x500")  # Window size
        self.configure(bg="lightblue")  # background colour
        self.total_score = 0
        self.games_played = 0
        self.play_round()

    def play_round(self):
        try:
            num = simpledialog.askinteger("Number of Dice Rolls", "Enter the number of dice rolls:")
            if num is None or num <= 0:
                return  # Exit if user cancels or provides invalid input

            rolls = [random.randint(1, 6) for _ in range(num)]
            total = sum(rolls)
            self.total_score += total
            self.games_played += 1
        except ValueError as e:
            print("Invalid input:", e)

        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.play_round()
        else:
            self.show_score()

    def show_score(self):
        if self.games_played > 0:
            average_score = self.total_score / self.games_played
        else:
            average_score = 0
        messagebox.showinfo("Game Over", f"Total score: {self.total_score}\nAverage score: {average_score:.2f}")
        self.master.show()


class JamaicanTrivia(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Jamaican Trivia")
        self.geometry("700x500")  # Window size
        self.configure(bg="lightblue")  # background colour
        self.score = 0
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


class MathQuiz(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Math Quiz")
        self.geometry("700x500")  # Window size
        self.configure(bg="lightblue")  # background colour
        self.scores = []
        self.num_questions = 0
        self.play()

    def generate_question(self):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        user_answer = simpledialog.askinteger("Math Quiz", f"What is the sum of {num1} and {num2}?")
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


if __name__ == "__main__":
    app = GameMenu()
    app.mainloop()