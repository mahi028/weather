import requests

def wether_data(coordinate : list,
                current_date : str,
                current_time : str
                ):
    

    api_address = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{coordinate[0]},{coordinate[1]}/{current_date}T{current_time}?unitGroup=metric&key=TA7F22RE83G7Q4MEGR5DY6W8E&include=current&elements=%2Baqieur"

    a = requests.get(api_address)
    return a.json()