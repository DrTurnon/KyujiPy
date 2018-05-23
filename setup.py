from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='kyujipy',
    version='0.1.0',
    description='A Python library to convert Japanese texts from Shinjitai to Kyujitai and vice versa',
    url='https://github.com/DrTurnon/kyujipy',
    author='Emmanuel Ternon',
    author_email='emmanuel.ternon@outlook.com',
    license='MIT',
    packages=['kyujipy'],
    install_requires=[
        'cson',
    ],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
)
