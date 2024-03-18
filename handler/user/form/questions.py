import tornado.web
import json
from postgres import execute_query
from decorators import check_uuid

class UserFormQuestionsHandler(tornado.web.RequestHandler):
    @check_uuid
    def get(self, uid, form_uid):
        query = """
            select * from get_user_form_questions(%s,%s) 
        """
        params = (uid,form_uid)
        status, response = execute_query(query, params)
        self.set_status(status)
        self.write(response)
        self.finish()