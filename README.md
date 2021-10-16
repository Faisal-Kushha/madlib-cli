# Lab: File IO and Exceptions

Madlib-cli project

# Description

An application that read and write files

# Requirements

python 3.9.7
black
flake
pytest

# Feature Tasks

[x] Create a file called madlib.py at root of madlib_cli folder, which will contain all of the Python code that you will write relating to your Madlib game.
[x] Keeping in mind the concept of Single Responsibility Principle, build a command line tool which will perform the following:
[x] Print a welcome message to the user, explaining the Madlib process and command line interactions
[x] Read a template Madlib file (Example), and parse that file into usable parts.
[x] Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
[x] With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
[x] After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
[x] Write the completed text (Example)to a new file on your file system (in the repo).
Note: A smaller example file is included as well which can be handy when developing/testing.

# Testing Details

-[x]Create and test a read_template function that takes in a path to text file and returns a stripped string of the file’s contents.
read_template should raise a FileNotFoundError if path is invalid. -[x]Create and test a parse_template function that takes in a template string and returns a string with language parts removed and a separate list of those language parts. -[x] Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.

# Get Started

```
python
poetry install
poetry shell
pytest

```

# Developer

Faisal Kushha
I got help from Jehad Abu Awwad
Pull Request: https://github.com/Faisal-Kushha/madlib-cli/pull/1
