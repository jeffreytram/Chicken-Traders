from flask import Flask, render_template, url_for, redirect, request, flash, session
from forms import SettingForm, ConfirmForm, SPForm
from config import Config
from Universe import Universe, Region
from Player import Player
import random

app = Flask(__name__)
app.config.from_object(Config)

dictionary = {
    "pName": "",
    "pDiff": "",
    "pCredits": 0,
    "pSPLimit": 0,
    "sp1": 0,
    "sp2": 0,
    "sp3": 0,
    "sp4": 0,
    "currRegion": "",
}
posts = [
    {"first_name": "Jeffrey", "last_name": "Tram"},
    {"first_name": "Bradford", "last_name": "Peterson"},
    {"first_name": "Robert", "last_name": "Giuffreda"},
]


@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/settings", methods=["GET", "POST"])
def settings():
    settingform = SettingForm()
    if settingform.validate_on_submit():
        dictionary["pDiff"] = settingform.diff.data
        if settingform.diff.data == "easy":
            dictionary["pCredits"] = 1000
            dictionary["pSPLimit"] = 16
        if settingform.diff.data == "med":
            dictionary["pCredits"] = 800
            dictionary["pSPLimit"] = 14
        if settingform.diff.data == "hard":
            dictionary["pCredits"] = 500
            dictionary["pSPLimit"] = 12
        return redirect(url_for("skillpoints"))
    return render_template("settings.html", form=settingform)


@app.route("/skillpoints", methods=["GET", "POST"])
def skillpoints():
    spForm = SPForm()

    def validTotal(spArray):
        total = 0
        for spElement in spArray:
            total = total + spElement
        if total > int(dictionary["pSPLimit"]):
            flash(
                "You can only allocate "
                + str(dictionary["pSPLimit"])
                + " skill points."
            )
            return False
        return True

    # TODO: remove validTotal once we get form variable pass in working
    if spForm.validate_on_submit() and validTotal(
        [spForm.sp1.data, spForm.sp2.data, spForm.sp3.data, spForm.sp4.data]
    ):
        dictionary["sp1"] = spForm.sp1.data
        dictionary["sp2"] = spForm.sp2.data
        dictionary["sp3"] = spForm.sp3.data
        dictionary["sp4"] = spForm.sp4.data
        print("test???")
        return redirect(url_for("confirm"))
    return render_template("skillpoints.html", form=spForm, sp=dictionary["pSPLimit"])


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="About", posts=posts)


testUniverse = Universe()


@app.route("/confirm", methods=["GET"])
def confirm():
    #confirmform = ConfirmForm()
    #if confirmform.is_submitted:
    #    randRegion = random.randint(0, 9)
    #    dictionary["currRegion"] = randRegion
    #    player = Player(
    #       dictionary["pName"],
    #       [
    #       dictionary["sp1"],
    #        dictionary["sp2"],
    #        dictionary["sp3"],
    #       dictionary["sp4"],
    #        ],
    #        dictionary["pCredits"],
    #        testUniverse.regionList[randRegion],
    #    )
    #    return redirect(url_for("start"))
    return render_template(
        "confirm.html",
        title="Confirm Settings",
        #form=confirmform,
        name=dictionary["pName"],
        sp1=dictionary["sp1"],
        sp2=dictionary["sp2"],
        sp3=dictionary["sp3"],
        sp4=dictionary["sp4"],
        diff=dictionary["pDiff"],
        credits=dictionary["pCredits"],
    )


@app.route("/start", methods=["GET", "POST"])
def start():
    randRegion = random.randint(0, 9)
    dictionary["currRegion"] = randRegion
    return render_template(
        "start.html", universe=testUniverse, randRegionIndex=dictionary["currRegion"]
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)
