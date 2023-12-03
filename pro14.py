def write_to_file(file_path, lines):
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')

def main():
    file_path = "MyFile.txt"
    lines = []

    print("Please enter three lines:")
    for i in range(3):
        line = input(f"Line {i+1}: ")
        lines.append(line)

    try:
        write_to_file(file_path, lines)
        print(f"Lines written to '{file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
