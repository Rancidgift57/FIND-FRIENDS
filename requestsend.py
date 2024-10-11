import psycopg2

def frireq(old, new):
    hostname = 'localhost'
    database = 'newdata'
    username = 'postgres'
    pwd = 'root'
    port_id = 5432
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )
        cur = conn.cursor()
        create_script = f'''update friendfinf set "password"='{new}' where "password"='{old}';'''
        cur.execute(create_script)
        conn.commit()
        return cur.fetchall()  # This line may need modification based on your use case
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()

#frireq('tanmay', 60)
