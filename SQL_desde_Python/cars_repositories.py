from pathlib import Path
import csv

WORKING_PATH = Path.cwd()

class CarRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.cars_data = []

    def _load_csv_data (self):
        file_path = WORKING_PATH / "cars_data.csv"
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
    
    def _format_car(self, user_record):
        return {
            "id": user_record[0],
            "brand": user_record[1],
            "model": user_record[2],
            "manufacturing_year": user_record[3],
            "status": user_record[4]
        }

    def _insert_cars_rows(self):
        try:
            self.cars_data = self._load_csv_data()
            for i in range(len(self.cars_data)):
                row = self.cars_data[i]
                query = "INSERT INTO lyfter_car_rental.cars (brand, model, manufacturing_year, status) VALUES (%s, %s, %s, %s);"
                data = (row[0], row[1], row[2], row[3])
                self.db_manager.execute_query(query, *data)
            print("Cars inserted successfully")
            return True
        except Exception as error:
            print("Error inserting cars into the database: ", error)
            return False
        
    def create_and_insert_cars_table(self):
        try:
            self.db_manager.execute_query(
                "CREATE TABLE lyfter_car_rental.cars (" \
                "id SERIAL PRIMARY KEY," \
                "brand VARCHAR(100) NOT NULL," \
                "model VARCHAR(100) NOT NULL," \
                "manufacturing_year INTEGER NOT NULL," \
                "status VARCHAR(50) NOT NULL);", ())
            print("Cars table created successfully")

            self._insert_cars_rows()
            return True
        except Exception as error:
            print("Error creating table: ", error)
            return False 

    def insert_car(self, brand, model, manufacturing_year, status):
        try:
            query = "INSERT INTO lyfter_car_rental.cars (brand, model, manufacturing_year, status) VALUES (%s, %s, %s, %s);"
            data = (brand, model, manufacturing_year, status)
            self.db_manager.execute_query(query, *data)
            print("Car inserted successfully")
            return True
        except Exception as error:
            print("Error inserting car into the database: ", error)
            return False

    def update(self, status, id):
        try:
            cars_tuple = (status, id)
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET status = %s WHERE ID = %s",
                *cars_tuple
            )
            print("Car updated successfully")
            return True
        except Exception as error:
            print("Error updating a car from the database: ", error)
            return False

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.cars;"
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting a car from the database: ", error)
            return False
        
    def get_by_state(self, status):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.cars WHERE status = %s;",
                status
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting a car from the database: ", error)
            return False
        
    def delete(self, id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_car_rental.cars WHERE id = %s", id
            )
            print("User deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a user from the database: ", error)
            return False

    def drop_table(self):
        try:
            self.db_manager.execute_query(
                "DROP TABLE lyfter_car_rental.cars", ()
            )
            print("Users Table deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a user from the database: ", error)
            return False