from requests import get
from pandas import DataFrame

fuel_type="EL" # EL = electric, E = hybrid, D = diesel, BN = gasoline, 10 = hydrogen, 13 = LPG, 25 = flex-fuel

def get_cars_data(page=1):
    skip = (page - 1) * 22
    top = skip + 22
    url = f"https://www.kamux.fi/api/search?skip={skip}&top={top}&fuelTypeCode={fuel_type}"

    response = get(url)
    data = response.json()
    return data

print("Getting data from Kamux...")

cars_data = []
for page in range(1, 33):
    cars_data += get_cars_data(page)['results']


print(f"Total cars retrieved: {len(cars_data)}")
# exit()

car_specs = {}
for i, car in enumerate(cars_data):

    if not (car.get("batteryTestPdfUrl")):
        continue

    id = car.get("productId")
    manufacturer = car.get("manufacturer")
    model = car.get("model")
    manufacturer_and_model = car.get("manufacturerAndModel")
    model_year = car.get("modelYear")
    vehicle_type = car.get("vehicleType")
    outlet = car.get("outlet")
    first_registration_date = car.get("firstRegistrationDate")
    first_usage_date = car.get("firstUsageDate")
    purchase_date = car.get("purchaseDate")
    last_inspection_date = car.get("lastInspectionDate")
    battery_capacity_kWh = car.get("batteryCapacity")
    electric_range_km_reported = car.get("rangeOfElectricMotor")
    power_kW = car.get("powerValueKw")
    top_speed_kmh = car.get("topSpeed")
    mileage_km = car.get("mileage")
    price_eur = car.get("price")
    battery_test_pdf_url = car.get("batteryTestPdfUrl")
    is_imported = car.get("isImported")
    is_utility_vehicle = car.get("isUtilityVehicle")

    car_specs[i] = {
        "manufacturer": manufacturer,
        "model": model,
        "manufacturer_and_model": manufacturer_and_model,
        "model_year": model_year,
        "vehicle_type": vehicle_type,
        "outlet": outlet,
        "first_registration_date": first_registration_date,
        "first_usage_date": first_usage_date,
        "purchase_date": purchase_date,
        "last_inspection_date": last_inspection_date,
        "battery_capacity_kWh": battery_capacity_kWh,
        "electric_range_km_reported": electric_range_km_reported,
        "power_kW": power_kW,
        "top_speed_kmh": top_speed_kmh,
        "mileage_km": mileage_km,
        "price_eur": price_eur,
        "battery_test_pdf_url": battery_test_pdf_url,
        "is_imported": is_imported,
        "is_utility_vehicle": is_utility_vehicle
    }
    # print(car_specs[i])  # Print the first car's data to check the structure


print(f"Total cars with battery test report: {len(car_specs)}")

car_specs_df = DataFrame.from_dict(car_specs, orient='index')
car_specs_df.to_csv("kamux_cars_data.csv", index=False)

print(f"{len(car_specs_df)} Data saved to kamux_cars_data.csv")
