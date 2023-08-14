# Airbnb Console

# Project Description:
The Airbnb Console is a command-line interface (CLI) for managing data related to an Airbnb-like application. The project consists of various classes that represent different entities in the application such as users, cities, states, places, etc. The main goal of this project is to provide a way to interact with the application's data using the command line.

# Command Interpreter Description
The Command Interpreter is a Python module that provides an interactive command-line interface for managing the data of the Airbnb application. It allows users to create, read, update, and delete data stored in the application. The interpreter is implemented using the cmd module in Python.

# How to Start the Command Interpreter
Run the console.py file:
You can run commands using this syntax:
command argument1 argument2 ..
You can type "help command" for get the usage of a specific command.
Atlernatively, you can also run commands using this syntax:
class_name.command("arugment1", "argument2", ...)

# Here are some example commands:

To create a new user:

* Create User
or
* User.create

To show information about a user:

show User user_id
or
User.show(user_id)

To update a user's information:

update User user_id name "new_name"
oe
User.update(user_id, name="New Name")

To delete a user:

destroy User user_id
or
User.destroy(user_id)

To list all users:

all User
or
User.all()
