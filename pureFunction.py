import sm

class PureFunciton(sm.SM):
	def __init__(self, f):
		self.f = (f)

	def getNextValues(self, state, inp):
		return (state, self.f(inp))

if __name__=="__main__":
	sm = PureFunciton(lambda x:2 * x)
	print(sm.transduce([2, 3, 4, 5]))