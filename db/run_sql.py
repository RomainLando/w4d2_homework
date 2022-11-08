import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    results= []

    try:
        #connect to DB
        conn = psycopg2.connect("dbname='task_manager'")
        #define a cursor 
        cur = conn.cursor( cursor_factory=ext.DictCursor )
        # execute sql
        cur.execute( sql, values )
        #commit
        conn.commit()
        #fetch rresults
        results = cur.fetchall()
        #close connection
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        #print an error
        print(error)
    finally:
        #close connection
        if conn is not None:
            conn.close()
    # return results
    return results