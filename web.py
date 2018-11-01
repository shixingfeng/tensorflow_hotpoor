#/usr/bin/env/ python
#coding=utf8
import os
import tornado.ioloop
import tornado.web
import httplib
import md5
import urllib
import random
import tensorflow


settings ={
    "debug" : True,
    "static_path" : os.path.join(os.path.dirname(__file__),"static"),
}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Tensorflow,I'm shixing_feng!")

def make_app():
    return tornado.web.Application([
        (r"/tensorflow_page",tensorflow.FirstTensorflowPageHandler),
        (r"/tensorflow_camera",tensorflow.CameraHandler),
        (r"/", MainHandler),
    ],**settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
