#!/usr/bin/python

import sys
sys.path.append('../')
import NetScaler.Attribute as Attribute
import unittest

class TestAttribute(unittest.TestCase):

    def setUp(self):
        self.keyname = 'attr1'
        self.value1 = 'value1'
        self.value2 = 'value2'
        self.x = Attribute(self.keyname, self.value1)
        self.x.setquoted(True)

    def test_01_ObjectContent(self):
        self.assertEqual(self.x, 
            {
                'default_value': self.value1,
                'changed': False,
                'quoted': True,
                'key': self.keyname,
                'val': self.value1
            })

    def test_02_StringGeneration(self):
        self.assertEqual(str(self.x), '')

    def test_03_ChangedStringGeneration(self):
        self.x.val = self.value2
        self.assertEqual(str(self.x), "-{} \"{}\" ".format(self.keyname, self.value2))

    def test_04_ChangedObject(self):
        self.x.val = self.value2
        self.assertEqual(self.x, 
            {
                'default_value': self.value1,
                'changed': True,
                'quoted': True,
                'key': self.keyname,
                'val': self.value2
            })

if __name__ == '__main__':
    unittest.main()