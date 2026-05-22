import random

# Hangman stages - 6 chances
HANGMAN_STAGES = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========='''
]

def get_random_word():
    """ShadowFox related words for theme"""
    words = [
        'python', 'developer', 'shadowfox', 'programming', 'hangman', 
        'computer', 'keyboard', 'internet', 'github', 'vscode',
        'function', 'variable', 'string', 'integer', 'boolean'
    ]
    return random.choice(words).lower()

def display_game(word, guessed_letters, wrong_guesses):
    """Display current game state"""
    print(HANGMAN_STAGES[wrong_guesses])
    print()
    
    # Display word with guessed letters
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    print(f"Word: {display_word}")
    print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
    print(f"Wrong guesses: {wrong_guesses}/6")
    print("-" * 40)

def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6
    
    print("=== Welcome to ShadowFox Hangman ===")
    print("Guess the programming related word!")
    print("-" * 40)
    
    while wrong_guesses < max_wrong:
        display_game(word, guessed_letters, wrong_guesses)
        
        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(HANGMAN_STAGES[wrong_guesses])
            print(f"\n🎉 Congratulations! You guessed it: {word.upper()}")
            print("You saved the man!")
            return
        
        # Get user input
        guess = input("Enter a letter: ").lower().strip()
        
        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter!")
            continue
            
        if guess in guessed_letters:
            print("⚠️  You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! '{guess}' is not in the word.")
    
    # Game over
    display_game(word, guessed_letters, wrong_guesses)
    print(f"\n💀 Game Over! The word was: {word.upper()}")
    print("Better luck next time!")

if __name__ == "__main__":
    while True:
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing ShadowFox Hangman! 👋")
            break