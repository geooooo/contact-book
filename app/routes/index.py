"""
    Отдача главной страницы приложения
"""


from bottle import (
    get,
    template
)


@get("/")
def index():
    return template("index.html")
