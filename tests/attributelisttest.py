#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler.AttributeList as AttributeList
import unittest

class TestAttribute(unittest.TestCase):

    def setUp(self):
        self.keyname = 'attr1'
        self.value1 = 'value1'
        self.value2 = 'value2'
        self.x = AttributeList({
            "attribute1": "attr1value1",
            "attribute2": "attr2value1",
            "attribute3": "attr3value1",
            "attribute4": None,
            "attribute5": 1,
            "attribute6": True,
            "attribute7": "attr7value1",
            "attribute8": "attr8value1",
            })
        self.x.attribute1.setquoted(True)
        self.outtest = { 
                "attribute8": {
                    'default_value': 'attr8value1', 
                    'changed': False, 
                    'quoted': False,
                    'val': 'attr8value1', 
                    'key': 'attribute8'
                }, 
                "attribute2": {
                    'default_value': 'attr2value1', 
                    'changed': False, 
                    'quoted': False,
                    'val': 'attr2value1', 
                    'key': 'attribute2'
                }, 
                "attribute3": {
                    'default_value': 'attr3value1', 
                    'changed': False, 
                    'quoted': False,
                    'val': 'attr3value1', 
                    'key': 'attribute3'
                }, 
                "attribute1": {
                    'default_value': 'attr1value1', 
                    'changed': False, 
                    'quoted': True,
                    'val': 'attr1value1', 
                    'key': 'attribute1'
                }, 
                "attribute6": {
                    'default_value': True, 
                    'changed': False, 
                    'quoted': False,
                    'val': True, 
                    'key': 'attribute6'
                }, 
                "attribute7": {
                    'default_value': 'attr7value1', 
                    'changed': False, 
                    'quoted': False,
                    'val': 'attr7value1', 
                    'key': 'attribute7'
                }, 
                "attribute4": {
                    'default_value': None, 
                    'changed': False, 
                    'quoted': False,
                    'val': None, 
                    'key': 'attribute4'
                }, 
                "attribute5": {
                    'default_value': 1, 
                    'changed': False, 
                    'quoted': False,
                    'val': 1, 
                    'key': 'attribute5'
                } 
            }

    def test_01_ObjectContent(self):
        self.assertEqual(self.x, self.outtest)

    def test_02_QueryObject(self):
        self.assertEqual(self.x.attribute1, self.outtest['attribute1'])

    def test_03_StringGeneration(self):
        self.assertEqual(str(self.x), '')

    def test_04_ModifyObject(self):
        self.x['attribute1'] = "newvalue1"
        self.x['attribute2'] = "newvalue2"
        self.x['attribute3'] = "newvalue3"
        self.x['attribute4'] = 5
        self.x['attribute5'] = 9
        self.x['attribute6'] = False
        self.x['attribute7'] = "newvalue7"
        self.x['attribute8'] = "newvalue8"
        self.assertEqual(str(self.x), '-attribute8 newvalue8 -attribute2 newvalue2 -attribute3 newvalue3 -attribute1 \"newvalue1\" -attribute6 False -attribute7 newvalue7 -attribute4 5 -attribute5 9 ')

    def test_05_AttributeError(self):
        with self.assertRaises(AttributeError) as cm:
            self.x['invalidattribute'] = 5

if __name__ == '__main__':
    unittest.main()
