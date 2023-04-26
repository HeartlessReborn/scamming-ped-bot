import sqlite3

class Database:
    def __init__(self,db_file):
        "Инициализируем базу данных"
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS  "users" ( "id" INTEGER )')
        self.connection.commit()

    def user_exists(self,user_id):
        "На вход получаем ид пользователя, проверяем его в базе и на выход даем ответ в виде True - имеется и False - отсутсвует."
        with self.connection:
            result = self.cursor.execute('SELECT * FROM users WHERE id = ?',(user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self,user_id):
        "Добавляем пользователя в базу в вход требуется user_id."
        with self.connection:
            return self.cursor.execute('INSERT INTO users(id)VALUES (?)',(user_id,))

    def get_all_users(self):
        "для рассылки,получаем список юзеров"
        with self.connection:
            return self.cursor.execute('SELECT id FROM users').fetchall()
    
        
