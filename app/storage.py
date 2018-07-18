"""
    Модуль, отвечающий за работу с БД
"""


import sqlite3
import config
import os.path


# Соединение с БД
_connect = None


def add(contact):
    """
        Добавление контакта
        contact: {
            name  - имя
            phone - номер
            mail  - электронная почта
        }
    """
    sql = """
        INSERT INTO Contact
            (name, phone, mail)
        VALUES
            ('{name}', '{phone}', '{mail}')
    """.format(**contact)
    _execute(sql)


def update(contact):
    """
        Обновление контакта
        contact: {
            id    - уникальный идентификатор
            name  - имя
            phone - номер
            mail  - электронная почта
        }
    """
    sql = """
        UPDATE Contact
        SET
            name  = '{name}',
            phone = '{phone}',
            mail  = '{mail}'
        WHERE
            id = {id}
    """.format(**contact)
    _execute(sql)


def delete(id):
    """
        Удаление контакта

        id - уникальный идентификатор
    """
    sql = f"""
        DELETE FROM Contact
        WHERE id = {id}
    """
    _execute(sql)


def select(page_size, page_number, filter_name=None, filter_value=None):
    """
        Выборка данных

        page_size    - количество контактов на странице
        page_number  - номер страницы
        filter_name  - имя поля, по которому идёт фильтрация
        filter_value - значение фильтра
    """
    offset = page_size * (page_number - 1)
    where = ""
    if filter_name:
        where = f"""
            WHERE {filter_name} LIKE '{filter_value}%'
        """
    sql = f"""
        SELECT
            id,
            name,
            phone,
            mail
        FROM Contact
        {where}
        LIMIT {page_size} OFFSET {offset}
    """
    data = _execute(sql, is_select=True)
    sql = f"""
        SELECT
            COUNT(id)
        FROM Contact
        {where}"""
    cursor = _open()
    cursor.execute(sql)
    data["count"] = int(cursor.fetchone()[0])
    _close()
    return data


def _open():
    """
        Открыть соединение и получить курсор
    """
    global _connect
    _connect = sqlite3.connect(config.DB_NAME)
    return _connect.cursor()


def _close():
    """
        Закрыть соединение с БД
    """
    global _connect
    _connect.close()


def _execute(sql_query, is_select=False):
    """
        Выполнить SQL запрос
    """
    global _connect
    cursor = _open()
    cursor.execute(sql_query)
    _connect.commit()
    if is_select:
        data = {
            "contacts": [],
        }
        for record in cursor.fetchall():
            data["contacts"].append({
                "id":    record[0],
                "name":  record[1],
                "phone": record[2],
                "mail":  record[3]
            })
        return data


# Инициализация БД, если этого не было сделано

_is_empty_storage_file = (not os.path.exists(config.DB_NAME) or
                        os.path.getsize(config.DB_NAME) == 0)

if _is_empty_storage_file:
    _execute("""
        CREATE TABLE Contact (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            mail TEXT NOT NULL
        )
    """)
