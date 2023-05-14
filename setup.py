from setuptools import setup, find_packages

setup(
    name='brainsurf',
    version='0.0.2',
    description='EEG Signal Processing Library',
    author='preethivhiremath',
    author_email='preethivhiremath.vh@gmail.com',
    url='https://github.com/preethihiremath/brainsurf',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'mne',
        'nolds'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
)
