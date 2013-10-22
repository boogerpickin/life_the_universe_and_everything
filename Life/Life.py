import random
class Life(object):
    def __init__(self, spark = 42):
        self.TheAnswer = spark
        while (self.TheAnswer != 42):
            def sparkRandomize(self):
                self.TheAnswer = random.randint(40,45)
                if (self.TheAnswer != 42):
                    print "The answer is not ", self.TheAnswer, ""
            sparkRandomize(self)
        print "The Answer to Life, the Universe and Everything is: ", self.TheAnswer

NewLifeForm = Life(spark = 21)