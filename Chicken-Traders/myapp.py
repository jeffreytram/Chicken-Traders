from flask import Flask, render_template, url_for, redirect, request
from forms import SettingForm, ConfirmForm, SPForm
import utility
import json
from game import Game
from item import Item

app = Flask(__name__)
app.config["SECRET_KEY"] = "ayy"

# initialize setup and state dict
setup = {
    "pName": None,
    "pDiff": None,
    "pCredits": 0,
    "pSPLimit": 0,
    "sp1": 0,
    "sp2": 0,
    "sp3": 0,
    "sp4": 0,
}
state = {
    "game": None,
    "currRegion": None,
    "prev_region": None,
    "selectedItem": None,
    "fuel_error": None,
    "market_error": None,
    "npc": {},
    "negotiated": False,
    "choice_result": None,
    "second_test": True,
    "disabled": False,
    "end_game": None,
    "news": [],
    "time": 9,
    "day": 0
}

# home page
@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")


# settings page
@app.route("/settings", methods=["GET", "POST"])
def settings():
    settingform = SettingForm()
    if settingform.validate_on_submit():
        setup["pDiff"] = settingform.diff.data
        setup["pName"] = settingform.name.data
        if settingform.diff.data == "easy":
            setup["pCredits"] = 1000
            setup["pSPLimit"] = 16
        if settingform.diff.data == "med":
            setup["pCredits"] = 800
            setup["pSPLimit"] = 14
        if settingform.diff.data == "hard":
            setup["pCredits"] = 500
            setup["pSPLimit"] = 12
        return redirect(url_for("skillpoints"))
    return render_template("settings.html", form=settingform)


# skillpoints page
@app.route("/skillpoints", methods=["GET", "POST"])
def skillpoints():
    sp_form = SPForm(setup["pSPLimit"])
    if sp_form.validate_on_submit():
        setup["sp1"] = sp_form.sp1.data
        setup["sp2"] = sp_form.sp2.data
        setup["sp3"] = sp_form.sp3.data
        setup["sp4"] = sp_form.sp4.data
        return redirect(url_for("confirm"))
    return render_template(
        "skillpoints.html", diff=setup["pDiff"], form=sp_form, sp=setup["pSPLimit"]
    )


# confirm settings page
@app.route("/confirm", methods=["GET", "POST"])
def confirm():
    confirmform = ConfirmForm()
    if confirmform.validate_on_submit():
        chicken_traders = Game(setup["pDiff"])

        state["game"] = chicken_traders

        chicken_traders.start_game(
            setup["pName"],
            [setup["sp1"], setup["sp2"], setup["sp3"], setup["sp4"]],
            setup["pCredits"],
        )
        state["currRegion"] = chicken_traders.player.curr_region
        state["prev_region"] = state["currRegion"]
        return redirect(url_for("about"))
    return render_template(
        "confirm.html",
        title="Confirm Settings",
        form=confirmform,
        name=setup["pName"],
        sp1=setup["sp1"],
        sp2=setup["sp2"],
        sp3=setup["sp3"],
        sp4=setup["sp4"],
        diff=setup["pDiff"],
        credits=setup["pCredits"],
    )

# about page
@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", game=state["game"])

# collection page
@app.route("/collection", methods=["GET", "POST"])
def collection():
    if request.method == "POST":
        if "addCredits" in request.form:
            category = request.form["addCredits"]
            index = state["game"].player.collection.category.index(category)
            state["game"].player.collection.complete[index] = True
            state["game"].player.credit += 100
            return str(state["game"].player.credit)
    return render_template(
        "collection.html", game=state["game"], all_items=Item.__subclasses__()
    )

# ship page
@app.route("/ship", methods=["GET", "POST"])
def ship():
    return render_template(
        "ship.html", game=state["game"]
    )


