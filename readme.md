# Object-oriented Programming  

Programming paradigm based on the concept of objects.  

#### Classes

Logical collection of attributes and methods.  
In object-oriented languages.  
Classes include fields and methods which are *inherited* by instance objects for code reuse and extensibility.  

**Objects are instances of classes.**  

#### Objects  

Objects can contain  
1. Fields/attributes  
-- data about the object.  
2. Procedures/methods  
-- code/function  

Noun: class  
Adjective: attributes  
Verb: method  

- Attribute: property that further defines a class  
- Method: function within a class which can access all the attributes of a class and perform a specific task  


## 1. Inheritance

Creating new class using details of existing class.  
This allows classes to be arranged in a hierarchy that represents "is-a-type-of" relationships.  

- Reusability: reusing the fields and methods of the existing class.  
- Super class  
- Sub class  


## 2. Encapsulation  

**Bind together** the data and functions that manipulate the data, and keeps them **safe from outside interference** and misuse.  

Encapsulation prevents external code from being concerned with the internal workings of an object.  

public vs. private methods  

**Data-hiding** can be achieved by declaring all the variables in the class as private and writing public methods in the class to set and get the values of variables.  


## 3. Abstraction  

**Only the essential details are displayed to the user.**  
The trivial or the non-essentials units are not displayed to the user. Ex: A car is viewed as a car rather than its individual components.  

## 4. Polymorphism  

Calling code can be agnostic as to which class in the supported hierarchy it is operating on - the parent class or one of its descendants.  

E.g., objects of type Circle and Square are derived from a common class called Shape. The Draw function for each type of Shape implements what is necessary to draw itself while calling code can remain indifferent to the particular type of Shape is being drawn.  


## Advantages  

1. **Modularity**: provides separation of duties  
2. **Extensibility**: objects can be extended to include new attributes and behaviors  
3. **Reusability**: objects can be reused across applications  
4. 1-3 : Improved software maintainability  
5. Faster development: reuse enables faster development.  
6. Lower cost of development.  
7. 5-6: Higher-quality software.  

## Disadvantages  

1. Steep learning curve  
2.  Larger program size: more lines of code than procedural programs.  
3. Slower programs  
Object-oriented software can entail extra housekeeping code not necessary in other computer languages; the computer must execute the additional programming, slowing an application's response time. For projects where speed is important, programmers may choose to write the most time-critical parts in non-OOP languages  


# Object Oriented Programming in Python  

## Polymorphism  
- The ability of an entity to be able to exist in more than one form.  

#### Overriding  
- Redefining the behavior of a base class method in a derived class.  

```python
class BaseClass:
	def baseClassMethod():
		# define behavior

class DerivedClass(BaseClass):
	def baseClassMethod():
		# redefine behavior
```

#### Operator Overriding  
- Defining a special method for an operator within your class to handle the operation between the objects of that class,  

Overloading the addition operator  
```python
class ClassName:
	def __add__(objectOne, objectTwo):
		# Define how addition needs to be performed
```

#### Abstract Base Class  
- A base class which consists of abstract methods that should be implemented in its derived class.  

```python
from abc import ABCMeta, abstractmethod
class baseClass(metaclass = ABCMeta):
	@abstractmethod
	def abstractMethod(self):
		return
```


References  
https://en.wikipedia.org/wiki/Object-oriented_programming#Composition,_inheritance,_and_delegation  
https://www.geeksforgeeks.org/object-oriented-programming-oops-concept-in-java/  
https://resources.saylor.org/wwwresources/archived/site/wp-content/uploads/2013/02/CS101-2.1.2-AdvantagesDisadvantagesOfOOP-FINAL.pdf  
https://www.techwalla.com/articles/advantages-disadvantages-of-object-oriented-programming  

Python  
https://www.udemy.com/course/python-oops-beginners  
https://www.programiz.com/python-programming/object-oriented-programmings  
https://python.swaroopch.com/oop.html  
https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-1-class-and-its-members/  
