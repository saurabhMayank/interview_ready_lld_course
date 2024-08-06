
"""
Locks not implemented, can suggest as an extension
Little idea of implementing threading at code level
Complex requirement -> leave it for now
"""

"""
Make a new repo of machine coding and put all the code there

"""


from abc import ABC, abstractmethod

class BlockDevice:
    def __init__(self, size, block_size):
        self.size = size
        self.block_size = block_size
        # bytearray divides total size into bytes of 1 block
        # it is native to python
        self.blocks = bytearray(size)  # Initialize a large block of memory
        self.free_blocks = set(range(size // block_size))

    def read_block(self, block_num):
        start = block_num * self.block_size
        end = start + self.block_size
        return self.blocks[start:end]

    def write_block(self, block_num, data):
        start = block_num * self.block_size
        end = start + self.block_size
        self.blocks[start:end] = data  # Directly modify the block of memory
        self.free_blocks.discard(block_num)

    def free_block(self, block_num):
        self.free_blocks.add(block_num)

"""
Calculate Total Number of Blocks:

size // block_size calculates how many blocks of block_size bytes 
can fit into the total size bytes of the block device.
For example, if size is 1024 bytes and block_size is 128 bytes,
 then size // block_size is 1024 // 128, which equals 8. This means there are 8 blocks available.
Generate a Range of Block Indices:

range(size // block_size) generates a sequence of numbers from 
0 up to (but not including) the total number of blocks.
Continuing with the example, range(8) generates the sequence 
0, 1, 2, 3, 4, 5, 6, 7.
Convert the Range to a Set:

set(range(size // block_size)) converts this sequence into a
 set of integers representing the indices of all available blocks.
Using the example, this would create the set {0, 1, 2, 3, 4, 5, 6, 7}.

"""


class Inode:
    def __init__(self, filename, size, block_nums):
        self.filename = filename
        self.size = size
        self.block_nums = block_nums


class VFS(ABC):
    def __init__(self, block_device):
        self.block_device = block_device
        self.inodes = {}
    
    @abstractmethod
    def fopen(self):
        pass
    
    @abstractmethod
    def fread(self):
        pass
    
    @abstractmethod
    def fwrite(self):
        pass
    
    @abstractmethod
    def fclose(self):
        pass



class FileSystem(VFS):
    def __init__(self, block_device):
        self.block_device = block_device
        self.inodes = {}
        
    # mode is not implemented -> suggest as extension
    def fopen(self, filename, mode, file_size=0, block_num=[]):
        
        if filename in self.inodes:
            # if file name present
            # return its inode directly
            inode = self.inodes[filename]
        else:
            # if file name not present
            # create the file i.e its inode and add it into list
            # and return inode
            inode = Inode(filename, file_size, block_num)
            self.inodes[filename] = inode
        
        # return the inode of the file -> its metadata
        # its metadata can be helpful to read the file
        return inode

    def fwrite(self, inode, data):
        
        blocks_needed = (len(data) + self.block_device.block_size - 1) // self.block_device.block_size
        
        # if blocks in the current file are less than blocks needed to write data
        if len(inode.block_nums) < blocks_needed:
            raise Exception("Data is exceeding file size choose a bigger file")
            # Extension -> below code -> can add more blocks if needed
            # by checking if free blocks are available in block_device
            # of the file system

            # for _ in range(blocks_needed - len(inode.block_nums)):
            #     if not self.block_device.free_blocks:
            #         raise Exception("No free blocks available")
            #     inode.block_nums.append(self.block_device.free_blocks.pop())

        # inode.block_nums -> number of blocks assigned to the file
        # iterate over each block & add data to the block
        # using block_device
        for i, block_num in enumerate(inode.block_nums):
            start = i * self.block_device.block_size
            end = start + self.block_device.block_size
            self.block_device.write_block(block_num, data[start:end])

        # this is not needed because we are not adding more free blocks
        # so size of file will be same
        # inode.size = len(data)

    
    def fread(self, inode):
        data = bytearray()
        for block_num in inode.block_nums:
            # add the content from block_device into data array
            data.extend(self.block_device.read_block(block_num))
        return data[:inode.size]

    def fclose(self, inode):
        pass  # Nothing to do here in this simple example

# Initialize block device and file system
block_device = BlockDevice(1024 * 1024, 1024)  # 1MB device with 1KB blocks
file_system = FileSystem(block_device)

# Test the file system
inode = file_system.fopen("testfile", "w", file_size=3, block_num=[0, 1, 2])
file_system.fwrite(inode, b"Hi")
print(file_system.fread(inode))
