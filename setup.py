from setuptools import setup, find_packages

setup(
    name='arduino_translator',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'arduino-translate=arduino_translator.cli:main',
        ],
    },
    install_requires=[],
    author='Francisco Iago Lira Passos',
    description='A translator for custom Arduino language to Arduino code.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seu_usuario/arduino_translator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
