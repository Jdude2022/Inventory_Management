"""Main interface for the created items.

Author: John Jalali JJalali@ksu.edu
Version: 0.1
TODO: Tentative Feels like a lot of abstract methods.
"""
from abc import ABC, abstractmethod
from typing import List


class Item(ABC):
    """Impliments getters for shared class attribues."""
    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        """Checks class and subclass"""
        if cls is Item:
            callables: List[str] = ["name", "stock_num", "qty", "locaiton",
                                   "priority", "cost", "restock_estimate"]
            ret = True
            for call in callables:
                ret = ret and (hasattr(subclass, call) and 
                               callable(getattr(subclass, call)))
            return ret
        else:
            return NotImplemented

    @property
    @abstractmethod
    def name(self) -> str:
        """Getter for Name."""
        raise NotImplementedError

    @property
    @abstractmethod
    def stock_num(self) -> str:
        """Getter for stock number."""
        raise NotImplementedError

    @property
    @abstractmethod
    def quantity(self) -> str:
        """Getter for quantity."""
        raise NotImplementedError

    @property
    @abstractmethod
    def location(self) -> str:
        """Getter for location."""
        raise NotImplementedError

    @property
    @abstractmethod
    def priority(self) -> str:
        """Getter for priority."""
        raise NotImplementedError

    @property
    @abstractmethod
    def cost(self) -> str:
        """Getter for cost."""
        raise NotImplementedError

    @property
    @abstractmethod
    def restock_estimate(self) -> str:
        """Getter for restock estimate."""
        raise NotImplementedError
