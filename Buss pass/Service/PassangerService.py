from Beans.Passanger import Passanger
from Cassandra.Connector import Connector


class PassangerService:
    def __init__(self):
        self.connection = Connector()

    def applyPass(self, passanger):
        category = passanger.passdetails
        number = int(passanger.number)
        name = passanger.name
        age = int(passanger.age)
        gender = passanger.gender
        route = passanger.getRoute()
        self.connection.insert(name, age, gender,category,number, route, )

    def displayPass(self, phno):
        self.connection.myPass(int(phno))

    def importData(self):
        print(self.connection.ID)
        return self.connection.ID


