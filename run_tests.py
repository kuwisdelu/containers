
import unittest

# import test modules

from containers.tests import test_LinkedList
from containers.tests import test_HashMap
from containers.tests import test_TreeMap

# initialize test suite

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite

suite.addTest(loader.loadTestsFromModule(test_LinkedList))
suite.addTest(loader.loadTestsFromModule(test_HashMap))
suite.addTest(loader.loadTestsFromModule(test_TreeMap))

# initialize a test runner and run the test suite

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
