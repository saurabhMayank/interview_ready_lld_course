
# Creational Pattern =>  Factory used in this Question


# storage is fixed for all types of cache
# dont need a factory pattern implementation for this
class Storage:

    def __init__(self, capacity:int):
        # predecided capacity of cache
        self.capacity = capacity
        # hashmap is used -> to store elements in the cache
        self.storage_dict = {}


    def add(self, key: str, value: str):
        if(self.is_storage_full()):
            print("storage is full")
        
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
        if(self.storage_dict.size() == self.capacity):
            return True
        else:
            return False
        


# not implementing all the methods
# in LLD coding -> only the class structure and imp methods -> are necessary
# other simple methods are not necessary to be implemented
# simply put the method definition -> and call the method

class DLL:
    def __init__(self):
        self.head = DLLNode(-1,-1)
        self.tail = DLLNode(-1, -1)


    
    def detach_node(self, node):
        # remove the node
        # the node will be remove from next of head
        node.next.prev = node.prev
        node.prev.next = node.next

    def attach_node_at_tail_prev(self, node):
        # For better implementation codewise
        # make dummy head and tail nodes
        # add the node before dummy tail
        tail_prev_node = self.tail.prev

        tail_prev_node.next = node
        node.next = self.tail

        self.tail.prev = node
        node.prev = tail_prev_node


    
    # for better implementation code wise
    # making head dummy node and putting the Least Recently Used
    # at the next of head -> Dummy node concept helps to avoid unknown errors
    def move_head(self):
        pass

    def get_current_head_next(self):
        # For better implementation codewise
        # make dummy head and tail nodes
        # remove the node which is next node of dummy head
        node = self.head.next
        return node



class DLLNode:
    """
    Class representing the Doubly linklist node
    DLL Node takes both key and value 
    """
    def __init__(self, key: str, val: str):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None



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
        # cache elements are stored in the hashmap that we have built earlier in the 
        # storage class
        # now when we want to remove elements from cache -> which element to remove
        # that strategy is impelmented via Doubly LinkList in the LRU Eviction policy

        self.dll = DLL()
        self.dll_node = DLLNode()

        # {key: DLLNodePointer}
        # address mapper of each node -> reference to each node mapped with key
        # DLLNodePointer object contains pointer of the node
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
            # (In the cache class -> key already put in hashmap of storage class -> 
            # then `key_accessed` function is called)
            # So this doubt is almost clear

            # there should be also be a code to store the key in the hashmap created in Storage class
            # by checking its size here
            # If key is not present in the cache and we are storing it in the DLL which is implemented
            # for the eviction policy -> should new node key and value -> stored in Hashmap of storage class


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
        self.pos_mapper.pop(key)

        # self.dll.move_head()
        
        # same doubt as above
        # should we not remove the cache element from the hashmap 
        # created in the storage class
        


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
        # the node will be inserted in the head and after that
        key = self.dll.get_current_head_next()
        # remove the key from the pos mapper as it is no longer in the DLL
        # so no need to store its address
        self.pos_mapper.pop(key)
        # For better implementation -> head and tail are made as dummy node
        # the head next node will have the first node
        # self.dll.move_head()



class EvictionPolicyFactory:
    def __init__(self):
        pass
    

    def get_eviction_policy(self, policy_val: str):
        if policy_val == "lru":
            return LRUEvictionPolicy()
        elif policy_val == "fifo":
            return FIFOEvictionPolicy()
        else:
            # if no policy val corresponding to exisiting policies
            # provided
            return None


# main class of cache
class Cache:
    """
    Main Cache class. 
    Cache has 2 components
    i) Storage -> Hashmap to store the values of cache
    ii) EvictionPolicyImplementation -> Eviction Policy for cache

    Cache does 2 operations
    i) Put {key, value} in the cache
    ii) Retrieve value based on key from the cache
    """

    def __init__(self, eviction_policy: IEvictionPolicy, storage: Storage):
        self.eviction_policy = eviction_policy
        self.storage = storage
    
    # need to put values in the cache
    def put(self, key: str, val: str):
        """
        Putting {key, value} in cache
        i) First check if cache is full or not -> yes then evict key from cache
        ii) Add key in storage
        iii) call the key accessed function as when node is stored 
        then also it is accessed
        """
        # first check if the storage of the cache is full or not
        if(self.storage.is_storage_full()):
            # evict a key from the Cache using eviction_policy
            self.eviction_policy.evict_key()
            # DOUBT HERE
            # once the evict key is called -> node must be evicted from
            # the DLL
            # That node exists in the Storage Hashmap
            # Shouldn't it be removed from there also
        
        # add the node in the storage class hashamp
        self.storage.add(key, val)

        # when a value is put then also it is accessed
        # change the order of keys takes place in 
        # EvictionPolicy Datastructure using
        # key_accessed function
        self.eviction_policy.key_accessed(key)

    
    def get(self, key: str):
        """Get value for a corresponding key from the cache

        Args:
            key (str): _description_
        """
        value = self.storage.get(key)
        # when a value is get then also it is accessed
        self.eviction_policy.key_accessed(key)
        return value



# main block of python
if __name__ == "__main__":
    print("Ye hain main block, yahaan execution hoga")
    print("\n")
    eviction_policy_factory = EvictionPolicyFactory()
    eviction_policy = eviction_policy_factory.get_eviction_policy("lru")
    storage_obj = Storage(10)
    cache_obj = Cache(eviction_policy, storage_obj)

