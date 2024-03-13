import tornado.web
import json
from postgres import execute_query
from decorators import check_uuid

class UserOptionsHandler(tornado.web.RequestHandler):
    @check_uuid
    def get(self, uid):
        # Ottenere uid dalla parte dinamica dell'URL
        # Esegui le operazioni desiderate con uid
        query = """
            select * from get_user_options(%s) 
        """
        params = (uid,)
        results = execute_query(query, params)
        response = {"data": results}
        self.write(json.dumps(response))

    @check_uuid
    def delete(self,uid):
        # Ottenere uid dalla parte dinamica dell'URL
        # Esegui le operazioni desiderate con uid
        query = """
            select * from delete_user_options(%s) 
        """
        params = (uid,)
        results = execute_query(query, params)
        response = {"data": results}
        self.write(json.dumps(response))
        self.finish()

    @check_uuid
    def post(self,uid):
        # Ottenere uid dalla parte dinamica dell'URL
        # Esegui le operazioni desiderate con uid
        # Analizza il corpo della richiesta JSON
        body = json.loads(self.request.body)
        
        # Estrai le opzioni dal corpo della richiesta, utilizzando valori di default se non presenti
        hideconfigbutton = body.get("hideconfigbutton", False)
        ispinned = body.get("ispinned", False)
        showconfig = body.get("showconfig", False)
        sidebartype = body.get("sidebartype", None)
        isrtl = body.get("isrtl", False)
        color = body.get("color", None)
        isnavfixed = body.get("isnavfixed", False)
        isabsolute = body.get("isabsolute", False)
        shownavs = body.get("shownavs", False)
        showsidenav = body.get("showsidenav", False)
        shownavbar = body.get("shownavbar", False)
        showfooter = body.get("showfooter", False)
        showmain = body.get("showmain", False)
        isdarkmode = body.get("isdarkmode", False)
        navbarfixed = body.get("navbarfixed", None)
        absolute = body.get("absolute", None)

        # Esegui le operazioni desiderate con uid e le opzioni
        query = """
            select * from post_user_options(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            uid,
            hideconfigbutton,
            ispinned,
            showconfig,
            sidebartype,
            isrtl,
            color,
            isnavfixed,
            isabsolute,
            shownavs,
            showsidenav,
            shownavbar,
            showfooter,
            showmain,
            isdarkmode,
            navbarfixed,
            absolute
        )
        results = execute_query(query, params)
        response = {"data": results}
        self.write(json.dumps(response))
        self.finish()

    @check_uuid
    def put(self,uid):
        # Ottenere uid dalla parte dinamica dell'URL
        # Esegui le operazioni desiderate con uid
        # Analizza il corpo della richiesta JSON
        body = json.loads(self.request.body)
        
        # Estrai le opzioni dal corpo della richiesta, utilizzando valori di default se non presenti
        hideconfigbutton = body.get("hideconfigbutton", False)
        ispinned = body.get("ispinned", False)
        showconfig = body.get("showconfig", False)
        sidebartype = body.get("sidebartype", None)
        isrtl = body.get("isrtl", False)
        color = body.get("color", None)
        isnavfixed = body.get("isnavfixed", False)
        isabsolute = body.get("isabsolute", False)
        shownavs = body.get("shownavs", False)
        showsidenav = body.get("showsidenav", False)
        shownavbar = body.get("shownavbar", False)
        showfooter = body.get("showfooter", False)
        showmain = body.get("showmain", False)
        isdarkmode = body.get("isdarkmode", False)
        navbarfixed = body.get("navbarfixed", None)
        absolute = body.get("absolute", None)

        # Esegui le operazioni desiderate con uid e le opzioni
        query = """
            select * from put_user_options(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            uid,
            hideconfigbutton,
            ispinned,
            showconfig,
            sidebartype,
            isrtl,
            color,
            isnavfixed,
            isabsolute,
            shownavs,
            showsidenav,
            shownavbar,
            showfooter,
            showmain,
            isdarkmode,
            navbarfixed,
            absolute
        )
        results = execute_query(query, params)
        response = {"data": results}
        self.write(json.dumps(response))
        self.finish()