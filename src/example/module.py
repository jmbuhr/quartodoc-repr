



class MyClass():
    """This is a class


    Attributes
    ----------
    name :
        The name of the class
    """
    def __init__(self, name):
        self.name = name
        print("We are in MyClass")

    def say_hello(self) -> int:
        """This is a method

        It prints the name of the class.
        And returns 1

        Returns
        -------
        1 This is always one.
        """
        print("Hello, I am {}".format(self.name))
        return 1



def main():
    print("We are in module.py")

