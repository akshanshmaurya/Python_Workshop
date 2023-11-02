
# Object:-
# Object in python represent real worls entities.They are instances of classes.
# in the "objects" example ,we create a different class to represent dogs .
# The init_ method is a special method used to initialize the object when it is created.
# In this case sets the name attributes of the dog object.







class dog:
    def __init__(self, name):
        self.name=name

dog1= dog("Buddy")
print(dog1.name)        