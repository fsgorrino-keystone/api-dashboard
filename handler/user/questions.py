import tornado.web
import json
from postgres import execute_query
from decorators import check_uuid

class UserQuestionsHandler(tornado.web.RequestHandler):
    @check_uuid
    def get(self, uid):
        query = """
            select * from get_user_questions(%s) 
        """
        params = (uid,)
        status, response = execute_query(query, params)
        self.set_status(status)
        self.write(response)
        self.finish()