# travel page
@app.route("/travel", methods=["GET", "POST"])
def travel():
    if state["npc"]:
        if isinstance(state["npc"], str):
            state["news"].insert(0, state["npc"])
            if len(state["news"]) > 5:
                state["news"].pop(-1)
            state["time"] += 3
            if state["time"] == 24:
                state["day"] += 1
                state["time"] = 0
                utility.restock(state["game"].universe.region_list)
            state["npc"] = None
        else:
            return redirect(url_for("encounter"))
    if request.method == "POST":
        if "currIndex" in request.form:
            index = request.form["currIndex"]
            travel_region = state["game"].universe.region_list[int(index) - 1]
            travel_status = utility.travel_check(state["game"], travel_region)
            if travel_status == 1:
                state["fuel_error"] = None
                state["selectedItem"] = None
                state["market_error"] = None
                state["prev_region"] = state["currRegion"]
                state["currRegion"] = travel_region
                state["npc"] = utility.encounter_check(
                    state["game"].encounter_factor,
                    state["game"].player,
                    state["game"].universe.region_list,
                    state["time"]
                )
                utility.travel(state["game"].player, travel_region)
            else:
                state["fuel_error"] = travel_status
        if "addFuel" in request.form:
            state["game"].player.ship.fuel_level += 100
            return str(state["game"].player.ship.fuel_level)
        if "addCredits" in request.form:
            state["game"].player.credit += 100
            return str(state["game"].player.credit)
        if "addHealth" in request.form:
            state["game"].player.ship.health_level += 100
            return str(state["game"].player.ship.health_level)
        if "force" in request.form:
            force_npc = request.form["force"]
            if force_npc == "bandit":
                state["npc"] = utility.gen_bandit()
            if force_npc == "trader":
                state["npc"] = utility.gen_trader()
            if force_npc == "police":
                state["npc"] = utility.gen_police(state["game"].player)
    return render_template(
        "travel.html",
        day=state["day"],
        time=state["time"],
        news=state["news"],
        fuel_error=state["fuel_error"],
        game=state["game"],
        currRegion=state["currRegion"],
        universe=state["game"].universe,
    )


# market page
@app.route("/market", methods=["GET", "POST"])
def market():
    if state["game"].player.win:
        state["end_game"] = "WIN"
        return redirect(url_for("end"))
    if request.method == "POST":
        if "selectedIndex" in request.form:
            selected_index = int(request.form["selectedIndex"]) - 1
            state["selectedItem"] = state["currRegion"].market[selected_index]
            return json.dumps(state["selectedItem"].__dict__)

        if "statementIndex" in request.form:
            return (
                "Purchase <strong>"
                + state["selectedItem"].name
                + "</strong> for <strong>"
                + str(state["selectedItem"].b_price)
                + "</strong>?"
            )
        if "buyIndex" in request.form:
            status = state["game"].player.trade_buy(state["selectedItem"], 1)
            if status != "Success":
                state["market_error"] = status
            else:
                state["market_error"] = None
        if "sellIndex" in request.form:
            inv_index = int(request.form["sellIndex"]) - 1
            state["game"].player.trade_sell(inv_index, 1)
        if "updateCredits" in request.form:
            return str(state["game"].player.credit)
        if "addFuel" in request.form:
            state["game"].player.purchase_fuel(50)
            return str(state["game"].player.ship.fuel_level)
        if "addHealth" in request.form:
            state["game"].player.buy_repairs(10)
            return str(state["game"].player.ship.health_level)
    return render_template(
        "market.html",
        market_error=state["market_error"],
        game=state["game"],
        currRegion=state["currRegion"],
        selectedItem=state["selectedItem"],
    )


# end page
@app.route("/end", methods=["GET", "POST"])
def end():
    return render_template(
        "end.html",
        end_game=state["end_game"],
        game=state["game"],
        currRegion=state["currRegion"],
        universe=state["game"].universe,
    )


