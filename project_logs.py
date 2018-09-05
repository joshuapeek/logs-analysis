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
    # defines, then executes query,
    # returning top 3 articles by views
    query = """
    SELECT articles.title,
       count(articles.title) AS views
    FROM articles
    JOIN log ON log.path = '/article/' || articles.slug
    WHERE log.status = '200 OK'
    GROUP BY articles.title
    ORDER BY views DESC
    LIMIT 3;
    """
    c.execute(query)
    # displays 'title' text of question
    print('\n1. What are the most popular three articles of all time?')
    qone = c.fetchall()
    db.close()
    # iterates through each item returned by query,
    # adding formatting to match required display
    for i in qone:
        print('\t "{}" - {} views'.format(i[0], i[1]))
    return qone


# 'question_two' function completes the first project requirement
def question_two():
    # connects to 'news' database
    db = psycopg2.connect(database=DBNAME)
    # creates a cursor to execute query
    c = db.cursor()
    # defines, then executes query,
    # returning top 3 article authors by views
    query = """
    SELECT authors.name,
       count(articles.title) AS views
    FROM authors
    JOIN articles ON authors.id = articles.author
    JOIN log ON log.path = '/article/' || articles.slug
    WHERE log.status = '200 OK'
    GROUP BY authors.name
    ORDER BY views DESC;
    """
    c.execute(query)
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
    query = """
    SELECT a.date AS date,
        a.error AS error,
        b.success AS success,
        cast(a.error AS float)/cast(b.success AS float) AS percentage
    FROM
        (SELECT to_char(TIME, 'FMMonth FMDD, FMYYYY') AS date,
            count(status) AS error
        FROM log
        WHERE status = '404 NOT FOUND'
        GROUP BY date
        ORDER BY date DESC) a
    JOIN
        (SELECT to_char(TIME, 'FMMonth FMDD, FMYYYY') AS date,
            count(status) AS success
        FROM log
        WHERE status = '200 OK'
        GROUP BY date
        ORDER BY date DESC) b ON a.date = b.date
    WHERE cast(a.error AS float)/cast(b.success AS float) > .01;
    """
    c.execute(query)
    # displays 'title' text of question
    print('\n3. On which days did more than 1% of requests lead to errors?')
    qthree = c.fetchall()
    db.close()
    # iterates through each item returned by query,
    # adding formatting to match required display
    for i in qthree:
        print('\t'), i[0], ('-'), ("{:.1%}".format(i[3])), ('errors')
    return qthree


if __name__ == '__main__':
    # assure user the queries are running,d have not stalled
    print("\nPlease wait a moment, while data is retrieved from the database.")

    # calls functions in order to solve for question one, two then three
    question_one()
    question_two()
    question_three()

    # prints a blank line after the last function's return,
    # for visual separation from terminal line
    print('\n')
