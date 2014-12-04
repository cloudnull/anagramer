#!/usr/bin/env python
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

import setuptools
import sys

import anagramer

with open('requirements.txt') as f:
    required = f.read().splitlines()

if sys.version_info < (2, 6, 0):
    sys.stderr.write('Anagramer Presently requires Python 2.6.0 or greater')
    raise SystemExit(
        'Upgrade python because your version of it is deprecated'
    )
elif sys.version_info < (2, 7, 0):
    required.append('argparse')

with open('README.rst', 'rb') as r_file:
    LDINFO = r_file.read()

setuptools.setup(
    name=anagramer.__appname__,
    version=anagramer.__version__,
    author=anagramer.__author__,
    author_email=anagramer.__email__,
    description=anagramer.__description__,
    long_description=LDINFO,
    license='License :: OSI Approved :: Apache Software License',
    packages=[
        'anagramer'
    ],
    url=anagramer.__url__,
    install_requires=required,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        "console_scripts": [
            "anagramer = anagramer.executable:main"
        ]
    }
)
