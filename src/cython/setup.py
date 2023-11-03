from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension


extensions = [
    Extension(
        "ctensor",
        sources=["tensor.pyx"],
    ),
]

setup(
    ext_modules=cythonize(extensions)
)
