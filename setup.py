from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='EllipsePy',
    version='0.0.3',
    author='Lalith Uriti',
    author_email='lalithuriti@gmail.com',
    description='Orbital Mechanics Data Analysis Package',
    long_description='''<!-- EllipsePy | Lalith Uriti 2021 -->

<p align="center"><img src="https://raw.githubusercontent.com/lalithu/EllipsePy/main/images/orbit.png"></p>

<h1 align="center">EllipsePy</h1>

<h3 align="center">
Orbital Mechanics Data Visualization and Analysis Library
</h3>

<p align="center">

<a href="https://github.com/r-spacex/SpaceX-API/releases">
<img src="https://img.shields.io/github/contributors/lalithu/EllipsePy?style=flat-square">
</a>

<a href="https://en.wikipedia.org/wiki/Representational_state_transfer">
<img src="https://img.shields.io/github/issues/lalithu/EllipsePy?style=flat-square">
</a>

<a href="https://hub.docker.com/r/jakewmeyer/spacex-api/">
<img src="https://img.shields.io/github/v/release/lalithu/EllipsePy?style=flat-square">
</a>

<a href="https://github.com/r-spacex/SpaceX-API/actions?query=workflow%3ATest">
<img src="https://img.shields.io/github/license/lalithu/EllipsePy?style=flat-square">
</a>

</p>

<h3 align="center">

<a href="https://github.com/lalithu/EllipsePy">V1 Docs</a> - <a href="https://pypi.org/project/EllipsePy">PyPI</a> - <a href="https://github.com/lalithu/EllipsePy/issues">Status</a>
<br/>

</h3>

## Installation

```sh
pip install EllipsePy
```

## Requirements

- NumPy

  ```sh
  pip install numpy
  ```

- SciPy

  ```sh
  pip install scipy
  ```

- Plotly
  ```sh
  pip install plotly
  ```

## Examples

_For more examples, please refer to the [Documentation](https://github.com/lalithu/EllipsePy)_

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Lalith U - [@BlueUnveiling](https://twitter.com/BlueUnveiling) - lalithuriti@gmail.com

Project Links:

- PyPI: [https://github.com/lalithu/EllipsePy-Testing](https://pypi.org/project/EllipsePy/)
- Github: [https://github.com/lalithu/EllipsePy-Testing](https://github.com/lalithu/EllipsePy)
''',
    long_description_content_type='text/markdown',
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
