####################
#At present I am only concerning myself with Chordata classes.
# o = Eukarya
# , k = Animalia
# , p = Chordata
# , c = Mammalia
# , o = Primates
# , f = Hominidae 
# , g = Homo Sapien (sapien)
####################
from Species import Species
import random
class Subspecies(Species):
    def __init__(self, spark = 42, d = -1, k = -1, p = -1, c = -1, o = -1, f = -1, g = -1, s = -1, ss = -1):
        self.d = d
        self.k = k
        self.p = p
        self.c = c
        self.o = o
        self.f = f
        self.g = g
        self.s = s
        self.ss = ss
        
        Species.__init__(self, d = self.d, k = self.k, p = self.p, c = self.c, o = self.o, f = self.f, g = self.g, s = self.s)
        self.subspecs = ['sapiens']
        self.subspecies = self.subspecs[self.ss]
        def subspeciesRandomize(self):
            self.ss = random.randint(0, 34)
            self.subspecies = self.subspecs[self.ss]
            pass
        if (self.ss < 0):
            speciesRandomize(self)

        if __name__== '__main__':
            #print "The Answer to Life, the Universe and Everything is: ", self.TheAnswerToLifeTheUniverseAndEverything 
            pass

newHuman = Subspecies(spark = 42, d = 2, k = 5, p = 7, c = 19, o = 0, f = 0, g = 2, s = 14, ss = 0)
print "newHuman.TheAnswerToLifeTheUniverseAndEverything:  ", newHuman.TheAnswerToLifeTheUniverseAndEverything
print "newHuman.subspecies: ", newHuman.subspecies
print "newHuman.species:    ", newHuman.species
print "newHuman.genus:      ", newHuman.genus
print "newHuman.family:     ", newHuman.family
print "newHuman.order:      ", newHuman.order
print "newHuman.class_:     ", newHuman.class_
print "newHuman.phylum:     ", newHuman.phylum
print "newHuman.kindom:     ", newHuman.kingdom
print "newHuman.domain:     ", newHuman.domain
