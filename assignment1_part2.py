#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1 - Part 2"""

class Book(object):
    """This class creates a book.
    
    Attributes:
        attr1 (str): The title of the book.
        attr2 (str): The author of the book.
    """

    title = ''
    author = ''

    def __init__(self, title, author):
        """The book constructor.
        
        Creates a new book with title and author properties.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """

        self.author = author
        self.title = title
    
    def display(self):
        """This will display the book's info.
        
        Will format a string with the properties of 
        the book in order to display the information.
        
        Returns:
            str: Tells who wrote the book.
        """

        return "{}, written by {}.".format(self.title, self.author)

book_1 = Book('Of Mice and Men', 'John Steinbeck')
book_2 = Book('To Kill a Mockingbird', 'Harper Lee')

print book_1.display()
print book_2.display()