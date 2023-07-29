import pyodbc

class ItemDatabaseUser:
    def __init__(self):
        self.conn = pyodbc.connect("DRIVER={SQL Server};SERVER=LucasLima;DATABASE=Metalsa")
        self.cursor = self.conn.cursor()

    def criaUsuario(self,free,nome,email,password,cargoUser):
        sql = f"""insert into USUARIOS(Free,Name,Email,Password,CargoUser)
            VALUES
                (?, ?, ?, ?, ?)
        """
        self.cursor.execute(sql,(free,nome,email,password,cargoUser))
        self.cursor.commit()

    def procuraUserFree(self,free):
        result = []
        sql = "SELECT Free, Password FROM USUARIOS WHERE Free = ?"
        self.cursor.execute(sql, (free,))

        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["Free"] = row[0]
            item_dict["Password"] = row[1]
            result.append(item_dict)

        return result

    def procuraTodosIDUser(self):
        result = []
        sql = "SELECT Free FROM USUARIOS"
        self.cursor.execute(sql)

        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict["Free"] = row[0]
            result.append(item_dict)

        return result