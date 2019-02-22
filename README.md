# 0x00. AirBnB clone - The console

A command interpreter to manage your AirBnB objects, it is a limited to specific use-cases for managing the objects of this project.

---

## Getting Started :wrench:

Interactive mode: Run `./console.py` at the root directory to execute the console.

Non-Interactive Mode: Pipe commands, ex: `echo "help" | ./console.py`

---

### Console Commands :computer:

#### `quit` or hit CTRL-D
To quit and exit the console.

#### `help`
To show help information of all commands. You can also show help of specific commands by adding a command after help, ex: `help quit`.

#### `create <class>`
To create a new instance of a class, ex: `create BaseModel` or `create Review`. It saves it JSON file and then print's the `id`.

#### `show`
To show the string representation of an instance based on the class name and `id` ex: `show BaseModel` or `show BaseModel 1234-1234-1234`.

#### `destroy`
To delete and instance based off the class name and id, and then save changes to JSON file. ex: `destroy BaseModel 1234-1234-1234`. 

#### `all`
To print all string representation of all instances based or not on the class name, ex: `all BaseModel` or `all`.

#### `update`
To update an instance based on the class name and `id` by adding or updating attribute. It then saves changes to JSON file. ex: `update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"`

---

## Repository Contents :file_folder:

* [console.py](./console.py)
  - A custom command interpreter with commands to interact with the objects and storage management.

* [base_model.py](./models/base_model.py)
  - This is the base class for all other classes that inherits from this, it gets created via console command `create`.

* [file_storage.py](./models/engine/file_storage.py)
  - Manages all of the instances when called via console commands.

* [user.py](./models/user.py)
  - Inherits from BaseModel to create user's `email`, `password`, `first_name`, and `last_name`

* [state.py](./models/state.py)
  - Inherits from BaseModel to create state's `name`

* [city.py](./models/city.py)
  - Inherits from BaseModel to create city's `state_id`, and `name`

* [amenity.py](./models/amenity.py)
  - Inherits from BaseModel to create amenity's `name`

* [place.py](./models/place.py)
  - Inherits from BaseModel to create place's `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, `latitude`, `longitude`, and `amenity_ids`

* [review.py](./models/review.py)
  - Inherits from BaseModel to create review's `place_id`, `user_id`, and `text`

---

## Tasks :page_facing_up:

### 0. README, AUTHORS
* Write a `README.md`.

### 1. Be PEP8 compliant!
* Write beautiful code that passes the PEP8 checks.

### 2. Unittests
* All your files, classes, functions must be tested with unit tests.

### 3. BaseModel
* Write a class BaseModel that defines all common attributes/methods for other classes.

### 4. Create BaseModel from dictionary
* Update `models/base_model.py` to have `*args, **kwargs`

### 5. Store first object
* Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances.

### 6. Console 0.0.1
* Write a program called `console.py` that contains the entry point of the command interpreter.

### 7. Console 0.1
* Update your command interpreter `console.py`.

### 8. First User
* Write a class `User` that inherits from `BaseModel`.

### 9. More classes!
* Write all those classes that inherit from `BaseModel`.

### 10. Console 1.0
* Update `FileStorage` to manage correctly serialization and deserialization of all our new classes.
* Update your command interpreter `console.py`.

---

## Example of the console's interactive mode

![interactive](https://i.imgur.com/qSuOplr.png)

## Example of the console's non-interactive mode

![non-interactive](https://i.imgur.com/4V2LC7J.png)

---

## Authors

* **Derrick Gee** - [kai-dg](https://github.com/kai-dg)
* **Fernando Gonzalez** - [fgonza52](https://github.com/fgonza52)
