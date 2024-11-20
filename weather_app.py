import requests

# Class to access the openweather api and manage weather details for cities
class WeatherApp:
    def __init__(self):
        self.api_key = '69fc597c3d9b254b48be0875d5783648'
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'
        self.favourite_cities = []
        
    def validate_city_name(self, city):
        # Check if the city is a Valid str.
        # Returns bool (True if valid else False).
        return bool(city.strip())
    
    def get_weather(self, city):
        # Fetch the current weather for a given city.
        # returns weather details as dict or str
        if not self.validate_city_name(city):
            return "City name cannot be empty. Please enter a valid city."
        
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Parse the weather details
            return {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'weather': data['weather'][0]['description']
            }
        except requests.RequestException as e:
            return f"Error fetching weather: {e}"
        except KeyError:
            return "City not found or invalid response from API."

    def add_to_favourites(self, city):
        # Add a city to the list of favourites, ensuring the limit is 3 cities.
        if len(self.favourite_cities) >= 3:
            print("Cannot add more than 3 cities. Please update favourites.")
        else:
            if city not in self.favourite_cities:
                self.favourite_cities.append(city)
                print(f"{city} added to favourites.")
            else:
                print(f"{city} is already in favourites.")

    def list_favourites(self):
        #List all favourite cities along with their current weather details.
        print("Favourite Cities Weather:")
        for city in self.favourite_cities:
            weather = self.get_weather(city)
            if isinstance(weather, dict):
                print(f"{weather['city']}: {weather['temperature']}°C, {weather['weather']}")
            else:
                print(weather)

    def update_favourites(self, old_city, new_city):
        # Replace an old favourite city with a new one, maintaining the favourites limit.
        if old_city in self.favourite_cities:
            self.favourite_cities.remove(old_city)
            self.add_to_favourites(new_city)
        else:
            print(f"{old_city} is not in favourites.")

def main():
    # Main menu-driven application for managing weather details and favourite cities.
    app = WeatherApp()
    while True:
        print("\nMenu:")
        print("1. Search for weather details")
        print("2. Add city to favourites")
        print("3. List favourite cities")
        print("4. Update favourite cities")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            city = input("Enter city name: ")
            weather = app.get_weather(city)
            if isinstance(weather, dict):
                print(f"{weather['city']}: {weather['temperature']}°C, {weather['weather']}")
            else:
                print(weather)
        elif choice == '2':
            city = input("Enter city name to add to favourites: ")
            app.add_to_favourites(city)
        elif choice == '3':
            app.list_favourites()
        elif choice == '4':
            old_city = input("Enter city to remove: ")
            new_city = input("Enter city to add: ")
            app.update_favourites(old_city, new_city)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
