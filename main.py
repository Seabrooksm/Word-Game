secret_word = "lighthouse" # This is the hardcoded secret word
guesses = [] # This list will store the player's guesses

def display_secret_word(secret_word, guesses):
  # Print the secret word with underscores for unguessed letters
  for letter in secret_word:
    if letter in guesses:
      print(letter, end="")
    else:
      print("_", end="")
  print() # Add a newline

while True: # This will repeat the game logic until the player wins or loses
  display_secret_word(secret_word, guesses) # Call the display_secret_word function

  # Ask the player for their next guess
  guess = input("Guess a letter: ")

  # Check if the player has already guessed this letter
  if guess in guesses:
    print("You already guessed that letter!")
    continue # Go back to the start of the loop

  # Check if the guess is in the secret word
  if guess in secret_word:
    print("Nice guess!")
  else:
    print("Incorrect guess.")
    # Calculate the number of strikes the player has remaining
    strikes = len([g for g in guesses if g not in secret_word])
    print("You have " + str(strikes) + " out of 5 strikes.")

  # Add the guess to the list of guesses
  guesses.append(guess)

  # Check if the player has won
  if all(letter in guesses for letter in secret_word):
    print("Congratulations! You won the game.")
    break # End the game

  # Check if the player has lost
  if len(guesses) > 5:
    print("Sorry, you lost the game. The secret word was '" + secret_word + "'.")
    break # End the game

