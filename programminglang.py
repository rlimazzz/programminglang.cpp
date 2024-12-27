import sys

class Evaluate:
	def evaluate(self, s):
		lines = [x for x in s.split('\n') if x.strip() != ""]
		
		for line in lines: 
			print(self.evaluate_expression(line))

	def evaluate_expression(self, s):
		tokens = s.split()
		print(tokens)
		stack = []
		
		for token in tokens: 
			if token.isdigit():
				stack.append(int(token))
				
			elif token == '+':
				rightop = stack.pop()
				leftop = stack.pop()
				stack.append(rightop + leftop)
				
			elif token == '-':
				rightop = stack.pop()
				leftop = stack.pop()
				stack.append(rightop - leftop)
				
			elif token == '*':
				rightop = stack.pop()
				leftop = stack.pop()
				stack.append(rightop * leftop)
				
			elif token == '/':
				rightop = stack.pop()
				leftop = stack.pop()
				stack.append(rightop / leftop)
			
		return stack[0]
	
Evaluate().evaluate(open(sys.argv[1]).read())
