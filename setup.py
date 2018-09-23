#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2017 HellWorld, Inc.
#
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

import sys
from os.path import dirname, join
from pip.req import parse_requirements

from setuptools import (
    find_packages,
    setup,
)

with open(join(dirname(__file__), 'src/VERSION.txt'), 'rb') as f:
    version = f.read().decode('ascii').strip()

requirements = [str(ir.req) for ir in parse_requirements("requirements.txt", session=False)]

# if sys.version_info.major == 2:
#     requirements += [str(ir.req) for ir in parse_requirements("requirements-py2.txt", session=False)]

setup(
    name='helloworld',
    version=version,
    description='helloworld',
    scripts=[''],
    classifiers=[],
    keywords='helloworld',
    author='allen',
    author_email='hujb2000@163.com',
    url='https://github.com/hujb2000/helloworld.git',
    license='Apache License 2.0',
    packages=find_packages(exclude=[]),
    package_data={'': ['*.*']},
    include_package_data=True,
    zip_safe=True,
    install_requires=requirements,
    project_urls={
        "Bug Tracker": "https://github.com/hujb2000//HelloWorld/",
        "Documentation": "https://github.com/hujb2000//HelloWorld/",
        "Source Code": "https://github.com/hujb2000//HelloWorld/",
    },
    entry_points={'blogtool.parsers': '.rst = some_module:SomeClass'},
    #python_requires,
    #setup_requires
    #dependency_links
    #namespace_packages
    #test_suite
    #test_require
    #test_loader
    #eager_resources
    #use_2to3
    #covert_2to3_doctests
    #use_2to3_fixers

)
