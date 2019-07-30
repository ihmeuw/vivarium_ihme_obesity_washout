#!/usr/bin/env python
import os

from setuptools import setup, find_packages

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    src_dir = os.path.join(base_dir, "src")

    about = {}
    with open(os.path.join(src_dir, "vivarium_ihme_obesity_washout", "__about__.py")) as f:
        exec(f.read(), about)

    with open(os.path.join(base_dir, "README.rst")) as f:
        long_description = f.read()

    install_requirements = [
        'vivarium==0.8.22',
        'vivarium_public_health==0.9.18',
        'vivarium_cluster_tools==1.0.14',
        'vivarium_inputs[data]==3.0.1',
        'vivarium_gbd_access==2.0.4', # we need direct access to this for artifact builder

        # These are pinned for internal dependencies on IHME libraries
        'numpy<=1.15.4',
        'tables<=3.4.0',

        'pandas',
        'scipy',
        'matplotlib',
        'seaborn',
        'jupyter',
        'jupyterlab',
        'pytest',
        'pytest-mock',
        'click',
        'pyyaml',
    ]

    setup(
        name=about['__title__'],
        version=about['__version__'],

        description=about['__summary__'],
        long_description=long_description,
        license=about['__license__'],
        url=about["__uri__"],

        author=about["__author__"],
        author_email=about["__email__"],

        package_dir={'': 'src'},
        packages=find_packages(where='src'),
        include_package_data=True,

        install_requires=install_requirements,

        entry_points='''
            [console_scripts]
            build_washout_artifact=vivarium_ihme_obesity_washout.tools.cli:build_washout_artifact
        ''',

        zip_safe=False,
    )
