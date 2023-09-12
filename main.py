"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
  if n <= 1:
    return 1
  else:
    return a*simple_work_calc(n/b,a,b)+n

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
  if(n<=1):
    return 1
  else:
    return a*work_calc(n/b,a,b,f)+f(n)
	pass

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
  if(n<=1):
    return 1
  else:
    return a*work_calc(n/b,a,b,f)+f(n)
	pass



def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in input_sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2
  def work_fn1(n):
    return work_calc(n, 64, 2, lambda n: math.pow(n,2.0))
  def work_fn2(n):
    return work_calc(n, 64, 2, lambda n: math.pow(n,10.0))
  def work_fn3(n):
    return work_calc(n, 64, 2, lambda n: math.pow(n,6.0))
    res = compare_work(work_fn1, work_fn2)
	print(res)

def test_compare_span():
	# TODO
  def span_fn1(n):
    return span_calc(n, 64, 2, lambda n: math.pow(n,2.0))
  def span_fn2(n):
    return span_calc(n, 64, 2, lambda n: math.pow(n,10.0))
  def span_fn3(n):
    return span_calc(n, 64, 2, lambda n: math.pow(n,6.0))
  res = compare_span(span_fn1, span_fn2)
  print(res)

