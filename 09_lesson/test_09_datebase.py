from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:t6XbHWsGfw6@localhost:5432/postgres"
db = create_engine(db_connection_string)         #  подключение к базе данных

# Получить список предметов
def test_db_connection():
# Используем инспектор для получения информации о таблицах
	inspector = inspect(db)
	names = inspector.get_table_names()
	assert names[1] == 'subject'

# Получить строки из таблицы: select
def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM subject"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['subject_id'] == 1
    assert row1['subject_title'] == "English"
    connection.close()

# Получить строку по одному фильтру
def test_select_1_row():
	connection = db.connect()
	sql_statement = text("SELECT * FROM subject WHERE subject_id = :subject_id")
	result = connection.execute(sql_statement, {"subject_id": 6})
	rows = result.mappings().all()
	assert len(rows) == 1
	assert rows[0]["subject_title"] == "Russian"
	connection.close()

	# Получить строки по двум фильтрам
def test_select_1_row_with_two_filters():
    connection = db.connect()
    sql_statement = text("SELECT * FROM subject " "WHERE \"subject_id\" = :subject_id AND subject_title = :subject_title")
    result = connection.execute(sql_statement, {"subject_id": 9, "subject_title": "Biology"})
    rows = result.mappings().all()

    assert len(rows) == 1

# 	Добавить предмет: insert
def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO subject(\"subject_title\") VALUES (:subject_title)")
    connection.execute(sql, {"subject_title":"Philosophy"})

    transaction.commit()
    connection.close()

# 	Обновить таблицу: update
def test_update():
    connection = db.connect()                      #  подключение к базе данных
    transaction = connection.begin()

    sql = text("UPDATE student SET level = :level WHERE user_id = :user_id")
    connection.execute(sql, {"level": 'Advanced', "user_id": 827})

    transaction.commit()
    connection.close()

# 	Удалить предмет: delete
def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM subject WHERE subject_title = :subject_title")
    connection.execute(sql, {"subject_title": "Philosophy"})

    transaction.commit()
    connection.close()




