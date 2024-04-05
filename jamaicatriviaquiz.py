import random

class JamaicaTriviaQuiz:
    def __init__(self):
        self.score = 0
        self.questions = {
            "What is the capital of Jamaica?": ["A) Kingston", "B) Montego Bay", "C) Ocho Rios", "D) Negril"],
            "Which famous reggae musician is from Jamaica?": ["A) Bob Marley", "B) Jimmy Cliff", "C) Peter Tosh", "D) Shaggy"],
            "What is Jamaica's national dish?": ["A) Jerk Chicken", "B) Ackee and Saltfish", "C) Curry Goat", "D) Escovitch Fish"],
            "Which Jamaican sprinter holds the world record for the 100m dash?": ["A) Usain Bolt", "B) Asafa Powell", "C) Yohan Blake", "D) Shelly-Ann Fraser-Pryce"],
            "What is the currency of Jamaica?": ["A) Dollar", "B) Peso", "C) Euro", "D) Pound"]
        }

    def start_quiz(self):
        print("Welcome to Jamaica Trivia Quiz!")
        start_choice = input("Do you want to start? (yes or no): ").lower()
        if start_choice != 'yes':
            print("Goodbye!")
            return
        else:
            self.play()

    def play(self):
        for question in self.questions:
            print(f"\n{question}")
            for option in self.questions[question]:
                print(option)
            
            user_answer = input("Enter your choice (A, B, C, or D): ").upper()

            if user_answer == "A":
                if question == "What is the capital of Jamaica?":
                    self.score += 10
            elif user_answer == "B":
                if question == "Which famous reggae musician is from Jamaica?":
                    self.score += 10
                elif question == "What is Jamaica's national dish?":
                    self.score += 10
            elif user_answer == "C":
                if question == "Which Jamaican sprinter holds the world record for the 100m dash?":
                    self.score += 10
            elif user_answer == "D":
                if question == "What is the currency of Jamaica?":
                    self.score += 10
            else:
                self.score -= 10

            print(f"Your current score is: {self.score}")

            choice = input("Would you like to continue (yes/no)? ").lower()
            if choice != 'yes':
                break

    def display_score(self):
        print(f"\nTotal Score: {self.score}")

game = JamaicaTriviaQuiz()
game.start_quiz()
game.display_score()
