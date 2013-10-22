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
from Genus import Genus
import random
class Species(Genus):
    def __init__(self, spark = 42, d = -1, k = -1, p = -1, c = -1, o = -1, f = -1, g = -1, s = -1):
        self.d = d
        self.k = k
        self.p = p
        self.c = c
        self.o = o
        self.f = f
        self.g = g
        self.s = s
        
        Genus.__init__(self, d = self.d, k = self.k, p = self.p, c = self.c, o = self.o, f = self.f, g = self.g)
        self.specs = ['Denisova hominin','antecessor   ','cepranensis  ','erectus  ','ergaster ','floresiensis ','gautengensis ','habilis  ','heidelbergensis','neanderthalensis','rhodesiensis ','rudolfensis  ','Red Deer Cave people','sapiens idaltu   ','sapiens']
        self.species = self.specs[self.s]
        def speciesRandomize(self):
            self.s = random.randint(0, 34)
            self.species = self.specs[self.s]
            pass
        if (self.s < 0):
            speciesRandomize(self)

        if __name__== '__main__':
            print "Domain: The Answer to Life, the Universe and Everything is: ", self.TheAnswer 
            pass

# newSpecies = Species(spark = 42, d = 2, k = 5, p = 7, c = 19, o = 0, f = 0, g = 2, s = 14)
# print "newSpecies.species: ", newSpecies.species
# print "newSpecies.genus:   ", newSpecies.genus
# print "newSpecies.family:  ", newSpecies.family
# print "newSpecies.order:   ", newSpecies.order
# print "newSpecies.class_:  ", newSpecies.class_
# print "newSpecies.phylum:  ", newSpecies.phylum
# print "newSpecies.kindom:  ", newSpecies.kingdom
# print "newSpecies.domain:  ", newSpecies.domain
