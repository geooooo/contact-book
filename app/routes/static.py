"""
    Отдача статических файлов
"""

from os import getcwd
from bottle import (
    static_file,
    route
)


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=f"{getcwd()}/static")
