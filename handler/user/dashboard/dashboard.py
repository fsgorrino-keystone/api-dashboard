import tornado.web
import json
from postgres import execute_query
from decorators import check_uuid

class UserDashboardHandler(tornado.web.RequestHandler):
    @check_uuid
    def delete(self, uid, dashboard_uid):
        query = """
            select * from delete_user_dashboard(%s,%s) 
        """
        params = (uid,dashboard_uid)
        status, response = execute_query(query, params)
        self.set_status(status)
        self.write(response)
        self.finish()