# empty playground for tests
# Reading a file using open() function
file_path = "example.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

# Writing to a file using open() function
new_content = "This is the new content of the file."
try:
    with open(file_path, "w") as file:
        file.write(new_content)
        print("File updated successfully.")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")