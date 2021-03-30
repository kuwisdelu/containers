
import unittest

# import test modules

from containers.tests import test_llist
from containers.tests import test_htable
from containers.tests import test_bstree

# initialize test suite

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite

suite.addTest(loader.loadTestsFromModule(test_llist))
suite.addTest(loader.loadTestsFromModule(test_htable))
suite.addTest(loader.loadTestsFromModule(test_bstree))

# initialize a test runner and run the test suite

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
