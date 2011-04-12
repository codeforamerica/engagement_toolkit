"""
xml2dict
Thunder Chen<nkchenz@gmail.com> 2007.9.1

Convert an XML string or file with XML data to a dict object.
http://code.google.com/p/xml2dict/
"""

from .xml2dict import XML2Dict

def xml2dict(data):
    converter = XML2Dict()
    
    if hasattr(data, 'read'):
        data = data.read()
    
    return converter.fromstring(data)
