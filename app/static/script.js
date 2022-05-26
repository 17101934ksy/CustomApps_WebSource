var container = document.getElementById('map'); 
var options = {
       center: new kakao.maps.LatLng(37.5166119773031, 127.041258693516),
       level: 3
}; 
var map = new kakao.maps.Map(container, options); 
var markerPosition  = new kakao.maps.LatLng(37.5166119773031, 127.041258693516);  
var marker = new kakao.maps.Marker({position: markerPosition}); 
marker.setMap(map); 

function location(lat, lng) {
    return lat * lng ;    
}