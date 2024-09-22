# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is the first line.\n")
        file.write("The second line contains a number: 42.\n")
        file.write("Finally, here is the third line.\n")
    print("File created and initial content written successfully.")

except Exception as e:
    print(f"An error occurred while creating the file: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nContents of 'my_file.txt':")
        print(content)

except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except PermissionError:
    print("Error: Permission denied while trying to read the file.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    # Open "my_file.txt" in append mode
    with open("my_file.txt", "a") as file:
        file.write("Appending a new line to the file.\n")
        file.write("This is another line added to the file.\n")
        file.write("And here's one more line.\n")
    print("Additional lines appended successfully.")

except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except PermissionError:
    print("Error: Permission denied while trying to append to the file.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

finally:
    print("\nFile handling operations completed.")
