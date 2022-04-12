from flask import Flask, render_template, url_for, redirect, request
from forms import SettingForm, ConfirmForm, SPForm
import utility
import json
from game import Game
from item import Item
from transactions import Transactions

app = Flask(__name__)
app.config["SECRET_KEY"] = "ayy"

# initialize setup and state dict
setup = {
    "pName": None,
    "pDiff": None,
    "pCredits": 0,
    "pSPLimit": 0,
    "pilot": 0,
    "fighter": 0,
    "merchant": 0,
    "engineer": 0,
}
state = {}

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
        setup["pilot"] = sp_form.pilot.data
        setup["fighter"] = sp_form.fighter.data
        setup["merchant"] = sp_form.merchant.data
        setup["engineer"] = sp_form.engineer.data
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
        chicken_traders.start_game(
            setup["pName"],
            [setup["pilot"], setup["fighter"], setup["merchant"], setup["engineer"]],
            setup["pCredits"],
        )

        # initialize game states
        global state
        state["game"] = chicken_traders
        state["currRegion"] = chicken_traders.player.curr_region
        state["prev_region"] = state["currRegion"]
        state["selectedItem"] = None
        state["fuel_error"] = None
        state["market_error"] = None
        state["npc"] = {}
        state["negotiated"] = False
        state["choice_result"] = None
        state["second_test"] = True
        state["disabled"] = False
        state["end_game"] = None

        return redirect(url_for("about"))
    return render_template(
        "confirm.html",
        title="Confirm Settings",
        form=confirmform,
        name=setup["pName"],
        pilot=setup["pilot"],
        fighter=setup["fighter"],
        merchant=setup["merchant"],
        engineer=setup["engineer"],
        diff=setup["pDiff"],
        credits=setup["pCredits"],
    )


# about page
@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", game=state["game"])


# travel page
@app.route("/travel", methods=["GET", "POST"])
def travel():
    utility.update_all_travel_cost(state["game"], state["currRegion"])
    if state["npc"]:
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
                    state["game"].time,
                )
                utility.travel(state["game"], travel_region)
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
        if "selectedItem" in request.form:
            selected_id = int(request.form["selectedItem"])
            state["market_error"] = None
            for item in state["currRegion"].market:
                if item.id == selected_id:
                    state["selectedItem"] = item
                    return json.dumps(state["selectedItem"].__dict__)

        if "statementIndex" in request.form:
            return (
                "Purchase <strong>"
                + state["selectedItem"].name
                + "</strong> for <strong>"
                + str(state["selectedItem"].b_price)
                + "</strong>?"
            )
        if "purchase" in request.form:
            status = state["game"].player.attempt_buy(state["selectedItem"], 1)
            if status != "Success":
                state["market_error"] = status
                return status
            else:
                state["market_error"] = None
            for item in state["game"].player.ship.cargo:
                if item.id == state["selectedItem"].id:
                    return json.dumps(item.__dict__)
            
        if "sellId" in request.form:
            item_id = int(request.form["sellId"])
            for index, item in enumerate(state["game"].player.ship.cargo):
                if item.id == item_id:
                    state["game"].player.trade_sell(index, 1)
                    return str(item.amount)
        if "updateCredits" in request.form:
            return str(state["game"].player.credit)
        if "updateStorageCapacity" in request.form:
            return str(state["game"].player.ship.cargo_size)
        if "addFuel" in request.form:
            state["game"].player.purchase_fuel(50)
            return str(state["game"].player.ship.fuel_level)
        if "addHealth" in request.form:
            state["game"].player.buy_repairs(10)
            return str(state["game"].player.ship.health_level)
    return render_template(
        "market.html",
        repair_cost=utility.repair_cost(10, state["game"].player.engineer),
        market_error=state["market_error"],
        game=state["game"],
        currRegion=state["currRegion"],
        selectedItem=state["selectedItem"],
    )

# ship page
@app.route("/ship", methods=["GET", "POST"])
def ship():
    return render_template("ship.html", game=state["game"])

# collection page
@app.route("/collection", methods=["GET", "POST"])
def collection():
    if request.method == "POST":
        if "addCredits" in request.form:
            category = request.form["addCredits"]
            index = state["game"].player.collection.category.index(category)
            state["game"].player.collection.complete[index] = True
            state["game"].player.credit += 100
            state["game"].player.transaction_history.append(Transactions("Collection reward", 100, "collection", "earnings"))
            return str(state["game"].player.credit)
    return render_template(
        "collection.html", game=state["game"], all_items=Item.__subclasses__()
    )

