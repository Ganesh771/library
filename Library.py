#Creatting a class
class Library:

#Intilaize constructor
    def __init__(
            self,
            author = None,
            tittle = None,
            avaliability = None
            ):
       
        self.author = author
        self.title = tittle
        self.avaliability = avaliability
        self.books =[]


    #Creating an list of arrays
    def addbooks(self , book):
        self.books.append(book.__dict__)
        return self.books
    
    def search_book__by_author(self , author):
        authorbooks = []
        for book in self.books:
            if book.get("author") == author:
                authorbooks.append(book)
        return authorbooks



#Creating an instance
b=Library()
book1 = Library("Sumin" , "Saya" , "No")
book2 = Library("Karnali Blues" , "Budhi Sagar" , "Yes")

print(b.addbooks(book1))
print(b.addbooks(book2))

print(b.search_book__by_author("Sumin"))


        
        
        
    

    

        
