#!/usr/bin/env python
# encoding: utf-8

import unittest
import envoy

class SimpleTest(unittest.TestCase):

    def testInput(self):
        r = envoy.run("sed s/i/I/g", "Hi")
        self.assertEqual(r.std_out, "HI")
        self.assertEqual(r.status_code, 0)

    def testPipe(self):
        r = envoy.run("echo -n 'hi'| tr [:lower:] [:upper:]")
        self.assertEqual(r.std_out, "HI")
        self.assertEqual(r.status_code, 0)

    def testTimeout(self):
        r = envoy.run("yes | head", timeout=1)
        self.assertEqual(r.std_out, "y\ny\ny\ny\ny\ny\ny\ny\ny\ny\n")
        self.assertEqual(r.status_code, 0)

    def test_quoted_args(self):
        sentinel = 'quoted_args' * 3
        r = envoy.run("python -c 'print \"%s\"'" % sentinel)
        self.assertEqual(r.std_out.rstrip(), sentinel)
        self.assertEqual(r.status_code, 0)

if __name__ == '__main__':
    unittest.main()


