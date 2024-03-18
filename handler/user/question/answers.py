import tornado.web
import json
from postgres import execute_query
from decorators import check_uuid

class UserQuestionAnswersHandler(tornado.web.RequestHandler):
    @check_uuid
    def get(self, uid, question_uid):
        # Ottenere uid dalla parte dinamica dell'URL
        # Esegui le operazioni desiderate con uid
        query = """
            select * from get_user_question_answers(%s,%s) 
        """
        params = (uid,question_uid)
        status, response = execute_query(query, params)
        self.set_status(status)
        self.write(response)
        self.finish()