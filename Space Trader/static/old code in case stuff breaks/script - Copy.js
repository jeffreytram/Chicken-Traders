let settings = {
    name: "",
    difficulty: "",
    pilotSP: 0,
    fighterSP: 0,
    merchantSP: 0,
    engineerSP: 0,
    credits: 0,
    remainingSP: 16,
    everythingFilled: false,
    saveName: function () {
        let nameTF = document.getElementById("name");
        this.name = nameTF.value;
    },
    saveDifficulty: function () {
        let selectedDiff = document.getElementsByClassName("active");
        if (selectedDiff.length > 0) {
            this.difficulty = selectedDiff[0].textContent;
        }
    },
    displayName: function () {
        let nameP = document.getElementById("displayName");
        nameP.innerHTML = this.name;
    },
    displaySP: function () {
        let pilotP = document.getElementById("pilotSP");
        let fighterP = document.getElementById("fighterSP");
        let merchantP = document.getElementById("merchantSP");
        let engineerP = document.getElementById("engineerSP");
        pilotP.innerHTML = this.pilotSP;
        fighterP.innerHTML = this.fighterSP;
        merchantP.innerHTML = this.merchantSP;
        engineerP.innerHTML = this.engineerSP;
    },
    displayDifficulty: function () {
        let diffP = document.getElementById("difficulty");
        diffP.innerHTML = this.difficulty;
    },
    setDifficulty: function (diff) {
        this.difficulty = diff;
    },
    setCredits: function () {
        if (this.difficulty === "easy") {
            this.credits = 1000;
        } else if (this.difficulty === "medium") {
            this.credits = 800;
        } else {
            this.credits = 500;
        }
    },
    displayCredits: function () {
        let creditsP = document.getElementById("credits");
        creditsP.innerHTML = this.credits;
    },
    increaseSP: function (skill) {
        if (skill.classList.contains("pilotSP")) {
            this.pilotSP++;
        } else if (skill.classList.contains("fighterSP")) {
            this.fighterSP++;
        } else if (skill.classList.contains("merchantSP")) {
            this.merchantSP++;
        } else {
            this.engineerSP++;
        }
        this.remainingSP--;
    },
    decreaseSP: function (skill) {
        if (skill.classList.contains("pilotSP")) {
            this.pilotSP--;
        } else if (skill.classList.contains("fighterSP")) {
            this.fighterSP--;
        } else if (skill.classList.contains("merchantSP")) {
            this.merchantSP--;
        } else {
            this.engineerSP--;
        }
        this.remainingSP++;
    },
    displayRemainingSP: function () {
        let remSP = document.getElementById("remSP");
        remSP.innerHTML = this.remainingSP;
    },
    confirmSP: function () {
        let confirmPilotSP = document.getElementById("displayPilotSP");
        let confirmFighterSP = document.getElementById("displayFighterSP");
        let confirmMerchantSP = document.getElementById("displayMerchantSP");
        let confirmEngineerSP = document.getElementById("displayEngineerSP");
        confirmPilotSP.innerHTML = this.pilotSP;
        confirmFighterSP.innerHTML = this.fighterSP;
        confirmMerchantSP.innerHTML = this.merchantSP;
        confirmEngineerSP.innerHTML = this.engineerSP;
    },
    checkEverythingFilled: function () {
        if (this.name != "" && this.difficulty != "" && this.remainingSP === 0) {
            this.everythingFilled = true;
        } else {
            this.everythingFilled = false;
        }
    },
    clearWarnings: function () {
        let warning = document.getElementById("warning");
        warning.innerHTML = "";
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
        //save difficulty
        settings.saveDifficulty();
        //set credits
        settings.setCredits();
    },
    displaySelectedSettings: function () {
        //display name
        settings.displayName();
        //display SP
        settings.confirmSP();
        //display difficulty
        settings.displayDifficulty();
        //display credits
        settings.displayCredits();
    },
    setDifficulty: function (diff) {
        settings.setDifficulty(diff);
    },
    highlightButton: function (button) {
        let active = document.getElementsByClassName("active");
        if (active.length > 0) {
            active[0].className = active[0].className.replace(" active", "");
        }
        button.className += " active";
    },
    increaseSP: function (skill) {
        settings.increaseSP(skill);
    },
    decreaseSP: function (skill) {
        settings.decreaseSP(skill);
    },
    updateSP: function () {
        settings.displaySP();
        settings.displayRemainingSP();
    },
    checkEverythingFilled: function () {
        settings.clearWarnings();
        settings.checkEverythingFilled();
        if (settings.name === "") {
            view.nameWarning();
        }
        if (settings.difficulty === "") {
            view.difficultyWarning();
        }
        if (settings.remainingSP > 0) {
            view.remainingSPWarning();
        }
    },
    travel: function(region) {
        console.log(region)
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

        let upArrows = document.getElementsByClassName("up");
        Array.from(upArrows).forEach(function (element) {
            element.addEventListener("click", function (event) {
                if (settings.remainingSP > 0) {
                    handlers.increaseSP(event.target);
                    handlers.updateSP();
                }
            });
        });
        let downArrows = document.getElementsByClassName("down");
        Array.from(downArrows).forEach(function (element) {
            element.addEventListener("click", function (event) {
                let temp = document.getElementById(event.target.classList[2]);
                if (temp.innerHTML > 0) {
                    handlers.decreaseSP(event.target);
                    handlers.updateSP();
                }
            });
        })
        let continueButton = document.getElementById("continueButton");
        continueButton.addEventListener("click", function () {
            handlers.setSettings();
            handlers.checkEverythingFilled();
            if (settings.everythingFilled) {
                handlers.displayAndHide("confirm", "settings");
                handlers.displaySelectedSettings();
            }
        });
        //CONFIRM SECTION
        let backButton = document.getElementById("backButton");
        backButton.addEventListener("click", function () {
            handlers.displayAndHide("settings", "confirm");
        });
        let confirmButton = document.getElementById("confirmButton");
        confirmButton.addEventListener("click", function () {
            //TODO: check if all values filled out by user
            //TODO: check if all skill points used?
            handlers.displayAndHide("startgame", "confirm");
        });
        
        let regionButtonDiv = document.getElementById("regionButtons")
        regionButtonDiv.addEventListener("click", function (event) {
            handlers.travel(event.target);
        });
        
    },
    nameWarning: function () {
        let warning = document.getElementById("warning");
        warning.innerHTML += "Enter a name. <br/>"
    },
    difficultyWarning: function () {
        let warning = document.getElementById("warning");
        warning.innerHTML += "Select a difficulty. <br/>"
    },
    remainingSPWarning: function () {
        let warning = document.getElementById("warning");
        warning.innerHTML += "You have " + settings.remainingSP + " remaining skill points.";
    }
}
view.setUpEventListeners();