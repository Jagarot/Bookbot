def get_book_text(path_to_file):
    with open(path_to_file, 'r') as f:
        text = f.read()  # Read the entire content of the file
    return text

def number_of_words(content):  
    words = content.split()  # Split the content into words based on whitespace
    num_words = len(words)  # Count the number of words 
    return num_words  # Return the word count
   

def main():
    # Relative path to the Frankenstein text file
    path = 'books/frankenstein.txt'
    
    # the text
    book_text = get_book_text(path)
    
    # Count the number of words in the book
    num_words = number_of_words(book_text)
    
    # Print the word count to the console
    print (f"{num_words} words found in the document")

# Don't forget this line!
main()
