from typing import Mapping, Set, List, NoReturn
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums: List[int] = []
        self.numidx: Mapping[int, Set[int]] = {} #事实证明Map可以当做字典用

    def insert(self, val: int) -> int:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.nums.append(val)
        if val in self.numidx.keys():
            self.numidx[val].add(len(self.nums) - 1)
            return False
        else:
            self.numidx[val] = set()
            self.numidx[val].add(len(self.nums) - 1)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not val in self.numidx.keys():
            return False
        if len(self.numidx[val]) == 0:
            return False

        idx = self.numidx[val].pop() #得到被删除的末尾元素的idx
        self.nums[idx], self.nums[len(self.nums) - 1] = self.nums[len(self.nums) - 1], self.nums[idx]#交换被删除的元素和末尾元素
        self.numidx[self.nums[idx]].add(idx)
        self.numidx[self.nums[idx]].remove(len(self.nums) - 1)   #将最后一个元素交换的前面来，只记得加入新idx，忘了删除就idx
        self.nums.pop()#删除末尾元素
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


