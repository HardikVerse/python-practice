'''Create a class with a class attribute
 a; create an object from it and set 'a'
directly using 'object.a = 0'. Does this 
change the class attribute?'''


class Demo:
    a = 5


d = Demo()
d.a = 0
print(d.a)
print(Demo.a)

''' Instance attributes, take preference over 
class attributes during assignment &
retrieval.'''