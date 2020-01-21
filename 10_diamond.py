#       Class A         Level 1
#       /   \
# Class B   Class C     Level 2
#       \   /
#       Class D         Level 3


class A:
    def method(self):
        print("This method belongs to class A")


class B(A):
    def method(self):
        print("This method belongs to class B")
    pass


class C(A):
    def method(self):
        print("This method belongs to class C")
    pass


class D(B, C):
    pass


d = D()
d.method()