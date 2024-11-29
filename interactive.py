import pyodbc

# Параметри підключення до SQL Server
server = 'localhost'
database = 'fitnessdb'
username = 'SA'
password = 'Inna2006@'

# Підключення до SQL Server
try:
    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    cursor = conn.cursor()
    print("Підключено до бази даних!")
except Exception as e:
    print(f"Помилка підключення: {e}")

# Функція для додавання нового користувача
def add_user():
    username = input("Введіть ім'я користувача: ")
    email = input("Введіть email користувача: ")
    
    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    cursor = conn.cursor()

    # Вставка нового користувача в таблицю Users
    cursor.execute(''' 
    INSERT INTO Users (username, email) VALUES (?, ?)
    ''', (username, email))

    conn.commit()

    # Отримуємо ID останнього доданого користувача
    cursor.execute('SELECT last_insert_rowid()')
    user_id = cursor.fetchone()[0]

    print(f"Користувач доданий з ID: {user_id}")
    
    conn.close()

# Функція для додавання нового тренування
def add_training():
    user_id = input("Введіть ID користувача: ")
    workout_type = input("Введіть тип тренування: ")
    duration = int(input("Введіть тривалість тренування (хв): "))
    intensity = int(input("Введіть інтенсивність тренування (1-10): "))
    date = input("Введіть дату тренування (YYYY-MM-DD): ")
    
    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    cursor = conn.cursor()

    # Вставка нового тренування в таблицю Trainings
    cursor.execute(''' 
    INSERT INTO Trainings (user_id, workout_type, duration, intensity, training_date) 
    VALUES (?, ?, ?, ?, ?)
    ''', (user_id, workout_type, duration, intensity, date))

    conn.commit()
    print("Тренування додано!")
    
    conn.close()

# Функція для порівняння тренувань між користувачами
def compare_users():
    # Введення ID користувачів для порівняння
    user_ids = input("Введіть ID користувачів, яких хочете порівняти (через кому): ").split(',')

    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    cursor = conn.cursor()

    # Створення списків для даних про тренування
    user_names = []  # Для зберігання імен користувачів
    durations = []  # Для зберігання тривалості тренувань
    intensities = []  # Для зберігання інтенсивності тренувань

    # Перебираємо ID користувачів і отримуємо їх тренування
    for user_id in user_ids:
        user_id = user_id.strip()  # Видаляємо зайві пробіли
        cursor.execute(''' 
        SELECT u.username, t.workout_type, t.duration, t.intensity, t.training_date
        FROM Users u
        JOIN Trainings t ON u.user_id = t.user_id
        WHERE u.user_id = ?
        ''', (user_id,))

        # Додаємо користувача і його тренування до списків
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                user_names.append(row[0])  # Додаємо ім'я користувача
                durations.append(row[2])  # Додаємо тривалість тренування
                intensities.append(row[3])  # Додаємо інтенсивність тренування
        else:
            print(f"Тренування для користувача з ID {user_id} не знайдено.")
    
    conn.close()

    # Якщо є дані, вивести їх у вигляді таблиці
    if user_names:
        from prettytable import PrettyTable
        table = PrettyTable()
        table.field_names = ["Користувач", "Тип тренування", "Тривалість", "Інтенсивність", "Дата тренування"]

        for i in range(len(user_names)):
            table.add_row([user_names[i], workout_type, durations[i], intensities[i], training_date])

        print(table)

# Основний цикл для взаємодії з користувачем
def main():
    while True:
        print("1. Додати користувача")
        print("2. Додати тренування")
        print("3. Порівняти тренування користувачів")
        print("4. Вийти")
        option = input("Виберіть опцію: ")

        if option == "1":
            add_user()
        elif option == "2":
            add_training()
        elif option == "3":
            compare_users()  # Викликає функцію порівняння
        elif option == "4":
            break
        else:
            print("Невірна опція. Спробуйте ще раз.")

# Запускаємо основний цикл
if __name__ == "__main__":
    main()
