import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    # Find mean out of remaining number guessing pool
    x = (poss_values[0] + poss_values[-1]) // 2   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    # If next_val is greater and user is correct
    if (next_val > current_val) and (user_input == "h"):
        return True
    # If next_val is lesser and user is correct
    elif (next_val < current_val) and (user_input == "l"):
        return True
    # If user is incorrect
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    # If letter is in word...
    if letter in word:
        # Go through word
        for i in range(0, len(word)):
            if word[i] == letter:
                # Replace each relevant _ in board with letter
                board[i] = letter
        
        # Print result
        print(f"Well done! '{letter}' is in the word")
        return True
    else:
        # Print results if letter is not in word
        print(f"Sorry, '{letter}' is not in the word")
        return False
        
