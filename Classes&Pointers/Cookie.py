#Classes - cookie cutters
#Python has built-in cookie cutters 
#When you create a class, you are creating your own data type 


# define - function #__double underscore, self - keyword - method part of a class.
class Cookie:
    def __init__(self, color): #self is the instance of this class like this in java
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

#cookie_one is the variable name and is set to type Cookie with a passed color of green
cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())