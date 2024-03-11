from setuptools import setup , find_packages

setup(
    name='packageSensitiveInfo',
    version='1.0.0',
    author='Simran',
    author_email='simran.saxena@dataverze.ai',
    description='It contains data and regex patterns in 2 separate files. My package validates how many regex patterns matches the data.',
    packages=find_packages(),
    #namespace_packages=['packageSensitiveInfo'],
    #package_dir={'packageSensitiveInfo': 'src'},
    install_requires=[
        'black==24.2.0',
        'pytest==8.0.2',
        'setuptools==59.6.0',
        'wheel==0.42.0',
        'twine==5.0.0',
    ],
    package_data={'packageSensitiveInfo': ['data/*.txt', 'logs/*', 'tests/*.py']},
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    
)