#  This file is part of spurdo-as-a-service.
#
#  spurdo-as-a-service is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  spurdo-as-a-service is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with spurdo-as-a-service.  If not, see <https://www.gnu.org/licenses/>.

import os
import random

from flask import Flask, render_template, request

SPURDO_REPLACEMENTS = {
    'kek': 'geg',
    'some': 'sum',
    'meme': 'maymay',
    'epic': 'ebin',
    'wh': 'w',
    'th': 'd',
    'af': 'ab',
    'ap': 'ab',
    'ca': 'ga',
    'ck': 'gg',
    'co': 'go',
    'ev': 'eb',
    'ex': 'egz',
    'et': 'ed',
    'iv': 'ib',
    'it': 'id',
    'ke': 'ge',
    'nt': 'nd',
    'op': 'ob',
    'ot': 'od',
    'po': 'bo',
    'pe': 'be',
    'pi': 'bi',
    'up': 'ub',
    'va': 'ba',
    'cr': 'gr',
    'kn': 'gn',
    'lt': 'ld',
    'mm': 'm',
    'pr': 'br',
    'ts': 'dz',
    'tr': 'dr',
    'bs': 'bz',
    'ds': 'dz',
    'es': 'es',
    'fs': 'fz',
    'gs': 'gz',
    ' is': ' iz',
    'ls': 'lz',
    'ms': 'mz',
    'ns': 'nz',
    'rs': 'rz',
    'ss': 'sz',
    'us': 'uz',
    'ws': 'wz',
    'ys': 'yz',
    'alk': 'olk',
    'ing': 'ign',
    'ic': 'ig',
    'ng': 'nk',
}

EBIN_FACES = [':D', ':DD', ':DDD', ':-D', 'XD', 'XXD', 'XDD', 'XXDD', 'xD', 'xDD', ':dd']


def create_app():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    app = Flask('spurdo-as-a-service', template_folder=f'{BASE_DIR}/templates', static_folder=f'{BASE_DIR}/static')

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if 'text' not in request.values or not request.values['text']:
            return render_template('index.html', base_url=request.base_url)

        input_text = request.values['text']
        return translate_to_spurdo(input_text)

    return app


def translate_to_spurdo(input_text: str):
    for key, value in SPURDO_REPLACEMENTS.items():
        input_text = input_text.replace(key, value)

    for symbol in ['!', '.', ',', '?']:
        while symbol in input_text:
            input_text = input_text.replace(symbol, f' {random.choice(EBIN_FACES)}', 1)

    return input_text
