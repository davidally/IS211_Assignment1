#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Book(object):

    author = ''
    title = ''

    def __init__(self, title, author):
        self.author = author
        self.title = title
    
    def display(self):
        return "{}, written by {}.".format(self.title, self.author)

book1 = Book('Of Mice and Men', 'John Steinbeck')
book2 = Book('To Kill a Mockingbird', 'Harper Lee')

print book1.display()
print book2.display()