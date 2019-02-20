#!/usr/bin/python3
import cmd
import sys
import os  # TODO how are we using this?
import models
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it to JSON storage, and prints id.
        """
        args = parse(args)
        if not args:
            print("** class name missing **")
        elif args[0] in models.classes:
            instance = models.classes[args[0]]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance."""
        args = parse(args)
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            store = models.storage.all()
            instance = args[0] + '.' + args[1]
            if instance in store.keys():
                print(store[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        args = parse(args)
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            store = models.storage.all()
            instance = args[0] + '.' + args[1]
            if instance in store.keys():
                del store[instance]
                models.storage.save()

    def do_update(self, args):
        """Updates an instance based on the class name and id."""
        args = parse(args)
        if not args:
            print("** class name missing **")
        elif len(args) < 1:
            print("** instance id missing **")
        elif len(args) < 2:
            print("** attribute name missing **")
        elif len(args) < 3:
            print("** value missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            store= models.storage.all()
            instance = args[0] + '.' + args[1]
            if instance in store.keys():
                setattr(store[instance], args[2], args[3])  # TODO cast val properly
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances."""
        store = models.storage.all()
        args = parse(args)
        if not args:
            print([str(v) for v in store.values()])
        elif args[0] in models.classes:
            print([str(v) for v in store.values()
                  if type(v).__name__ == args[0]])
        else:
            print("** class doesn't exist **")

    def do_EOF(self, args):
        """EOF command to exit the program."""
        print()
        return True

    def do_help(self):
        pass

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Called when empty line is entered in prompt."""
        pass

    def do_json(self):
        """Prints the contents of `file.json`"""
        print(models.storage.all())


def parse(line):
    """Convert a series of zero or more numbers to an argument list."""
    return shlex.split(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
