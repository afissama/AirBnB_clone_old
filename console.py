#!/usr/bin/python3
"""
This contains the Entry point of the command interpreter
"""
import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        objs = models.storage.all()

        if len(nb_args) and (not self.check_if_args_is_correct(nb_args, True)):
            return

        if len(nb_args):
            print([
                str(objs[key]) for key in objs.keys()
                if str(key).startswith(nb_args[0])
            ])
            return

        print([
            str(objs[key]) for key in objs.keys()
        ])

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

    def default(self, arg):
        """The default method"""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "update": self.do_update,
            "destroy": self.do_destroy,
            "count": self.count_instance
        }
        nb_args = arg.split(".")

        if not len(nb_args):
            return super().default(arg)

        cls_name = nb_args[0]
        cmd_ = nb_args[1]


        if ("(" not in cmd_):
            return super().default(arg)

        tab_args = cmd_.split("(")

        if not len(tab_args):
            return super().default(arg)

        cmd_ = tab_args[0]

        if ")" not in tab_args[1]:
            return super().default(arg)

        s_arg = tab_args[1].replace(")", "")

        if "," in tab_args[1]:
            s_arg = s_arg.replace(",", "")

        cls_name = cls_name + " " + s_arg

        if cmd_ in arg_dict.keys():
            arg_dict[cmd_](cls_name)
            return

        return super().default(arg)

    def count_instance(self, args):
        """Count instance"""
        nb_args = args.split()
        if not self.check_if_args_is_correct(nb_args, True):
            return

        objs = models.storage.all()
        print(len(
                [str(objs[key]) for key in objs.keys()
                    if str(key).startswith(nb_args[0])]
            ))

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
