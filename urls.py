# -*- coding:utf-8 -*-
from handlers.client import ClientIndexHandler
from handlers.server import ServerIndexHandler


url_patterns = [
    (r'^/$', ClientIndexHandler),

    (r'^/w$', ServerIndexHandler),
]