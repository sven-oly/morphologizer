#!/usr/bin/python3
# -*- coding: utf-8 -*-

# [START gae_python37_app]
from flask import Flask, render_template, stream_with_context, request, Response, send_file, jsonify

# https://flask.palletsprojects.com/en/2.1.x/patterns/fileuploads/

# The rules for particular morphologizers
from cherokee_morphy import cherokee_morphy

import cher_morph_defs

import samples

import datetime

from io import BytesIO
from io import StringIO

import json
import logging
import os
import time

import google.auth

from google.cloud import tasks

import sys

# Global for debugging
debug = False

morphers = {
    'chr': cherokee_morphy(),
    'chr_cher': cher_morph_defs.morph_chr_syllabary(),
    'chr_latn': cher_morph_defs.morph_chr_latin(),
}

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

ts_client = tasks.CloudTasksClient()

_, PROJECT_ID = google.auth.default()
QUEUE_NAME = 'font-convert-queue'
REGION_ID = LOCATION_ID = 'us-central1'
QUEUE_PATH = ts_client.queue_path(PROJECT_ID, REGION_ID, QUEUE_NAME)

@app.route('/')
def hello():
    """Top of the conversion application."""
    who = request.url
    return render_template('main.html', base=who)


@app.route('/cherokee/')
def morphy_cherokee():
    # TODO: Generalize to other languages
    lang_code = 'chr'
    base_morpher = morphers['chr']
    morpher = morphers['chr_latn']
    # morpher = morphers['chr_cher']  # Using the syllabary

    chr_samples = samples.samples['chr']

    return render_template(
        'morph_lang.html',
        gloss_parts=base_morpher.gloss.gloss_parts,
        lang_name='ᏣᎳᎩ',
        lang_code=lang_code,
        rules=len(morpher.rules),
        samples=chr_samples,
        stems=morpher.stems,
        use_textarea=1
    )


@app.route('/get_morph_results/', methods=['GET', 'POST'])
def morphy_results():
    if request.method == 'POST':
        lang_code = request.form['lang_code']
        input_text = request.form['input_text']
        requested_function = request.form['function']
    else:
        lang_code=request.args.get('lang_code', 'und')
        input_text=request.args.get('input_text')
        requested_function= request.args.get('function')

    # Generalize based on language code
    morpher = morphers[lang_code]
    if debug:
        print('input_text = %s' % input_text)
        print('lang_code = %s' % lang_code)
        print('morpher = %s' % morpher)

    result = '<No result>'
    if requested_function == 'generate':
        result = morpher.generate(input_text)
    elif requested_function == 'parse':
        result = morpher.parse(input_text)
    elif requested_function == 'paradigm':
        result = morpher.paradigm(input_text)
    else:
        # Unknown
        print('unknown result = %s' % result)

    # Simply pass back results as JSON data
    data = {'result_text': result}
    jdata = json.dumps(data);
    return jdata


@app.route('/generate/')
def generate():
    lang_code = request.args.get('lang_code', 'und')
    input_text = request.args.get('gen_text')

    # Generalize based on language code
    morpher = cherokee_morphy()

    generated = morpher.generate(input_text)

    return render_template(
        'generated_text.html',
        lang_code=lang_code,
        input_text=input_text,
        morpher=morpher,
        generated=generated
        )


@app.route('/parse/')
def parse():
    lang_code = request.args.get('lang_code', 'und')
    input_text = request.args.get('parse_text')

    # Generalize based on language code
    morpher = cherokee_morphy()

    parsed = morpher.parse(input_text)

    return render_template(
        'parsed_text.html',
        lang_code=lang_code,
        input_text=input_text,
        morpher=morpher,
        parsed=parsed
        )


@app.route('/test/')
def test():
    lang_code = request.args.get('lang_code', 'und')
    input_text = request.args.get('text')

    # Generalize based on language code
    morpher = cherokee_morphy()

    result =  morpher.test(input_text)

    return render_template(
        'test_text.html',
        lang_code=lang_code,
        input_text=input_text,
        morpher=morpher,
        test_result=result
        )


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True, threaded=True)
# [END gae_python37_app]

