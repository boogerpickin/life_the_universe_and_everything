from Life import Life
class Domain(Life):
    def __init__(self, spark = 42):
        Life.__init__(self)
        self.domains = ["Bacteria", "Archaea", "Eukaryota"]
        if __name__ == '__main__':
            print "The Answer to Life, the Universe and Everything is: ", self.TheAnswer 

newDomain = Domain(-1)
print newDomain.TheAnswer
        


