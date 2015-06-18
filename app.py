# -*- coding:utf-8 -*-
import os
import sys

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options

from urls import url_patterns


PROJECT_PATH = os.path.dirname(__file__)


class TornadoApplication(tornado.web.Application):
    def __init__(self):
        settings = {
            "debug": True,
            "static_path": os.path.join(PROJECT_PATH, "static"),
            "template_path": os.path.join(PROJECT_PATH, "templates")
        }
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    try:
        port = int(sys.argv[1])
    except:
        port = 8080

    app = TornadoApplication()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(port)
    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
