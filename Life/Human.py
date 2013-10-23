#############
# Creates a human with no name and of indiscriminate gender, but you can pass these attributes.  
# Set a negative value for ageMax to generate random age and ageMax values
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
        , age = 0.0
        , ageMax = 0.0
        ):
        self.genderDictionary = {0: "Male", 1: "Female", 2: "Other"}

        self.gender = gender
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.age = age
        self.ageMax = ageMax
        def ageRandomize(self):
            m  = 365.24*122+164
            self.ageMax = round(random.uniform(0, m), 2)/365.24
            self.age = round(random.uniform(0, m), 2)/365.2
            while (self.age > self.ageMax):
                self.ageMax = round(random.uniform(0, m), 2)/365.24

        def genderRandomize(self):
            self.gender= random.randint(0,2)
        if (ageMax < 0):
            ageRandomize(self)


        
        if (self.gender < 0):
            genderRandomize()
        
        print "age: ", self.age, "ageMax: ", self.ageMax
        print "Name: ", self.nameFirst, self.nameLast
        print "Gender: ", self.genderDictionary[self.gender]

    


Adam = Human(nameFirst = 'Adam', ageMax = -1)
# print Adam.gender
# Eve = Human( nameFirst = 'Eve')
# print Eve.nameFirst, Eve.nameLast