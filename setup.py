try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(name='utilvolc',
      version='1.0.0',
      url='https://github.com/aring1988/utilvolc',
      license='MIT',
      include_package_data=True,
      author='Allison M. Ring',
      author_email='Allison.Ring@noaa.gov',
      maintainer='Allison Ring',
      maintainer_email='Allison.Ring@noaa.gov',
      packages=find_packages(),
      package_data={
          '': [
              'data/*.txt', 'data/*.dat', 'data/*.hdf', 'data/*.ncf',
              'data/*.jpg', 'data/*.png'
          ]
      },
      keywords=[
          'volcano', 'volcat', 'hysplit',
          'evaluation'
      ],
      description='Utilities for use with VOLCAT and HYSPLIT',
      install_requires=[
          'pandas', 'xarray', 'numpy', 'matplotlib',
          'cartopy', 'scipy', 'lxml', 'datetime', 'monetio'
      ])
