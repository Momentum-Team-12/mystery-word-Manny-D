import random

def play_game():
    with open('test-word.txt') as f:
        word_string = f.read()
        word_list = word_string.split()
        current_word = random.choice(word_list)
        # print(current_word)
        
    # Do you want to build a snowman?!    
    interested = input("Shall we play a game? y/n \n")
    if interested.lower() == "y":
        print("Ok.. let's play!\n" "Your word is", len(current_word), "letters long.")
    else:
        print("Ok.. no soup for you!!")
        exit()

# The Game - Guesses while loop
    answer = ' '
    count = 8

    while count > 0:
        guess = input("\nPlease enter 1 letter to guess: ")
        answer += guess

        for letter in current_word:
            if letter in answer:
                print(letter, end = " ")

            elif letter not in answer:
                print("_", end = " ")
        
        if guess in current_word:
            count -= 1
            print("\nYou got one!\nYou have " + str(count) + " guesses remaining.")
        elif guess not in current_word:
            count -= 1
            print("\nSorry no " + guess + "'s try again!\nYou have " + str(count) + " guesses remaining.")

        elif count == 0:
            print("Game Over!!\nNo more guesses left =(\nThe word was " + current_word)


if __name__ == "__main__":
    play_game()
