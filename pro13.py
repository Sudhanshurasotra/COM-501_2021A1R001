def get_unique_words(file_path):
    unique_words = set()

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase for case-insensitivity
                clean_word = word.strip('.,!?()[]{}":;')
                clean_word = clean_word.lower()
                unique_words.add(clean_word)

    return sorted(list(unique_words))

def main():
    file_path = input("Enter the path of the text file: ")

    try:
        unique_words = get_unique_words(file_path)
        print("Unique words in alphabetical order:")
        for word in unique_words:
            print(word)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
