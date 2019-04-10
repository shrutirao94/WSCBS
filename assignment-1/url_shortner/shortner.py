import functools
import short_url

from urllib.parse import urlparse
from flask import (Blueprint, flash, g, redirect, render_template, request,
        session, url_for)
from werkzeug.exceptions import abort
from url_shortner.db import get_db
from flask import jsonify

bp = Blueprint('shortner', __name__)

@bp.route('/', methods=('GET', 'DELETE', 'POST'))
def index():
    db = get_db()

    if request.method == 'DELETE':
        db.execute('DELETE FROM url')
        db.commit()

        return "", 204

    if request.method == 'POST':
        try:
            url = request.form['url']
        except:
            abort(400, 'param url is required.')

        if not valid_url(url):
            abort(400, 'Invalid url.')

        new_short_url = short_url.encode_url(get_new_id())
        db.execute(
                'INSERT INTO url (url_full, url_short)'
                'VALUES (?, ?)',
                (url, new_short_url)
                )
        db.commit()
        return "127.0.0.1:5000/{0}".format(new_short_url), 201

    urls = db.execute(
            'SELECT u.id, url_full, url_short FROM url u'
            ' ORDER BY created DESC'
            ).fetchall()

    payload = {}
    for url in urls:
        payload[url['id']] = {'short': url['url_short'], 'full': url['url_full']}

    return jsonify(payload), 200

@bp.route('/<url_short>', methods=('GET', 'DELETE', 'PUT'))
def show(url_short):
    url = get_url(url_short)
    db = get_db()

    if request.method == 'DELETE':
        db.execute('DELETE FROM url WHERE id = ?',
                (url['id'],)
                )
        db.commit()
        return "", 204

    if request.method == 'PUT':
        try:
            new_url = request.form['url']
        except:
            abort(400, 'param url is required.')

        if not valid_url(new_url):
            abort(400, 'Invalid url.')

        db = get_db()
        db.execute(
                'UPDATE url SET url_full = ?'
                'WHERE id = ?',
                (new_url, url['id'])
                )
        db.commit()
        return "", 200

    return redirect(url['url_full']), 301

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

def get_url(url_short):
    url = get_db().execute(
            'SELECT u.id, url_full, url_short FROM url u'
            ' WHERE url_short = ?',
            (url_short,)
            ).fetchone()

    if url is None:
        abort(404, "Url id {0} does not exist.".format(id))

    return url
