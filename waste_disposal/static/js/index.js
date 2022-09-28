
 x = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
  
  
}

function getReverseGeocodingData(lat, lng) {
  
}


function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
  const uluru = { lat: position.coords.latitude, lng: position.coords.longitude };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 9,
    center: uluru,
  });
  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
  });
}
x.addEventListener("click",getLocation)