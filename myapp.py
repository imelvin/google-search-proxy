#!/usr/bin/env python

import os

import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import define, options

import handlers

define("port", default=8888, help="run on the given port", type=int)

settings = {
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
    "template_path" : os.path.join(os.path.dirname(__file__), "template"),
}

def initialize():
	application = tornado.web.Application([
        (r"/", handlers.HomeHandler),
        (r"/search", handlers.SearchHandler),
        ], **settings
    )

	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

def main():
	initialize()

if __name__ == "__main__":
	main()