from setuptools import setup

setup(
    name='di',
    packages=['di'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pyodbc',
        'flask-bcrypt'
    ],
)
