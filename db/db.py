import sqlite3

PARKING_SPOTS = [(1, "False"), (1, "False"), (1, "False"), (2, "True"), (2, "False"),
                 (2, "False"), (3, "False"), (3, "True"), (3, "True"), (4, "True")]
CARS = [("HWR3886", "MONSTER_TRUCK", "1,2", 15), ("WDR3244", "MONSTER_TRUCK",
                                                  "4,5", 15), ("QAS2953", "REGULAR", "3", 10), ("KFV684", "REGULAR", "6", 10)]


class Sqlite:
    """ All the database methods are abstracted in this class"""

    def __init__(self):
        self.conn = sqlite3.connect('./db/database.db')
        if self.conn:
            print("Opened database successfully")
        else:
            raise Exception

    def initDB(self):
        self.c = self.conn.cursor()
        self.c.execute(
            'CREATE TABLE cars (id INTEGER PRIMARY KEY AUTOINCREMENT, no TEXT, type TEXT, spot_id TEXT DEFAULT "0", money INTEGER, enter_time INTEGER DEFAULT 0, exit_time INTEGER DEFAULT 0,  FOREIGN KEY (spot_id) REFERENCES parking_spot (id))')

        self.c.execute(
            'CREATE TABLE parking_spots (id INTEGER PRIMARY KEY AUTOINCREMENT, block_id INTEGER, availability TEXT)')
        print("Table created successfully")
        self.c.close()

    def insertData(self):
        self.c = self.conn.cursor()
        self.c.execute('INSERT INTO parking_spots (block_id,availability) VALUES (1,"False"), (1,"False"), (1,"False"), (2,"True"), (2,"False"), (2,"False"), (3,"False"), (3,"True"), (3,"True"), (4,"True")')
        self.conn.commit()
        self.c.execute('INSERT INTO cars (no, type, spot_id, money) VALUES ("HWR3886", "MONSTER_TRUCK", "1,2", 15), ("WDR3244", "MONSTER_TRUCK", "4,5", 15),("QAS2953", "REGULAR", "3", 10),("KFV684", "REGULAR", "6", 10)')
        self.conn.commit()
        self.c.close()

    def getAllCarsRevenue(self):
        self.c = self.conn.cursor()
        self.c.execute("SELECT COUNT(*), SUM(money) FROM cars")
        response = self.c.fetchall()
        self.c.close()
        print(response[0])
        return response[0]

    def getNoOfParkedCars(self):
        self.c = self.conn.cursor()
        self.c.execute("SELECT COUNT(*) FROM cars WHERE spot_id !=0")
        response = self.c.fetchall()
        self.c.close()
        return response[0][0]

    def getNoOfParkedCarsByType(self, type):
        self.c = self.conn.cursor()
        self.c.execute(
            "SELECT COUNT(*) FROM cars WHERE spot_id !=0 AND type='"+type+"'")
        response = self.c.fetchall()
        self.c.close()
        return response[0][0]

    def getAvailableParkingSpot(self):
        self.c = self.conn.cursor()
        self.c.execute(
            "SELECT id FROM parking_spots WHERE availability='True'")
        response = self.c.fetchone()
        self.c.close()
        if response:
            return response[0]
        else:
            return None

    def getAllAvailableParkingSpots(self):
        self.c = self.conn.cursor()
        self.c.execute(
            "SELECT id,block_id FROM parking_spots WHERE availability='True'")
        response = self.c.fetchall()
        self.c.close()
        return response

    def bookSpots(self, spotIds):
        self.c = self.conn.cursor()
        for spotId in spotIds:
            self.c.execute(
                "UPDATE parking_spots SET availability='False' WHERE id =?", (spotId,))
            response = self.conn.commit()
        self.c.close()
        return response

    def addCar(self, car):
        self.c = self.conn.cursor()
        query = "INSERT INTO cars (no, type, spot_id, money) VALUES (?,?,?,?)"
        self.c.execute(query, car)
        # self.c.execute("INSERT INTO cars (no, type, spot_id, money) VALUES ('"+no+"','"+carType+"','"+str(spotId)+"',"+money+")")
        response = self.conn.commit()
        self.c.close()
        print("response in add car db file is ", response)
        return response


if __name__ == "__main__":
    db = Sqlite()
    db.initDB()
    db.insertData()
