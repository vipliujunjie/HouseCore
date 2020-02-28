import time
from collections import Iterable
from collections import Iterator

"""
什么是迭代器：
	一个对象里面包含 __iter__  和  __next__
"""

# 如果一个对象是迭代器，那么它一定可以迭代
# 如果一个东西可以迭代，它不一定是一个迭代器
class Classmate(object):
	def __init__(self):
		self.names = list()
		self.current_num = 0

	def add(self, name):
		self.names.append(name)

	def __iter__(self):
		"""如果想要一个对象成为 可以迭代的对象，可以使用for，那么必须实现__iter__方法"""
		return self 

	def __next__(self):
		if self.current_num < len(self.names):
			ret = self.names[self.current_num]
			self.current_num += 1
			return ret
		else:
			raise StopIteration  # for循环检测到返回 StopIteration 就会自动停止循环


classmate = Classmate()
classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

# print("判断classmate是否是可以迭代的对象", isinstance(classmate, Iterable))
# classmate_iterator = iter(classmate)
# print("判断classmate是否是迭代器", isinstance(classmate_iterator, Iterable))

# print(next(classmate_iterator))

# 判断一个对象是否是可迭代对象必须满足 1.有__iter__方法	
#__iter__方法返回哪个对象，就调用哪个对象里面的__next__方法
for name in classmate:
	# if not name:
	#	break
	print(name)
	time.sleep(1)
	
