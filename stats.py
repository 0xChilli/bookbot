def get_num_words(book_text):
    list_of_text = book_text.split()        
    return len(list_of_text)

def count_chars(text):
    # Create an empty dictionary to store character counts
    char_count = {}
    
    # Loop through each character in the text
    for char in text:
        # Convert the character to lowercase
        char = char.lower()
        
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # Otherwise, add it to the dictionary with a count of 1
        else:
            char_count[char] = 1
            
    return char_count

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(char_counts):
    # Create a list to store dictionaries
    result = []
    
    # Convert each key-value pair in the dictionary to a dictionary
    for char, count in char_counts.items():
        # Create a dictionary for each character
        char_dict = {"char": char, "num": count}
        # Add the dictionary to the result list
        result.append(char_dict)
    
    # Sort the list in descending order using the sort_on function
    result.sort(reverse=True, key=sort_on)
    
    return result
    

def report(word_count, char_counts):
    # First convert the dictionary to a sorted list
    sorted_chars = chars_dict_to_sorted_list(char_counts)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count in the sorted order
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")
    