from dataclasses import dataclass,field,asdict
from typing import List, Set
import random

@dataclass(order=True)
class Symbol:
	'''Class for tracking each symbol'''
	nameStr: str
	relationshipInt: int = field(init=False)
	
	def __post_init__(self):
		self.relationshipInt = random.randint(100000, 999999)
		
@dataclass(unsafe_hash=True)
class SymbolList:
	'''Class for tracking every symbol we've seen so far'''
	symbolList: Set[str] = field(default_factory=list)
	
@dataclass(frozen=True)
class InputStr:
	valueStr: str
	
@dataclass(unsafe_hash=True)
class InputStrList:
	'''Class for tracking every symbol we've seen so far'''
	InputStrList: Set[str] = field(default_factory=list)

@dataclass(frozen=True)
class Fact:
	subjectStr: str
	verbStr: str
	objectStr: str
	contextStr: str
	
if __name__ == '__main__':
	s = Symbol('a')
	assert asdict(s) == {'nameStr': 'a','relationshipInt': s.relationshipInt}
	print(s)
	s2 = Symbol('b')
	sl = SymbolList([s,s2])
	print(sl)
	i = InputStr('a red fox jumped over a brown dog')
	i = InputStr('fox jumped over dog')
	# assert asdict(i) == {'value': 'a red fox jumped over a brown dog'}
	print(i)
	isl = InputStrList([i])
	print(isl)
	f = Fact('a red fox','jumped over','a brown dog','test')
	print(f)

