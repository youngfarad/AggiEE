from pyparsing import *
import re

'''
Grammar for a transfer function:
(1)
transfer_function = expression (op expression)*
expression ::= expr | expr / expr 
expr ::= expr1 (op expr1)*
expr1 ::= (number*var | var | number) [exp]
exp ::= '^' number
number :: = '0' | '1' | '2' | ... | '9'
op ::= '+' | '-'
var ::= 's'

(2)

'''

class TransferFunction(object):
	def __init__(self, num, denom):
		self.t_num =  self.parse_input(num)
		self.t_denom =  self.parse_input(denom)
		
	def parse_input(self, in_str):
		'''
		badChars = [" ", ")", "("]
		str_input = "".join([char for char in str_input if char not in badChars])
		str_input = [c for c in str_input]
		digits = ['0','1','2','3','4','5','6','7','8','9']
		for (idx,char) in enumerate(str_input):
			if (char == "s" or char == "S") and idx < len(str_input)-2:
				if str_input[idx+1] in digits:
					str_input[idx] += "^1"
			elif (char == "s" or char == "S") and idx == len(str_input)-1:
					str_input[idx] += "^1"

		str_input = "".join(str_input)
		
		# work through the grammar bottom to top - tokens
		var = oneOf('s S')
		op = oneOf('+ -')
		number = oneOf(" ".join(digits))

		exponent = number
		factor = OneOrMore(number)

		### expr1 ::= (number*var | var | number) (exp) ###		
		exp = Optional(Literal('^') + exponent)

		expr1 = (factor + Optional(Literal('*')) + var) + exp

		expr = expr1 + ZeroOrMore(op + expr1)
		#ZeroOrMore(Combine(expr1 + ZeroOrMore(Combine(op+expr1)),'/'))

		expression = Group(expr) + Suppress(Literal('/')) + Group(expr)

		# transfer_function = (
		# 	Combine(expression + ZeroOrMore(Combine(op + expression)))
		# )
		#str_input = str_input.split("/")
		#return [expr.parseString(str_input.split("/")[0], expr.parseString(str_input.split("/")[1]))]
		#return [expr.parseString(s) for s in str_input]
		return expression.parseString(str_input)
		'''


		
tf = TransferFunction('2*s^3','(2*s+1)(2s+3)')
print(tf.t_func)