# encounter page
@app.route("/encounter", methods=["GET", "POST"])
def encounter():
    if not state["npc"]:
        if state["game"].player.lose:
            state["end_game"] = "LOSE"
            return redirect(url_for("end"))
        return redirect(url_for("travel"))
    gen_npc = state["npc"]
    if request.method == "POST":
        if "return_travel" in request.form:
            state["npc"] = None
            state["choice_result"] = None
            state["disabled"] = False
        elif not state["disabled"]:
            state["disabled"] = True
            # bandit choices
            if "pay_bandit" in request.form:
                result = utility.pay_bandit(state["game"].player, state["npc"])
                if result == 1:
                    state["choice_result"] = (
                        "You paid the bandit. (-"
                        + str(state["npc"]["demand"])
                        + " credits)"
                    )
                elif result == 2:
                    state["choice_result"] = (
                        "You attempted to pay the bandit without enough money!"
                        + "The bandit steals all your cargo!"
                    )
                else:
                    state["choice_result"] = (
                        "You attempted to pay the bandit without anything to offer!"
                        + "The bandit attacks you out of anger! (-15 health)"
                    )
            if "fight_bandit" in request.form:
                curr_credits = state["game"].player.credit
                if utility.fight_bandit(state["game"].player, state["npc"]):
                    state["choice_result"] = (
                        "You successfully defeated the bandit. You took the Bandit's credits. \n(+"
                        + str(int((5 / 4) * state["npc"]["demand"]))
                        + " credits)"
                    )
                else:
                    state["choice_result"] = (
                        "You lost to the Bandit! The Bandit "
                        + "took all your credits and injured you. (-"
                        + str(curr_credits)
                        + " credits, -20 health)"
                    )
            if "flee_bandit" in request.form:
                curr_credits = state["game"].player.credit
                if utility.flee_bandit(state["game"].player):
                    state["currRegion"] = state["prev_region"]
                    state["game"].player.curr_region = state["prev_region"]
                    state[
                        "choice_result"
                    ] = "You successfully fled to the previous region!"
                else:
                    state["choice_result"] = (
                        "You failed to flee the Bandit. "
                        + "The Bandit took all your credits and injured you. (-"
                        + str(curr_credits)
                        + " credits, -20 health)"
                    )
            # trader choices
            if "buy_trader" in request.form:
                if state["game"].player.trade_buy(state["npc"]["item"], 1) == "Success":
                    state["second_test"] = True
                    state["negotiated"] = False
                    state["choice_result"] = (
                        "You bought a " + state["npc"]["item"].name + "."
                    )
                else:
                    state["disabled"] = False
                    state["second_test"] = False
                    state["choice_result"] = "You don't have enough credits!"
            if "ignore_trader" in request.form:
                state["second_test"] = True
                state["negotiated"] = False
                state["choice_result"] = "You chose to ignore the Trader."
            if "rob_trader" in request.form:
                state["second_test"] = True
                state["negotiated"] = False
                if utility.rob_trader(state["game"].player, state["npc"]):
                    state["choice_result"] = (
                        "You robbed the Trader! (+1 " + state["npc"]["item"].name + ")"
                    )
                else:
                    state[
                        "choice_result"
                    ] = "The Trader caught you in the act and slapped you. (-10 health)"
            if "negotiate_trader" in request.form:
                state["disabled"] = False
                state["second_test"] = False
                if not state["negotiated"]:
                    state["negotiated"] = True
                    if utility.negotiate_trader(state["game"].player, state["npc"]):
                        state[
                            "choice_result"
                        ] = "You negotiated a deal with the Trader."
                    else:
                        state[
                            "choice_result"
                        ] = "The Trader was insulted by your negotiation attempt!"
                else:
                    state["choice_result"] = "You can only negotiate once! D:<"
            # police choices
            if "forfeit_police" in request.form:
                utility.forfeit_police(state["game"].player, state["npc"])
                state["choice_result"] = (
                    "You forfeited the item. (-all " + state["npc"]["item"].name + ")"
                )
            if "flee_police" in request.form:
                if utility.flee_police(state["game"].player, state["npc"]):
                    state["currRegion"] = state["prev_region"]
                    state[
                        "choice_result"
                    ] = "You successfully fled to the previous region!"
                else:
                    state["choice_result"] = (
                        "You failed to flee from the Police. The Police took"
                        + " the item, charged you a fee, and slapped you. (-all "
                        + state["npc"]["item"].name
                        + ", -70 credits, -15 health)"
                    )
            if "fight_police" in request.form:
                if utility.fight_police(state["game"].player, state["npc"]):
                    state["choice_result"] = "You fought off the Police!"
                else:
                    state["choice_result"] = (
                        "You failed to fight of the Police! "
                        + "The Police took the item from you! (-all "
                        + state["npc"]["item"].name
                        + ")"
                    )
    return render_template(
        "encounter.html",
        second_test=state["second_test"],
        text=state["choice_result"],
        npc=gen_npc,
        game=state["game"],
        currRegion=state["currRegion"],
        universe=state["game"].universe,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)
