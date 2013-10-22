####################
#At present I am only concerning myself with Chordata classes.
####################
from Phylum import Phylum
import random
class Class_(Phylum):
    def __init__(self, spark = 42, k = 5, p = -1, c = -1):
        Phylum.__init__(self)
        self.k = k
        self.p = p
        self.c = c
        self.classes = ['Cephalochordata','Leptocardii','Urochordata','Appendicularia','Ascidiacea','Sorberacea','Thaliacea','Vertebrata','Agnatha','Cyclostomata','Myxini','Petromyzontida','Gnathostomata','Chondrichthyes','Holocephali','Elasmobranchii','Tetrapoda','Amphibia','Amniota','Mammalia','Aves','Reptilia','Osteichthyes','Actinopterygii','Sarcopterygii']
        self.class_ = self.classes[self.c]
        def class_Randomize(self):
            self.c = random.randint(0, 34)
            self.class_ = self.classes[self.c]
            pass
        if (self.c < 0):
            class_Randomize(self)

        if __name__== '__main__':
            print "Domain: The Answer to Life, the Universe and Everything is: ", self.TheAnswer 
            pass

newClass_ = Class_(spark = 42, c = 19)
print "newClass_.class_:  ", newClass_.class_
print "newClass_.phylum:  ", newClass_.phylum
print "newClass_.kindom:  ", newClass_.kingdom
print "newClass_.domain:  ", newClass_.domain
