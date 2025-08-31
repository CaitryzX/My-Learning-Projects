# NEW Programming Challenges - Advanced Level

print("=== NEW PROGRAMMING CHALLENGES ===\n")

# CHALLENGE 1: Password Generator
print("CHALLENGE 1: Password Generator")
import random
import string

def generate_password(length=8):
    """Generate a random password with letters, numbers, and symbols"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print(f"Generated password: {generate_password(12)}")
print(f"Another password: {generate_password(8)}\n")

# CHALLENGE 2: Word Counter
print("CHALLENGE 2: Word Counter")
def analyze_text(text):
    """Analyze text and return word count, character count, and most common word"""
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    
    # Count word frequency
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Find most common word
    most_common = max(word_freq, key=word_freq.get)
    
    return {
        'words': word_count,
        'characters': char_count,
        'most_common': most_common,
        'word_frequency': word_freq
    }

sample_text = "Python is amazing Python is powerful Python is fun"
analysis = analyze_text(sample_text)
print(f"Text: '{sample_text}'")
print(f"Word count: {analysis['words']}")
print(f"Character count: {analysis['characters']}")
print(f"Most common word: '{analysis['most_common']}'")
print(f"Word frequency: {analysis['word_frequency']}\n")

# CHALLENGE 3: Number Pattern Generator
print("CHALLENGE 3: Number Pattern Generator")
def print_pattern(n):
    """Print a pyramid pattern with numbers"""
    for i in range(1, n + 1):
        # Print spaces
        print(" " * (n - i), end="")
        # Print numbers
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

print("Pattern for n=5:")
print_pattern(5)
print()

# CHALLENGE 4: Data Validator
print("CHALLENGE 4: Data Validator")
def validate_data(data):
    """Validate different types of data"""
    results = {}
    
    for key, value in data.items():
        if key == 'email':
            # Check if email contains @ and .
            results[key] = '@' in str(value) and '.' in str(value)
        elif key == 'age':
            # Check if age is between 0 and 150
            try:
                age = int(value)
                results[key] = 0 <= age <= 150
            except:
                results[key] = False
        elif key == 'phone':
            # Check if phone has 10 digits
            phone = str(value).replace('-', '').replace(' ', '')
            results[key] = phone.isdigit() and len(phone) == 10
        elif key == 'password':
            # Check if password is at least 8 characters
            results[key] = len(str(value)) >= 8
    
    return results

test_data = {
    'email': 'user@example.com',
    'age': 25,
    'phone': '123-456-7890',
    'password': 'secret123'
}

validation = validate_data(test_data)
print("Data validation results:")
for field, is_valid in validation.items():
    status = "✅ Valid" if is_valid else "❌ Invalid"
    print(f"  {field}: {status}")
print()

# CHALLENGE 5: Simple Game - Number Guessing with Hints
print("CHALLENGE 5: Number Guessing Game with Hints")
def number_guessing_game():
    """Interactive number guessing game"""
    import random
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("I'm thinking of a number between 1 and 100!")
    print(f"You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
            
            # Give hints
            if attempts == max_attempts // 2:
                if secret_number % 2 == 0:
                    print("💡 Hint: The number is even!")
                else:
                    print("💡 Hint: The number is odd!")
            
        except ValueError:
            print("❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid input
    
    print(f"😔 Game Over! The number was {secret_number}")

# Uncomment the next line to play the game
# number_guessing_game()

print("=== END OF CHALLENGES ===")
print("Try running these challenges and experiment with the code!")
print("Modify the functions to add new features!")
print("Create your own variations!")
