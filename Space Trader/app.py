from flask import Flask, render_template, url_for, redirect, request, flash
from forms import SettingForm, ConfirmForm
from config import Config
from Universe import Universe, Region
from Player import Player
app = Flask(__name__)
app.config.from_object(Config)

posts = [
    {
        'first_name': 'Jeffrey',
        'last_name': 'Tram',
    },
    {
        'first_name': 'Bradford',
        'last_name': 'Peterson'
    },
    {
        'first_name': 'Robert',
        'last_name': 'Giuffreda'
    }
]

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    settingform = SettingForm()
    if settingform.validate_on_submit():
        p_name = settingform.name.data
        p_diff = settingform.diff.data
        p_sp1 = settingform.sp1.data
        p_sp2 = settingform.sp2.data
        p_sp3 = settingform.sp3.data
        p_sp4 = settingform.sp4.data
        #TODO: how to determine region and credits?
        #TODO: how to pass player created to confirm page?
        region1 = Region(1, 'Bob\'s Farm')
        skillpoints = [p_sp1, p_sp2, p_sp3, p_sp4]
        player = Player(p_name, skillpoints, region1 , 800)
        return redirect('/confirm')
    return render_template('settings.html', form=settingform)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About', posts=posts)

@app.route('/confirm', methods=['GET'])
def confirm():
    confirmform = ConfirmForm()
    region1 = Region(1, 'Bob\'s Farm')
    skillpoints = [1,1,1,1]
    player = Player('test', skillpoints, region1 , 800)
    if confirmform.validate_on_submit():
        #TODO: create player
        return redirect('/start')
    return render_template('confirm.html', title='Confirm Settings', player=player)


testUniverse = Universe()
@app.route('/start', methods=['GET','POST'])
def start():
    return render_template('start.html', universe=testUniverse)


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 80, debug = True)