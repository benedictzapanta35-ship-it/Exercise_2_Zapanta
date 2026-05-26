note = input("Enter a short note/message: ")
try:
    with open("notes.txt", "w") as file:
        file.write(note)
    print("\nNote saved successfully!\n")

    with open("notes.txt", "r") as file:
        content = file.read()
    print("Current content of notes.txt:")
    print(content)

    new_note = input("\nEnter another note to add: ")
    with open("notes.txt", "a") as file:
        file.write("\n" + new_note)

    with open("notes.txt", "r") as file:
        updated_content = file.read()
    print("\nUpdated content of notes.txt:")
    print(updated_content)

except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
