import tornado.ioloop
from handler.main_handler import MainHandler
from handler.not_found_handler import NotFoundHandler
from handler.user.options import UserOptionsHandler

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
         (r"/user/([^/]+)/options", UserOptionsHandler),
    ], default_handler_class=NotFoundHandler)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)  # Il server ascolta sulla porta 8888
    tornado.ioloop.IOLoop.current().start()