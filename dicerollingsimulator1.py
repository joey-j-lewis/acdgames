import random

class DiceRollingSimulator1:
    def __init__(self):
        self.score = 0

    def play(self):
        try:
            num = int(input("Enter the number of dice rolls: "))
            if num <= 0:
                raise ValueError("Number of dice rolls should be a positive integer.")
            
            rolls = [random.randint(1, 6) for _ in range(num)]
            total = sum(rolls)
            print("Dice rolls:", rolls)
            print("Total score:", total)
            self.score += total
        except ValueError as e:
            print("Invalid input:", e)

if __name__ == "__main__":
    dice_game = DiceRollingSimulator1()
    dice_game.play()
