"""
Library management System

Not coding these requirements
i) Calculate fine -> explain theoretically
ii) Explain theoretically
History of book -> Which users have taken this book
History of User -> Which books this user has taken

Notes in good notes

"""
from datetime import datetime
import uuid

# from ABC import abc

class UserModel:
    def __init__(self, name: str, email: str):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.borrow_list: BookItemModel = []
        self.reserve_list: BookModel = []
        self.fine = 0

    
    def get_name(self):
        return self.name

    def get_borrowed_book_list(self):
        borrow_list_val = []
        for book in self.borrow_list:
            borrow_list_val.append(book.name)
        return borrow_list_val

    def update_fine(self, fine_amount: int):
        self.fine = self.fine + fine_amount
    
    def get_fine(self):
        return self.fine
    

    def get_reserve_book_list(self):
        reserve_list_val = []

        for book in self.reserve_list_val:
            reserve_list_val.append(book.name)
        return reserve_list_val


class BookModel:
    
    def __init__(self, name="", author="", publisher="", category=""):
        self.id = uuid.uuid4()
        self.name = name
        self.author = author
        self.publisher = publisher
        self.category = category
        # every book will be initialised with same count
        # but its count can change in the program
        self.count = 10
    
    def increment_book_count(self):
        self.count = self.count + 1
        return self.count
    
    def get_current_book_count(self):
        return self.count
    
    def decrement_book_count(self):
        self.count = self.count - 1
        return self.count


class BookItemModel:
    def __init__(self, book:BookModel):
        id = uuid.uuid4()
        self.book = book
        self.issue_date = datetime.now()
        self.issue_limit = 10 # 10 days from issue_date
    

class LibraryModel:
    def __init__(self):
        self.book_list: BookModel = []
        self.user_list: UserModel = []
    

    def get_library_members(self):
        user_list_val = []
        for user in self.user_list:
            user_list_val.append(user.name)
        return user_list_val

    def add_book_to_library(self, book:BookModel):
        self.book_list.append(book)
    
    def add_user_to_library(self, user: UserModel):
        self.user_list.append(user)

    def get_books_in_library(self):
        book_list_val = []

        for book in self.book_list:
            book_list_val.append({book.name:book.get_current_book_count()})
        return book_list_val



class UserService:
    def __init__(self, user: UserModel):
        self.user = user
    
    
    def add_user_to_library(self, user:UserModel, library:LibraryModel):
        """
         add user to library
        """
        library.add_user_to_library(user)
    
    
    # for simplicity mandating to search only via one argument
    # in real world systems this can be optimised
    def search_book(self, title = "", author = "", publication = "", category = ""):
        """
        Search a book
        """
        if title:
            book_item = SearchByTitleService(title)
        elif author:
            book_item = SearchByAuthorService(author)
        elif publication:
            book_item = SearchByPublicationService(publication)
        elif category:
            book_item = SearchByCategoryService(category)
        
        return book_item
    

    def borrow_book(self, book:BookModel):
        """
        borrow book
        returns a book item
        """
        book_service = BookService()
        book_item = book_service.borrow_book_item(book)

        if book_item:
            self.user.borrow_list.append(book_item)
        else:
            # reserve the book
            self.reserve_book(book)

    
    def return_book(self, book_item:BookItemModel):
        """
        return book item
        """
        # remove the book from user borrow list
        self.user.borrow_list.remove(book_item)

        # calculate fine
        curr_date = datetime.now()
        issue_date = book_item.issue_date
        issue_limit = book_item.issue_limit

        datetime_diff = curr_date-issue_date
        days_diff = datetime_diff.days

        print(f"days_diff: {days_diff}")

        if days_diff > issue_limit:
            print(f"pay fine: {days_diff}")
            self.user.update_fine(days_diff)


        book_service = BookService()

        book = book_item.book

        book_service.return_book(book)
    

    def reserve_book(self, book:BookModel):
        """
        reserve book
        """
        self.user.borrow_list.append(book)



class BookService:
    def __init__(self):
        pass
    

    def add_book(self, book:BookModel, library:LibraryModel):
        """
        will add the book and also add book item
        """
        library.add_book_to_library(book)
    
    def borrow_book_item(self, book:BookModel):
        if book.get_current_book_count() > 0:
            # if book exists
            book.decrement_book_count()

            book_item = BookItemModel(book)
        
        else: 
            return None
    

    def return_book(self, book_item:BookItemModel):
        book = book_item.book
        book.increment_book_count()



# abstract class
# strategy pattern applied -> to make code
# extensible to add lot of search strategies
# ISearchService(abc)
# assume this is abstract class -> not installing abc here
# as its a 3rd party library
class ISearchService():

    def __init__(self):
        pass

    def search_book(self, query_str: str):
        pass


class SearchByTitleService(ISearchService):
    def __init__(self):
        pass
    

    def search_book(self, title: str):
        # search logic is black box
        book = BookModel(title=title, author="", category="", publication="")
        book_item = BookItemModel(book)
        return book_item

class SearchByAuthorService(ISearchService):
    def __init__(self):
        pass

    def search_book(self, author: str):
        # search logic is black box
        book = BookModel(title="", author=author, category="", publication="")
        book_item = BookItemModel(book)
        return book_item
    

class SearchByCategoryService(ISearchService):
    def __init__(self):
        pass
    

    def search_book(self, category: str):
        # search logic is black box
        book = BookModel(title="", author="", category=category, publication="")
        book_item = BookItemModel(book)
        return book_item


class SearchByPublicationService(ISearchService):
    def __init__(self):
        pass
    

    def search_book(self, publication: str):
        # search logic is black box
        book = BookModel(title="", author="", category="", publication=publication)
        book_item = BookItemModel(book)
        return book_item



if __name__ == "__main__":
    print("hello from the library system")
    print("\n")

    print("Lets add a user to library")

    user = UserModel(name="Mayank", email="abc@gmail.com")

    library = LibraryModel()
    library.add_user_to_library(user)
    print(f"memebers in library: {library.get_library_members()}")

    print("\n")
    book1 = BookModel(name="selected_poems", author="gulzar")
    book2 = BookModel(name="wings_of_fire", author="kalam_sir")
    book3 = BookModel(name="mastery", author="geoge_leonard")

    library.add_book_to_library(book1)
    library.add_book_to_library(book2)
    library.add_book_to_library(book3)


    print(f"books in library: {library.get_books_in_library()}")

    print("Borrow wings of fire")
    user_service = UserService(user)

    user_service.borrow_book(book2)

    print(f"Current borrowed books by user: {user.get_borrowed_book_list()}")

    print("\n")

    print(f"updated books in library: {library.get_books_in_library()}")


    # rest of the functions needed can be implemented of reserved and all



