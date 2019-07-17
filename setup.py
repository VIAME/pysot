from setuptools import find_packages, setup

from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        name='toolkit.utils.region',
        sources=[
            'toolkit/utils/region.pyx',
            'toolkit/utils/src/region.c',
        ],
        include_dirs=[
            'toolkit/utils/src'
        ]
    )
]

setup(
    name='pysot',
    package_data={'vot_iter': ['tracker_SiamRPNpp.m']},
    packages=find_packages(exclude=('demo', 'experiments', 'testing_dataset',
                                    'training_dataset')),
    ext_modules=cythonize(ext_modules),
    install_requires=['pyyaml', 'yacs', 'tqdm',
                      'colorama', 'matplotlib',
                      'cython', 'tensorboardX']
)
