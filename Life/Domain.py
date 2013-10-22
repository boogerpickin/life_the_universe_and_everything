from Life import Life
import random
class Domain(Life):
    def __init__(self, spark = 42, d = -1):
        Life.__init__(self)
        self.d = d
        self.domains = ["Bacteria", "Archaea", "Eukaryota"]
        self.domain = self.domains[self.d]
        def domainRandomize(self):
                self.d = random.randint(0,2)
                self.domain = self.domains[self.d]
                pass
        if (self.d < 0):
            domainRandomize(self)
            pass

        if __name__ == '__main__':
            print "The Answer to Life, the Universe and Everything is: ", self.TheAnswer 

# newDomain = Domain(-1)
# print "Outside print; Domain: ", newDomain.d
        


