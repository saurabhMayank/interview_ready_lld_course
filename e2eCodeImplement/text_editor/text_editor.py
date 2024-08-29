class Action:
    def __init__(self, action_name: str, content: str,  line_num: int, undo: bool, redo: bool):
        self.action_name = action_name
        self.content = content
        self.line_num = line_num
        self.undo = undo
        self.redo = redo


class BaseExceptionError(Exception):
    """
    Base Exception class for v2 APIs.
    All custom exceptions are created by extending this class.
    Exception has 4 attributes corresponding to details sent in 'error' object
    in response JSON -
        status - http status code
        code - application specific error code
        title - title of error
        detail - details of error
    """

    def __init__(self, status, code, title, detail):
        Exception.__init__(self)
        self.title = title
        self.detail = detail

    def as_dict(self):
        return {"title": self.title, "detail": self.detail}

    def as_str(self):
        exception_str = "Exception Type : " + self.__class__.__name__
        exception_str += "\nTitle - " + self.title if self.title else ""
        exception_str += "\nDetails - " + self.detail if self.detail else ""
        return exception_str

    def __str__(self):
        return f"{self.__class__.__name__} ({self.title}): {self.detail}"


class SizeOutofBoundsError(BaseExceptionError):
    def __init__(self, title=None, detail=None):
        self.title = "Size out of Bounds"
        if detail:
            self.detail = detail

class TextNotFoundError(BaseExceptionError):
    def __init__(self, title=None, detail=None):
        self.title = "Text Not Found"
        if detail:
            self.detail = detail

class NoTextCopiedError(BaseExceptionError):
    def __init__(self, title=None, detail=None):
        self.title = "No Text Copied"
        if detail:
            self.detail = detail


class File:
    undo_stack: Action = []
    redo_stack: Action = []
    

    def __init__(self, capacity):
        self.capacity = capacity
        # every line is an element in file_list arr
        # is initialised as empty string
        self.file_list = [""]*self.capacity
        # copy_var is a empty string
        self.copy_var = ""


    def insert_text(self, line_num: int, text: str):
        """
        Insert text into single line
        Responsibility to 
        -> check if passed line number exceeds the capacity
        -> Insert the text in the give line num

        """
        if line_num > self.capacity:
            raise SizeOutofBoundsError(f"Line Num {line_num} passed is bigger than the file length")
            print("\n")
        else:
            # file_list is 0 indexed that is why
            self.file_list[line_num-1] = text
            print("----display file---")
            print("\n")
            self.display_file()
    
    def insert_text_multiple_lines(self, text_line_dict: dict):
        """
        Insert text into multiple lines
        Responsiblity to internally call the insert_text function
        for the input 
        """
        for line_num, text in text_line_dict.items():
            self.insert_text(line_num, text)

    def delete_text(self, line_num: int):
        """
        Delete text from a single line
        Responsibility of this function
        -> Check if the line_num is not exceeding the capacity
        -> Check if line_num passed has any text or not
        -> Replace the content with empty string
        """
        if line_num > self.capacity:
            raise SizeOutofBoundsError(f"Line Num {line_num} passed is bigger than the file length")
            print("\n")
        elif self.file_list[line_num-1] == "":
            raise TextNotFoundError(f" Line number passed {line_num} does not contain any text")
        else:
            self.file_list[line_num-1] = ""
        
        print("----display file---")
        print("\n")
        self.display_file()
    
    def copy_text(self, line_num: int):
        """
        Copy text into single line
         Responsibility of this function
        -> Check if the line_num is not exceeding the capacity
        -> Check if line_num passed has any text or not
        -> Copy the text into instance variable

        """
        if line_num > self.capacity:
            raise SizeOutofBoundsError(f"Line Num {line_num} passed is bigger than the file length")
        elif self.file_list[line_num-1] == "":
            raise TextNotFoundError(f" Line number passed {line_num} does not contain any text")
        else:
            if len(self.copy_var) > 0:
                # if there is an element already in copy_var
                # remove that element so we can store the next one
                self.copy_var = ""
            self.copy_var = self.file_list[line_num-1]
    
    def paste_text(self, line_num: int):
        """
        Paste text into single line
        """
        if not self.copy_var:
            raise NoTextCopiedError("Nothing copied, Please copy first")
        elif line_num > self.capacity:
            SizeOutofBoundsError(f"Line Num {line_num} passed is bigger than the file length")
        else:
            self.file_list[line_num-1] = self.copy_var
            print("----display file---")
            print("\n")
            self.display_file()


    def delete_file(self):
        """
        Delete the whole file and display it
        """
        # reassign the list to empty value
        # for all indexes
        self.file_list = [0]*self.capacity

        self.display_file()

    
    def display_file(self):
        for i, item in enumerate(self.file_list, start=1):
            print(f"{i}. {item}")
    
    def undo(self):
        pass
    
    def redo(self):
        pass

class TextEditorSingleton:
    # class instance
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TextEditorSingleton, cls).__new__(cls)
            # Additional initialization can be done here
        return cls._instance

    def __init__(self):
        pass
    

    def create_file(self, name: str, capacity: int):
        """
        Functional API to create files
        """
        print("--File Created---")
        # initialize instance of the file and return
        file_obj = File(capacity)
        return file_obj


import json

# import text_editor

from text_editor_main import TextEditorSingleton



# from text_editor.text_editor_main import TextEditorSingleton

def run_handler():
    print("----Text Editor opened---")

    text_editor_singelton_obj = TextEditorSingleton()


    print("\n")
    print("---Create a File with a defined file size---")
    file_name = input("Enter file name: ")
    file_size = int(input("Enter file size: "))


    # Case 1 -> Initialise a file of a definite capacity & insert text
    file_1_obj = text_editor_singelton_obj.create_file(name = file_name, capacity = file_size)

    print("\n")
    print(f"---File {file_name} of size {file_size} is created----")

    # print("\n")
    # print("---Enter text to insert and also on which line number----")
    # text_to_insert = input("Enter text to insert: ")
    # line_num_to_insert = int(input("Enter line number to insert to: "))

    # file_1_obj.insert_text(line_num_to_insert, text_to_insert)


    # Case 2 -> Insert text into multiple lines
    print("\n")
    print("---Enter texts to insert and also on which line numbers----")

    # user_input is either string or dict
    user_input = input("Enter key-value pairs separated by commas (e.g., lineNum1:text1,lineNum2:text2): ")

    user_input_dict = json.loads(user_input)
    data = {}
    user_input_dict = json.loads(user_input_dict)
    
    for key, val in user_input_dict.items():
        int_key = int(key)
        data[int_key] = val

    file_1_obj.insert_text_multiple_lines(data)


    # Case 3 -> delete text from a specific line
    print("\n")
    print("---Delete text from a specific line_num--")
    line_num_to_delete = int(input("Enter line number to delete text from: "))

    file_1_obj.delete_text(line_num_to_delete)

    print("\n")

    # Case 4 -> Copy text to from a specific line &
    # Paste text to a specific line
    print("---Copy text from a specific line_num----")
    print("\n")
    line_num_to_copy = int(input("Enter line number to copy text from: "))

    file_1_obj.copy_text(line_num_to_copy)

    print("\n")
    print("---Paste text to a specific line_num----")
    print("\n")
    line_num_to_paste = int(input("Enter line number to paste text to: "))
    
    file_1_obj.paste_text(line_num_to_paste)

    
if __name__ == "__main__":
    run_handler()