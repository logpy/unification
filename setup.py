from os.path import exists
from setuptools import setup

setup(name='unification',
      version='0.3.1',
      description='Unification algorithm',
      url='http://github.com/logpy/logpy',
      author='Matthew Rocklin',
      author_email='mrocklin@gmail.com',
      license='BSD',
      packages=['unification'],
      install_requires=[],
      tests_require=[
          'pytest',
      ],
      long_description=open('README.rst').read() if exists("README.rst") else "",
      long_description_content_type="text/x-rst",
      zip_safe=False,
      classifiers=["Development Status :: 5 - Production/Stable",
                   "License :: OSI Approved :: BSD License",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: Implementation :: CPython",
                   "Programming Language :: Python :: Implementation :: PyPy",
      ],
)
