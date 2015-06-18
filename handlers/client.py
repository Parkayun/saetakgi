#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web


class ClientIndexHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
    	if self.get_argument('s', '') == '!':
    		self.render("saetakgi.html")
    	else:
        	self.render("index.html")
