from setuptools import find_packages, setup

from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        name='pysot.toolkit.utils.region',
        sources=[
            'pysot/toolkit/utils/region.pyx',
            'pysot/toolkit/utils/src/region.c',
        ],
        include_dirs=[
            'pysot/toolkit/utils/src'
        ]
    )
]

setup(
    name='pysot',
    package_data={'pysot/vot_iter': ['tracker_SiamRPNpp.m']},
    packages=find_packages(exclude=('pysot/demo', 'pysot/experiments', 'pysot/testing_dataset',
                                    'pysot/training_dataset')),
    ext_modules=cythonize(ext_modules),
    install_requires=['pyyaml', 'yacs', 'tqdm',
                      'colorama', 'matplotlib',
                      'cython', 'tensorboardX']
)
