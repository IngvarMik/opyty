class User:
    age=0
    name = "No Name"
    email = "mail@test.ru"

    def __init__(self , name , age , email):
        self.age = age
        self.name = name
        self.email = email

    def sayName(self):
        print( self.name)
    
    def sayEmail(self):
        print (self.email)
    
    def sayAge(self):
        print (self.age)


newUser = User ("jopa",29,"hello jopa@mail.ru" )
newUser.sayAge()
newUser.sayName()
newUser.sayEmail()
newUser.sayAge()

