# Bookstore management system

Today you're in charge of building a simple Bookstore system. It will store authors and books, just like a bookstore would! We will be representing these items using dictionaries. It's important when writing code for this that you make sure that the **interface** works as expected. That means reading and understanding the tests in tests.py to dictate how you should design your code. 

There are two hints in this file directory... please don't use them unless you get stuck for a while. 

#### Creating a bookstore

The first thing we need to do is "create a bookstore". We'll then use the bookstore to add authors or books. What _"is"_ a bookstore? Well, in the real world you know that. For this project, we get to design and model the bookstore how we choose (in this case a dictionary to take advantage of key-value pairs). We need it to store the bookstore's name, all the authors in it, and all of the books in it. You will have to choose how you want to store this information. 

```python
bookstore = create_bookstore("Rmotr's bookstore")
```

If you look at the empty functions in bookstore.py, every one of them after create_bookstore receives `bookstore` as the first parameter. For this project, a bookstore is created in the tests and treated like a global dictionary for your tests. Remember how your bookstore is a dictionary? Dictionaries are mutable. That means if we pass your bookstore dictionary to each of the other functions, if the function changes or adds a value to the dictionary, that change remains in your dictionary after the function ends. Use this knowledge to store and access books and authors in your functions. :)

#### Adding authors

Once you create a bookstore, you can add authors to it. For example:

```
poe = add_author(bookstore, 'Edgar Allan Poe', 'US')
print(poe['name'])
print(poe['nationality'])
```

From the context above, you should be able to tell that Authors are represented as dictionaries. The add_author function receives the bookstore dictionary, author name, and nationality. The name and nationality  information is stored in the author dictionary. Note the keys must match what is in the tests. Make sure to store your author in your bookstore dictionary and pay attention if this function returns something or not. 

#### Searching authors (by name)

There's a utility function to search for an author by name. It's as simple as:

```python
bookstore = create_bookstore("Rmotr's bookstore")
poe = add_author(bookstore, 'Edgar Allan Poe', 'US')
poe_author = bookstore.get_author_by_name('poe')
```

#### Adding books

We'll also be able to add books to our bookstore. When we want to add a book to our bookstore, we'll use the following information:

* Book's title
* Book's ISBN
* Book's author

Example:

```python
bookstore = create_bookstore("Rmotr's bookstore")
poe = add_author(bookstore, 'Edgar Allan Poe', 'US')

# We now add our book:
raven = add_book(bookstore, 'The Raven', 'XXX-1', poe)  
```

#### Searching books (by title and by author)

There's also a utility function to search a book by title. It's as simple as:

```python
book = get_book_by_title(bookstore, 'raven')
print(book['title']) # 'The Raven'
```

We can also search for **all** the books by a given author. In this case, the result will be a **list** of books, not just one element. See the next example:

```python
bookstore = create_bookstore("Rmotr's bookstore")
poe = add_author(bookstore, 'Edgar Allan Poe', 'US')

# We now add a couple of books:
raven = add_book(bookstore, 'The Raven', 'XXX-1', poe)
valdemar = add_book(bookstore, 'The Facts in the Case of M. Valdemar', 'XXX-2', poe])

# Finally, we search books by author:
poe_books = get_books_by_author(bookstore, poe)
for book in poe_books:
    print(book['title']
# We should see printed out:
# The Raven
# The Facts in the Case of M. Valdemar
```
