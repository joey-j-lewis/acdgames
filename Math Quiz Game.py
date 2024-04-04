import random
import statistics

class MathQuizGame:
    def __init__(self):
        self.scores = []
        self.num_questions = 0

    def generate_question(self):
        # Generate two random numbers for the question
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        # Prompt the user with the question
        user_answer = input(f"What is the sum of {num1} and {num2}? ")
        # Check if the user's answer is correct
        if user_answer.isdigit():
            if int(user_answer) == num1 + num2:
                print("Correct!")
                self.scores.append(1)
            else:
                print("Incorrect!")
            self.num_questions += 1
        else:
            print("Please enter a valid number.")

    def play(self):
        print("Welcome to the Math Quiz Game!")
        while True:
            self.generate_question()
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != 'yes':
                break
        print(f"Game Over! You answered {self.num_questions} questions.")
        self.display_scores()

    def display_scores(self):
        if self.scores:
            mean_score = statistics.mean(self.scores)
            mode_score = statistics.mode(self.scores)
            median_score = statistics.median(self.scores)
            print(f"Mean Score: {mean_score}")
            print(f"Mode Score: {mode_score}")
            print(f"Median Score: {median_score}")
        else:
            print("No scores recorded.")

# Main function to start the game
def main():
    math_quiz_game = MathQuizGame()
    math_quiz_game.play()

if __name__ == "__main__":
    main()

