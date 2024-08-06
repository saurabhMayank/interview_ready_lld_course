* Block Device: Manages a block of memory and simulates reading and writing blocks.
* Inode: Stores metadata about a file, including its name, size, and the blocks it occupies.
* File System:
- fopen: Opens a file and returns its inode.
- fwrite: Writes data to a file, allocating blocks as needed.
- fread: Reads data from a file.
- fclose: A placeholder, as no cleanup is needed in this simple implementation.

- This implementation demonstrates a basic virtual file system with the required functionalities. For concurrent reads/writes, we use a lock to ensure thread safety.

* In Python, a bytearray is a mutable sequence of bytes. It's an array that can hold bytes (values in the range 0-255) and allows for efficient manipulation and storage of binary data. 



* ba = bytearray(10) (Array of 10 bytes -> is mutable)