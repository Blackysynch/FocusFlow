import sqlite3
    
def init_db():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    
    # Create the notes table with user_id column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            user_id INTEGER NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Table created successfully.")

if __name__ == "__main__":
    init_db() 