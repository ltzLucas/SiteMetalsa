from DaoUser import ItemDatabaseUser
db = ItemDatabaseUser()
# criaUsuario(2335,'Lucas LIma','lucas.lima@metalsa.com','senha123','Admin')

x = db.procuraTodosIDUser()

for y in x:
    if y == 2335:
        print('é igual')


