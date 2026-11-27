from db import PgManager
from users_repositories import UserRepository
from cars_repositories import CarRepository
from user_car_repositories import UserCarRepository

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
)
users_repo = UserRepository(db_manager)
#users_repo.create_and_insert_users_table()
cars_repo = CarRepository(db_manager)
#cars_repo.create_and_insert_cars_table()
user_car_repo = UserCarRepository(db_manager, users_repo, cars_repo)
#user_car_repo.create_and_insert_user_car_table()

user_car_repo.update("completed", 37)

# #Ejemplo de uso de Tarea 2 punto 6:
#cars_repo.update("available", 7)
# user_car_repo.update("completed", 7, "active")

# #Ejemplo Tarea 2 punto 7:
# cars_repo.update("unavailable", 8)

