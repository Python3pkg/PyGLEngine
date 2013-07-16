from setuptools import setup, find_packages

import GameEngine

setup( 
    name='PyGLEngine',
    version=GameEngine.__version__,
    author='Kyle Rockman',
    author_email='kyle.rockman@mac.com',
	install_requires=['numpy==1.7.1','pyglet==1.1.4','pymunk==3.0.0'],
    packages = find_packages(),
    package_data = {
        # If any subfolder contains these extensions, include them:
        '': ['*.json',],
        },
    zip_safe=False,
    url='https://github.com/rocktavious/PyGLEngine',
    license=open('LICENSE.txt').read(),
    description='Python Based OpenGL Game Engine',
    long_description=open('README.txt').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing',
    ],
)