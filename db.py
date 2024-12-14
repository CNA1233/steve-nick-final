import sqlite3

DATABASE = 'players2.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    try:
        with get_db() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS player (
                    player_id INTEGER PRIMARY KEY NOT NULL,
                    bat_order INTEGER NOT NULL,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    position TEXT NOT NULL,
                    at_bats INTEGER,
                    hits INTEGER
                );
            ''')
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")

def get_all_players():
    conn = get_db()
    players = conn.execute('SELECT * FROM player').fetchall()
    conn.close()
    return players


def add_player(bat_order, first_name, last_name, position, at_bats, hits):
    conn = get_db()
    conn.execute('''
        INSERT INTO player (bat_order, first_name, last_name, position, at_bats, hits)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (bat_order, first_name, last_name, position, at_bats, hits))
    conn.commit()


def update_player(player_id, bat_order, first_name, last_name, position, at_bats, hits):
    conn = get_db()
    conn.execute('''
        UPDATE player
        SET bat_order = ?, first_name = ?, last_name = ?, position = ?, at_bats = ?, hits = ?
        WHERE player_id = ?
    ''', (bat_order, first_name, last_name, position, at_bats, hits, player_id))
    conn.commit()


def delete_player(player_id):
    conn = get_db()
    conn.execute('DELETE FROM player WHERE player_id = ?', (player_id,))
    conn.commit()