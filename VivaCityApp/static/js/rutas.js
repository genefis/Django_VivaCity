// rutas.js

// Variables para almacenar los marcadores de diferentes categorías
var hotelMarkers = [];
// Añade más variables según las categorías que necesites

// Variable para almacenar el mapa
var map;

// Función para inicializar el mapa y marcadores
function initMap() {
    // Coordenadas de Loja, Ecuador
    var loja = { lat: -3.9931, lng: -79.2045 };

    // Opciones del mapa
    var mapOptions = {
        center: loja,
        zoom: 14
    };

    // Crear el mapa en el contenedor con ID "map"
    map = new google.maps.Map(document.getElementById('map'), mapOptions);

    // Llama a la función para mostrar hoteles
    showHotels();
}

// Funciones para mostrar marcadores según la categoría seleccionada
function showHotels() {
    // Limpia los marcadores existentes
    clearMarkers();

    // Realiza una búsqueda cercana de hoteles en Loja
    var request = {
        location: { lat: -3.9931, lng: -79.2045 },
        radius: 5000, // Radio de búsqueda en metros (ajusta según sea necesario)
        types: ['lodging'] // Tipo de lugares, en este caso, 'lodging' para hoteles
    };

    var service = new google.maps.places.PlacesService(map);
    service.nearbySearch(request, function (results, status) {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
            // Muestra los marcadores para cada resultado de búsqueda
            for (var i = 0; i < results.length; i++) {
                createMarker(results[i]);
            }
        }
    });
}

// Función para crear un marcador para un lugar
function createMarker(place) {
    var marker = new google.maps.Marker({
        map: map,
        position: place.geometry.location,
        title: place.name
    });

    // Añade el marcador a la lista de hoteles
    hotelMarkers.push(marker);
}

// Función para limpiar todos los marcadores
function clearMarkers() {
    for (var i = 0; i < hotelMarkers.length; i++) {
        hotelMarkers[i].setMap(null);
    }
    hotelMarkers = [];
}

// Espera a que se cargue el contenido de la página antes de inicializar el mapa
document.addEventListener('DOMContentLoaded', function () {
    initMap();
});
