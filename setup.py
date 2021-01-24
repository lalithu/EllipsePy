from setuptools import setup, find_packages

setup(
    name='EllipsePy',
    version='0.0.1',
    author='Lalith U.',
    author_email='lalithuriti@gmail.com',
    description='Orbital Mechanics Data Analysis Package',
    packages=find_packages(),
    install_requires=['numpy', 'plotly', 'scipy'],
    keywords=['python', 'Orbital Mechanics', 'EllipsePy'],
    classifiers=[
        "Development Status :: Early Stages",
        "Intended Audience :: Education & Research",
        "Programming Language :: Python :: 3",
    ]
)
