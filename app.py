import sqlite3
import customtkinter as ctk

DATABASE = 'notes.db'

def create_note():
    """Create a new note in the database."""
    user_id = user_id_entry.get()
    title = title_entry.get()
    content = content_entry.get("1.0", "end-1c")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notes (title, content, user_id) VALUES (?, ?, ?)', (title, content, user_id))
    conn.commit()
    conn.close()

    title_entry.delete(0, 'end')
    content_entry.delete("1.0", "end")
    user_id_entry.delete(0, 'end')

    print("Note created successfully!")
    display_last_note()  # Show only the last created note

def view_last_note():
    """Retrieve the last note from the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notes ORDER BY id DESC LIMIT 1')
    note = cursor.fetchone()
    conn.close()
    return note

def display_last_note():
    """Display the last created note in the text box."""
    note = view_last_note()
    all_notes_textbox.delete("1.0", "end")  # Clear the previous text
    if note:
        all_notes_textbox.insert('end', f"ID: {note[0]}, Title: {note[1]}, Content: {note[2]}, User ID: {note[3]}\n\n")

def view_notes():
    """Retrieve all notes from the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()
    conn.close()
    return notes

def update_note():
    """Update an existing note in the database."""
    note_id = note_id_entry.get()
    if note_id:
        title = title_entry.get()
        content = content_entry.get("1.0", "end-1c")

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('UPDATE notes SET title = ?, content = ? WHERE id = ?', (title, content, note_id))
        conn.commit()
        conn.close()
        title_entry.delete(0, 'end')
        content_entry.delete("1.0", "end")
        note_id_entry.delete(0, 'end')
        print("Note updated successfully!")
        display_all_notes()  # Refresh the displayed notes

def delete_note():
    """Delete a note from the database."""
    note_id = note_id_entry.get()
    if note_id:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
        conn.commit()
        conn.close()
        print("Note deleted successfully!")
        display_all_notes()  # Refresh the displayed notes

def display_all_notes():
    """Display all notes in the text box."""
    notes = view_notes()
    all_notes_textbox.delete("1.0", "end")  # Clear the previous text
    for note in notes:
        all_notes_textbox.insert('end', f"ID: {note[0]}, Title: {note[1]}, Content: {note[2]}, User ID: {note[3]}\n\n")

# GUI Setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Note Taking App")
app.geometry("500x600")

# Central Frame
central_frame = ctk.CTkFrame(app)
central_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Input fields
user_id_label = ctk.CTkLabel(central_frame, text="User ID:")
user_id_label.grid(row=0, column=0, pady=5, sticky='w')  # Align left
user_id_entry = ctk.CTkEntry(central_frame, width=1200)  # Set a fixed width
user_id_entry.grid(row=0, column=1, pady=5, sticky='w')  # Align left

title_label = ctk.CTkLabel(central_frame, text="Title:")
title_label.grid(row=1, column=0, pady=5, sticky='w')  # Align left
title_entry = ctk.CTkEntry(central_frame, width=1200)  # Set a fixed width
title_entry.grid(row=1, column=1, pady=5, sticky='w')  # Align left

content_label = ctk.CTkLabel(central_frame, text="Content:")
content_label.grid(row=2, column=0, pady=5, sticky='w')  # Align left
content_entry = ctk.CTkTextbox(central_frame, width=1200, height=100)  # Set width
content_entry.grid(row=2, column=1, pady=5, sticky='w')  # Align left

note_id_label = ctk.CTkLabel(central_frame, text="Note ID (for update/delete):")
note_id_label.grid(row=3, column=0, pady=5, sticky='e')  # Align right
note_id_entry = ctk.CTkEntry(central_frame, width=1200)  # Set a fixed width
note_id_entry.grid(row=3, column=1, pady=5, sticky='w')  # Align left

# Buttons
button_frame = ctk.CTkFrame(central_frame)
button_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=30, sticky='nsew')

button_width = 295  # Set a fixed width for buttons
create_button = ctk.CTkButton(button_frame, text="Create Note", command=create_note, width=button_width)
create_button.grid(row=0, column=0, padx=5)

view_button = ctk.CTkButton(button_frame, text="View All Notes", command=display_all_notes, width=button_width)
view_button.grid(row=0, column=1, padx=5)

update_button = ctk.CTkButton(button_frame, text="Update Note", command=update_note, width=button_width)
update_button.grid(row=0, column=2, padx=5)

delete_button = ctk.CTkButton(button_frame, text="Delete Note", command=delete_note, width=button_width)
delete_button.grid(row=0, column=3, padx=5)

# Box for displaying all notes
all_notes_textbox = ctk.CTkTextbox(central_frame, width=295)  # Set width
all_notes_textbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

# Configure additional row weight for the textbox
central_frame.grid_rowconfigure(5, weight=1)

# Configure column weight to ensure even distribution
central_frame.grid_columnconfigure(0, weight=0)  # Label column
central_frame.grid_columnconfigure(1, weight=1)  # Entry column

app.mainloop()