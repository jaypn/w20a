import dbcreds
import mariadb
def select_all_posts(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM  w20.blog_post")
    allPost = cursor.fetchall()
    print(allPost)
    cursor.close()

def update_info(username,content):
    content = input("please give us some content about you: ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO w20.blog_post(username, content, id) VALUES(?,?, NULL)",[username,content])
    conn.commit()
    cursor.close()

conn = mariadb.connect(user=dbcreds.user,password=dbcreds.password,host=dbcreds.host,database=dbcreds.database,port=dbcreds.port)

username = input("what is your username?: ")
option = input("What option would you like to select? (1: INSERT or 2: SEE ALL) ")

if option == '1':
    update_info(username,option)
    
elif option == '2':
    select_all_posts(conn)
    
conn.close()