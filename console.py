#!/usr/bin/python3
"""
This contains the Entry point of the command interpreter
"""
import cmd
import sys
import models
from models.base_model import BaseModel
import inspect


class HBNBCommand(cmd.Cmd):
    """
    Command Line Enterprerter class
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program
        """
        sys.exit(1)

    def do_EOF(self, args):
        """ Implement EOF so (Ctrl + D) will quit"""
        return True

    def do_create(self, args):
        """
        Create an instance of BaseModel
        Save it and prints its id.
        """
        nb_args = args.split()
        if not self.check_if_args_is_correct(nb_args, True):
            return

        base_ = eval(nb_args[0])()
        base_.save()
        print(base_.id)

    def do_show(self, args):
        """
        Prints string representation of an Insatance
        """
        nb_args = args.split()
        if not self.check_if_args_is_correct(nb_args, True, True):
            return

        id = "{}.{}".format(nb_args[0], nb_args[1])
        print(str(models.storage.all()[id]))

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        """
        nb_args = args.split()
        if not self.check_if_args_is_correct(nb_args, True, True):
            return

        id = "{}.{}".format(nb_args[0], nb_args[1])

        del models.storage.all()[id]
        models.storage.save()

    def do_all(self, args):
        """
        Prints all string representation
        """

        nb_args = args.split()
        if len(nb_args) and (not self.check_if_args_is_correct(nb_args, True)):
            return

        print([str(obj) for obj in models.storage.all().values()])

    def do_update(self, args):
        """ Updates an instance based on the class name and id"""

        nb_args = args.split()
        if not self.check_if_args_is_correct(nb_args, True, True):
            return

        id = "{}.{}".format(nb_args[0], nb_args[1])

        if len(nb_args) < 3:
            print("** attribute name missing **")
            return

        if len(nb_args) < 4:
            print("** value missing **")
            return

        if nb_args[2] in ["id", "created_at", "updated_at"]:
            return

        setattr(models.storage.all()[id], nb_args[2],
                type(nb_args[2])(nb_args[3]))
        models.storage.all()[id].save()

    def emptyline(self):
        """If line is empty"""
        return

    def check_if_args_is_correct(self, nb_args, check_clsname=True,
                                 check_id=False):
        """Check if passed args repect some
           Criteria
        """

        if (check_clsname):
            if not len(nb_args):
                print("** class name missing **")
                return 0

            try:
                base_ = eval(nb_args[0])()
                id = "{}.{}".format(nb_args[0], base_.id)
                del models.storage.all()[id]
                models.storage.save()
            except NameError:
                print("** class doesn't exist **")
                return 0

        if check_id:
            if len(nb_args) < 2:
                print("** instance id missing **")
                return 0

            id = "{}.{}".format(nb_args[0], nb_args[1])
            if (id not in models.storage.all().keys()):
                print("** no instance found **")
                return 0

        return 1


if __name__ == "__main__":
    HBNBCommand().cmdloop()
