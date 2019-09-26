#!/usr/bin/env python3

import Cython.Build
import numpy
import setuptools
import setuptools.extension


_DIRECTIVES = {'language_level': '3'}


setuptools.setup(
    name='evosimz',
    author='Zhengting Zou, Hongjiu Zhang, Yuanfang Guan, Jianzhi Zhang',
    author_email='ztzou@umich.edu, zhanghj@umich.edu, '
                 'gyuanfan@umich.edu, jianzhi@umich.edu',
    keywords='bioinformatics',
    python_requires='>=3.6.0',
    packages=setuptools.find_packages(exclude=['tests']),
    ext_modules=Cython.Build.cythonize(
        [setuptools.extension.Extension('*', ['evosimz/*.pyx'])],
        compiler_directives=_DIRECTIVES,
    ),
    include_dirs=[numpy.get_include()],
    entry_points={
        'console_scripts': [
            'evosimz = evosimz.simulators:_entrypoint',
        ],
    },
    package_data={
        'utils': ['*.pxd', '*.pyx'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)
