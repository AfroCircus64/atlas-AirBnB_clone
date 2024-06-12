#!/usr/bin/python3
""" Console module """
import cmd
import sys
import uuid
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console """

    # Determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Place': Place,
        'Review': Review,
        'Amenity': Amenity
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'first_name': str,
        'number_rooms': int,
        'number_bathrooms': int,
        'max_guest': int,
        'price_by_night': int,
        'email': str,
        'latitude': float,
        'longitude': float,
        'last_name': str,
        'password': str
    }

    def preloop(self):
        """ Prints if isatty is false """
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def postcmd(self, stop, line):
        """ Prints if isatty is false """
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
            return stop

    def do_quit(self, command):
        """ Method to exit the HBNB console """
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Create an object of any class """
        if not args:
            print("** class name missing **")
            return

        # Split the arguments by spaces
        arg_list = args.split()

        # Get the class name from the first argument
        class_name = arg_list[0]

        # CHeck if the class exists in HBNBCommand.classes
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        # Remove the class name from the argument list
        arg_list = arg_list[1:]

        # Create a dictionary to store the attributes
        attributes = {}

        # Parse and process the parameters
        for param in arg_list:
            # Split the parameter by '=' to get key and value
            param_parts = param.split('=')

            # Check if the parameter has valid format (key=value)
            if len(param_parts) != 2:
                continue

            key, value = param_parts[0], param_parts[1]

            # Unquote, underscore to space
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1].replace('_', ' ')

            # Convert values to appropriate data types (float, int, str)
            if '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    pass
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        pass

            # Store the key value pair in the attributes dictionary
            attributes[key] = value

        # Create an instance of the specified class with the attributes
        new_instance = HBNBCommand.classes[class_name](**attributes)

        # Save the new instance to the storage
        storage.new(new_instance)
        storage.save()

        # Print the id of the new object
        print(new_instance.id)

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """shows an individual object"""
        new = args.partition(" ")
        io_name = new[0]
        io_id = new[2]

        if io_id and ' ' in io_id:
            io_id = io_id.partition(' ')[0]

        if not io_name:
            print("** class name missing **")
            return

        if io_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not io_id:
            print("** instance id missing **")
            return

        key = io_name + "." + io_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ show command help """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """destroys an object"""
        new = args.partition(" ")
        io_name = new[0]
        io_id = new[2]
        if io_id and ' ' in io_id:
            io_id = io_id.partition(' ')[0]

        if not io_name:
            print("** class name missing **")
            return

        if io_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not io_id:
            print("** instance id missing **")
            return

        key = io_name + "." + io_id
        try:
            del (storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """destroy command help"""
        print("Destroys an instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """displays all objects"""
        obj_list = []

        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    obj_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                obj_list.append(str(v))

        print(obj_list)

    def help_all(self):
        """all command help"""
        print("Shows all objects")
        print("[Usage]: all <className>\n")

    def do_update(self, args):
        """updates an instance"""
        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
        io_name = arg_list[0]

        if io_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]

        key = io_name + "." + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        attribute_name = arg_list[2]

        if len(arg_list) < 4:
            print("** value missing **")
            return

        new_value = arg_list[3]

        new_value = new_value.strip("\"")

        instance = storage.all()[key]
        attribute_type = type(getattr(instance, attribute_name, None))

        if attribute_name in ["id", "created_at", "updated_at"]:
            return

        try:
            if "." in new_value:
                value = float(new_value)
            else:
                value = int(new_value)
        except ValueError:
            value = new_value

        obj = storage._FileStorage__objects[key]

        storage.update(obj, attribute_name, value)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
