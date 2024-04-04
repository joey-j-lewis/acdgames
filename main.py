import random


def choose_word():
    words = ["python", "home", "friend", "food", "word", "love", "time", "family", "School", "money", "health"]
    return random.choice(words)


def jumble_word(word):
    jumbled_word = list(word)
    random.shuffle(jumbled_word)
    return ''.join(jumbled_word)


def main():
    total_score = 0
    games_played = 0

    play_again = True
    while play_again:
        word = choose_word()
        jumbled = jumble_word(word)
        print("Jumbled word:", jumbled)

        guess = input("Guess the word: ").lower()

        if guess == word:
            print("Congratulations! That's correct.")
            total_score += 10
            print("point earned: 10")
        else:
            print("Sorry, that's incorrect. The word was:", word)

        games_played += 1
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == "yes"

    print("Total score:", total_score)
    if games_played > 0:
        average_score = total_score / games_played
        print("Average score:", average_score)


if __name__ == "__main__":
    main()
  
