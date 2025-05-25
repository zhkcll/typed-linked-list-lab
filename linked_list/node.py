from typing import Optional, Generic, TypeVar

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.prev: Optional['Node[T]'] = None
        self.next: Optional['Node[T]'] = None
