####################
#At present I am only concerning myself with Chordata classes.
# o = Eukarya
# , k = Animalia
# , p = Chordata
# , c = Mammalia
# , o = Primates
# ,  Hominidae Homo Sapien (sapien)
####################
from Class_ import Class_
import random
class Order(Class_):
    def __init__(self, spark = 42, d = -1, k = -1, p = -1, c = -1, o = -1):
        self.d = d
        self.k = k
        self.p = p
        self.c = c
        self.o = o
        
        Class_.__init__(self, d = self.d, k = self.k, p = self.p, c = self.c)
        self.orders = []
        self.order = self.orders[self.o]
        def orderRandomize(self):
            self.c = random.randint(0, 34)
            self.Order = self.classes[self.c]
            pass
        if (self.c < 0):
            OrderRandomize(self)

        if __name__== '__main__':
            print "Domain: The Answer to Life, the Universe and Everything is: ", self.TheAnswer 
            pass

newOrder = Order(spark = 42, d = 2, k = 5, p = 7, c = 19, o = -1)
print "newOrder.Order:   ", newOrder.order
print "newOrder.class_:  ", newOrder.class_
print "newOrder.phylum:  ", newOrder.phylum
print "newOrder.kindom:  ", newOrder.kingdom
print "newOrder.domain:  ", newOrder.domain