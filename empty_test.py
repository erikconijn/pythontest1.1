'''
Created on Oct 8, 2018

@author: exc06
'''
import unittest


class Test(unittest.TestCase):


	def setUp(self):
		pass


	def tearDown(self):
		pass

	def do_something(self):
		print ('something')


	def test_01(self):
		print 'Doing'
		
		raise Exception("Something went wrong")
		print "Done"
		pass


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_01']
	unittest.main()