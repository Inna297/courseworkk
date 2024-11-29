import pyodbc

# Параметри підключення до SQL Server
server = 'localhost'  # Адреса сервера
database = 'fitnessdb'  # Назва бази даних
username = 'SA'  # Ваше ім'я користувача
password = 'Inna2006@'  # Ваш пароль

# Підключення до SQL Server
conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
cursor = conn.cursor()

# Функція для додавання нового користувача
def add_user(username, email):
    cursor.execute("INSERT INTO Users (username, email) VALUES (?, ?)", (username, email))
    conn.commit()
    print(f"Користувач {username} доданий!")

# Функція для додавання тренування
def add_training(user_id, workout_type, duration, intensity, workout_date):
    cursor.execute("INSERT INTO Workouts (user_id, workout_type, duration, intensity, workout_date) VALUES (?, ?, ?, ?, ?)",
                   (user_id, workout_type, duration, intensity, workout_date))
    conn.commit()
    print(f"Тренування для користувача з ID {user_id} додано!")

# Тестові додавання
add_user('Oleg', 'jleh@gmail.com')
add_training(1, 'Running', 45, 7, '2024-11-26')
add_training(1, 'Swimming', 30, 5, '2024-11-27')

# Закриття підключення
conn.close()

