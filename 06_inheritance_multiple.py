# Multiple Inheritance


class OperatingSystem:
    multitasking = True
    name = "Mac OS"


class Apple:
    website = "www.apple.com"
    name = "Apple"


class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking == True:
            print("This is a multi tasking system. Visit {} for more details".format(self.website))
            # Will use OperatingSystem attribute since first in list
            print("Name : ", self.name)


macBook = MacBook()