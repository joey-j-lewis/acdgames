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
        self.games_played = 1
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
                # Disable the Check button after the answer is checked
                check_button.config(state=tk.DISABLED)
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
            # Enable the Check button when playing again
            check_button.config(state=tk.NORMAL)

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
        words = ["python", "home", "friend", "food", "word", "love", "time", "family", "school", "money", "health"]
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
        self.configure(bg="lightblue")  # Background colour

        self.label = tk.Label(self, text="Welcome to the Dice Roll Game!", font=("Arial", 20), bg="lightblue")
        self.label.pack(pady=20)

        label = tk.Label(master=self,
                         text="In the Dice Roll game, you get to decide how many times the dice are rolled. Just tell me the number of rolls you'd like, and I'll show you the outcome. After each roll, I'll display the result of each dice roll and the total score. If you feel like rolling again, just let me know. It's all about having fun and seeing how your luck plays out!",
                         font=("Arial", 12), bg="lightblue", wraplength=600)
        label.pack(pady=10)

        self.entry_label = tk.Label(self, text="Enter the number of dice rolls:", font=("Arial", 16), bg="lightblue")
        self.entry_label.pack()

        self.num_entry = tk.Entry(self, font=("Arial", 14))
        self.num_entry.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 16), bg="lightblue", wraplength=600)
        self.result_label.pack(pady=10)

        self.play_button = tk.Button(self, text="Roll Dice", command=self.roll_dice, font=("Arial", 14),
                                     bg="lightgreen", fg="black", width=12)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self, text="Stop Game", command=self.stop_game, font=("Arial", 14),
                                     bg="lightcoral", fg="black", width=12)
        self.stop_button.pack(pady=10)

    def roll_dice(self):
        try:
            num_rolls = int(self.num_entry.get())  # Get the number of rolls from the entry widget
            if num_rolls <= 0:
                raise ValueError("Number of rolls must be positive")
            elif num_rolls > 5:  # Check if number of rolls exceeds the limit
                raise ValueError("Number of rolls cannot exceed 5")
            rolls = [random.randint(1, 6) for _ in range(num_rolls)]
            total = sum(rolls)
            self.result_label.config(text=f"Dice rolls: {rolls}\nTotal score: {total}")
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def stop_game(self):
        self.master.deiconify()  # Show the main menu window
        self.destroy()  # Close the current game window


