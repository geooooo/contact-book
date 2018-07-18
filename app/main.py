"""
    Главный файл приложения
"""


import bottle
import config

import routes.error
import routes.static
import routes.index
import routes.contact


bottle.run(
    port=config.PORT,
    debug=config.DEBUG,
    reloader=config.RELOADER
)
