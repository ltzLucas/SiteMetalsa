# from DaoUser import DatabaseUser
# from modelo.User import User
#
# # Create a User instance
# # new_user = User(123, "lucas", "lucas@example.com", "mypassword")
#
# # print(new_user.validatePassword("mypassword2"))
#
# # Create a DatabaseUser instance
# db = DatabaseUser()
#
# # # # Insert the user into the database
# # db.insertUser(new_user)
#
# searched_user = db.searchUserByFree(1223)
# #
# if searched_user:
#     print(f"Found user: {searched_user.name}, {searched_user.email} , {searched_user.free}")
# else:
#     print("User not found")
#
# # all_users = db.searchAllUsers()
# #
# # if not all_users:
# #     print("No users found.")
# # else:
# #     for user in all_users:
# #         print(f"Name: {user.free}, Email: {user.email}")
#
# # # db.deleteUser(1234)
# #
# # db.close()
#
from BD.DaoUser import DatabaseUser

db = DatabaseUser()
free = 2335
passwordUser = 123456

user = db.searchUserByFree(int(free))
if user:
    if user.free != free or user.password != passwordUser:
        print('senha errada')
    else:
        print('senha certa')
