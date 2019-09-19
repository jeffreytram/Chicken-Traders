let settings = {
    name: "",
    difficulty: "",
    pilotSP: 0,
    fighterSP: 0,
    merchantSP: 0,
    engineerSP: 0,
    saveName: function () {
        let nameTF = document.getElementById("name");
        this.name = nameTF.value;
    },
    saveSP: function () {
        let pilotTF = document.getElementById("pilotSP");
        let fighterTF = document.getElementById("fighterSP");
        let merchantTF = document.getElementById("merchantSP");
        let engineerTF = document.getElementById("engineerSP");
        this.pilotSP = pilotTF.value;
        this.fighterSP = fighterTF.value;
        this.merchantSP = merchantTF.value;
        this.engineerSP = engineerTF.value;
    },
    setName: function () {
        let nameP = document.getElementById("displayName");
        nameP.innerHTML = this.name;
    },
    setSP: function () {
        let pilotP = document.getElementById("displayPilotSP");
        let fighterP = document.getElementById("displayFighterSP");
        let merchantP = document.getElementById("displayMerchantSP");
        let engineerP = document.getElementById("displayEngineerSP");
        pilotP.innerHTML = this.pilotSP;
        fighterP.innerHTML = this.fighterSP;
        merchantP.innerHTML = this.merchantSP;
        engineerP.innerHTML = this.engineerSP;
    }
}
let handlers = {
    displayAndHide: function (eleToShow, eleToHide) {
        let currHidden = document.getElementsByClassName(eleToShow);
        let currShow = document.getElementsByClassName(eleToHide);
        //TODO: change so applies if multiple elements in array
        currHidden[0].className = currHidden[0].className.replace(" hidden", "");
        currShow[0].className += " hidden";
    },
    saveSettings: function () {
        //save name
        settings.saveName();
        //TODO: save difficulty chose
        //save skill point allocation
        settings.saveSP();
    },
    displaySelectedSettings: function () {
        //display name
        settings.setName();
        //display SP
        settings.setSP();
    }
}
let view = {
    setUpEventListeners: function () {
        let buttonDiv = document.getElementById("buttonDiv");
        buttonDiv.addEventListener("click", function (event) {
            if (event.target.className === "start") {
                handlers.displayAndHide("settings", "welcome");
            }
        });
        let continueButton = document.getElementById("continueButton");
        continueButton.addEventListener("click", function () {
            handlers.displayAndHide("confirm", "settings");
            handlers.saveSettings();
            handlers.displaySelectedSettings();
        });
        let backButton = document.getElementById("backButton");
        backButton.addEventListener("click", function () {
            handlers.displayAndHide("settings", "confirm");
        });
        let confirmButton = document.getElementById("confirmButton");
        confirmButton.addEventListener("click", function () {
            //TODO: check for SP allocation overflow
            handlers.displayAndHide("startgame", "confirm");
        });
    }
}
view.setUpEventListeners();