# stats page
@app.route("/stats", methods=["GET", "POST"])
def stats():
    processed_transaction_history = []
    for entry in state["game"].player.transaction_history:
        processed_transaction_history.append(json.dumps(entry.__dict__))
    return render_template("stats.html", 
        game=state["game"], 
        net_worth_data=state["game"].net_worth_data, 
        transaction_history=processed_transaction_history,
        npc_count=state["game"].player.npc_count,
        distance_traveled=state["game"].player.distance_traveled)

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
        # encounter interaction finished, go back to travel page
        if "updateCredits" in request.form:
            return str(state["game"].player.credit)
        if "updateHealth" in request.form:
            return str(state["game"].player.ship.health_level)
        if "return_travel" in request.form:
            state["npc"] = None
            state["choice_result"] = None
            state["disabled"] = False
        elif not state["disabled"]:
            state["disabled"] = True
            curr_credits = state["game"].player.credit
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
                        "You attempted to pay the bandit without enough money! "
                        + "The bandit steals all your cargo!"
                    )
                else:
                    state["choice_result"] = (
                        "You attempted to pay the bandit without anything to offer!"
                        + "The bandit attacks you out of anger! (-15 health)"
                    )
                return state["choice_result"]

            if "fight_bandit" in request.form:
                if utility.fight_bandit(state["game"].player, state["npc"]):
                    state["choice_result"] = (
                        "You successfully defeated the bandit. You took the Bandit's credits. \n(+"
                        + str(int((5 / 4) * state["npc"]["demand"]))
                        + " credits)"
                    )
                else:
                    state["choice_result"] = (
                        "You lost to the Bandit! The Bandit "
                        + "took most of your credits and injured you. (-"
                        + str(curr_credits - int(curr_credits / 3))
                        + " credits, -20 health)"
                    )
                return state["choice_result"]

            if "flee_bandit" in request.form:
                if utility.flee_bandit(state["game"].player):
                    state["currRegion"] = state["prev_region"]
                    state["game"].player.curr_region = state["prev_region"]
                    state[
                        "choice_result"
                    ] = "You successfully fled to the previous region!"
                else:
                    state["choice_result"] = (
                        "You failed to flee the Bandit. "
                        + "The Bandit took half of your credits and injured you. (-"
                        + str(curr_credits - int(curr_credits / 2))
                        + " credits, -20 health)"
                    )
                return state["choice_result"]

            # trader choices
            if "buy_trader" in request.form:
                if state["game"].player.attempt_buy(state["npc"]["item"], 1) == "Success":
                    state["second_test"] = True
                    state["negotiated"] = False
                    state["choice_result"] = (
                        "You bought a " + state["npc"]["item"].name + "."
                    )
                else:
                    state["disabled"] = False
                    state["second_test"] = False
                    state["choice_result"] = state["game"].player.attempt_buy(state["npc"]["item"], 1)
                return state["choice_result"]

            if "ignore_trader" in request.form:
                state["second_test"] = True
                state["negotiated"] = False
                state["choice_result"] = "You chose to ignore the Trader."
                return state["choice_result"]

            if "rob_trader" in request.form:
                state["second_test"] = True
                state["negotiated"] = False
                result = utility.rob_trader(state["game"].player, state["npc"])
                if result == 1:
                    state["choice_result"] = (
                        "You robbed the Trader! (+1 " + state["npc"]["item"].name + ")"
                    )
                elif result == 2:
                    state[
                        "choice_result"
                    ] = "The Trader caught you in the act and slapped you. (-10 health)"
                else:
                    state[
                        "choice_result"
                    ] = "You successfully robbed the trader, but have no room to hold the item!"
                return state["choice_result"]

            if "negotiate_trader" in request.form:
                state["disabled"] = False
                state["second_test"] = False
                if not state["negotiated"]:
                    state["negotiated"] = True
                    if utility.negotiate_trader(state["game"].player, state["npc"]):
                        state[
                            "choice_result"
                        ] = "You negotiated a deal with the Trader. (-33% price)"
                    else:
                        state[
                            "choice_result"
                        ] = "The Trader was insulted by your negotiation attempt! (+33% price)"
                else:
                    state["choice_result"] = "You can only negotiate once! D:<"
                return state["choice_result"]
            # police choices
            if "forfeit_police" in request.form:
                utility.forfeit_police(state["game"].player, state["npc"])
                state["choice_result"] = (
                    "You forfeited the item. (-all " + state["npc"]["item"].name + ")"
                )
                return state["choice_result"]

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
                        + ", -100 credits, -15 health)"
                    )
                return state["choice_result"]

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
                return state["choice_result"]

    return render_template(
        "encounter.html",
        pilot=utility.get_skill_check(state["game"].player.pilot),
        fighter=utility.get_skill_check(state["game"].player.fighter),
        merchant=utility.get_skill_check(state["game"].player.merchant),
        engineer=utility.get_skill_check(state["game"].player.engineer),
        second_test=state["second_test"],
        text=state["choice_result"],
        npc=gen_npc,
        game=state["game"],
        currRegion=state["currRegion"],
        universe=state["game"].universe,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)
