from distutils.core import setup

setup(
    name="likeminded",
    description="A wrapper for the LikeMinded REST API",
    version="0.1",
    packages=['likeminded','likeminded.utils','likeminded.utils.xml2dict'],
    
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
