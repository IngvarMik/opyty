class User:

    def __init__(self,first_name,last_name,year,sex):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.sex = sex


    def sayName(self):
        print ( " Меня зовут :", self.first_name)

    def saySurname(self):
        print ("моя фамилия :" , self.last_name)

    def sayYear(self):
        print(" мне во скока лет :" , self.year)

    def saySex(self):
        print("вот и кто я? :" , self.sex)

    