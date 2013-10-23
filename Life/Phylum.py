####################
#At present I am only concerning myself with Animal phyla.
####################
from Kingdom import Kingdom
import random
class Phylum(Kingdom):
    def __init__(self, spark = 42, d = -1, k = 5, p = -1):
        self.d = d
        self.k = k
        self.p = p
        Kingdom.__init__(self, d = self.d, k = self.k)
        #print "selfattribute.k: ", self.k
        
        self.p = p
        self.phylums = ['Acanthocephala','Acoelomorpha','Annelida','Arthropoda','Brachiopoda','Bryozoa','Chaetognatha','Chordata','Cnidaria','Ctenophora','Cycliophora','Echinodermata','Entoprocta','Gastrotricha','Gnathostomulida','Hemichordata','Kinorhyncha','Loricifera','Micrognathozoa','Mollusca','Nematoda','Nematomorpha','Nemertea','Onychophora','Orthonectida','Phoronida','Placozoa','Platyhelminthes','Porifera','Priapulida','Rhombozoa','Rotifera','Sipuncula','Tardigrada','Xenoturbellida']
        self.phylum = self.phylums[self.p]
        def phylumRandomize(self):
            self.p = random.randint(0, 34)
            self.phylum = self.phylums[self.p]
            pass
        if (self.p < 0):
            phylumRandomize(self)

        if __name__== '__main__':
            #print "The Answer to Life, the Universe and Everything is: ", self.TheAnswer 
            pass

# newPhylum = Phylum(spark = 42, p = 7)
# print "newPhylum.phylum: ", newPhylum.phylum
# print "newPhylum.kindom: ", newPhylum.kingdom
# print "newPhylum.domain: ", newPhylum.domain
