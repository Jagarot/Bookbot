from stats import number_of_words
from stats import number_of_characters
from stats import sorted_as_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file, 'r') as f:
        text = f.read()  # Read the entire content of the file
    return text
  

def main():
    # Check if a path was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command-line arguments
    path = sys.argv[1]
    
    # the text
    book_text = get_book_text(path)
    
    # Count the number of words in the book
    num_words = number_of_words(book_text)

    #Counts the number of each character in the book
    char_counts = number_of_characters(book_text)

    sorted_char_list = sorted_as_list (char_counts)

    #Print the text before the information 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    # Print the word count to the console
    print (f"Found {num_words} total words")
    #Print the character count
    print("--------- Character Count -------")
    for char, count in sorted_char_list:
        if char.isalpha():  # Only print alphabetic characters
         print(f"{char}: {count}")
    print("============= END ===============")




# Don't forget this line!
main()
