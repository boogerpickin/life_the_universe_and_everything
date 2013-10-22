#############
# Creates a human with no name and of indiscriminate gender, but you can pass these attributes.  
# If an age is not entered, it will generate a random age
# somewhere between 0 and 122 years 164 days, the age of 
# Jeanne Calment, the oldest known living person in the common era.
#
#############
import random
class Human(object):
    def __init__(self
        , gender =0
        , nameFirst = 'none'
        , nameLast = 'none'
        , age = 0):

        self.gender = gender
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        if (age != 0):
            self.age = age
        else:
            n  = 365.24*122+164
            age = round(random.uniform(0, n), 2)/365.24
        if (gender != 0):
            self.gender = gender
        else: self.gender = random.randint(1,2)
        print "n: ", n
        print "age: ", age
        print "Name: ", nameFirst, nameLast

# Adam = Human(gender = 1, nameFirst = 'Adam')
# print Adam.gender
# Eve = Human( nameFirst = 'Eve')
# print Eve.nameFirst, Eve.nameLast