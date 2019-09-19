let settings = {
    name: "",
    difficulty: "",
    pilotSP: 0,
    fighterSP: 0,
    merchantSP: 0,
    engineerSP: 0,
    credits: 0,
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
    saveDifficulty: function() {
        let selectedDiff = document.getElementsByClassName("active");
        this.difficulty = selectedDiff[0].textContent;
    },
    displayName: function () {
        let nameP = document.getElementById("displayName");
        nameP.innerHTML = this.name;
    },
    displaySP: function () {
        let pilotP = document.getElementById("displayPilotSP");
        let fighterP = document.getElementById("displayFighterSP");
        let merchantP = document.getElementById("displayMerchantSP");
        let engineerP = document.getElementById("displayEngineerSP");
        pilotP.innerHTML = this.pilotSP;
        fighterP.innerHTML = this.fighterSP;
        merchantP.innerHTML = this.merchantSP;
        engineerP.innerHTML = this.engineerSP;
    },
    displayDifficulty: function() {
        let diffP = document.getElementById("difficulty");
        diffP.innerHTML = this.difficulty;
    },
    setDifficulty: function(diff){
        this.difficulty = diff;
    },
    setCredits: function(){
        if(this.difficulty === "easy"){
            this.credits = 1000;
        } else if (this.difficulty === "medium"){
            this.credits = 800;
        } else {
            this.credits = 500;
        }
    },
    displayCredits: function(){
        let creditsP = document.getElementById("credits");
        creditsP.innerHTML = this.credits;
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
    setSettings: function () {
        //save name
        settings.saveName();
        //save skill point allocation
        settings.saveSP();
        //save difficulty
        settings.saveDifficulty();
        //set credits
        settings.setCredits();
    },
    displaySelectedSettings: function () {
        //display name
        settings.displayName();
        //display SP
        settings.displaySP();
        //display difficulty
        settings.displayDifficulty();
        //display credits
        settings.displayCredits();
    },
    setDifficulty: function(diff){
        settings.setDifficulty(diff);
    },
    highlightButton: function(button){
        let active = document.getElementsByClassName("active");
        if (active.length > 0) {
            active[0].className = active[0].className.replace(" active", "");
        }
        button.className += " active";
    }
}
let view = {
    setUpEventListeners: function () {
        //WELCOME SECTION
        let buttonDiv = document.getElementById("buttonDiv");
        buttonDiv.addEventListener("click", function (event) {
            if (event.target.className === "start") {
                handlers.displayAndHide("settings", "welcome");
            }
        });
        //SETTINGS SECTION
        let continueButton = document.getElementById("continueButton");
        continueButton.addEventListener("click", function () {
            handlers.displayAndHide("confirm", "settings");
            handlers.setSettings();
            handlers.displaySelectedSettings();
        });
        let diffButtonDiv = document.getElementById("difficultyDiv");
        diffButtonDiv.addEventListener("click", function (event) {
            if (event.target.id === "easy") {
                handlers.highlightButton(event.target);
            }
            if (event.target.id === "medium") {
                handlers.highlightButton(event.target);
            }
            if (event.target.id === "hard") {
                handlers.highlightButton(event.target);
            }
        });
        //CONFIRM SECTION
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