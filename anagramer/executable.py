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

import os

from cloudlib import arguments


# Create a dictionary for use in storing the identified anagrams.
ANAGRAMS = dict()


def _parser(sorted_word, word):
    """Add word to a default dictionary.

    :param sorted_word: A sorted string from a word.
    :type sorted_word: ``str``
    :param word: The whole unsorted word.
    :type word: ``str``
    """

    ANAGRAMS.setdefault(sorted_word, list()).append(word)


def _catalog(words_files):
    """Open a word file and parse all words looking for anagrams.

    :param words_files: List of paths to a word files.
    :type words_files: ``list``
    """

    _word_files = [i for i in words_files if os.path.isfile(i)]
    if not _word_files:
        raise SystemExit('No word files were found at: %s' % words_files)

    for word_file in _word_files:
        with open(word_file) as words:
            for word in words:
                word = word.strip()
                _parser(
                    sorted_word=''.join(sorted(word)),
                    word=word
                )


def _render_output(constraint):
    """Iterate through all of the ANAGRAM items and print them as a string.

    This will print all of the anagrams which there are at least the
    constrained letters in the word and at least as many anagrams as there are
    letters.

    :param constraint: the constraint for the values being provided.
    :type constraint: ``int``
    """

    for key, value in ANAGRAMS.items():
        if len(value) >= len(key) >= constraint:
            print(' '.join(value))


def _arguments():
    """Return CLI arguments."""

    arguments_dict = {
        'optional_args': {
            'words_file': {
                'commands': [
                    '--words-files'
                ],
                'help': 'Path to a dictionary file. The file should contain'
                        ' one word per line. Default: %(default)s',
                'metavar': '[PATH]',
                'nargs': '+',
                'default': ['/usr/share/dict/words']
            },
            'value_constraint': {
                'commands': [
                    '--value-constraint'
                ],
                'help': 'Constrain the results to a given number of anagrams'
                        ' for a given word. This will find all of the'
                        ' anagrams which there are at least the constrained'
                        ' letters in the word and that also have at least as'
                        ' many anagrams as there are letters.'
                        ' Default: %(default)s',
                'metavar': '[INT]',
                'default': 4
            }
        }
    }

    return arguments.ArgumentParserator(
        arguments_dict=arguments_dict,
        epilog='Licensed Apache2',
        title='Parse a list of words and find all of the anagrams',
        detail='Anagram finder',
        description='From a given list of words or a file containing a list of'
                    ' words find and print out all of the anagrams possible'
                    ' for a given word.',
        env_name='ANAGRAM'
    ).arg_parser()


def main():
    """Run the main program."""

    args = _arguments()
    _catalog(words_files=args['words_files'])
    _render_output(constraint=int(args['value_constraint']))


if __name__ == '__main__':
    main()
