let loc = document.getElementById('location')

function getLocaltime(){
    hrs = String(new Date().getHours())
    time = String(new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
    currentTime = hrs+':'+time.slice(3,5)+':00'
    return currentTime;

}

function get_location(){
    loc.innerHTML = 'Please wait a moment'
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(showPosition);

    }else{
        window.location.href = '/location/'+'None'+'/'+'None'
    }
}

function showPosition(position){
    console.log(getLocaltime());
    coordinates = {'latitude':position.coords.latitude, 'longitude':position.coords.longitude}
    window.location.href = '/location/'+coordinates['latitude']+'/'+coordinates['longitude']+'/'+getLocaltime()

}
