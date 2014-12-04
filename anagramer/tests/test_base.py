# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import sys
import unittest

import mock

from anagramer import executable


class TestBase(unittest.TestCase):
    def setUp(self):
        self.args_patched = mock.patch(
            'anagramer.executable.arguments.ArgumentParserator.arg_parser'
        )
        self.isf = self.args_patched.start()
        self.isf.return_value = {
            'system_config': None,
            'value_constraint': 4,
            'words_files': [
                '/usr/share/dict/words'
            ]
        }

    def tearDown(self):
        self.args_patched.stop()

    def test_constant(self):
        self.assertTrue(isinstance(executable.ANAGRAMS, dict))

    def test_arguments_type(self):
        self.assertTrue(isinstance(executable._arguments(), dict))


class TestBaseParser(unittest.TestCase):
    def tearDown(self):
        executable.ANAGRAMS = dict()

    def test_parser(self):
        executable._parser(sorted_word='aer', word='are')
        for k, v in executable.ANAGRAMS.items():
            self.assertTrue(isinstance(v, list))
            self.assertTrue(v[0] == 'are')


class TestBaseCatalog(unittest.TestCase):
    def setUp(self):
        self.isf_patched = mock.patch('anagramer.executable.os.path.isfile')
        self.isf = self.isf_patched.start()

        self.mock_open_patch = mock.patch(
            'anagramer.executable.open',
            create=True
        )
        self.mock_open = self.mock_open_patch.start()

    def tearDown(self):
        self.isf_patched.stop()
        self.mock_open_patch.stop()
        executable.ANAGRAMS = dict()

    def test_catalog_no_file(self):
        self.isf.return_value = False
        self.assertRaises(
            SystemExit,
            executable._catalog,
            words_files=['fail']
        )

    def test_catalog_file(self):
        self.isf.return_value = True
        self.mock_open.return_value = io.StringIO(u'are\nera\n')
        executable._catalog(['test-file'])
        for k, v in executable.ANAGRAMS.items():
            self.assertTrue(isinstance(v, list))
            self.assertTrue(v[0] == 'are')
            self.assertTrue(v[1] == 'era')


class TestBaseRender(unittest.TestCase):
    def setUp(self):
        if sys.version_info >= (3, 2, 0):
            self.mock_print_patch = mock.patch(
                'sys.stdout', new_callable=io.StringIO
            )
        else:
            self.mock_print_patch = mock.patch(
                'sys.stdout', new_callable=io.BytesIO
            )
        self.mock_print = self.mock_print_patch.start()

    def tearDown(self):
        executable.ANAGRAMS = dict()
        self.mock_print_patch.stop()

    def test_print(self):
        executable.ANAGRAMS = {
            'aacinr': [
                'acinar',
                'arnica',
                'canari',
                'carina',
                'crania',
                'narica'
            ]
        }
        executable._render_output(constraint=4)
        self.assertTrue(
            self.mock_print.getvalue() == 'acinar arnica canari carina crania'
                                          ' narica\n'
        )

    def test_print_nothing(self):
        executable.ANAGRAMS = {
            'are': [
                'era',
                'are'
            ]
        }
        executable._render_output(constraint=4)
        self.assertTrue(self.mock_print.getvalue() == '')
