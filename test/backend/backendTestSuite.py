import unittest

# import backend test modules
from test.backend import Test_PointCloudReader

#initialize the test suit
loader = unittest.TestLoader()
suite = unittest.TestSuite()

#add test to the test suite
suite.addTest(loader.loadTestsFromModule(Test_PointCloudReader))

#initialize a runner, pass it your suit and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)