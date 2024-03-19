import tornado.web
import json
from postgres import execute_query
from decorators import check_uuid

class UserDashboardDefaultHandler(tornado.web.RequestHandler):
    @check_uuid
    def post(self, uid, dashboard_id):
        query = """
            select * from post_user_dashboard_default(%s,%s) 
        """
        params = (uid,dashboard_id)
        status, response = execute_query(query, params)
        self.set_status(status)
        self.write(response)
        self.finish()