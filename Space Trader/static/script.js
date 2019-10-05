let player = {
    currentRegion: "Home",
    travel: function (region) {
        this.currentRegion = region.className;
    },
    displayCurrRegion: function (region) {
        let headerElement = document.getElementById("currRegion");
        headerElement.innerHTML = region.innerText;
    }
}
let handlers = {
    highlightButton: function (button) {
        let active = document.getElementsByClassName("active");
        if (active.length > 0) {
            active[0].className = active[0].className.replace(" active", "");
        }
        button.className += " active";
    },
    travel: function(region) {
        console.log(region);
        player.travel(region);
        player.displayCurrRegion(region);
    }
}
let view = {
    setUpEventListeners: function () {
        let regionButtonDiv = document.getElementById("regionButtons")
        regionButtonDiv.addEventListener("click", function (event) {
            handlers.travel(event.target);
        });
        
    }
}
view.setUpEventListeners();