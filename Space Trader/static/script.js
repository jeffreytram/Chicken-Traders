let player = {
    currentRegion: "Home",
    travel: function (region) {
        this.currentRegion = region.className;
    },
    displayCurrRegion: function (region) {
        let headerElement = document.getElementById("currRegion");
        headerElement.innerHTML = region.innerText;
    },
    displayCurrRegionMap: function (region) {
        let headerElement = document.getElementById("currRegion");
        headerElement.innerHTML = "Region: " + region[0] + " X:" + region[1] + "Y: " + region[2] + " Tech Level: " + region[3];
    },
    displayRegionList: function () {
        let regionList = document.getElementsByClassName("regionButtons");
        if (regionList[0].classList.contains("hidden")) {
            regionList[0].className = regionList[0].className.replace(" hidden", "");
        } else {
            regionList[0].className += " hidden";
        }
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
    highlightTravel: function (button) {
        let active = document.getElementsByClassName("active2");
        if (active.length > 0) {
            active[0].className = active[0].className.replace(" active2", "");
        } else {
            button.className += " active2";
        }
    },
    travel: function (region) {
        player.travel(region);
        player.displayCurrRegion(region);
    },
    travelMap: function(region) {
        player.displayCurrRegionMap(region);
    },
    displayRegionList: function () {
        player.displayRegionList();
    }
}
let view = {
    setUpEventListeners: function () {
        let travelButton = document.getElementById("travel");
        travelButton.addEventListener("click", function (event) {
            handlers.displayRegionList();
            handlers.highlightTravel(event.target);
        });
    }
}
view.setUpEventListeners();
