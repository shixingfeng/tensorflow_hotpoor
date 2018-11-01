#/usr/bin/env/ python
#coding=utf8
import tornado.ioloop
import tornado.web
import httplib
import md5
import urllib
import random

class FirstTensorflowPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template/hello_tsfjs.html")

class CameraHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template/camera.html")