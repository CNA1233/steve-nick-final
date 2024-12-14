from flask import Flask, render_template, redirect, url_for, request
from db import get_all_players, add_player, update_player, delete_player, create_db
from forms import PlayerForm

app = Flask(__name__)
app.secret_key = 'abc_123'
create_db()


@app.route('/')
def home():
    players = get_all_players()
    return render_template('player_list.html', players=players)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = PlayerForm()
    if form.validate_on_submit():
        bat_order = form.bat_order.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        position = form.position.data
        at_bats = form.at_bats.data
        hits = form.hits.data
        add_player(bat_order, first_name, last_name, position, at_bats, hits)
        return redirect(url_for('home'))
    return render_template('add_player.html', form=form)


@app.route('/edit/<int:player_id>', methods=['GET', 'POST'])
def edit(player_id):
    player = get_all_players()[player_id-1]
    form = PlayerForm(obj=player)
    if form.validate_on_submit():
        bat_order = form.bat_order.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        position = form.position.data
        at_bats = form.at_bats.data
        hits = form.hits.data
        update_player(player_id, bat_order, first_name, last_name, position, at_bats, hits)
        return redirect(url_for('home'))
    return render_template('edit_player.html', form=form)

@app.route('/delete/<int:player_id>')
def delete(player_id):
    delete_player(player_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
