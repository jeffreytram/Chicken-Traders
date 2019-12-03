let player = {
}
let handlers = {
    //highlights only the selected button
    highlightButton: function (button) {
        let regionButtonsDiv = document.getElementsByClassName("regionButtons");
        let active = regionButtonsDiv[0].getElementsByClassName("active");
        if (active.length > 0) {
            active[0].className = active[0].className.replace(" active", "");
        }
        button.className += " active";
    }
}
let view = {
}
