import psycopg2

# Configurazione della connessione al database
conn = psycopg2.connect(
    dbname="dbzu978xtjwlg0",
    user="u60449bmfqkru",
    password="Key2020!",
    host="35.214.216.112",
    port="5432"
)

def execute_query(query, params=None):
    """
    Esegue una query su un database PostgreSQL.
    
    Args:
    query (str): La query SQL da eseguire.
    params (tuple, optional): Parametri da sostituire nella query (se presente). Default è None.
    
    Returns:
    list: Una lista di tuple contenenti i risultati della query.
    """
    
    # Creazione di un oggetto cursore
    cur = conn.cursor()
    try:
        # Esecuzione della query con o senza parametri
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        
        # Recupero dei risultati
        rows = cur.fetchall()
        return rows
    except psycopg2.Error as e:
        print("Errore durante l'esecuzione della query:", e)
    finally:
        # Chiusura del cursore e della connessione
        cur.close()