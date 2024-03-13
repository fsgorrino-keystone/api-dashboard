import tornado.web
import json
from postgres import execute_query
from decorators import check_uuid

class UserFormsHandler(tornado.web.RequestHandler):
    @check_uuid
    def get(self, uid):
        query = """
            select * from get_user_forms(%s) 
        """
        params = (uid,)
        results = execute_query(query, params)
        response = {"data": results}
        self.write(json.dumps(response))
        self.finish()