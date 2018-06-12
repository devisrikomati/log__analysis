import psycopg2

conn = psycopg2.connect(dbname='news', user='vagrant', password='vagrant')
cur = conn.cursor()
try:
    print("successfully connected")
except Exception as e:
        print(e)


def top_three_article_views():
    cur.execute("select title,views from article_views limit 3;")
    j = cur.fetchall()
    print("The most popular three articles of all time are:")
    for i in j:
        print(str(i)+"--->views")


def popular_authors_views():
    cur.execute("select name, views from author_view;")
    j = cur.fetchall()
    print("The most popular authors of all time are:")
    for i in j:
        print(str(i)+"--->views")


def high_error_rate():
    cur.execute("select *from log_view where Error_Percent>1;")
    j = cur.fetchall()
    print("more than 1% of requests lead to errors")
    for i in j:
        print(str(i)+"--->errors")


top_three_article_views()
popular_authors_views()
high_error_rate()
cur.close()
conn.close()

