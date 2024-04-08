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

    def play(self):
        print("Hi, User! Welcome to Jamaica Trivia Quiz.")
        choice = input("Do you want to start? (yes/no): ").lower()
        if choice != 'yes':
            print("Maybe next time!")
            return

        for question in self.questions:
            print(f"\n{question}")
            for option in self.questions[question]:
                print(option)
            
            user_answer = input("Enter your choice (A, B, C, or D): ").upper()

            if user_answer in ["A", "B", "C", "D"]:
                if user_answer == self.questions[question][0][0]:
                    print("Your answer is correct!")
                    self.score += 10
                else:
                    print(f"Your answer is wrong! The correct answer is {self.questions[question][0]}")
                    self.score -= 10
            else:
                print("Invalid input! Your answer is wrong!")
                self.score -= 10

            print(f"Your current score is: {self.score}")

            choice = input("Would you like to continue (yes/no)? ").lower()
            if choice != 'yes':
                break

    def display_score(self):
        print(f"\nTotal Score: {self.score}")

game = JamaicaTriviaQuiz()
game.play()
game.display_score()

