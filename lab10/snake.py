import sqlite3

conn = sqlite3.connect("snake_game.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    level INTEGER,
    score INTEGER,
    FOREIGN KEY(user_id) REFERENCES user(id)
);
""")
conn.commit()

def create_user(username):
    cursor.execute("INSERT OR IGNORE INTO user (username) VALUES (?)", (username,))
    conn.commit()

def get_user_level(username):
    cursor.execute("SELECT user_score.level FROM user_score \
                    JOIN user ON user.id = user_score.user_id \
                    WHERE user.username = ? \
                    ORDER BY user_score.id DESC LIMIT 1", (username,))
    result = cursor.fetchone()
    return result[0] if result else 1

def save_user_score(username, level, score):
    cursor.execute("SELECT id FROM user WHERE username = ?", (username,))
    user_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO user_score (user_id, level, score) VALUES (?, ?, ?)", (user_id, level, score))
    conn.commit()

if __name__ == "__main__":
    username = input("Enter your username: ")
    create_user(username)
    level = get_user_level(username)
    print(f"Starting at level: {level}")

    # Simulated pause and score save (in real game, trigger this with a pause key)
    score = int(input("Enter current score to save: "))
    save_user_score(username, level, score)
    print("Game state saved!")
