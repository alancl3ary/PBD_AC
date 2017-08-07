import unittest #module allows us to do test driven development

from calculator import add, subtract, multiply, divide, factorial, square_root, power, sine, cos, tan, nCr, nPr
#test the factorial functionality
class TestCalculator(unittest.TestCase):   	#object orientated
	
	# test cases for the add fuction. compares our expected value with what we observed
	def testAdd(self):
		self.assertEqual(4, add(2,2))
		self.assertEqual(6, add(2,4))
		self.assertEqual(6, add(4,2))
		self.assertEqual(4, add(4,0))
		self.assertEqual(3, add(4,-1))
		self.assertEqual(0, add(-2,2))
		self.assertEqual(round(5/6.0,4),		
				round(add(2/4.0, 2/6.0),4))
	
	# test cases for the subtract fuction. compares our expected value with what we observed
	def testSubtract(self):
		self.assertEqual(0, subtract(2,2))
		self.assertEqual(1, subtract(3,2))
		self.assertEqual(-1, subtract(2,3))
		self.assertEqual(3, subtract(2,-1))
	
	# test cases for the multiply fuction. compares our expected value with what we observed
	def testMultiply(self):
		self.assertEqual(4, multiply(2,2))	
		self.assertEqual(-4, multiply(2,-2))
		self.assertEqual(4, multiply(-2,-2))
		self.assertEqual(0, multiply(6,0))
		self.assertEqual(8, multiply(16,.5))
	
	# test cases for the divide fuction. compares our expected value with what we observed	
	def testDivide(self):
		self.assertEqual(1, divide(2,2))
		self.assertEqual(5, divide(10,2))
		self.assertEqual(-5, divide(20,-4))
		self.assertEqual(.5, divide(3.0,6))
		self.assertEqual(1.25, divide(7.5,6.))
	
	# test cases for the factorial fuction. compares our expected value with what we observed	
	def testFactorial(self):
		self.assertEqual(120, factorial(5))
		self.assertEqual(1, factorial(0))
		self.assertEqual(1, factorial(1))
		self.assertEqual(720, factorial(6))
		self.assertEqual(3628800, factorial(10))
		# expectation vs observation 
	
	# test cases for the square root fuction. compares our expected value with what we observed
	def testSquare_root(self):
		self.assertEqual(4.0, square_root(16))
		self.assertEqual(7.0, square_root(60-11))
		self.assertEqual(3.872983346207417, square_root(15))
		self.assertEqual(8, square_root(2*32))
		self.assertEqual(4.949747468305833, square_root(24.5))
	
	# test cases for the power fuction. compares our expected value with what we observed
	def testPower(self):
		self.assertEqual(4, power(2,2))
		self.assertEqual(0.25, power(2,-2))
		self.assertEqual(4.0, power(16,.5))
		self.assertEqual(100000, power(10,5))
		self.assertEqual(0.00047018498457599973, power(.6,15))
		
	# test cases for the sine fuction. compares our expected value with what we observed
	def testSine(self):
		self.assertEqual(0.42261826174069944, sine(25))
		self.assertEqual(-0.573576436351046, sine(-35))
		self.assertEqual(1.2246467991473532e-16, sine(180))
		self.assertEqual(0.766044443118978, sine(180-50))
		self.assertEqual(0.0045203873676650415, sine(0.259))
		
	# test cases for the cos fuction. compares our expected value with what we observed
	def testCos(self):
		self.assertEqual(0.9063077870366499, cos(25))
		self.assertEqual(0.8191520442889918, cos(-35))
		self.assertEqual(-1.0, cos(180))
		self.assertEqual(-0.6427876096865394, cos(180-50))
		self.assertEqual(0.9999897829968295, cos(0.259))
	
	# test cases for the tan fuction. compares our expected value with what we observed
	def testTan(self):
		self.assertEqual(0.4663076581549986, tan(25))
		self.assertEqual(-0.7002075382097097, tan(-35))
		self.assertEqual(-1.2246467991473532e-16, tan(180))
		self.assertEqual(-1.19175359259421, tan(180-50))
		self.assertEqual(0.004520433552948983, tan(0.259))
	
	# test cases for the nCr fuction. compares our expected value with what we observed
	def testNCr(self):
		self.assertEqual(10, nCr(5,2))
		self.assertEqual(15504, nCr(20,5))
	
	# test cases for the nPr fuction. compares our expected value with what we observed
	def testNPr(self):
		self.assertEqual(20, nPr(5,2))
		self.assertEqual(1860480, nPr(20,5))
	
if __name__ == '__main__': ## tests are only run when the program is run directly from the command line
    unittest.main()