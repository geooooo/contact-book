"""
    Обработка запросов от клиента
    при работе с контактами
"""


import json
from urllib.parse import unquote as urldecode
from bottle import (
    get,
    post,
    put,
    delete,
    route,
    response,
    request,
    hook
)

import storage


@post("/contact")
def contact_add():
    contact = {
        'name':  urldecode(request.params.name),
        'phone': urldecode(request.params.phone),
        'mail':  urldecode(request.params.mail)
    }
    storage.add(contact)


@put("/contact")
def contact_update():
    contact = {
        'id':    int(request.params.id),
        'name':  urldecode(request.params.name),
        'phone': urldecode(request.params.phone),
        'mail':  urldecode(request.params.mail)
    }
    storage.update(contact)


@delete("/contact")
def contact_delete():
    id = int(request.params.id)
    storage.delete(id)


@get("/contact")
def contact_select():
    page_size   = int(request.params.page_size)
    page_number = int(request.params.page_number)
    data = storage.select(page_size, page_number)
    return json.dumps(data)


@get("/contact/filter")
def contact_select_filter():
    page_size     = int(request.params.page_size)
    page_number   = int(request.params.page_number)
    filter_name   = urldecode(request.params.filter_name).lower()
    filter_value  = urldecode(request.params.filter_value)
    if filter_name == "имя":
        filter_name = "name"
    elif filter_name == "номер":
        filter_name = "phone"
    elif filter_name == "почта":
        filter_name = "mail"
    data = storage.select(page_size, page_number, filter_name, filter_value)
    return json.dumps(data)


@hook("after_request")
@route("/contact", method="OPTIONS")
def cors():
    response.set_header('Access-Control-Allow-Headers', 'Access-Control-Allow-Origin, verwrite, Destination, Content-Type, Depth, User-Agent, X-File-Size, X-Requested-With, If-Modified-Since, X-File-Name, Cache-Control')
    response.set_header('Access-Control-Allow-Origin',  '*')
    response.set_header('Access-Control-Allow-Methods', ' PROPFIND, PROPPATCH, COPY, MOVE, DELETE, MKCOL, LOCK, UNLOCK, PUT, GETLIB, VERSION-CONTROL, CHECKIN, CHECKOUT, UNCHECKOUT, REPORT, UPDATE, CANCELUPLOAD, HEAD, OPTIONS, GET, POST')
