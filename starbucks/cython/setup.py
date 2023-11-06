from setuptools           import setup
from Cython.Build         import cythonize
from setuptools.extension import Extension


extensions = [
    Extension(
        '*',
        sources=['*.pyx'],
        extra_compile_args=['-std=c++17'],
        language='c++',
    ),

  #  Extension(
  #       'damtest',
  #       sources=['damtest.pyx'],
  #       extra_compile_args=['-std=c++11'],
  #       language='c++',
  #   ),

  #   Extension(
  #       'tensor',
  #       sources=['tensor.pyx'],
  #       extra_compile_args=['-std=c++11'],
  #       language='c++',
  #   ),
]

setup(
    ext_modules=cythonize(extensions),
)

