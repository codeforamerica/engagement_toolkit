"""
Tests for the utils package.
"""

import unittest
from likeminded.utils.testing import patch

import likeminded.utils.xml2dict as x2d

class Test_X2D (unittest.TestCase):
    pass

class Test_D2X (unittest.TestCase):
    
    def test_DictShouldProduceExpectedXML(self):
        pairs = [
            ({'a' : None},
             '<?xml version="1.0" encoding="UTF-8"?>\n<a />'),
            ({'a' : 5},
             '<?xml version="1.0" encoding="UTF-8"?>\n<a>5</a>'),
            ({'a' : 'x'},
             '<?xml version="1.0" encoding="UTF-8"?>\n<a><![CDATA[x]]></a>'),
            ({'a' : {'b' : [{'c' : 5}, 6, 'x', None], 'd' : 7}},
             '<?xml version="1.0" encoding="UTF-8"?>\n<a><b><c>5</c></b><b>6</b><b><![CDATA[x]]></b><b /><d>7</d></a>'),
        ]
        
        for d, x in pairs:
            self.assertEqual(x2d.dict2xml(d), x)
    
    def test_BadDicts(self):
        bad_values = [
            {'a':None,'b':None},
            {'a':[None, None]},
            {'a':[None, [None, None]]},
            {},
        ]
        bad_types = [
            [{'a':None}],
            'a',
            None,
        ]
        
        for d in bad_values:
            #print d
            self.assertRaises(ValueError, x2d.dict2xml, d)
        
        for d in bad_types:
            #print d
            self.assertRaises(TypeError, x2d.dict2xml, d)
