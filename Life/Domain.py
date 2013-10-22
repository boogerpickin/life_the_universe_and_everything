from Life import Life
import random
class Domain(Life):
    def __init__(self, spark = 42, d = -1):
        Life.__init__(self)
        self.d = d
        self.domains = ["Bacteria", "Archaea", "Eukaryota"]
        def domainRandomize(self):
                d = random.randint(0,2)
                self.d = self.domains[d]
                pass
        if (d < 0):
            domainRandomize(self)
            pass

        if __name__ == '__main__':
            print "The Answer to Life, the Universe and Everything is: ", self.TheAnswer 

newDomain = Domain(-1)
print newDomain.d
        


