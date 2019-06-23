from setuptools import setup

setup(
    name='di',
    packages=['di'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-mysql',
        'flask-bcrypt'
    ],
)
