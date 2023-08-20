
# Creational Pattern Factory used in this


# this Creator method does not need an interface implementation
# this is fixed for all the types of cache
class Storage:

    def __init__(self, capacity:int):
        # predecided capacity of cache
        self.capacity = capacity
        # hashmap is used -> to store elements in the cache
        self.storage_dict = {}


    def add(self, key: str, value: str):
        if(self.is_storage_full()){
            print("storage is full")
        }
        self.storage_dict[key] = value
    

    def remove(self, key: str):
        if(key not in self.storage_dict):
            print(f"{key} not present in the cache")
        # pop method is used to remove -> element from the dictionary
        self.storage_dict.pop(key)
    

    def get(self, key: str):
        if(key not in self.storage_dict):
            print(f"{key} not present in the cache")
        
        return self.storage_dict[key]
    

    def is_storage_full(self):
        if(storage_dict.size() == self.capacity){
            return true
        }else {
            return false
        }


# not implementing all the methods
# in LLD coding -> only the class structure and imp methods -> are necessary
# other simple methods are not necessary to be implemented
# simply put the method definition -> and call the method

class DLL:

    def __init__(self):
        self.dll_node = DLLNode()
    
    def detach_node(self, node: DLLNode, pos):
        # remove the node
        pass

    def attach_node_at_tail_prev(self, node: DLLNode):
        # For better implementation codewise
        # make dummy head and tail nodes
        # add the node before dummy tail
        pass

    def move_head(self):
        pass

    def get_current_head_next(self):
        # For better implementation codewise
        # make dummy head and tail nodes
        # remove the node which is next node of dummy head
        pass



class DLLNode:

    def __init__(self):
        pass

from abc import ABC, abstractmethod

# abstract class of eviction policy
# this class extended -> to create various eviction policies 

# Creator Interface (Factory Design Pattern)
class IEvictionPolicy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def key_accessed(self, key: str):
        pass

    @abstractmethod
    def evict_key(self):
        pass


# Concrete Creator -> Implementation of Creator Interface
class LRUEvictionPolicy(IEvictionPolicy):
    def __init__(self):
        # cache elements are stored in the hashmap that we have built earlier in the storage class
        # now when we want to remove elements from cache -> which element to remove
        # that strategy is impelmented via Doubly LinkList in the LRU Eviction policy

        self.dll = DLL()
        self.dll_node = DLLNode()

        # {key: DLLNode}
        # address mapper of each node
        # DLLNode object contains address of the node
        # this is made so that -> position of a node -> can be found in O(1) time
        # no need to traverse and search for the node

        self.pos_mapper = {}
    
    def key_accessed(self, key: str):
        """
        Why Key accessed is the part of eviction policy ?
        Possible Ans ->
        Eviction Policy is concerned with -> which key to evict
        Based on Key access in Some Eviction Policy -> order of elements in cache can change
        That directly impacts the eviction policy -> that is which key to be evicted

        So whenever a key is accessed -> in some eviction policies -> order of elements needs
        to be changed.
        This is the reason key accessed is also a part of Eviction Policy.


        Check if key is present in the pos mapper or not
        Case 1:- 
        If key is present in the pos mapper => node is already present
        Detach node from current pos. 
        Attach node at the end. Make it Tail Node

        Case 2:- 
        => key is not present in the doubly link List and the POS mapper
        => Key must be getting stored in the hashmap
        => But key might not have been accessed till now so its position is not present
        in POS mapper and Doubly Link List
        => So when key accessed -> it is stored in doubly linklist and position mapper

        If key is not present in the pos mapper => node is not present in Doubly LinkList
        Create a new node in the Doubly LinkList
        Put the {key:DLLNode} in the mapper.
        Attach the node at the end.

        """

        if key in self.pos_mapper:
            # detach from the current position
            self.dll.detach_node(key)
        elif key not in self.pos_mapper:
            # check if the current size allows addition or need to evict a key

            # Doubt in this ??
            # there should be also be a code to store the key in the hashmap created in Storage class
            # by checking its size here
            # Because when a key value pair stored in the cache then also it is accessed


            new_node = DLLNode()
            self.pos_mapper[key] = new_node

        # attach node -> at the end in doubly link list

        self.dll.attach_node_at_tail_prev(self.pos_mapper[key])
    
    def evict_key(self):
        """
        Remove key at head from the mapper
        Move head
        """
        key = self.dll.get_current_head_next()
        # remove the key from the POS mapper
        pos_mapper.pop(key)

        # self.dll.move_head()
        
        # same doubt as above
        # should we not remove the cache element from the hashmap created in the storage class
        


# yes, we can use queue time implement fifo.
#  
# Its just that we were already using Linkedlist methods, and building a queue would mean extra piece of code. 

# Thirdly, if you see, queue is buillt via linked list or array only internally. And thats what we are doing

# Concrete Creator -> Implementation of Creator Interface
class FIFOEvictionPolicy(IEvictionPolicy):
    """
    First in first Out eviction policy
    """
    def __init__(self):
        self.dll = DLL()
        self.dll_node = DLLNode()
        # {key: DLLNode}
        # address mapper of each node
        # DLLNode object contains address of the node
        self.pos_mapper = {}
    
    def key_accessed(self, key: str):
        # no extra logic needed to move element when key accessed
        # based on the key accessed -> we need not change its order 
        # as per the fifo eviction policy
        return

    def evict_key(self):
        # first in first out -> first data that is accessed needs to be removed
        key = self.dll.get_current_head()
        pos_mapper.pop(key)
        self.dll.move_head()



