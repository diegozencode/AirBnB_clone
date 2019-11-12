# AirBnB clone - The console
![Holberton logo](https://www.holbertonschool.com/holberton-logo.png)
> Create a simple command interpreter to manage AirBnB objects

## What is a command interpreter
In general command interpreters have commands and queries available for different operations such as in this case:
* Create a new object (ex: a new User or a new Place).
* Retrieve an object from a file, a database etc.
* Do operations on objects (count, compute stats, etc).
* Update attributes of an object.
* Destroy an object.

## Learning objectives
* How to create a Python package.
* How to create a command interpreter in Python using the cmd module.
* What is Unit testing and how to implement it in a large project.
* How to serialize and deserialize a Class.
* How to write and read a JSON file.
* How to manage datetime.
* What is an UUID.
* What is *args and how to use it.
* What is **kwargs and how to use it.
* How to handle named arguments in a function.

## Requirements
Python3 (version 3.4.3) or higher.

## Example
### Clone repo using HTTPS
```
$ https://github.com/arq-gabo/AirBnB_clone.git
```

### Usage
#### Interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

#### Non interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Authors
* **José Gabriel Guerra** - [arq-gabo](https://github.com/arq-gabo)
* **Diego Monroy** - [diegozencode](https://github.com/diegozencode)
