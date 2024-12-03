# This task requires us to set a target number between 1 and 100. Users can guess the number by entering it on the console. If the input is incorrect, too large or too small, feedback should be given to the user and they should be asked to re-enter it. Once the user guesses correctly, the program will be terminated

# Code logic:
# 1. Set a 'target_num'
# 2. Use a while statement to allow users to input repeatedly
# 3. Check if the user input is an integer
# 4. Check if the input number is between 1 and 100
# 5. Check if the input number is greater or less than 'target_num' and provide corresponding feedback
# 6. Provide feedback and terminate the program when the user inputs the correct number
target_num = 62     # Set target number

# Use while loop to make user input number with multiple chance
while True:
    # Use input() to make user input number in cmd
    # The string in 'input' is the cue words, user will input value behind them
    # The default data type from input() is String, we should use int() to transform it into integer
    guess_num = int(input("Please input a number between 1 and 100: "))
    # Use 'if' statement to check the 'guess_num' can afford the requirements
    # Check if the input value can be transformed into integer
    if guess_num is int:
        # Check if the 'guess_num' between 1 and 100
        # "Or" means one of the conditions is True, the full statement is True.
        if guess_num < 1 or guess_num > 100:
            print("Invalid input! The number must be between 1 and 100.")   # Given feedback if 'guess_num' not between 1 and 100
        # When "guess_num" is integer
        else:
            if guess_num > target_num:
                # When "guess_num" > "target_num"
                print("You number is too large!")
            elif guess_num < target_num:
                # The statements under 'elif' will be executed when 'if' statement is False
                # When "guess_num" < "target_num"
                print("You number is too small!")
            else:
                # The code under 'else' statement will be executed when the condition of 'if' statement and 'elif' statements are False
                # When "guess_num" is same as "target_num", given feedback and terminate the program
                # We can stop a while loop by "break"
                print("Your guess is correct!")
                break
    else:
        print("Invalid input! Please input an integer.")