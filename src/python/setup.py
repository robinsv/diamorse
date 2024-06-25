from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy

extensions = [
    Extension("*", ["*.pyx"],
        include_dirs=[numpy.get_include(), '../lib']),
]

setup(
    ext_modules=cythonize(extensions,compiler_directives={'language_level' : '3'}),
    extra_compile_args=["-g"],
    extra_link_args=["-g"]
)
