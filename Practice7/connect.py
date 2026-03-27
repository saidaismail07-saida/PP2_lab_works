import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="phonebook_db",     # имя вашей базы данных
            user="postgres",           # ваш PostgreSQL пользователь
            password="your_password",  # ваш пароль
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Ошибка подключения к базе данных:", e)
        return None