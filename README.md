# project-logs
This python script was written as part the first project within Udacity's Full Stack Web Developer Nanodegree.
Written by Joshua Peek.

### Index
1. [Download and Installation](#download-and-installation)
2. [Project Requirements](#project-requirements)
3. ['news' Database Structure](#news-database-structure)
4. [Code Design](#code-design)

### Download and Installation
**Download Required Files**

**Install Dependencies**

**Install Database**

[Back to Index](#index)




### Project Requirements
For those enrolled, [have a look at the full project rubric here.](https://review.udacity.com/#!/rubrics/277/view)

The script's code must conform to:
- Proper SQL style, and
- PEP8 style guide for Python code.

The script must perform the following:
- Connect to the provided 'news' database
- Perform sql queries to answer three given questions:
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?
- Report the returned data:
  - As sorted lists,
  - In text format,
  - Matching a given answer format
  - Correctly answering the given questions


**Answer Formats**
The expected answer format for each given question is seen below. _Note: These answers are not correct, they simply show format._
1. What are the most popular three articles of all time?
   - "Princess Shellfish Marries Prince Handsome" — 1201 views
   - "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
   - "Political Scandal Ends In Political Scandal" — 553 views
2. Who are the most popular article authors of all time?
   - Ursula La Multa — 2304 views
   - Rudolf von Treppenwitz — 1985 views
   - Markoff Chaney — 1723 views
   - Anonymous Contributor — 1023 views
3. On which days did more than 1% of requests lead to errors?
   - July 29, 2016 — 2.5% errors

[Back to Index](#index)




### "news" Database Structure
The "news" database contains three tables, with the following structure:

_articles table:_

|Column|Key?   |Type       |
|------|-------|-----------|
|author|foreign|integer    |
|title |       |text       |
|slug  |       |text       |
|lead  |       |text       |
|body  |       |text       |
|time  |       |timestamptz|
|id    |primary|integer    |

_authors table:_

|Column|Key?   |Type       |
|------|-------|-----------|
|name  |foreign|text       |
|bio   |       |text       |
|id    |primary|integer    |

_log table:_

|Column|Key?   |Type       |
|------|-------|-----------|
|path  |       |text       |
|ip    |       |inet       |
|method|       |text       |
|status|       |text       |
|time  |       |timestamptz|
|id    |primary|integer    |

[Back to Index](#index)




### Code Design
