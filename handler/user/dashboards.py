import tornado.web
import json
from postgres import execute_query
from decorators import check_uuid

class UserDashboardsHandler(tornado.web.RequestHandler):
    @check_uuid
    def put(self, uid):
        body = json.loads(self.request.body)
        
        # Estrai le opzioni dal corpo della richiesta, utilizzando valori di default se non presenti
        name = body.get("name", None)
        description = body.get("description", None)
        if name != None:
            query = """
                select * from put_user_dashboards(%s,%s,%s) 
            """
            params = (uid,name,description)
            status, response = execute_query(query, params)
            self.set_status(status)
            self.write(response)
        else:
            self.set_status(422)
            self.write(json.dumps({"error": "Name non setted"}))
        self.finish()