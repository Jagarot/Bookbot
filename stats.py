from collections import Counter

def number_of_words(content):  
    words = content.split()  # Split the content into words based on whitespace
    num_words = len(words)  # Count the number of words 
    return num_words  # Return the word count

def number_of_characters(context):
    # Remove the file opening code - we already have the content in "context"
    context = context.lower()
    char_counts = {}
    # Count each character
    for char in context:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
def sorted_as_list(char_counts):
    # Create a list of tuples (char, count)
    chars_list = [(char, count) for char, count in char_counts.items()]
    
    # Sort by count in descending order
    chars_list.sort(key=lambda x: x[1], reverse=True)
    return chars_list
    
    # Sort by count in descending order
    chars_list.sort(key=lambda x: x["count"], reverse=True)
    return chars_list
    
