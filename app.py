import sqlite3

DATABASE = 'notes.db'

def create_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    
    conn = sqlite3.connect(DATABASE) # creates a connection to the database, notes.db, stored in the variable DATABASE.
    # A cursor is created to execute commands
    cursor = conn.cursor() 
    cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content)) 
    # By using ? as placeholders, the database engine treats the inputs as data rather than executable code. This mitigates the risk of SQL injection.
    conn.commit()
    conn.close()
    print("Note created successfully!")

def view_notes():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notes') # fetches all records from the notes table.
    notes = cursor.fetchall() # retrieves all the results from the executed SQL command and stores them in the notes variable as a list of tuples.

    if notes:
        for note in notes:
            # print(f"ID: {note[0]}, Title: {note[1]}, Content: {note[2]}")
            print("ID: {}, Title: {}, Content: {}".format(*note))
    else:
        print("No notes found.")
    
    conn.close()

def update_note():
    note_id = input("Enter the ID of the note to update: ")
    title = input("Enter new title: ")
    content = input("Enter new content: ")
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('UPDATE notes SET title = ?, content = ? WHERE id = ?', (title, content, note_id))
    conn.commit()
    conn.close()
    print("Note updated successfully!")

def delete_note():
    note_id = input("Enter the ID of the note to delete: ")
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()
    print("Note deleted successfully!")

def main():
    while True:
        print("\nNote Taking App")
        print("1. Create Note")
        print("2. View Notes")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            create_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            update_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main() # if script is executed directly, then the main function is called and the block of code then runs. 