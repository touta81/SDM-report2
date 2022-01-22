#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (-1, calc(-1,50))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0.3,50))

        def test_sample3 (self):
                self.assertEqual (2000,calc(40,50))

        def test_sample4 (self):
                self.assertEqual (2500,calc(50,50))

        def test_sample5 (self):
                self.assertEqual (3000,calc(60,50))

        def test_sample6 (self):
                self.assertEqual (-1,calc(10.5,50))

        def test_sample7 (self):
                self.assertEqual (-1,calc(999.9,50))
        
        def test_sample8 (self):
                self.assertEqual (-1,calc(1000,50))
