####################
#At present I am only concerning myself with Humanity.
#   o = Eukarya
# , k = Animalia
# , p = Chordata
# , c = Mammalia
# , o = Primates
# ,  Hominidae Homo Sapien (sapien)
####################
from Class_ import Class_
import random
class SubClass(Class_):
    def __init__(self, spark = 42, d = -1, k = -1, p = -1, c = -1, sc = -1):
        self.d = d
        self.k = k
        self.p = p
        self.c = c
        self.sc = sc
        
        Class_.__init__(self, d = self.d, k = self.k, p = self.p, c = self.c )
        self.subclasses = ['Cephalochordata','Leptocardii','Urochordata','Appendicularia','Ascidiacea','Sorberacea','Thaliacea','Vertebrata','Agnatha','Cyclostomata','Myxini','Petromyzontida','Gnathostomata','Chondrichthyes','Holocephali','Elasmobranchii','Tetrapoda','Amphibia','Amniota','Mammalia','Aves','Reptilia','Osteichthyes','Actinopterygii','Sarcopterygii']
        self.subclass = self.subclasses[self.sc]
        def subclassesRandomize(self):
            self.sc = random.randint(0, 34)
            self.subclass = self.subclasses[self.sc]
            pass
        if (self.sc < 0):
            subclassesRandomize(self)

        if __name__== '__main__':
            #print "The Answer to Life, the Universe and Everything is: ", self.TheAnswer 
            pass

newSubclass = SubClass(spark = 42, d = 2, k = 5, p = 7, c = 19, sc = 1)
print "newSubclass.subclass:  ", newSubclass.subclass
print "newSubclass.class_:    ", newSubclass.class_
print "newSubclass.phylum:    ", newSubclass.phylum
print "newSubclass.kindom:    ", newSubclass.kingdom
print "newSubclass.domain:    ", newSubclass.domain
