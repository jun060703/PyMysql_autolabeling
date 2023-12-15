import pymysql
import time

db_config = {
    "host": "yout_host",
    "user": "yout_user",
    "password": "yout_password",
    "db": "your_db",
    "charset": "utf8"
}

conn = None     

try:
    while True:
        conn = pymysql.connect(**db_config)

        with conn.cursor() as cursor:
            update_query = """
            UPDATE tag_all     
            SET label_g = 1    
            WHERE your_조건
            """
            result = cursor.execute(update_query)   #update해주는
            print(f"쿼리 실행 결과: {result}")
            time.sleep(0.1)

        conn.commit()

except pymysql.MySQLError as e:
    print(f"에러 발생: {e}")  #에러발생 이유

finally:
    if conn:
        conn.close()
