class Cloth:

    def __init__(self,blazer,trousers,shirt,sneakers):
        self.blazer = blazer
        self.trousers = trousers
        self.shirt = shirt
        self.sneakers = sneakers

    def sayBlazer(self):
        print (" на мне надет лапсердак:", self.blazer)
    
    def sayTrousers(self):
        print ( "на мен надеты портки :", self.trousers)

    def sayShirt(self):
        print ( " мацка алкоголичка :", self.shirt)

    def saySneakers(self):
        print ( " какие гавноступики :", self.sneakers)