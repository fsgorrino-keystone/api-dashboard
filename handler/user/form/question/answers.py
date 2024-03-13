import tornado.web
import json
from postgres import execute_query
from decorators import check_uuid

class UserFormQuestionAnswersHandler(tornado.web.RequestHandler):
    @check_uuid
    def get(self, uid, form_uid, question_uid):
        query = """
            select * from get_user_form_question_answers(%s,%s,%s) 
        """
        params = (uid,form_uid,question_uid)
        results = execute_query(query, params)
        response = {"data": results}
        self.write(json.dumps(response))
        self.finish()