let loc = document.getElementById('location')

function get_location(){
    loc.innerHTML = 'Please wait a moment'
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(showPosition);
    }else{
        window.location.href = '/location/'+'None'+'/'+'None'
    }
}

function showPosition(position){
    coordinates = {'latitude':position.coords.latitude, 'longitude':position.coords.longitude}
    window.location.href = '/location/'+coordinates['latitude']+'/'+coordinates['longitude']

}