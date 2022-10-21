class Passanger:

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def gender(self):
        return self.__gender

    @property
    def number(self):
        return self.__number

    @property
    def passdetails(self):
        return self.__passdetails

    def getRoute(self):
        return self.__root


    # -----------------------------------------------------
    @name.setter
    def name(self, newname):
        self.__name = newname



    @age.setter
    def age(self, newage):
        self.__age = newage

    @gender.setter
    def gender(self, newgender):
        self.__gender = newgender

    @number.setter
    def number(self, newnum):
        self.__number = newnum

    @passdetails.setter
    def passdetails(self,details):
        self.__passdetails = details

    def setRoute(self, src, dest):
        root = {"source": src, "destination": dest}
        self.__root = root

# p = Passanger()
# p.name = "sanketh"
# print(p.name)
# p.setRoot("abc","dddsd")
# print(p.getRoot())
