from setuptools import setup, find_packages

setup(
    name='esp',
    version='0.1',
    description='EEG Signal Processing Library',
    author='RPR',
    author_email='preethivhiremath.vh@gmail.com',
    url='https://github.com/preethihiremath/esp',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'mne',
        # Add any other dependencies here
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
