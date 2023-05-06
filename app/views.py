import os
import random
import string
from flask import render_template, redirect, url_for

from . import app, db
from .forms import URLForm
from .models import URLmodel


def get_short():
    while True:
        short = ''.join(random.choices(string.ascii_letters + \
        string.ascii_letters, k=int(os.environ.get('SHORT_LEN'))))
        if URLmodel.query.filter(URLmodel.short == short).first():
            continue
        return short


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        url = URLmodel()
        url.original_url = form.original_url.data
        url.short = get_short()
        db.session.add(url)
        db.session.commit()
        return redirect(url_for('urls'))
    return render_template('index.html', form=form)


@app.route('/urls', methods=['GET'])
def urls():
    urls = URLmodel.query.all()
    return render_template('urls.html', urls=urls[::-1])


@app.route('/<string:short>', methods=['GET'])
def url_redirect(short):
    url = URLmodel.query.filter(URLmodel.short == short).first()
    if url:
        url.visits += 1
        db.session.add(url)
        db.session.commit()
        return redirect(url.original_url)
