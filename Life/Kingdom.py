from Domain import Domain
import random
class Kingdom(Domain):
    def __init__(self, spark = 42, k = -1):
        Domain.__init__(self)
        self.k = k
        self.kingdoms = ['Bacteria', 'Protazoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
        self.kingdom = self.kingdoms[self.k]

        if (k == 0):
            print "k: ", self.k
            self.d = int(raw_input('For kingdom Bacteria, you must specify domain Bacteria=0 or Archaea=1: '))
            Domain.__init__(self, d = self.d)
        else: Domain.__init__(self, d = 2)
        def kingdomRandomize(self):
            self.k = random.randint(0, 4)
            self.kingdom = self.kingdoms[self.k]
            pass
        if (self.k < 0):
            kingdomRandomize(self)
            pass

        if __name__== '__main__':
            print "Domain: The Answer to Life, the Universe and Everything is: ", self.TheAnswer 

newKingdom = Kingdom(spark = 42, k = 5)
print "newKingdom.kingdom: ", newKingdom.kingdom
print "newKingdom.domain: ", newKingdom.domain