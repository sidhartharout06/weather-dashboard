const locationBtn = document.getElementById("location-btn");

locationBtn.addEventListener("click", function () {

    if (navigator.geolocation) {

        navigator.geolocation.getCurrentPosition(function(position) {

            const lat = position.coords.latitude;
            const lon = position.coords.longitude;

            window.location.href = `/location/?lat=${lat}&lon=${lon}`;

        }, function() {
            alert("Unable to retrieve your location.");
        });

    } else {
        alert("Geolocation is not supported by your browser.");
    }

});