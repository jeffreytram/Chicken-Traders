import utility
from flask import Flask, render_template, url_for, redirect, request
from forms import SettingForm, ConfirmForm, SPForm
from game import Game

app = Flask(__name__)
app.config["SECRET_KEY"] = "ayy"

dictionary = {
    "game": None,
    "player": None,
    "pName": None,
    "pDiff": None,
    "pCredits": 0,
    "pSPLimit": 0,
    "sp1": 0,
    "sp2": 0,
    "sp3": 0,
    "sp4": 0,
    "currRegion": None,
    "selectedItem": None,
    "fuel_error": None,
    "market_error": None,
    "npc": None,
}


@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/settings", methods=["GET", "POST"])
def settings():
    settingform = SettingForm()
    if settingform.validate_on_submit():
        dictionary["pDiff"] = settingform.diff.data
        dictionary["pName"] = settingform.name.data
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
    sp_form = SPForm(dictionary["pSPLimit"])
    if sp_form.validate_on_submit():
        dictionary["sp1"] = sp_form.sp1.data
        dictionary["sp2"] = sp_form.sp2.data
        dictionary["sp3"] = sp_form.sp3.data
        dictionary["sp4"] = sp_form.sp4.data
        return redirect(url_for("confirm"))
    return render_template("skillpoints.html", form=sp_form, sp=dictionary["pSPLimit"])


@app.route("/confirm", methods=["GET", "POST"])
def confirm():
    confirmform = ConfirmForm()
    if confirmform.validate_on_submit():
        space_trader = Game(dictionary["pDiff"])

        dictionary["game"] = space_trader

        space_trader.start_game(
            dictionary["pName"],
            [
                dictionary["sp1"],
                dictionary["sp2"],
                dictionary["sp3"],
                dictionary["sp4"],
            ],
            dictionary["pCredits"],
        )
        dictionary["currRegion"] = space_trader.player.curr_region
        return redirect(url_for("travel"))
    return render_template(
        "confirm.html",
        title="Confirm Settings",
        form=confirmform,
        name=dictionary["pName"],
        sp1=dictionary["sp1"],
        sp2=dictionary["sp2"],
        sp3=dictionary["sp3"],
        sp4=dictionary["sp4"],
        diff=dictionary["pDiff"],
        credits=dictionary["pCredits"],
    )


@app.route("/ship", methods=["GET", "POST"])
def ship():
    return render_template(
        "ship.html", game=dictionary["game"], currRegion=dictionary["currRegion"]
    )


@app.route("/travel", methods=["GET", "POST"])
def travel():
    if dictionary["npc"]:
        return redirect(url_for("encounter"))
    if request.method == "POST":
        if "currIndex" in request.form:
            index = request.form["currIndex"]
            travel_region = dictionary["game"].universe.region_list[int(index) - 1]
            if dictionary["game"].travel_sequence(travel_region):
                dictionary["fuel_error"] = None
                dictionary["selectedItem"] = None
                dictionary["currRegion"] = travel_region
                dictionary["npc"] = utility.encounter_check(
                    dictionary["game"].encounter_factor, dictionary["game"].player
                )
                return (
                    "Region: "
                    + dictionary["currRegion"].name
                    + " ("
                    + str(dictionary["currRegion"].coordinates.x_position)
                    + ", "
                    + str(dictionary["currRegion"].coordinates.y_position)
                    + ") Tech Level: "
                    + dictionary["currRegion"].tech_level.name
                )
            else:
                dictionary["fuel_error"] = True
                return "-1"
        if "addFuel" in request.form:
            dictionary["game"].player.ship.fuel_level += 100
        if "addCredits" in request.form:
            dictionary["game"].player.credit += 100
        if "addHealth" in request.form:
            dictionary["game"].player.ship.health_level += 100
        if "force" in request.form:
            dictionary["npc"] = request.form["force"]
    return render_template(
        "travel.html",
        fuel_error=dictionary["fuel_error"],
        game=dictionary["game"],
        currRegion=dictionary["currRegion"],
        universe=dictionary["game"].universe,
    )


@app.route("/market", methods=["GET", "POST"])
def market():
    if request.method == "POST":
        if "selectedIndex" in request.form:
            selected_index = int(request.form["selectedIndex"]) - 1
            dictionary["selectedItem"] = dictionary["currRegion"].market[selected_index]
            return dictionary["selectedItem"].description

        if "statementIndex" in request.form:
            return (
                "Purchase <strong>"
                + dictionary["selectedItem"].name
                + "</strong> for <strong>"
                + str(dictionary["selectedItem"].b_price)
                + "</strong>?"
            )
        if "buyIndex" in request.form:
            status = dictionary["game"].player.trade_buy(dictionary["selectedItem"], 1)
            if status != "Success":
                dictionary["market_error"] = status
            else:
                dictionary["market_error"] = None
        if "sellIndex" in request.form:
            inv_index = int(request.form["sellIndex"]) - 1
            dictionary["game"].player.trade_sell(inv_index, 1)
            return "Credits: " + str(dictionary["game"].player.credit)

    return render_template(
        "market.html",
        market_error=dictionary["market_error"],
        game=dictionary["game"],
        currRegion=dictionary["currRegion"],
        selectedItem=dictionary["selectedItem"],
    )


@app.route("/test", methods=["GET", "POST"])
def test():
    return render_template(
        "test.html",
        game=dictionary["game"],
        currRegion=dictionary["currRegion"],
        universe=dictionary["game"].universe,
    )


@app.route("/encounter", methods=["GET", "POST"])
def encounter():
    if dictionary["npc"] == "bandit":
        gen_npc = utility.gen_bandit()
    elif dictionary["npc"] == "police":
        gen_npc = utility.gen_police(dictionary["game"].player)
    elif dictionary["npc"] == "trader":
        gen_npc = utility.gen_trader()
    dictionary["npc"] = None
    return render_template(
        "encounter.html",
        npc=gen_npc,
        game=dictionary["game"],
        currRegion=dictionary["currRegion"],
        universe=dictionary["game"].universe,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)
