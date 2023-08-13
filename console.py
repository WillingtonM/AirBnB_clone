#!/usr/bin/python3
# this program conatin the entry point of our command interpreter
# + which creats instances, modify instances, delete instances and so on

import cmd
from models.base_model import BaseModel
from models import storage
import sys
import json
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """ this class inherits Cmd class and acts like a shell
       uniquely for our project where it take care instances"""

    prompt = "(hbnb) "
    existingClasses = {'BaseModel': BaseModel, 'User': User, 'City': City,
                       'Place': Place, 'Amenity': Amenity, 'Review': Review,
                       'State': State}

    def do_quit(self, arg):
        """ allows the exit of our program on quit"""
        print()
        exit()

    def do_EOF(self, arg):
        """ allows the exit of our program on EOF"""
        print()
        exit()

    def emptyline(self):
        """ overides the default emptyline method which executes the
           previous line and just do nothing"""
        pass

    def do_create(self, arg):
        """ creats instances """
        if not arg:
            print("** class name missing **")
            return
        elif arg:
            if arg not in self.existingClasses:
                print("** class doesn't exist **")
                return
            obj = self.existingClasses[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in self.existingClasses:
            print("** class doesn't exist **")
        else:
            if len(arg) == 1:
                print("** instance id missing **")
                return
            store = storage.all()
            key = arg[0] + '.' + arg[1]
            if key not in store:
                print("** no instance found **")
            else:
                print(store[key])
        return

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if arg[0] not in self.existingClasses:
            print("** class doesn't exist **")
        else:
            if len(arg) == 1:
                print("** instance id missing **")
                return
            store = storage.all()
            key = arg[0] + '.' + arg[1]
            if key not in store:
                print("** no instance found **")
            else:
                store.pop(key)
                storage.save()
        return

    def do_all(self, arg):
        """Prints all string representation of all instances
           based or not on the class name"""
        arg = arg.split()
        if len(arg) == 0:
            print([str(value) for value in storage.all().values()])
        elif arg[0] not in self.existingClasses or len(arg) > 1:
            print("** class doesn't exist **")
        else:
            new = [str(value) for key, value in storage.all().items()
                   if key.split(".")[0] == arg[0]]
            print(new)

    def do_update(self, arg):
        """Updates an instance based on the class name and
           id by adding or updating attribute"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in self.existingClasses:
            print("** class doesn't exist **")
        else:
            if len(arg) == 1:
                print("** instance id missing **")
                return
            store = storage.all()
            key = arg[0] + '.' + arg[1]
            if key not in store:
                print("** no instance found **")
            else:
                if len(arg) == 2:
                    print("** attribute name missing **")
                elif len(arg) == 3:
                    print("** value missing **")
                else:
                    setattr(store[key], arg[2], arg[3][1:-1])
                    storage.save()
        return

    def do_count(self, arg):
        """a class that counts number of objects stored"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in self.existingClasses:
            print("** class doesn't exist **")
        else:
            i = 0
            for value in storage.all().values():
                if value.__class__.__name__ == arg[0]:
                    i += 1
            print(i)

    def default(self, arg):
        """ handles <class name>.func() commands"""
        if arg is None:
            return

        command_p = "^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"  # noqa: regex pattern
        matched_p = re.match(command_p, arg)
        if not matched_p:
            super().default(arg)
            return
        cls, func, arguments = matched_p.groups()
        arguments = " ".join(arguments.split(','))
        arguments = arguments[1:-1]
        args = " ".join([cls] + [arguments])
        if func == 'all':
            return self.do_all(args)
        if func == 'count':
            return self.do_count(args)
        if func == 'show':
            return self.do_show(args)
        if func == 'destroy':
            return self.do_destroy(args)
        if func == 'update':
            return self.do_update(args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
