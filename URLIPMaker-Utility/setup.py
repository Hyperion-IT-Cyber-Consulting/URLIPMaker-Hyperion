from setuptools import setup, find_packages

setup(
    name='IPCheckerMaker',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Any dependencies you have, e.g., 'requests'
    ],
    entry_points={
        'console_scripts': [
            'IPURLCheck:IPURLCheck:main',  # Adjust the path as necessary
        ],
    },
)