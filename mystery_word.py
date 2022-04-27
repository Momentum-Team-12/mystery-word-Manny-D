import random

def play_game():
    with open('test-word.txt') as f:
        word_string = f.read()
        word_list = word_string.split()
        current_word = random.choice(word_list)
        # print(current_word)
        
    # Do you want to build a snowman?!    
    interested = input("Greetings Professor Falken.\nShall we play a game? y/n \n")
    if interested.lower() == "y":
        print("Ok.. let's play!\n" "Your word is", len(current_word), "letters long.")
    else:
        print("A strange game.\nThe only winning move is not to play.\nHow about a nice game of chess?")
        exit()

# The Game
    answer = []
    #global count -> may need later
    count = 8

    while count > 0:
        guess = input("\nPlease enter 1 letter to guess: ")
        answer += guess
        w = 0

        # Guess tracking
        if not guess.isalpha(): # looks to be working now
            print("Invalid entry. Please enter letters only.")
            
        elif len(guess) > 1:   # looks to be working even if correct letter entered
            answer = ""
            print("Invalid entry. Only 1 letter please.")

        elif guess in current_word:
            #count -= 1 # Removing as user shouldn't lose guesses if correct
            print("\nYou got one!\nYou have " + str(count) + " guesses remaining.")

        elif guess not in current_word:
            count -= 1
            print("\nSorry no " + guess + "'s try again!\nYou have " + str(count) + " guesses remaining.")


        # Loop: letters (char) vs _'s vs Win
        for char in current_word:
            if char in answer:
                print(char, end = "")
        
            #elif char not in answer:
            else:
                print("_", end = "")
                w += 1

        if w == 0: # works but want to try something different
            print("\nYou did it!\nThe Mystery Word was " + current_word + " and was solved in " + str(8 - count) + " guesses!")
            exit()

        # elif guess in answer:
        #     print("You already tried that letter.\nYou have " + str(count) + " guesses remaining.")


    if count == 0:
        print("\nGame Over!!\nNo more guesses left =(\nThe word was " + current_word + ".")
    #break



    # Ends game when count is 0
    # while count == 0:
    #     print("\nGame Over!!\nNo more guesses left =(\nThe word was " + current_word + ".")
    #     break

if __name__ == "__main__":
    play_game()
