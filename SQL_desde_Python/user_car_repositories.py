from pathlib import Path
import csv

WORKING_PATH = Path.cwd()

class UserCarRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.rental_data = self._load_csv_data()
        self._create_and_insert_user_car_table()

    def _load_csv_data (self):
        file_path = WORKING_PATH / "rental_data.csv"
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)
                return list(reader)
        except FileNotFoundError:
            print("Error: CSV file not found.")
            exit()
        except Exception as e:
            print(f"Unexpected error: {e}")
            exit()
    
    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "full_name": user_record[1],
            "email": user_record[2],
            "password": user_record[3],
        }

    def _insert_users_cars_rows(self):
        try:
            for i in range(len(self.rental_data)):
                row = self.rental_data[i]
                query = "INSERT INTO lyfter_car_rental.usercar (user_id, car_id, rent_state) VALUES (%s, %s, %s);"
                data = (row[0], row[1], row[2])
                self.db_manager.execute_query(query, *data)
            print("Users cars relations and rental information inserted successfully")
            return True
        except Exception as error:
            print("Error inserting rental data into the database: ", error)
            return False
        
    def _create_and_insert_user_car_table(self):
        try:
            self.db_manager.execute_query(
                "CREATE TABLE lyfter_car_rental.usercar (" \
                "id SERIAL PRIMARY KEY," \
                "user_id INTEGER NOT NULL," \
                "car_id INTEGER NOT NULL," \
                "rent_date DATE NOT NULL DEFAULT CURRENT_DATE," \
                "rent_state VARCHAR(30) NOT NULL," \
                "FOREIGN KEY (user_id) REFERENCES lyfter_car_rental.users(id)," \
                "FOREIGN KEY (car_id) REFERENCES lyfter_car_rental.cars(id));", ())
            print("UserCar table created successfully")

            self._insert_users_cars_rows()
            return True
        except Exception as error:
            print("Error creating table: ", error)
            return False 

    def insert_new_rent(self, user_id, car_id, rent_state):
        try:
            query = "INSERT INTO lyfter_car_rental.usercar (user_id, car_id, rent_state) VALUES (%s, %s, %s);"
            data = (user_id, car_id, rent_state)
            self.db_manager.execute_query(query, *data)
            print("New rent inserted successfully")
            return True
        except Exception as error:
            print("Error inserting rental data into the database: ", error)
            return False

    def update(self, new_rent_state, car_id, actual_rent_state):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.usercar SET (rent_state) = (%s) WHERE CAR_ID = %s AND RENT_STATE = (%s) ",
                (new_rent_state, car_id, actual_rent_state),
            )
            print("Car updated successfully")
            return True
        except Exception as error:
            print("Error updating a car from the database: ", error)
            return False

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, full_name, email, password FROM lyfter_duad.users;"
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False

    def get_by_id(self, _id):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, full_name, email, password FROM lyfter_duad.users WHERE id = %s;",
                (_id,),
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False
        
    def delete(self, _id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_car_rental.users WHERE id = (%s)", (_id,)
            )
            print("User deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a user from the database: ", error)
            return False

    def drop_table(self):
        try:
            self.db_manager.execute_query(
                "DROP TABLE lyfter_car_rental.users", ()
            )
            print("Users Table deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a user from the database: ", error)
            return False