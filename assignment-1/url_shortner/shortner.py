import functools
import short_url
from urllib.parse import urlparse

from flask import (Blueprint, flash, g, redirect, render_template, request,
        session, url_for)
from werkzeug.exceptions import abort

from url_shortner.db import get_db

bp = Blueprint('shortner', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()

    if request.method == 'POST':
        db.execute('DELETE FROM url')
        db.commit()

        return redirect(url_for('shortner.index'))

    urls = db.execute(
            'SELECT u.id, url_full, url_short FROM url u'
            ' ORDER BY created DESC'
            ).fetchall()
    return render_template('shortner/index.html', urls=urls)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        url = request.form['url']
        error = None

        if not url:
            error = 'Url is required.'

        if not valid_url(url):
            error = 'Invalid url.'

        if error is not None:
            flash(error)
        else:
            db = get_db()

            db.execute(
                    'INSERT INTO url (url_full, url_short)'
                    'VALUES (?, ?)',
                    (url, short_url.encode_url(get_new_id()))
                    )
            db.commit()
            return redirect(url_for('shortner.index'))

    return render_template('shortner/create.html')

@bp.route('/<int:id>')
def show(id):
    url = get_url(id)

    return render_template('shortner/show.html', url=url)

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    url = get_url(id)

    if request.method == 'POST':
        url = request.form['url']
        error = None

        if not url:
            error = 'Url is required.'

        if not valid_url(url):
            error = 'Invalid url.'

        if error is not None:
            flash(error)
            return redirect(url_for('shortner.update', id=id))
        else:
            db = get_db()
            db.execute(
                    'UPDATE url SET url_full = ?'
                    'WHERE id = ?',
                    (url, id)
                    )
            db.commit()
            return redirect(url_for('shortner.index'))

    return render_template('shortner/update.html', url=url)

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    db = get_db()

    db.execute('DELETE from url WHERE id = ?', (id,))
    db.commit()

    return redirect(url_for('shortner.index'))

def valid_url(url):
    schemes = ['http', 'https', 'ftp']
    pieces = urlparse(url)

    if pieces.scheme in schemes:
        return True
    else:
        return False

def get_new_id():
    if get_last_row() is None: return 1

    last_id = get_last_row()['id']

    return last_id + 1

def get_last_row():
    db = get_db()
    return db.execute(
            'SELECT u.id FROM url u'
            ' ORDER BY created DESC'
            ).fetchone()

def get_url(id):
    url = get_db().execute(
            'SELECT u.id, url_full, url_short FROM url u'
            ' WHERE id = ?',
            (id,)
            ).fetchone()

    if url is None:
        abort(404, "Url id {0} does not exist.".format(id))

    return url
