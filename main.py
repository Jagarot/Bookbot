
def get_book_text(path_to_file):
        with open(path_to_file, 'r') as f:
            text = f.read()
        return text

def main():
    # Relative path to the Frankenstein text file
    path = 'books/frankenstein.txt'
    
    # Get the full text of the book
    book_text = get_book_text(path)
    
    # Print the entire contents to the console
    print(book_text)
    return main