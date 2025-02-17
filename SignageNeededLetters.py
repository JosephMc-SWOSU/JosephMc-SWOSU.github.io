from collections import Counter

def get_needed_letters(old_message: str, new_message: str):
    old_message = old_message.replace(" ", "").lower()
    new_message = new_message.replace(" ", "").lower()
    
    # Count the occurrences of each letter in both messages
    old_counter = Counter(old_message)
    new_counter = Counter(new_message)
    
    # Determine the needed letters
    needed_letters = {}
    for letter, count in new_counter.items():
        if count > old_counter.get(letter, 0):
            needed_letters[letter] = count - old_counter.get(letter, 0)
    
    return needed_letters

if __name__ == "__main__":
    print("Welcome to the Signage Letter Helper Program!")
    print("This program will help you determine which letters you need to bring to update the signage.")
    
    # Read the old and new signage messages
    old_message = input("Enter the old signage message: ")
    new_message = input("Enter the new signage message: ")
    
    # Get the needed letters
    needed_letters = get_needed_letters(old_message, new_message)
    
    # Output the results
    print("\nLetters needed to update the signage:")
    for letter, count in sorted(needed_letters.items()):
        print(f"{letter}: {count}")
    
    print("Thank you for using the Signage Letter Helper Program!")