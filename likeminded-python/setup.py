from distutils.core import setup

setup(
    name="likeminded",
    description="A wrapper for the LikeMinded REST API",
    version="0.2.0",
    packages=['likeminded','likeminded.utils','likeminded.utils.xml2dict'],
    install_requires=['httplib2==0.6.0'],
    
    author="Mjumbe Poe, Code for America",
    author_email="mjumbe@codeforamerica.org",
    
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)
