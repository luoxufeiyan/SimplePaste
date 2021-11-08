#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 20-01-25 下午4:22
# @Author  : LXFY
# @Site    : http://paste.fledding.com
# @File    : app.py
# @Software: PyCharm

from __future__ import unicode_literals

from flask import (Flask, render_template, redirect, url_for, request, flash)
from flask_bootstrap import Bootstrap
from flask_login import login_required, login_user, logout_user, current_user


from forms import ContentForm, LoginForm, CodeForm, ModifyForm
from ext import db, login_manager
from models import PasteText, User
import secure

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Read config
app.config.from_object('secure')

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login"


@app.route('/', methods=['GET', 'POST'])
# @csrf.exempt
def show_index():
    content_form = ContentForm()
    # code_form = CodeForm()
    if request.method == 'GET':
        return render_template('index.html', content_form=content_form)
    else:
        if content_form.validate_on_submit() and content_form.content:
            NewText = PasteText(0, content_form.content.data, 1)
            db.session.add(NewText)
            db.session.flush()
            NewPostID = NewText.id
            db.session.commit()
            flash('Paste posted! Paste code: ' + str(NewPostID))
            return redirect((url_for('show_paste', pid=NewPostID)))
        else:
            flash(content_form.errors)
        return redirect(url_for('show_index'))


@app.route('/submit', methods=['POST'])
# @csrf.exempt
def submit_content():
    content_form = ContentForm()
    if content_form.validate_on_submit() and content_form.content:
        NewText = PasteText(0, content_form.content.data, 1)
        db.session.add(NewText)
        db.session.flush()
        NewPostID = NewText.id
        db.session.commit()
        flash('Paste posted! Paste code: ' + str(NewPostID))
        return redirect((url_for('show_paste', pid=NewPostID)))
    else:
        flash(content_form.errors)
    return redirect(url_for('show_index'))


@app.route('/entercode', methods=['GET', 'POST'])
# @csrf.exempt
def enter_code():
    code_form = CodeForm()
    if request.method == 'GET':
        return render_template('enter_code.html', code_form=code_form)
    else:
        if code_form.validate_on_submit() and code_form.code:
            return redirect((url_for('show_paste', pid=code_form.code.data)))
        else:
            flash(code_form.errors)
        return redirect(url_for('enter_code'))


@app.route('/p/<pid>')
def show_paste(pid):
    paste_id = pid
    paste_text = PasteText.query.get(paste_id)
    if paste_text and paste_text.status == 1:
        return render_template('view.html', form=paste_text, pid=pid)
    else:
        return render_template('404.html')


@app.route('/manage')
@login_required
def show_paste_list():
    form = ContentForm()
    pasteList = PasteText.query.all()
    return render_template('manage.html', pastelists=pasteList, form=form)


# This function has been abandoned, plase use modify to change the display status
# TODO Code will be deleted in future version.
@app.route('/delete/<int:id>')
@login_required
def delete_paste(id):
    # hide, not delete
    pastelist = PasteText.query.filter_by(id=id).first_or_404()
    pastelist.status = 0
    db.session.commit()
    flash('You have deleted a paste.')
    return redirect(url_for('show_paste_list'))


@app.route('/change/<int:id>', methods=['GET', 'POST'])
@login_required
def change_paste(id):
    if request.method == 'GET':
        pasteList = PasteText.query.filter_by(id=id).first_or_404()
        form = ModifyForm()
        form.content.data = pasteList.content
        return render_template('modify.html', form=form)
    else:
        form = ModifyForm()
        if form.validate_on_submit():
            pasteList = PasteText.query.filter_by(id=id).first_or_404()
            pasteList.content = form.content.data
            pasteList.status = form.status.data
            db.session.commit()
            flash('You have modify a pasteList')
        else:
            flash(form.errors)
        return redirect(url_for('show_paste_list'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.form['username'], password=request.form['password']).first()
        if user:
            login_user(user)
            flash('you have logged in!')
            return redirect(url_for('show_paste_list'))
        else:
            flash('Invalid username or password')
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have logout!')
    return redirect(url_for('login'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
