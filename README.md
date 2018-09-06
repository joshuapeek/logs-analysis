# project-logs
The project-logs python script will interact with a provided 'news' database, performing queries and returning results.
This script demonstrates mastery of skills learned within the first project of Udacity's Full Stack Web Developer Nanodegree.

project-logs was written by Joshua Peek.

## Index
1. [Download and Installation](#download-and-installation)
2. [Project Requirements](#project-requirements)
3. ['news' Database Structure](#news-database-structure)
4. [Code Design](#code-design)

## Download and Installation
Be sure to follow these items in order, starting at the top, and working downward.
Ex: _Virtual Machine Elements_ first, and _The 'news' Database_ last.

**Virtual Machine Elements**

This project makes use of a Linux-based virtual machine (VM).
It's suggested that you use the tools Vagrant and VirtualBox to install and manage the VM.
The course provides [this helpful video](https://www.youtube.com/watch?v=djnqoEO2rLc) as a conceptual overview of virtual machines and Vagrant, if you're not familiar with either.

VirtualBox installation:
1. [Download VirtualBox from VirtualBox.org, here.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
2. Install the _platform package_ for your operating system. You will not need the extension pack or SDK.

Vagrant installation:
1. [Download Vagrant from VagrantUp.com, here](https://www.vagrantup.com/downloads.html)
2. Install the appropriate version for your operating system.
3. Windows users: If prompted, be sure to grant network permissions to Vagrant, or make a firewall exception.
_Run `vagrant --version` in your terminal. A returned version number verifies correct installation._

VM Configuration:
1. Within GitHub, fork and clone [the configuration repository, here](https://github.com/udacity/fullstack-nanodegree-vm)
2. When launching Vagrant, be sure to `cd` into the **vagrant** directory created by this Configuration

Starting the VM:
1. From your terminal, inside the **vagrant** subdiractory, run the command `vagrant up`.
2. Vagrant will perform necessary setup, which may take several minutes.
3. When setup is completed, use your returned shell prompt to run `vagrant ssh`.
4. Vagrant will log you into your newly installed Linux VM!
_A shell prompt beginning with `vagrant` signifies correct installation._
_Remember to `cd` into the **vagrant** directory!_


**Python3 and Dependencies**

The project-logs script makes use of Python3.
To install Python3: [Select the version appropriate for your operating system, here.](https://www.python.org/downloads/)
_Note: If you're using Python2, the 'news' database, and project-logs script will not work._

You'll also need to install the psycopg2 library for use with Python.
- Within your terminal, simply run `pip install psycopg2`.
- [Complete documentation for psycopg2 is found here.](https://pypi.org/project/psycopg2/)

**The 'news' Database**

PostgreSQL is already installed on your VM, as part of the VM Configuration, detailed above.
To use the 'news' database, you'll need to have the provided PostgreSQL database 'news' installed.
You'll also need Python3 installed, the project-logs script itself, and all of the Python dependencies described below.

To use the project-logs script


[Back to Index](#index)




## Project Requirements
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




## "news" Database Structure
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




## Code Design
