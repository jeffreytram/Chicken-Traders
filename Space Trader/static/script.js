let player = {
    currentRegion: "Home",
    displayCurrRegionMap: function (region) {
        let headerElement = document.getElementById("currRegion");
        headerElement.innerHTML = "Region: " + region[0] + " (" + region[1] + ", " + region[2] + ") Tech Level: " + region[3];
        this.currentRegion = region[0];
    },
    display: function (screen) {
        let activeMenu = document.getElementsByClassName("menuActive");
        if (activeMenu.length > 0) {
            activeMenu[0].className = activeMenu[0].className.replace(" menuActive", " hidden");
        }
        if (screen.classList.contains("hidden")) {
            screen.className = screen.className.replace(" hidden", " menuActive");
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
    highlightMenuButton: function (button) {
        let active = document.getElementsByClassName("active2");
        if (active.length > 0) {
            active[0].className = active[0].className.replace(" active2", "");
        }
        button.className += " active2";
    },
    travelMap: function (region) {
        player.displayCurrRegionMap(region);
    },
    display: function (screen) {
        player.display(screen);
    }
}
let view = {
    setUpEventListeners: function () {
        let menu = document.getElementById("menu");
        menu.addEventListener("click", function (event) {
            if (event.target.id == "travel") {
                let buttonDiv = document.getElementsByClassName("travelMenu");
                handlers.display(buttonDiv[0]);
                handlers.highlightMenuButton(event.target);
            }
            if (event.target.id == "ship") {
                let shipDiv = document.getElementsByClassName("shipMenu");
                handlers.display(shipDiv[0]);
                handlers.highlightMenuButton(event.target);
            }
            if (event.target.id == "market") {
                let marketDiv = document.getElementsByClassName("marketMenu");
                handlers.display(marketDiv[0]);
                handlers.highlightMenuButton(event.target);
            }
        });
    }
}
view.setUpEventListeners();
