import pyodbc
from datetime import datetime

def get_workouts_for_period(start_date, end_date):
    # Параметри підключення до SQL Server
    server = 'localhost'
    database = 'fitnessdb'
    username = 'SA'
    password = 'Inna2006@'

    # Підключення до SQL Server
    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    cursor = conn.cursor()

    # Виконання SQL-запиту для отримання тренувань за період
    cursor.execute('''
    SELECT u.username, w.workout_type, w.duration, w.intensity, w.workout_date
    FROM Workouts w
    JOIN Users u ON w.user_id = u.user_id
    WHERE w.workout_date BETWEEN ? AND ?
    ORDER BY w.workout_date
    ''', (start_date, end_date))

    # Отримуємо всі результати
    workouts = cursor.fetchall()

    # Виведення результатів
    if workouts:
        print(f"Тренування з {start_date} по {end_date}:")
        for workout in workouts:
            print(f"Користувач: {workout[0]}, Тип тренування: {workout[1]}, "
                  f"Тривалість: {workout[2]} хв, Інтенсивність: {workout[3]}, Дата: {workout[4]}")
    else:
        print(f"Немає тренувань в період з {start_date} по {end_date}")

    # Закриваємо з'єднання з базою даних
    conn.close()

# Встановлення дат для отримання статистики
start_date = '2024-11-01'
end_date = '2024-11-30'

# Викликаємо функцію для отримання статистики
get_workouts_for_period(start_date, end_date)

