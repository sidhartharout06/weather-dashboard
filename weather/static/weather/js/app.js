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


const searchForm = document.querySelector("form");
const cityInput = document.querySelector('input[name="city"]');

searchForm.addEventListener("submit", function () {
    localStorage.setItem("lastCity", cityInput.value);
});

window.addEventListener("DOMContentLoaded", function () {

    const lastCity = localStorage.getItem("lastCity");

    const params = new URLSearchParams(window.location.search);
    const currentCity = params.get("city");

    const isHomePage = window.location.pathname === "/";

    if (isHomePage && !currentCity && lastCity) {
        window.location.href = `/?city=${encodeURIComponent(lastCity)}`;
        return;
    }

    if (cityInput && currentCity) {
        cityInput.value = currentCity;
    }

});