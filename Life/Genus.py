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
from Family import Family
import random
class Genus(Family):
    def __init__(self, spark = 42, d = -1, k = -1, p = -1, c = -1, o = -1, f = -1, g = -1):
        self.d = d
        self.k = k
        self.p = p
        self.c = c
        self.o = o
        self.f = f
        self.g = g
        
        Family.__init__(self, d = self.d, k = self.k, p = self.p, c = self.c, o = self.o, f = self.f)
        self.geni = ['Pan', 'Gorilla', 'Homo', 'Pongo']
        self.genus = self.geni[self.g]
        def genusRandomize(self):
            self.g = random.randint(0, 34)
            self.genus = self.geni[self.g]
            pass
        if (self.g < 0):
            genusRandomize(self)

        if __name__== '__main__':
            #print "The Answer to Life, the Universe and Everything is: ", self.TheAnswer 
            pass

# newGenus = Genus(spark = 42, d = 2, k = 5, p = 7, c = 19, o = 0, f = 0, g = 2)
# print "newGenus.genus:   ", newGenus.genus
# print "newGenus.family:  ", newGenus.family
# print "newGenus.order:   ", newGenus.order
# print "newGenus.class_:  ", newGenus.class_
# print "newGenus.phylum:  ", newGenus.phylum
# print "newGenus.kindom:  ", newGenus.kingdom
# print "newGenus.domain:  ", newGenus.domain
