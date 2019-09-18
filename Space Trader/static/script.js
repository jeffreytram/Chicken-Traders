let handlers = {
    displayText: function () {
        let hiddenElements = document.getElementsByClassName("hidden");
        let welcomeElements = document.getElementsByClassName("welcome");
        hiddenElements[0].className = hiddenElements[0].className.replace(" hidden", "");
        welcomeElements[0].className += " hidden";
        /*
        hiddenElements.forEach(function (element, position) {
            element.className = hiddenElements[position].className.replace(" hidden", "");
        });
        welcomeElements.forEach(function (element, position) {
            element[position].className += " hidden";
        });
        */
    }
}
let view = {
    setUpEventListeners: function () {
        let buttonDiv = document.getElementById("buttonDiv");
        buttonDiv.addEventListener("click", function (event) {
            debugger;
            if (event.target.className === "buttonTest") {
                handlers.displayText();
            }
        });
    }
}
view.setUpEventListeners();