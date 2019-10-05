from flask import Flask, render_template, url_for, redirect, request, flash, session
from forms import SettingForm, ConfirmForm, SPForm
from config import Config
from Universe import Universe, Region
from Player import Player
import random
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
        if settingform.diff.data == 'easy':
            credits = 1000
            sp = 16
            print('easy')
        if settingform.diff.data == 'med':
            credits = 800
            sp = 14
            print('med')
        if settingform.diff.data == 'hard':
            credits = 500
            sp = 12
            print('hard')
        return redirect(url_for('skillpoints', name=settingform.name.data, diff=settingform.diff.data, sp=sp, credits=credits))
    return render_template('settings.html', form=settingform)

@app.route('/skillpoints?name=<name>&diff=<diff>&sp=<sp>&credits=<credits>', methods=['GET', 'POST'])
def skillpoints(name, diff, sp, credits):
    spForm = SPForm()
    def validTotal(spArray):
        total = 0
        for spElement in spArray:
            total = total + spElement
        if total > int(sp):
            flash('You can only allocate ' +str(sp)+' skill points.')
            return False
        return True
    #TODO: remove validTotal once we get form variable pass in working
    if spForm.validate_on_submit() and validTotal([spForm.sp1.data, spForm.sp2.data, spForm.sp3.data, spForm.sp4.data]):
        sp1 = spForm.sp1.data
        sp2 = spForm.sp2.data
        sp3 = spForm.sp3.data
        sp4 = spForm.sp4.data
        return redirect(url_for('confirm', name=name, diff=diff, sp=sp, sp1=sp1, sp2=sp2, sp3=sp3, sp4=sp4, credits=credits))
    return render_template('skillpoints.html', form=spForm, sp=sp)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About', posts=posts)

testUniverse = Universe()
@app.route('/confirm?name=<name>&diff=<diff>&sp=<sp>&sp1=<sp1>&sp2=<sp2>&sp3=<sp3>&sp4=<sp4>&credits=<credits>', methods=['GET'])
def confirm(name, diff, sp, sp1,sp2,sp3,sp4,credits):
    confirmform = ConfirmForm()
    if confirmform.is_submitted:
        randRegion = random.randint(0,9)
        pSkillPoints = [sp1,sp2,sp3,sp4]
        player = Player(name,pSkillPoints, credits, testUniverse.regionList[randRegion])
        return redirect(url_for('start', startingRegion=randRegion))
    return render_template('confirm.html', title='Confirm Settings', form=confirmform, name=name, diff=diff, sp1=sp1, sp2=sp2, sp3=sp3, sp4=sp4, credits=credits)

@app.route('/start?startingRegion=<startingRegion>', methods=['GET','POST'])
def start(startingRegion):
    
    return render_template('start.html', universe=testUniverse, randRegionIndex=int(startingRegion))


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 80, debug = True)