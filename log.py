#!/usr/bin/env python3

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
    print("\n======================================================")
    print("What are the most popular three articles of all time ?")
    print("======================================================\n")
    for i, results in enumerate(j):
        print i+1, str(results[0]),   "---",   results[1], "views"


def popular_authors_views():
    cur.execute("select name, views from author_view;")
    j = cur.fetchall()
    print("\n======================================================")
    print("Who are the most popular article authors of all time ?")
    print("======================================================\n")
    for i, results in enumerate(j):
        print i+1, str(results[0]),   "---",   results[1], "views"


def high_error_rate():
    cur.execute("select *from log_view where Error_Percent>1;")
    j = cur.fetchall()
    print("\n======================================================")
    print("On which days did more than 1% of requests lead to errors ?")
    for i, results in enumerate(j):
        print str(results[0]),   "---",   results[1], '%' 'errors'
        print("======================================================")


top_three_article_views()
popular_authors_views()
high_error_rate()
cur.close()
conn.close()
