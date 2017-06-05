
from Hello import oauth2
from . import dataStore
from flask import Blueprint, current_app, redirect, render_template, request,session, url_for

crud = Blueprint('crud', __name__)



@crud.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)


        if 'profile' in session:
            data['Name'] = session['profile']['name']
            data['Id'] = session['profile']['id']
            data['Family_name'] = session['profile']['family_name']
            data['Given_name'] = session['profile']['given_name']

        junk = dataStore.create(data)

        return redirect(url_for('.add'))

    return render_template("saveUser.html", action="Add")

