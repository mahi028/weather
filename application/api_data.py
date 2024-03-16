import requests

def wether_data(coordinate : list,
                current_date : str,
                current_time : str
                ):
    

    api_address = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{coordinate[0]},{coordinate[1]}/{current_date}T{current_time}?unitGroup=metric&key=2HHMMX484QL8L2E46U4M2HWRL&include=current&elements=%2Baqieur"

    return api_address
    a = requests.get(api_address)
    return a.json()