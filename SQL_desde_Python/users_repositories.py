from pathlib import Path
import csv

WORKING_PATH = Path.cwd()

class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.users_data = []

    def _load_csv_data (self):
        file_path = WORKING_PATH / "users_data.csv"
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
            "name": user_record[1],
            "email": user_record[2],
            "username": user_record[3],
            "password": user_record[4],
            "birth_date": user_record[5],
            "account_status": user_record[6],
        }

    def _insert_users_rows(self):
        try:
            self.users_data = self._load_csv_data()
            for i in range(len(self.users_data)):
                row = self.users_data[i]
                query = "INSERT INTO lyfter_car_rental.users (name, email, username, password, birth_date, account_status) VALUES (%s, %s, %s, %s, %s, %s);"
                data = (row[0], row[1], row[2], row[3], row[4], row[5])
                self.db_manager.execute_query(query, *data)
            print("Users inserted successfully")
            return True
        except Exception as error:
            print("Error inserting users into the database: ", error)
            return False
        
    def create_and_insert_users_table(self):
        try:
            self.db_manager.execute_query(
                "CREATE TABLE lyfter_car_rental.users (" \
                "id SERIAL PRIMARY KEY, " \
                "name VARCHAR(100) NOT NULL, " \
                "email VARCHAR(150) UNIQUE NOT NULL," \
                "username VARCHAR(50) UNIQUE NOT NULL," \
                "password VARCHAR(255) NOT NULL," \
                "birth_date DATE NOT NULL," \
                "account_status VARCHAR(50) NOT NULL);", ())
            print("Users table created successfully")

            self._insert_users_rows()
            return True
        except Exception as error:
            print("Error creating table: ", error)
            return False 
        
    def insert_user(self, name, email, username, password, birth_date, account_status):
        try:
            query = "INSERT INTO lyfter_car_rental.users (name, email, username, password, birth_date, account_status) VALUES (%s, %s, %s, %s, %s, %s);"
            data = (name, email, username, password, birth_date, account_status)
            self.db_manager.execute_query(query, *data)
            print("User inserted successfully")
            return True
        except Exception as error:
            print("Error inserting user into the database: ", error)
            return False
        
    def update(self, account_status, id):
        try:
            users_tuple = (account_status, id)
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status = %s WHERE ID = %s",
                *users_tuple
            )
            print("User updated successfully")
            return True
        except Exception as error:
            print("Error updating a user from the database: ", error)
            return False

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.users;"
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False

    def get_by_id(self, id):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.users WHERE id = %s;",
                id
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False
        
    def delete(self, id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_car_rental.users WHERE id = %s", id
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