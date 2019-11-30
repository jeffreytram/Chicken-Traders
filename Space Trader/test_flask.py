import pytest
import utility

from flask import Flask
from myapp import app


def test_player_setup_easy(test_game):
    client = app.test_client()
    url = "/"
    response = client.get(url)
    assert test_game.player.name == "tester"
    assert test_game.player.pilot == 4
    assert test_game.player.fighter == 4
    assert test_game.player.merchant == 4
    assert test_game.player.engineer == 4
    assert test_game.player.credit == 1000
    assert test_game.player.karma == 0
    assert response.status_code == 200


def test_bandit_pay_fee(test_game):
    bandit = utility.gen_bandit()
    player = test_game.player

    # case 1: player has enough money to pay
    # bandit takes fee
    result1 = utility.pay_bandit(player, bandit)
    assert result1 == 1

    # case 2: player doesn't have enough money to pay
    # but has items
    # bandit takes all items
    player.trade_buy(player.curr_region.market[0], 1)
    player.credit = 0
    result2 = utility.pay_bandit(player, bandit)
    assert result2 == 2
    assert len(player.ship.cargo) == 0

    # case 3: player doesnt have enough money and has no items
    # -15 health
    result3 = utility.pay_bandit(player, bandit)
    assert result3 == 3
    assert player.ship.health_level == player.ship.max_health - 15


def test_bandit_fight(test_game):
    bandit = utility.gen_bandit()
    player = test_game.player

    win_checked = False
    lose_checked = False
    while ((not win_checked) or (not lose_checked)):
        player.ship.health_level = player.ship.max_health
        player.credit = 1000

        if utility.fight_bandit(player, bandit):
            # case 1: win fight
            # + bandit credits
            win_checked = True
            assert player.credit == 1000 + int(bandit["demand"] * 5 / 4)
        else:
            # case 2: lose fight
            # 0 credits, -20 health
            lose_checked = True
            assert player.credit == 0
            assert player.ship.health_level == player.ship.max_health - 20
