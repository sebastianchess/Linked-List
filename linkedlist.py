from __future__ import annotations
from typing import TypeVar
from dataclasses import dataclass, field


@dataclass
class Node[T]:
    value: T
    next_: Node[T] | None = field(init=False, default=None)


class LinkedList[T]:

    head: Node[T] | None 

    def __init__(self, *initial: T) -> None:
        if not initial: 
            self.head = None
            return 
        
        self.head = Node(initial[0])
        current = self.head 

        for v in initial[1:]:
            current.next_ = Node(v) 
            current = current.next_ 
    
    def append(self, element: T) -> None:
        """Appends an element to the linked List"""
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
            return

        current = self.head 

        while current.next_ is not None: 
            current = current.next_

        current.next_ = new_node

    def display(self) -> None: 
        current = self.head 

        while current is not None:
            print(current.value, end=", ")
            current = current.next_
        
        print("None") # last value
    
    def reverse(self) -> None:
        """It reverses a linked list iteratively"""
        new_llist = None 
        current = self.head 
        
        while current is not None: 
            next_node = current.next_
            current.next_ = new_llist
            new_llist = current 
            current = next_node
        
        self.head = new_llist

    def delete_element(self, element: T) -> None: 
        """Deletes an element from the llist by the element itself"""
        prev = None 
        current = self.head 

        while current is not None: 
            if current.value == element:
                if prev is None:
                    self.head = current.next_
                    return 
                
                prev.next_ = current.next_
                return 

            prev = current 
            current = current.next_

    def __getitem__(self, i: int) -> T | None: 
        counter = 0 

        current = self.head 

        while current is not None:
            if counter == i: 
                return current.value 
            counter += 1
            current = current.next_ 
        
        return None 
