
class Storage:

    def __init__(self, capacity:int):
        self.capacity = capacity
        self.storage_dict = {}


    def add(self, key: str, value: str):
        if(storage_dict.size() == self.capacity){
            print("storage is full")
        }
        self.storage_dict[key] = value
    

    def remove(self, key: str):
        if(key not in self.storage_dict):
            print(f"{key} not present in the cache")
        
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
# in LLD coding -> only the structure and imp methods -> are necessary
# other simple methods are not necessary to be implement
# simply put the method definition -> and call the method

class DLL:

    def __init__(self):
        self.dll_node = DLLNode()
    
    def detach_node(self, node: DLLNode, pos):
        pass

    def attach_node_at_tail(self, node: DLLNode):
        pass

    def move_head(self):
        pass

    def get_current_head(self):
        pass



class DLLNode:

    def __init__(self):
        pass

from abc import ABC, abstractmethod

# abstract class of eviction policy
# this class extended -> to create various eviction policies 
class IEvictionPolicy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def key_accessed(self, key: str):
        pass

    @abstractmethod
    def evict_key(self):
        pass


class LRUEvictionPolicy(IEvictionPolicy):
    def __init__(self):
        self.dll = DLL()
        self.dll_node = DLLNode()
        # {key: DLLNode}
        # address mapper of each node
        # DLLNode object contains address of the node
        self.pos_mapper = {}
        self.cache_size = 4
    
    def key_accessed(self, key: str):
        """
        Check if key is present in the pos mapper or not
        Case 1:- 
        If key is present in the pos mapper => node is already present
        Detach node from current pos. 
        Attach node at the end.

        Case 2:-
        If key is not present in the pos mapper => node is not present
        Create a new node
        Check if the current cache size if full or not. Apply restriction on map size
        Put the {key:DLLNode} in the mapper.
        Attach the node at the end.

        """

        if key in self.pos_mapper:
            self.dll.detach_node(key)
        elif key not in self.pos_mapper:
            # check if the current size allows addition or need to evict a key
            new_node = DLLNode()
            if self.pos_mapper.size() == self.cache_size:
                # cache is full
                self.evict_key()
            self.pos_mapper[key] = new_node
        
        # attach node -> at the end
        self.dll.attach_node_at_tail(new_node)
    
    def evict_key(self):
        """
        Remove key at head from the mapper
        Move head
        """
        key = self.dll.get_current_head()
        pos_mapper.pop(key)
        self.dll.move_head()
        



