from flask import Flask, render_template
from application.api_data import wether_data
import datetime

app = Flask(__name__, 
            static_url_path='', 
            static_folder='static',)


@app.route('/')
def index():
    return render_template('get_loc.html')

@app.route('/location/<latitude>/<longitude>')
def get_location(latitude, longitude):
    
    key = 'TA7F22RE83G7Q4MEGR5DY6W8E'
    if latitude == 'None' or longitude == 'None':
        return '<h1>Your Browser does not support geolocation</h1>'
    
    d = str(datetime.datetime.now()).split(' ')
    current_date = d[0]
    current_time = d[1].split('.')[0]

    coordinates = [latitude,longitude]
    icon_colors = {1:['green','Very Good'], 2: ['light-green', 'Good'], 3: ['yellow', 'Medium'], 4: ['orange','Poor'], 5: ['red', 'Very Poor'], 6:['red', 'Extreamly Poor']}
    data = wether_data(coordinate = coordinates,current_date = current_date, current_time = current_time)

    background_image = '/img/'+data['currentConditions']['icon']+'.jpg'
    print(icon_colors[data['currentConditions']['aqieur']][0])
    return render_template('index.html',
                            data = data,
                            background_image = background_image,
                            icon_color = icon_colors[data['currentConditions']['aqieur']][0],
                            aqi_condition = icon_colors[data['currentConditions']['aqieur']][1])

#DRIVER CODE
#IF RUNNIG ON A LOCAL MACHINE, UN-COMMENT THE NEXT TWO LINES. OTHERWSISE, LEAVE THEM AS IS.
# if __name__ == '__main__':
#     app.run(debug = False)