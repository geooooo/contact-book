"""
    Обработка запросов от клиента
    при работе с контактами
"""


import json
from bottle import (
    get,
    post,
    put,
    delete,
    request
)

import storage


@post("/contact")
def contact_add():
    contact = {
        'name':  request.forms.name,
        'phone': request.forms.phone,
        'mail':  request.forms.mail
    }
    storage.add(contact)


@put("/contact")
def contact_update():
    contact = {
        'id':    request.forms.id,
        'name':  request.forms.name,
        'phone': request.forms.phone,
        'mail':  request.forms.mail
    }
    storage.update(contact)


@delete("/contact")
def contact_delete():
    id = int(request.forms.id)
    storage.delete(id)


@get("/contact")
def contact_select():
    page_size   = int(request.query.page_size)
    page_number = int(request.query.page_number)
    data = storage.select(page_size, page_number)
    return json.dumps(data)


@get("/contact/filter")
def contact_select_filter():
    page_size     = int(request.query.page_size)
    page_number   = int(request.query.page_number)
    filter_name   = request.query.filter_name
    filter_value  = request.query.filter_value
    data = storage.select(page_size, page_number, filter_name, filter_value)
    return json.dumps(data)
