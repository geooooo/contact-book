"""
    Создание тестовой БД
"""


from os import remove
remove("storage.db")

import storage as s


# Заполнение таблицы
for i in range(100):
    s.add({
        "name":  f"name{i}",
        "phone": f"{i}{i}{i}",
        "mail":  f"name{i}@mail.ru"
    })
