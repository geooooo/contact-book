import bottle
import config

import routes.static
import routes.index


bottle.run(
    port=config.PORT,
    debug=config.DEBUG,
    reloader=config.RELOADER
)