class JamaicanTrivia(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Jamaican Trivia")
        self.geometry("700x500")  # Window size
        self.configure(bg="lightblue")  # background colour
        self.score = 0

        self.questions = [
            ("What is the capital of Jamaica?", ["A) Kingston", "B) Montego Bay", "C) Ocho Rios", "D) Negril"],
             "A) Kingston"),
            ("Which famous reggae musician is from Jamaica?",
             ["A) Bob Marley", "B) Jimmy Cliff", "C) Peter Tosh", "D) Shaggy"], "A) Bob Marley"),
            ("What is Jamaica's national dish?",
             ["A) Jerk Chicken", "B) Ackee and Saltfish", "C) Curry Goat", "D) Escovitch Fish"],
             "B) Ackee and Saltfish"),
            ("Which Jamaican sprinter holds the world record for the 100m dash?",
             ["A) Usain Bolt", "B) Asafa Powell", "C) Yohan Blake", "D) Shelly-Ann Fraser-Pryce"], "A) Usain Bolt"),
            ("What is the currency of Jamaica?", ["A) Dollar", "B) Peso", "C) Euro", "D) Pound"], "A) Dollar")
        ]
        self.current_question = None
        self.score = 0
        self.correct_answer = ""

        self.question_label = tk.Label(self, text="", font=("Arial", 16), wraplength=350)
        self.question_label.pack(pady=20)

        self.answers_frame = tk.Frame(self)
        self.answers_frame.pack(pady=20)

        self.selected_answer = tk.StringVar()

        self.check_button = tk.Button(self, text="Check Answer", command=self.check_answer, font=("Arial", 14),
                                      bg="lightgreen", fg="black", width=12)
        self.check_button.pack(pady=20)

        self.next_button = tk.Button(self, text="Next Question", command=self.ask_question, font=("Arial", 14),
                                     bg="lightgreen", fg="black", width=12, state="disabled")
        self.next_button.pack(pady=20)

        self.score_label = tk.Label(self, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack()

        self.ask_question()

    def ask_question(self):
        self.selected_answer.set(None)  # Clear the previous selection
        self.question_label.config(text="")  # Clear the previous question

        # Remove widgets for previous answers
        for widget in self.answers_frame.winfo_children():
            widget.destroy()

        if len(self.questions) == 0:
            self.display_score()
            return

        self.current_question, options, self.correct_answer = random.choice(self.questions)
        self.questions.remove(
            (self.current_question, options, self.correct_answer))  # Remove the question so it doesn't repeat

        self.question_label.config(text=self.current_question)  # Display the question

        # Display the answer options
        for option in options:
            button = tk.Radiobutton(self.answers_frame, text=option, variable=self.selected_answer, value=option)
            button.pack(anchor='w')

        self.check_button.config(state="normal")
        self.next_button.config(state="disabled")

    def check_answer(self):
        if self.selected_answer.get() == self.correct_answer:
            self.score += 10
            messagebox.showinfo("Correct!", "That's the right answer!")
        else:
            messagebox.showinfo("Incorrect!", f"Sorry, the correct answer was {self.correct_answer}.")

        self.score_label.config(text=f"Score: {self.score}")  # Update the score display
        self.next_button.config(state="normal")  # Enable the 'Next Question' button
        self.check_button.config(state="disabled")  # Disable the 'Check Answer' button

    def display_score(self):
        messagebox.showinfo("Quiz Complete", f"Your final score is {self.score}!")
        self.destroy()  # Close the application


import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import statistics


class MathQuiz(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Math Quiz")
        self.geometry("700x700")  # Window size
        self.configure(bg="lightblue")  # background colour
        self.scores = []
        self.num_questions = 0
        self.setup_ui()
        self.generate_question()

    def setup_ui(self):
        self.question_label = tk.Label(self, text="", font=("Arial", 16), bg="lightblue")
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self, font=("Arial", 14))
        self.answer_entry.pack(pady=10)

        self.check_button = tk.Button(self, text="Check", command=self.check_answer, font=("Arial", 14),
                                      bg="lightgreen", fg="black", width=10)
        self.check_button.pack(pady=10)

        self.play_again_button = tk.Button(self, text="Play Again", command=self.play, font=("Arial", 14),
                                           bg="lightgreen", fg="black", width=10, state=tk.DISABLED)
        self.play_again_button.pack(pady=10)

        self.stop_button = tk.Button(self, text="Stop Game", command=self.stop_game, font=("Arial", 14),
                                     bg="lightgreen", fg="black", width=10)
        self.stop_button.pack(pady=10)

        self.exit_button = tk.Button(self, text="Exit", command=self.exit_game, font=("Arial", 14),
                                     bg="lightgreen", fg="black", width=10)
        self.exit_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 14), bg="lightblue")
        self.result_label.pack(pady=10)

        self.incorrect_label = tk.Label(self, text="", font=("Arial", 14), bg="lightblue", fg="red")
        self.incorrect_label.pack(pady=10)

        self.score_label = tk.Label(self, text="Score: 0", font=("Arial", 14), bg="lightblue")
        self.score_label.pack(pady=10)

        self.mean_label = tk.Label(self, text="", font=("Arial", 14), bg="lightblue")
        self.mean_label.pack(pady=5)

        self.mode_label = tk.Label(self, text="", font=("Arial", 14), bg="lightblue")
        self.mode_label.pack(pady=5)

        self.median_label = tk.Label(self, text="", font=("Arial", 14), bg="lightblue")
        self.median_label.pack(pady=5)

    def generate_question(self):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        self.correct_answer = num1 + num2
        self.question_label.config(text=f"What is the sum of {num1} and {num2}?")

    def check_answer(self):
        user_answer = self.answer_entry.get()
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if user_answer == self.correct_answer:
                self.result_label.config(text="Correct!")
                self.scores.append(1)
            else:
                self.result_label.config(text="Incorrect!")
                self.incorrect_label.config(text=f"Correct answer: {self.correct_answer}")
            self.num_questions += 1
            self.score_label.config(text=f"Score: {len(self.scores)}")
            self.mean_label.config(text=f"Mean Score: {statistics.mean(self.scores)}")
            self.mode_label.config(text=f"Mode Score: {statistics.mode(self.scores)}")
            self.median_label.config(text=f"Median Score: {statistics.median(self.scores)}")
            self.check_button.config(state=tk.DISABLED)
            self.play_again_button.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def play(self):
        self.generate_question()
        self.result_label.config(text="")
        self.incorrect_label.config(text="")
        self.answer_entry.delete(0, tk.END)
        self.check_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)

    def stop_game(self):
        self.mean_label.config(text=f"Mean Score: {statistics.mean(self.scores)}")
        self.mode_label.config(text=f"Mode Score: {statistics.mode(self.scores)}")
        self.median_label.config(text=f"Median Score: {statistics.median(self.scores)}")
        self.stop_button.config(state=tk.DISABLED)
        self.exit_button.config(state=tk.NORMAL)

    def exit_game(self):
        self.destroy()

if __name__ == "__main__":
    app = GameMenu()
    app.mainloop()



