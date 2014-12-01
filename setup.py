__author__ = 'rizki'

from distutils.core import setup

setup(
    name='AngularSide',
    version='0.0.2',
    author='Iskandar Rizki',
    author_email='iskandar.rizki@gmail.com',
    packages=['aside'],
    scripts=[],
    package_data = {'aside' : ["aside/js/*"] },
    url='git+https://github.com/rizki96/angular-side.git',
    license='LICENSE.txt',
    description='pyside and angular js connector',
    long_description=open('README.md').read(),
    #install_requires=[
    #    "git+https://github.com/PureMVC/puremvc-python-multicore-framework.git",
    #],
)