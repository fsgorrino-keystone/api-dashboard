import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        response = {"message": "This is a GET request"}
        self.write(json.dumps(response))
        self.finish()
        
    def post(self):
        response = {"message": "This is a POST request"}
        self.write(json.dumps(response))
        self.finish()
        
    def put(self):
        response = {"message": "This is a PUT request"}
        self.write(json.dumps(response))
        self.finish()
        
    def delete(self):
        response = {"message": "This is a DELETE request"}
        self.write(json.dumps(response))
        self.finish()