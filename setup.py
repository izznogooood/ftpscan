from setuptools import setup


# noinspection PyBroadException
def get_long_description():
    try:
        with open('README.md', 'r') as f:
            return f.read()
    except:
        return ''


setup(
    name='ftpscan',
    version='1.0',
    url='https://github.com/izznogooood/ftpscan',
    license='MIT',
    author='Anders Magnus Andersen',
    author_email='ama @ getmail.no',
    description='Simple scanner to discover ftp servers with provided default username / password.',
    long_description=get_long_description(),
    py_modules=['ftpscan'],
    entry_points={
        'console_scripts': [
            'ftpscan = ftpscan:main'
        ]
    },
)
