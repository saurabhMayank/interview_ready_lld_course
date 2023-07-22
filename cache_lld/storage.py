
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