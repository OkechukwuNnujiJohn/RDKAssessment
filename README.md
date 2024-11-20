# **Sorting and Weather Application**

This project showcases two distinct features:
1. A command-line application to sort data and determine the median.
2. A program for managing weather that communicates with the OpenWeather API to retrieve and handle city-specific weather information.

---

## **Features**

### **1. Sorting and Median Calculation**
- Sorts a list of numbers in ascending order by implementing the Bubble Sort algorithm.
- Calculates the median of the sorted list:
  - For odd-length lists, the median is the middle number.
  - For even-length lists, the median is the average of the two middle numbers.
- Invalid inputs are handled with the proper error messages.

### **2. Weather Management Application**
- **Search for Weather**: Retrieve current weather details for a city using the OpenWeather API.
- **Add to Favorites**: Add up to three cities to a list of favorites.
- **List Favorites**: Display weather details for all favorite cities.
- **Update Favorites**: Replace a city in favorites with another city.

---

## **Technologies Used**
- **Python 3.8+**
- **OpenWeather API** for weather data
- **Requests Library** for making HTTP calls

---

## **Getting Started**

### **1. Prerequisites**
- Python 3.8 or higher installed.
- Access to the [OpenWeather API](https://openweathermap.org/api):
  - Create a free account and generate an API key.
