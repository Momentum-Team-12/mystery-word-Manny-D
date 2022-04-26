import random

def play_game(file):
    with open(file, 'r') as f:
        word_string = f.read()
        # random_word = random.choice(word_string)
        print(word_string)
        

    interested = input("Shall we play a game?\n")
    # print(interested)

    if interested.lower() == "y":
        word_list = word_string.split()
        current_word = word_list[0]
        print("Ok.. let's play!\n" "Your word is", len(current_word), "letters long.")
    else:
        print("Ok.. no soup for you!!")
        exit()

    


if __name__ == "__main__":
    # Copied from word_frequency assignment
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        play_game(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

    #play_game()
