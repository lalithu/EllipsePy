from setuptools import setup, find_packages

setup(
    name='EllipsePy',
    version='0.0.1',
    author='Lalith U.',
    author_email='lalithuriti@gmail.com',
    description='Orbital Mechanics Data Analysis Package',
    url="https://github.com/lalithu/EllipsePy",
    packages=find_packages(),
    install_requires=['numpy', 'plotly', 'scipy'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Astronomy"
    ]
)
