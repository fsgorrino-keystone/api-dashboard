import uuid
from functools import wraps
import tornado.web
import json

def check_uuid(func):
    @wraps(func)
    def wrapper(request_handler, *args, **kwargs):
        # Controlla tutte le variabili
        request_uuid = request_handler.request.headers.get("X-User-ID")
        if request_uuid == None:
            request_handler.set_status(400)
            request_handler.write(json.dumps({"errore": f"'X-User-ID' non è un impostato."}))
            request_handler.finish()
            return
        try:
            # Prova a creare un oggetto UUID dalla stringa fornita
            uuid_obj = uuid.UUID(request_uuid)
        except ValueError:
            # Se viene generato un ValueError, la variabile non è un UUID valido
            request_handler.set_status(400)
            request_handler.write(json.dumps({"errore": f"'{request_uuid}' non è un utente valido."}))
            request_handler.finish()
            return
        for arg in args:
            try:
                # Prova a creare un oggetto UUID dalla stringa fornita
                uuid_obj = uuid.UUID(arg)
            except ValueError:
                # Se viene generato un ValueError, la variabile non è un UUID valido
                request_handler.set_status(400)
                request_handler.write(json.dumps({"errore": f"'{arg}' non è un UUID valido."}))
                request_handler.finish()
                return

        # Se tutte le variabili sono UUID valide, esegui la funzione
        return func(request_handler, request_uuid, *args, **kwargs)
    return wrapper