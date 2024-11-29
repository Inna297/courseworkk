import pyodbc

def create_db():
    # Параметри підключення до SQL Server
    server = 'localhost'
    database = 'fitnessdb'
    username = 'SA'
    password = 'Inna2006@'

    # Підключення до SQL Server
    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    cursor = conn.cursor()

    # Створення таблиці для користувачів
    cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Users' AND xtype='U')
    CREATE TABLE Users (
        user_id INT PRIMARY KEY IDENTITY(1,1),
        username NVARCHAR(100) NOT NULL,
        email NVARCHAR(100) NOT NULL
    )
    ''')

    # Створення таблиці для тренувань
    cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Workouts' AND xtype='U')
    CREATE TABLE Workouts (
        workout_id INT PRIMARY KEY IDENTITY(1,1),
        user_id INT,
        workout_type NVARCHAR(100) NOT NULL,
        duration INT,
        intensity INT,
        workout_date DATE,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    )
    ''')

    # Створення таблиці для порівняння тренувань
    cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Trainings' AND xtype='U')
    CREATE TABLE Trainings (
        training_id INT PRIMARY KEY IDENTITY(1,1),
        user_id INT,
        workout_type NVARCHAR(100) NOT NULL,
        duration INT,
        intensity INT,
        training_date DATE,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    )
    ''')

    conn.commit()
    conn.close()

create_db()
