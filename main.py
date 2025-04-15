def get_book_text(path_to_file):
    with open(path_to_file, 'r') as f:
        text = f.read()  # Read the entire content of the file
    return text

def number_of_words(content):  # Accept the content as an argument
    words = content.split()  # Split the content into words based on whitespace
    word_count = len(words)  # Count the number of words
    return word_count  # Return the word count

def main():
    # Relative path to the Frankenstein text file
    path = 'books/frankenstein.txt'
    
    # Get the full text of the book
    book_text = get_book_text(path)
    
    # Count the number of words in the book
    word_count = number_of_words(book_text)
    
    # Print the word count to the console
    print(f"Word count: {word_count}")

# Don't forget this line!
main()
