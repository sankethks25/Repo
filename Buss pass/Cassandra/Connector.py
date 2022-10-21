import cassandra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
class Connector:
    def __init__(self):
        self.ID = [];

    def makeConnection(self):
        cloud_config = {'secure_connect_bundle': 'E:\secure-connect-test (1).zip'}
        auth_provider = PlainTextAuthProvider('JAWdBHFiZWNhtjenaMlTOPlm',
                                              '4.+rCJnnr4P_,tA8Hmzjj1.RIs+Xzs4SNrXdv5BfyHBy314YnrDdNYKIp0PlQz_0YE9E78ZxN1Kfb0UkIA5ZqkH--wv9gf1,J1h3+lh3Zfr6ZJMiqTidTB_xs4wSJq-9')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        session = cluster.connect()
        return session


    def dropTable(self):
        try:
            session = self.makeConnection()
            query = "DROP TABLE buspass.passangers;"
            row = session.execute(query).one()
            print("Table successfully Deleted")
        except Exception as e:
            print(str(e))

    def modifyTable(self):
        try:
            session = self.makeConnection()
            query = "ALTER TABLE buspass.passangers ADD category text;"
            row = session.execute(query).one()
            print("column successfully inserted")
        except Exception as e:
            print(str(e))

    def createTable(self):
        try:
            session=self.makeConnection()
            query = "CREATE TABLE buspass.passangers(ID uuid PRIMARY KEY,name text, age int,gender text,category text,phno bigint ,route map<text,text>)"
            row = session.execute(query).one()
            print("successfully created")
        except Exception as e:
            print(str(e))



    def insert(self,name, age, gender,category,phno, route):
        try:
            session=self.makeConnection()
            temp = [{"name":name,"age":age,"gender":gender,"category":category,"phno":phno,"route":route}]
            print(temp)
            query = "INSERT INTO buspass.passangers(ID,name,age,gender,category,phno,route) values(now(),?,?,?,?,?,?)"
            prepared = session.prepare(query)
            for data in temp:
                session.execute(prepared,(data['name'],data['age'],data['gender'],data['category'],data["phno"],data['route']))
            print("successfully inserted")
        except Exception as e:
            print(str(e))

    def viewTable(self):
        try:
            session=self.makeConnection()
            query = "select * from buspass.passangers"
            row = session.execute(query)
            for record in row:
                self.ID.append(record)
               # print(record)
        except Exception as e:
            print(str(e))

    def myPass(self,phno):
        try:
            session=self.makeConnection()
            query = "SELECT * FROM buspass.passangers WHERE phno = {}".format(phno)
            row = session.execute(query)
            for record in row:
                self.ID.append(record)
            print(self.ID)
        except Exception as e:
            print(str(e))

    def secondaryIndex(self):
        try:
            session=self.makeConnection()
            query = "CREATE INDEX ON buspass.passangers(phno);"
            row = session.execute(query)
        except Exception as e:
            print((str(e)))

    def drop(self):
        try:
            session=self.makeConnection()
            query = "DELETE FROM buspass.passanger WHERE id = 200;"
            row = session.execute(query).one()
            print("successfully Deleted")
        except Exception as e:
            print(str(e))



#c = Connector()
#c.dropTable()
# c.keySpace()
#c.createTable()
#c.insert('sanketh', 23, 'male',"day",8277337162, {'source': 'mejastic', 'destination': 'silk board'})
#c.viewTable()
#c.myPass(8277337162)
#c.drop()
# c.use()
# c.createTable_test()
#c.secondaryIndex()
#c.modifyTable()
#c.insert_test(82,'sanketh',23,'male')
# for i in c.ID:
#     print(i)
