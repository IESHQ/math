from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'calc',
  ext_modules = cythonize("calc.pyx"),
)