def count_characters(file_path):
    with open(file_path, 'r') as f:
        content = f.read().lower()
    
    e_count = content.count('e')
    t_count = content.count('t')
    
    print(f"File: {file_path}")
    print(f"e: {e_count}")
    print(f"t: {t_count}")

# Test all three books
count_characters("books/frankenstein.txt")
count_characters("books/mobydick.txt")
count_characters("books/prideandprejudice.txt")