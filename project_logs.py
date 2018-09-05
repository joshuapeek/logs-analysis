#!/usr/bin/env python3
#
# A script to satisfy the requirements of "Logs Analysis" Project
# The first Project of Udacity's "Full Stack Web Developer" Nanodegree
# Code written by Joshua Peek

# import psycopg2, which will be needed to interact with the database
import psycopg2

# define the name of the database to be interacted with
DBNAME = "news"


# 'question_one' function completes the first project requirement
def question_one():
    # connects to 'news' database
    db = psycopg2.connect(database=DBNAME)
    # creates a cursor to execute query
    c = db.cursor()
    # executes query, returning top 3 articles by views
    c.execute(
        "select articles.title, count(articles.title) as views "
        "from articles join log "
        "on log.path like concat('%', articles.slug, '%') "
        "where log.status like '%200%' "
        "group by articles.title "
        "order by views "
        "desc limit 3;"
        )
    # displays 'title' text of question
    print('\n1. What are the most popular three articles of all time?')
    qone = c.fetchall()
    db.close()
    # iterates through each item returned by query,
    # adding formatting to match required display
    for i in qone:
        print('\t'), i[0], ('-'), i[1], ('views')
    return qone


# 'question_two' function completes the first project requirement
def question_two():
    # connects to 'news' database
    db = psycopg2.connect(database=DBNAME)
    # creates a cursor to execute query
    c = db.cursor()
    # executes query, returning top 3 article authors by views
    c.execute(
        "select authors.name, count(articles.title) as views "
        "from authors "
        "join articles on authors.id = articles.author "
        "join log on log.path like concat('%', articles.slug, '%') "
        "where log.status like '%200%' "
        "group by authors.name "
        "order by views desc;"
        )
    # displays 'title' text of question
    print('\n2. Who are the most popular article authors of all time?')
    qtwo = c.fetchall()
    db.close()
    # iterates through each item returned by query,
    # adding formatting to match required display
    for i in qtwo:
        print('\t'), i[0], ('-'), i[1], ('views')
    return qtwo


# 'question_three' function completes the first project requirement
def question_three():
    # connects to 'news' database
    db = psycopg2.connect(database=DBNAME)
    # creates a cursor to execute query
    c = db.cursor()
    # executes query, returning any days where
    # more than 1% of requests led to errors
    c.execute(
        "select "
        "a.date as date, a.error as error, b.success as success, "
        "cast(a.error as float)/cast(b.success as float) as percentage "
        "from (select "
        "to_char(time, 'FMMonth FMDD, FMYYYY') as date, "
        "count(status) as error from log "
        "where status = '404 NOT FOUND' "
        "group by date "
        "order by date desc) a "
        "join (select "
        "to_char(time, 'FMMonth FMDD, FMYYYY') as date, "
        "count(status) as success "
        "from log "
        "where status = '200 OK' "
        "group by date "
        "order by date desc) b "
        "on a.date = b.date "
        "where cast(a.error as float)/cast(b.success as float) > .01;")
    # displays 'title' text of question
    print('\n3. On which days did more than 1% of requests lead to errors?')
    qthree = c.fetchall()
    db.close()
    # iterates through each item returned by query,
    # adding formatting to match required display
    for i in qthree:
        print('\t'), i[0], ('-'), ("{:.1%}".format(i[3])), ('errors')
    return qthree


# print statement assuring user the queries are running and have not stalled
print("\nPlease wait a moment, while data is retrieved from the database.")

# calls functions in order to solve for question one, two then three
question_one()
question_two()
question_three()

# prints a blank line after the last function's return,
# for visual separation from terminal line
print('\n')
