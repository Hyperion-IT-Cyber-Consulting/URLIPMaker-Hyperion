from setuptools import setup, find_packages

setup(
    name='URLIPMAKER-Util',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Any dependencies you have, e.g., 'requests'
    ],
    entry_points={
        'console_scripts': [
            'URLIPMaker-Util:URLIPMaker-Util:main',  # Adjust the path as necessary
        ],
    },
)