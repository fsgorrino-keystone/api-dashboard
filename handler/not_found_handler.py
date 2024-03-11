import tornado.web
import json

class NotFoundHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.set_status(404)
        self.write(json.dumps({"error": "Not Found"}))
        self.finish()