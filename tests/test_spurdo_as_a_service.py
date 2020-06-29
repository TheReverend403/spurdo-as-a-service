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

from spurdo_as_a_service import EBIN_FACES, translate_to_spurdo


def test_spurdo():
    translated = translate_to_spurdo('Testing spurdo translation')
    assert translated == 'Testign spurdo dranzlation'

    translated = translate_to_spurdo('Testing spurdo translation.')
    assert translated.startswith('Testign spurdo dranzlation ') \
        and any(translated.endswith(face) for face in EBIN_FACES)
