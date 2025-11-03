import sqlite3
import os

def create_database():
    if os.path.exists('students.db'):   # os.path -> buluduğun konumda işlem yapar. students.db varsa kaldır.
        os.remove('students.db')

    conn = sqlite3.connect('students.db')   #veritabanına bağlan ve burada veride gezinip veri okuma, güncelleme işlemleri için imleç oluşturulur.
    cursor = conn.cursor()
    return conn, cursor


def create_table(cursor):
    cursor.execute('''
    CREATE TABLE Students(
        id INTEGER PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR
    )
    ''')

    cursor.execute('''
    CREATE TABLE Courses
    (
        id INTEGER PRIMARY KEY,
        course_name VARCHAR NOT NULL,
        instructor TEXT,
        credits INTEGER
    )
    ''')

def insert_sample_data(cursor):

    student = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle'),
    ]

    cursor.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)", student)

    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Python Programming', 'Prof. Garcia', 2),
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)", courses)

def basic_sql_operations(cursor):

    # 1) SELECT ALL
    print("-----SELECT ALL-----------")
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall() # dataları almak için

    for row in records:
        print(row)

    # 2) SELECT COLUMNS
    print("-----SELECT COLUMNS-----------")
    cursor.execute("SELECT name,age FROM Students")
    print(cursor.fetchall())

    # 3) WHERE clause
    print("-----WHERE clause-----------")
    cursor.execute("SELECT * FROM Students WHERE age = 20")
    records = cursor.fetchall()
    print(records)

    # 4) ORDER BY
    print("-----ORDER BY-----------")
    cursor.execute("SELECT * FROM Students ORDER BY age")
    records = cursor.fetchall() # dataları almak için

    for row in records:
        print(row)

    # 4) LIMIT
    print("-----LIMIT-----------")
    cursor.execute("SELECT * FROM Students LIMIT 3")
    records = cursor.fetchall() # dataları almak için

    for row in records:
        print(row)

def sql_update_delete_insert_operations(conn, cursor):

    # 1) INSERT
    cursor.execute("INSERT INTO Students VALUES (6, 'Frank Miller', 23, 'frank@gmail.com', 'Miami')")
    conn.commit()

    # 2) UPDATE
    cursor.execute("UPDATE Students SET age = 24 WHERE id = 6")
    conn.commit()

    # DELETE
    cursor.execute("DELETE FROM Students WHERE id = 6")
    conn.commit()

def aggregate_functions(cursor):
    # 1) Count

    print("-----AGGREGATE FUNCTIONS COUNT-----------")
    cursor.execute("SELECT COUNT(*) FROM Students")
    result = cursor.fetchall() # fetchone() tek değer dömesi gereken yerlerde kullanılır -> (5,)
    print(result[0][0])

    # 2) Average
    print("-----AGGREGATE FUNCTIONS Average-----------")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 3) MAX - MIN
    print("-----AGGREGATE FUNCTIONS MAX - MIN-----------")
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    result = cursor.fetchone()
    print(result)

    # 3) GROUP BY
    print("-----AGGREGATE FUNCTIONS GROUP BY-----------")
    cursor.execute("SELECT city, COUNT(*) FROM Students GROUP BY city")
    result = cursor.fetchall()
    print(result)


def questions():
    '''
    Basit
    1) Bütün kursların bilgilerini getirin
    2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin
    3) Sadece 21 yaşındaki öğrencileri getirin
    4) Sadece Chicago'da yaşayan öğrencileri getirin
    5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    7) Sadece 3 ve üzeri kredi olan dersleri getirin

    Detaylı
    1) Öğrencileri alphabetic şekilde dizerek getirin
    2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin
    4) Sadece 'New York' ta yaşamayan öğrencileri getirin
    '''

def answer(cursor):

    # 1) Bütün kursların bilgilerini getirin

    print("-----Bütün kursların bilgileri--------")
    cursor.execute("SELECT * FROM Courses")
    result = cursor.fetchall()
    for row in result:
        print(row)

    # 2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin

    print("-----Sadece eğitmenlerin ismini ve ders ismi bilgileri--------")
    cursor.execute("SELECT course_name, instructor FROM Courses")
    result = cursor.fetchall()
    for row in result:
        print(row)

    # 3) Sadece 21 yaşındaki öğrencileri getirin

    print("-----Sadece 21 yaşındaki öğrenciler--------")
    cursor.execute("SELECT * FROM Students WHERE age = 21")
    result = cursor.fetchall()
    for row in result:
        print(row)

    # 4) Sadece Chicago'da yaşayan öğrencileri getirin

    print("-----Sadece Chicago'da yaşayan öğrenciler--------")
    cursor.execute("SELECT * FROM Students WHERE city = 'Chicago'")
    result = cursor.fetchall()
    for row in result:
        print(row)

    # 5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin

    print("-----Sadece 'Dr. Anderson' tarafından verilen dersler--------")
    cursor.execute("SELECT * FROM Courses WHERE instructor = 'Dr. Anderson'")
    result = cursor.fetchall()
    for row in result:
        print(row)

    # 6) Sadece ismi 'A' ile başlayan öğrencileri getirin

    print("-----Sadece ismi 'A' ile başlayan öğrenciler--------")
    cursor.execute("SELECT * FROM Students WHERE name LIKE 'A%'")
    result = cursor.fetchall()
    for row in result:
        print(row)

    # 7) Sadece 3 ve üzeri kredi olan dersleri getirin

    print("-----Sadece 3 ve üzeri kredi olan dersler--------")
    cursor.execute("SELECT * FROM Courses WHERE credits >= 3")
    result = cursor.fetchall()
    for row in result:
        print(row)

    # Detaylı

    print("1. Öğrencileri alphabetic şekilde dizerek getirin")
    cursor.execute("SELECT * FROM Students ORDER BY name")
    print(cursor.fetchall())

    print("2. 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin")
    cursor.execute("SELECT name, age FROM Students WHERE age > 20 ORDER BY name")
    print(cursor.fetchall())

    print("3. Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin")
    cursor.execute("SELECT name, city FROM Students WHERE city IN ('New York', 'Chicago')")
    print(cursor.fetchall())

    print("4. Sadece 'New York' ta yaşamayan öğrencileri getirin")
    cursor.execute("SELECT name, city FROM Students WHERE city != 'New York'")
    print(cursor.fetchall())

def main():
    conn, cursor = create_database()

    try:
        create_table(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_update_delete_insert_operations(conn, cursor)
        aggregate_functions(cursor)
        answer(cursor)
        conn.commit() # başarılı olursa imlecin yaptığı işleri uygula

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()

if __name__ == "__main__":
    main()