import sys
import random

class Introduction(object):

    def variables(self):
        print("======= Method \"%s\"" % sys._getframe().f_code.co_name)
        # integers
        myvar = 3
        myvar += 2
        myvar -= 1
        print("myvar: %s" % myvar)

        # strings
        mystr = "Hello"
        mystr += " world"
        print("mystr: %s" % mystr)

        # swap values
        myvar, mystr = mystr, myvar
        print("myvar after swap: %s" % myvar)
        print("mystr after swap: %s" % mystr)

    def data_types(self):
        print("======= Method \"%s\"" % sys._getframe().f_code.co_name)
        list_var = [1, 2, 2, 3]
        set_var = {1, 2, 2, 3}
        dict_var = {1: 10, 2: 20, 3: 30}
        tuple_var = (1, 2, 2, 3)
        print("List : %s, length: %s " % (list_var, len(list_var)))
        print("Set  : %(key_set)s, length: %(key_len)s" % {"key_set": set_var, "key_len": len(set_var)})
        print("Dict : {}, length: {}".format(dict_var, len(dict_var)))
        print(f"Tuple: {tuple_var}, length {len(tuple_var)}")

        # Lists
        sample = [1, ["another", "list"], ("a", "tuple")]
        print("Sample list: %s" % sample)
        mylist = ["List item 1", 2, 3.14]
        print("MyList: %s" % mylist)
        mylist[0] = "Changed list item 1"
        print("MyList with changed first element: %s" % mylist)
        mylist[-1] = -3.14
        print("MyList with changed last element : %s" % mylist)

        # Dict
        mydict = {"Key1": "Value1", 2: 3, "pi": 3.14}
        print("Dict: %s" % mydict)
        mydict["pi"] = -3.14
        mydict[2] = "Four"
        mydict["pu"] = "three.onefour"
        print("Changed dict: %s" % mydict)

        # Tuple
        mytuple = (1, 2, 3)
        print("MyTuple: (%s, %s, %s)" % mytuple)

        # Function
        myfunction = len
        print("MyFunction: %s" % myfunction(mylist))
        myfunction = lambda list: len(list)
        print("MyFunction: %s" % myfunction(mylist))

        # Ranges
        print("mylist[:]     : %s" % mylist[:])
        print("mylist[1:3]   : %s" % mylist[1:3])
        print("mylist[-3:-1] : %s" % mylist[-3:-1])
        print("mylist[:-1]   : %s" % mylist[:-1])
        print("mylist[1:]    : %s" % mylist[1:])
        print("mylist[::2]   : %s" % mylist[::2])
        print("mylist[::3]   : %s" % mylist[::3])

    def strings(self):
        print("======= Method \"%s\"" % sys._getframe().f_code.co_name)
        print("1. Output with backslashes at the line end: Name: %s, \
Number: %s, \
    String: %s" % ("Stavrov", 101, 3 * "-"))
        multiline = """This
is a
    multiline
        string"""
        print("2. Multiline string: %s" % multiline)

        print("3. This %s a substitute %s" % ("is", "test"))
        print("4. This %(verb)s a substitute %(noun)s" % {"verb": "is", "noun": "test"})
        print("5. This {} a substitute {}".format("is", "test"))
        test = "test"
        print(f"6. This is a substitute {test}")

    def flow_control(self):
        print("======= Method \"%s\"" % sys._getframe().f_code.co_name)
        range_list = range(10)
        print("range(10)       : %s" % range_list)
        range_list = list(range(10))
        print("list(range(10)) : %s" % range_list)

        mylist = [1, 2, 3]
        myvar = 10
        print("Passing example: %s, %s, %s" % self.passing_example(mylist, myvar))
        print("After passing example (changed only the list: %s, %s" % (mylist, myvar))

    def passing_example(self, a_list, a_val=2, a_str="A default string"):
        print("======= Method \"%s\"" % sys._getframe().f_code.co_name)
        a_list.append("Appended item")
        a_val = 4
        a_str = "Changed string"
        return a_list, a_val, a_str

    def classes(self):
        print("======= Method \"%s\"" % sys._getframe().f_code.co_name)

        instance_1 = TestClass1()
        print("instance_1.testfunction(): %s" % instance_1.testfunction())

        instance_2 = TestClass1()
        print("instance_1.common: %s" % instance_1.common)
        print("instance_2.common: %s" % instance_2.common)
        Introduction.common = 30
        print("instance_1.common after static change: %s" % instance_1.common)
        print("instance_2.common after static change: %s" % instance_2.common)
        instance_1.common = 10
        print("instance_1.common after self change: %s" % instance_1.common)
        print("instance_2.common: %s" % instance_2.common)
        Introduction.common = 50
        print("instance_1.common after 2nd static change: %s" % instance_1.common)
        print("instance_2.common after 2nd static change: %s" % instance_2.common)

    def inheritance(self):
        print("======= Method \"%s\"" % sys._getframe().f_code.co_name)

        instance_3 = TestClass2()
        print("instance_3.myvar: %s" % instance_3.myvar)
        print("instance_3.myvar_2: %s" % instance_3.myvar2)
        print("instance_3.testfunction: %s" % instance_3.testfunction())

    def exceptions(self):
        print("======= Method \"%s\"" % sys._getframe().f_code.co_name)
        try:
            10 / 0
        except ZeroDivisionError:
            print("Exception handler: devide by zero")
        else:
            print("No exception happened")
            pass
        finally:
            print("Finally block of the exception handler")

    def useimports(self):
        print("======= Method \"%s\"" % sys._getframe().f_code.co_name)
        randomint = random.randint(1, 100)
        print("Generated random integer: %s" % randomint)

    def list_comprehensions(self):
        print("======= Method \"%s\"" % sys._getframe().f_code.co_name)
        list_1 = [1, 2, 3]
        list_2 = [3, 4, 5]
        # List comprehensions
        print([x * y for x in list_1 for y in list_2])
        print([x for x in list_1 if 1 < x < 4])
        print(any([x % 3 == 0 for x in list_1]))
        print(any([x % 4 == 0 for x in list_1]))
        print(sum(1 for x in [2, 2, 3, 3, 4] if x % 3 == 0))

    def misc(self):
        print("======= Method \"%s\"" % sys._getframe().f_code.co_name)
        list_1 = [1, 2, 3]
        print("List1 after del %s" % list_1)
        del list_1
        try:
            print("List1 after del %s" % list_1)
        except UnboundLocalError:
            print("List1 has been deleted")

    def global_variables(self):
        print("======= Method \"%s\"" % sys._getframe().f_code.co_name)
        tmp = GlobalClass()
        tmp.func_1()
        tmp.func_2()
        tmp.func_3()
        tmp.func_1()


class TestClass1(object):
    common = 10

    def __init__(self):
        print("Constructor for TestClass1")
        self.myvar = 3

    def testfunction(self):
        return self.myvar


class TestClass2(TestClass1):
    def __init__(self):
        super().__init__()
        print("Constructor for TestClass2")
        self.myvar2 = 5

number = 5

class GlobalClass(object):
    def func_1(self):
        print("Number: %s" % number)
    def func_2(self):
        try:
            print("Number: %s" % number)
            number = 3
        except UnboundLocalError:
            print("Number is not bound to global space")
    def func_3(self):
        global number
        number = 3
        print("Number: %s" % number)

if __name__ == '__main__':
    intro = Introduction()
    intro.variables()
    intro.data_types()
    intro.strings()
    intro.flow_control()
    intro.classes()
    intro.inheritance()
    intro.exceptions()
    intro.useimports()
    intro.list_comprehensions()
    intro.misc()
    intro.global_variables()
