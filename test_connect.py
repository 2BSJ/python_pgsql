import psycopg2
try:
    conn = psycopg2.connect(
        user='webdb',
        password='webdb',
        host='192.168.1.92',
        port='5432',
        database='webdb')

    cursor = conn.cursor()
    cursor.execute('select version()')
    record = cursor.fetchone()

    print('connected to -  ',record)
except Exception as e:
    print(f'error:{e}')
finally:
    'conn' in locals() and conn and conn.close()
    #conn and conn.close() // conn 객체가 안만들어져 있던것처럼 보여서 close를 몬함