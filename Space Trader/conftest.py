import pytest

from flask import Flask
from myapp import app
from player import Player
from game import Game

@pytest.fixture(scope='session', autouse=True)
def test_game(request):
    chicken_traders = Game("easy")
    chicken_traders.start_game("tester", [4,4,4,4], 1000)
    return chicken_traders