import psycopg2

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="pp2",
    password="pp2_password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()


def init_db():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS game_sessions (
        id SERIAL PRIMARY KEY,
        player_id INTEGER REFERENCES players(id),
        score INTEGER NOT NULL,
        level_reached INTEGER NOT NULL,
        played_at TIMESTAMP DEFAULT NOW()
    );
    """)
    conn.commit()


def get_player(username):
    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    r = cur.fetchone()
    if r:
        return r[0]

    cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (username,))
    conn.commit()
    return cur.fetchone()[0]


def save_game(pid, score, level):
    cur.execute("""
        INSERT INTO game_sessions(player_id, score, level_reached)
        VALUES (%s, %s, %s)
    """, (pid, score, level))
    conn.commit()


def get_top10():
    cur.execute("""
        SELECT p.username, g.score, g.level_reached, g.played_at
        FROM game_sessions g
        JOIN players p ON p.id = g.player_id
        ORDER BY g.score DESC
        LIMIT 10
    """)
    return cur.fetchall()


def best_score(pid):
    cur.execute("SELECT MAX(score) FROM game_sessions WHERE player_id=%s", (pid,))
    return cur.fetchone()[0] or 0