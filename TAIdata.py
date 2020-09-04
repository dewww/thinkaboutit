from dataclasses import dataclass,field,asdict
from typing import List
import random

@dataclass(order=True)
class Symbol:
    '''Class for tracking each symbol'''
    name: str
    relationship_id: int = field(init=False)

    def __post_init__(self):
        self.relationship_id = random.randint(100000, 999999)

@dataclass(unsafe_hash=True)
class SymbolList:
    '''Class for tracking every symbol we've seen so far'''
    mylist: List[str] = field(default_factory=list)

@dataclass(frozen=True)
class InputStr:
    value: str

@dataclass(frozen=True)
class Fact:
    subject: str
    verb: str
    object: str
    context: str

if __name__ == '__main__':
    s = Symbol('a')
    assert asdict(s) == {'name': 'a'}
    print(s)
    sl = SymbolList(s)
    print(sl)
    i = InputStr('a red fox jumped over a brown dog')
    assert asdict(i) == {'value': 'a red fox jumped over a brown dog'}
    print(i)
    f = Fact('a red fox','jumped over','a brown dog','test')
    print(f)
