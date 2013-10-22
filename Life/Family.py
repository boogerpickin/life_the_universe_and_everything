####################
#At present I am only concerning myself with Chordata classes.
# o = Eukarya
# , k = Animalia
# , p = Chordata
# , c = Mammalia
# , o = Primates
# , f = Hominidae Homo Sapien (sapien)
####################
from Order import Order
import random
class Family(Order):
    def __init__(self, spark = 42, d = -1, k = -1, p = -1, c = -1, o = -1, f = -1):
        self.d = d
        self.k = k
        self.p = p
        self.c = c
        self.o = o
        self.f = f
        
        Order.__init__(self, d = self.d, k = self.k, p = self.p, c = self.c, o = self.o)
        self.families = ['Hominidae']
        self.family = self.families[self.f]
        def familyRandomize(self):
            self.f = random.randint(0, 34)
            self.family = self.families[self.f]
            pass
        if (self.f < 0):
            familyRandomize(self)

        if __name__== '__main__':
            print "Domain: The Answer to Life, the Universe and Everything is: ", self.TheAnswer 
            pass

# newFamily = Family(spark = 42, d = 2, k = 5, p = 7, c = 19, o = 0, f = 0)
# print "newFamily.Family:   ", newFamily.family
# print "newFamily.Order:   ", newFamily.order
# print "newFamily.class_:  ", newFamily.class_
# print "newFamily.phylum:  ", newFamily.phylum
# print "newFamily.kindom:  ", newFamily.kingdom
# print "newFamily.domain:  ", newFamily.domain
