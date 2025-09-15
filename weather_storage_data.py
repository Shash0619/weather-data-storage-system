# weather_data_storage.py

SENTINEL = -9999.0  # sentinel value for missing data


class WeatherRecord:
    def __init__(self, date: str, city: str, temperature: float):
        self.date = date
        self.city = city
        self.temperature = temperature

    def __str__(self):
        return f"Date: {self.date}, City: {self.city}, Temp: {self.temperature}"


class WeatherDataStorage:
    def __init__(self, years, cities):
        self.years = years
        self.cities = cities
        # 2D array (list of lists), initialized with sentinel values
        self.temperature_data = [[SENTINEL for _ in range(len(cities))] for _ in range(len(years))]

    # Insert new data
    def insert(self, city, year, temperature):
        if city in self.cities and year in self.years:
            row = self.years.index(year)
            col = self.cities.index(city)
            self.temperature_data[row][col] = temperature

    # Delete a record
    def delete(self, city, year):
        if city in self.cities and year in self.years:
            row = self.years.index(year)
            col = self.cities.index(city)
            self.temperature_data[row][col] = SENTINEL

    # Retrieve a record
    def retrieve(self, city, year):
        if city in self.cities and year in self.years:
            row = self.years.index(year)
            col = self.cities.index(city)
            return self.temperature_data[row][col]
        return SENTINEL

    # Row-major access
    def row_major_access(self):
        print("Row-Major Traversal:")
        for i in range(len(self.years)):
            for j in range(len(self.cities)):
                print(self.temperature_data[i][j], end=" ")
            print()

    # Column-major access
    def column_major_access(self):
        print("Column-Major Traversal:")
        for j in range(len(self.cities)):
            for i in range(len(self.years)):
                print(self.temperature_data[i][j], end=" ")
            print()

    # Handle sparse data
    def handle_sparse_data(self):
        print("Sparse Data Representation:")
        for i in range(len(self.years)):
            for j in range(len(self.cities)):
                if self.temperature_data[i][j] != SENTINEL:
                    print(f"Year: {self.years[i]}, City: {self.cities[j]}, Temp: {self.temperature_data[i][j]}")

    # Complexity analysis
    def analyze_complexity(self):
        print("Insert: O(1), Delete: O(1), Retrieve: O(1)")
        print("Row/Column Traversal: O(N*M)")
        print("Space Complexity: O(N*M) for full 2D array")


if __name__ == "__main__":
    years = [2023, 2024, 2025]
    cities = ["Delhi", "Mumbai", "Chennai"]

    storage = WeatherDataStorage(years, cities)

    # Insert records
    storage.insert("Delhi", 2023, 32.5)
    storage.insert("Mumbai", 2023, 29.0)
    storage.insert("Chennai", 2024, 34.0)

    # Retrieve
    print("Retrieve Delhi 2023:", storage.retrieve("Delhi", 2023))

    # Row-major & Column-major
    storage.row_major_access()
    storage.column_major_access()

    # Sparse data
    storage.handle_sparse_data()

    # Delete record
    storage.delete("Mumbai", 2023)
    print("After Deletion:")
    storage.handle_sparse_data()

    # Analyze complexity
    storage.analyze_complexity()
