# Hint 2 - Adding and searching authors

> You will be able to extend this example also for books

If you follow our previous hint, you now have a bookstore that looks something like:
```python
bookstore = {
    'name': "Rmotr's bookstore"
    'authors': [poe, borges, austen],
    'books': [raven, ficciones]
}
```

We need now to add different authors. And the question is, "what is an author?". We need to represent, in a single data structure, an author with her name and nationality. A dictionary might also be handy in this situation:

```python
author = {
    'name': 'Edgar Allan Poe',
    'nationality': 'US'
}
```

An author is created (and added to the bookstore at the same time) with the `add_author` function. This function receives the bookstore, the name of the author and the nationality of the author. We'll then add this "author" to the list of `authors` in the bookstore and also make sure we add the correct ID for that author.

```python
def add_author(bookstore, name, nationality):
    author = {
        'name': name,
        'nationality': nationality
    }
    bookstore['authors'].append(author)

    return author
```

Now, we need to, for example, search by name. We know that authors then is just a list of dictionaries containing the name and nationality of the author. We could do something like:

```python
name_to_search = 'James Joyce'
for author in authors:
    if author['name'] == name_to_search:
      return author
```
