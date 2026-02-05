from requests import get
from bs4 import BeautifulSoup
from sqlalchemy import null

def get_cars_data(page=1):
    url = f"https://www.kamux.fi/api/search?fuelTypeCode=EL&page={page}"
    response = get(url)
    data = response.json()
    return data

print("Getting data from Kamux...")

cars_data = []
cars_with_report = 0
for page in range(1, 29):  # Scrape first 5 pages
    cars_data += get_cars_data(page)['results']

print(cars_data[0])  # Print the first car's data to check the structure
# for cars in cars_data:
#     if cars["hasBatteryTest"] is not "null":
#         cars_with_report += 1
    
print(f"Retrieved {len(cars_data)} cars from Kamux.")
# print(f"Number of cars with battery test report: {cars_with_report}")
# print(cars_data)
