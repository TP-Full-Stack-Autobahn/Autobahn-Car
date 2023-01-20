from setuptools import setup, find_packages
  
setup(
    name='flaskapi',
    version='0.1',
    url='https://github.com/TP-Full-Stack-Autobahn/Autobahn-Car',
    description='Autobahn-Car service api',
    packages=find_packages(include=['src', 'src.*']),
    install_requires=[
        'flask',
        'flask-migrate',
        'python-dotenv',
        'flask-sqlalchemy',
        'pymysql'
    ],
)