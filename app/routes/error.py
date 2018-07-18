"""
    Страницы ошибок
"""


from bottle import (
    error,
    template
)


@error(404)
def error404(error):
    return template("404.html")


@error(500)
def error500(error):
    return template("500.html")
