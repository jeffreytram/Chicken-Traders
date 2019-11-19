from flask import Flask, render_template, url_for, redirect, request
from forms import SettingForm, ConfirmForm, SPForm
import utility
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
    "prev_region": None,
    "selectedItem": None,
    "fuel_error": None,
    "market_error": None,
    "npc": None,
    "negotiated": False,
    "choice_result": None,
    "second_test": True,
    "disabled": False,
    "end_game": None,
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
    return render_template(
        "skillpoints.html",
        diff=dictionary["pDiff"],
        form=sp_form,
        sp=dictionary["pSPLimit"],
    )


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
        dictionary["prev_region"] = dictionary["currRegion"]
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
                dictionary["prev_region"] = dictionary["currRegion"]
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
            force_npc = request.form["force"]
            if force_npc == "bandit":
                dictionary["npc"] = utility.gen_bandit()
            if force_npc == "trader":
                dictionary["npc"] = utility.gen_trader()
            if force_npc == "police":
                dictionary["npc"] = utility.gen_police(dictionary["game"].player)
    return render_template(
        "travel.html",
        fuel_error=dictionary["fuel_error"],
        game=dictionary["game"],
        currRegion=dictionary["currRegion"],
        universe=dictionary["game"].universe,
    )


@app.route("/market", methods=["GET", "POST"])
def market():
    if dictionary["game"].player.win:
        dictionary["end_game"] = "WIN"
        return redirect(url_for("end"))
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
        if "addFuel" in request.form:
            dictionary["game"].player.purchase_fuel(50)
        if "addHealth" in request.form:
            dictionary["game"].player.buy_repairs(10)
    return render_template(
        "market.html",
        market_error=dictionary["market_error"],
        game=dictionary["game"],
        currRegion=dictionary["currRegion"],
        selectedItem=dictionary["selectedItem"],
    )


@app.route("/end", methods=["GET", "POST"])
def end():
    return render_template(
        "end.html",
        end_game=dictionary["end_game"],
        game=dictionary["game"],
        currRegion=dictionary["currRegion"],
        universe=dictionary["game"].universe,
    )


@app.route("/encounter", methods=["GET", "POST"])
def encounter():
    if not dictionary["npc"]:
        if dictionary["game"].player.lose:
            dictionary["end_game"] = "LOSE"
            return redirect(url_for("end"))
        return redirect(url_for("travel"))
    gen_npc = dictionary["npc"]
    if request.method == "POST":
        if "return_travel" in request.form:
            dictionary["npc"] = None
            dictionary["choice_result"] = None
            dictionary["disabled"] = False
        elif not dictionary["disabled"]:
            dictionary["disabled"] = True
            # bandit choices
            if "pay_bandit" in request.form:
                state = utility.pay_bandit(dictionary["game"].player, dictionary["npc"])
                if state == 1:
                    dictionary["choice_result"] = (
                        "You paid the bandit. (-"
                        + str(dictionary["npc"]["demand"])
                        + " credits)"
                    )
                elif state == 2:
                    dictionary[
                        "choice_result"
                    ] = "You attempted to pay the bandit without enough money! The bandit steals all your cargo!"
                else:
                    dictionary[
                        "choice_result"
                    ] = "You attempted to pay the bandit without anything to offer! The bandit attacks you out of anger! (-15 health)"
            if "fight_bandit" in request.form:
                credits = dictionary["game"].player.credit
                if utility.fight_bandit(dictionary["game"].player, dictionary["npc"]):
                    dictionary["choice_result"] = (
                        "You successfully defeated the bandit. You took the Bandit's credits. (+"
                        + str(int((5 / 4) * dictionary["npc"]["demand"]))
                        + " credits)"
                    )
                else:
                    dictionary["choice_result"] = (
                        "You lost to the Bandit! The Bandit took all your credits and injured you. (-"
                        + str(credits)
                        + " credits, -20 health)"
                    )
            if "flee_bandit" in request.form:
                credits = dictionary["game"].player.credit
                if utility.flee_bandit(dictionary["game"].player):
                    dictionary["currRegion"] = dictionary["prev_region"]
                    dictionary[
                        "choice_result"
                    ] = "You successfully fled to the previous region!"
                else:
                    dictionary["choice_result"] = (
                        "You failed to flee the Bandit. The Bandit took all your credits and injured you. (-"
                        + str(credits)
                        + " credits, -20 health)"
                    )
            # trader choices
            if "buy_trader" in request.form:
                if (
                    dictionary["game"].player.trade_buy(dictionary["npc"]["item"], 1)
                    == "Success"
                ):
                    dictionary["second_test"] = True
                    dictionary["negotiated"] = False
                    dictionary["choice_result"] = (
                        "You bought a " + dictionary["npc"]["item"].name + "."
                    )
                else:
                    dictionary["disabled"] = False
                    dictionary["second_test"] = False
                    dictionary["choice_result"] = "You don't have enough credits!"
            if "ignore_trader" in request.form:
                dictionary["second_test"] = True
                dictionary["negotiated"] = False
                dictionary["choice_result"] = "You chose to ignore the Trader."
            if "rob_trader" in request.form:
                dictionary["second_test"] = True
                dictionary["negotiated"] = False
                if utility.rob_trader(dictionary["game"].player, dictionary["npc"]):
                    dictionary["choice_result"] = (
                        "You robbed the Trader! (+ 1 )"
                        + dictionary["npc"]["item"].name
                        + "!"
                    )
                else:
                    dictionary[
                        "choice_result"
                    ] = "The Trader caught you in the act and slapped you. (-10 health)"
            if "negotiate_trader" in request.form:
                dictionary["disabled"] = False
                dictionary["second_test"] = False
                if not dictionary["negotiated"]:
                    dictionary["negotiated"] = True
                    if utility.negotiate_trader(
                        dictionary["game"].player, dictionary["npc"]
                    ):
                        dictionary[
                            "choice_result"
                        ] = "You negotiated a deal with the Trader."
                    else:
                        dictionary[
                            "choice_result"
                        ] = "The Trader was insulted by your negotiation attempt!"
                else:
                    dictionary["choice_result"] = "You can only negotiate once! D:<"
            # police choices
            if "forfeit_police" in request.form:
                utility.forfeit_police(dictionary["game"].player, dictionary["npc"])
                dictionary["choice_result"] = (
                    "You forfeited the item. (-all "
                    + dictionary["npc"]["item"].name
                    + ")"
                )
            if "flee_police" in request.form:
                if utility.flee_police(dictionary["game"].player, dictionary["npc"]):
                    dictionary["currRegion"] = dictionary["prev_region"]
                    dictionary[
                        "choice_result"
                    ] = "You successfully fled to the previous region!"
                else:
                    dictionary["choice_result"] = (
                        "You failed to flee from the Police. The Police took the item, charged you a fee, and slapped you. (-all "
                        + dictionary["npc"]["item"].name
                        + ", -70 credits, -15 health)"
                    )
            if "fight_police" in request.form:
                if utility.fight_police(dictionary["game"].player, dictionary["npc"]):
                    dictionary["choice_result"] = "You fought off the Police!"
                else:
                    dictionary["choice_result"] = (
                        "You failed to fight of the Police! The Police took the item from you! (-all "
                        + dictionary["npc"]["item"].name
                        + ")"
                    )
    return render_template(
        "encounter.html",
        second_test=dictionary["second_test"],
        text=dictionary["choice_result"],
        npc=gen_npc,
        game=dictionary["game"],
        currRegion=dictionary["currRegion"],
        universe=dictionary["game"].universe,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)
