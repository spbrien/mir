#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

def read_file(file_name):
    """Read file and return its contents."""
    with open(file_name, 'r') as f:
        return f.read()

def read_requirements(file_name):
    """Read requirements file as a list."""
    reqs = read_file(file_name).splitlines()
    if not reqs:
        raise RuntimeError(
            "Unable to read requirements from the %s file"
            "That indicates this copy of the source code is incomplete."
            % file_name
        )
    return reqs

requirements = read_requirements('requirements.txt')

setup_requirements = [
    # TODO(spbrien): Put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: Put package test requirements here
]

setup(
    name='mir',
    version='1.2.8',
    description="Mir API Framework",
    long_description=readme + '\n\n' + history,
    author="Steven Brien",
    author_email='spbrien@gmail.com',
    url='https://github.com/spbrien/mir',
    packages=find_packages(include=['mir']),
    entry_points={
        'console_scripts': [
            'mir=mir.cli:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['*.*', '.*', '**/*.*', '**/.*'],
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='mir',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    use_2to3=True
)
