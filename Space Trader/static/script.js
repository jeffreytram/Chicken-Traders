let player = {
    currentRegion: "Home",
    travel: function (region) {
        this.currentRegion = region.className;
    },
    displayCurrRegion: function (region) {
        let headerElement = document.getElementById("currRegion");
        headerElement.innerHTML = region.innerText;
    },
    displayRegionList: function() {
        let hiddenRegionList = document.getElementsByClassName(" hidden");
        let regionList = document.getElementsByClassName("regionButtons");
        if (hiddenRegionList.length > 0) {
            hiddenRegionList[0].className = hiddenRegionList[0].className.replace(" hidden", "");
        } else{
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
    travel: function(region) {
        console.log(region);
        player.travel(region);
        player.displayCurrRegion(region);
    },
    displayRegionList: function() {
        player.displayRegionList();
    }
}
let view = {
    setUpEventListeners: function () {
        let regionButtonDiv = document.getElementsByClassName("regionButtons")
        regionButtonDiv[0].addEventListener("click", function (event) {
            handlers.travel(event.target);
        });
        let travelButton = document.getElementById("travel");
        travelButton.addEventListener("click", function (event) {
            console.log("click");
            handlers.displayRegionList();
        });
    }
}
view.setUpEventListeners();