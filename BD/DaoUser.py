import pyodbc
from modelo.User import User

class DatabaseUser:
    def __init__(self):
        self.conn = pyodbc.connect("DRIVER={SQL Server};SERVER=LucasLima;DATABASE=Metalsa")
        self.cursor = self.conn.cursor()

    def insertUser(self,user):
        sql = f"""insert into USUARIOS(Free,Name,Email,Password,CargoUser)
            VALUES
                (?, ?, ?, ?, ?)
        """
        self.cursor.execute(sql,(user.free,user.name,user.email,user.password,user.userPosition))
        self.cursor.commit()

    def searchUserByFree(self, free):
        sql = "SELECT * FROM USUARIOS WHERE Free = ?"
        self.cursor.execute(sql, (free,))
        user_data = self.cursor.fetchone()

        if user_data:
            user = User(user_data[0], user_data[1], user_data[2], user_data[3])
            return user
        else:
            return None

    def searchAllUsers(self):
        sql = "SELECT * FROM USUARIOS"
        self.cursor.execute(sql)
        users_data = self.cursor.fetchall()

        users = []
        for user_data in users_data:
            user = User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
            users.append(user)

        return users

    def deleteUser(self,free):
        sql = "DELETE USUARIOS WHERE free = ?"
        self.cursor.execute(sql, (free,))
        self.cursor.commit()

    def close(self):
        self.conn.close()