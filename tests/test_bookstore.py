
from bookstore import *


def test_create_bookstore():
    store = create_bookstore("rmotr's bookstore")
    assert store['name'] == "rmotr's bookstore"

def test_add_get_authors():
    store = create_bookstore("rmotr's bookstore")

    poe = add_author(store, 'Edgar Alan Poe', 'US')
    borges = add_author(store, 'Jorge Luis Borges', 'AR')
    joyce = add_author(store, 'James Joyce', 'UK')

    assert poe['name'] == 'Edgar Alan Poe'
    assert poe['id'] is not None
    assert poe['nationality'] == 'US'

    assert borges['name'] == 'Jorge Luis Borges'
    assert borges['id'] is not None
    assert borges['nationality'] == 'AR'

    assert joyce['name'] == 'James Joyce'
    assert joyce['id'] is not None
    assert joyce['nationality'] == 'UK'

    author = get_author_by_name(store, 'James Joyce')
    assert author['id'] == joyce['id']
    assert author['name'] == joyce['name']
    assert author['nationality'] == joyce['nationality']

    author = get_author_by_id(store, poe['id'])
    assert author['id'] == poe['id']
    assert author['name'] == poe['name']
    assert author['nationality'] == poe['nationality']

def test_add_get_books():
    store = create_bookstore("rmotr's bookstore")

    poe = add_author(store, 'Edgar Alan Poe', 'US')
    borges = add_author(store, 'Jorge Luis Borges', 'AR')
    joyce = add_author(store, 'James Joyce', 'UK')

    raven = add_book(store, 'The Raven', 'XXX-1', poe['id'])
    ulysses = add_book(store, 'Ulysses', 'XXX-2', joyce['id'])
    ficciones = add_book(store, 'Ficciones', 'XXX-3', borges['id'])
    aleph = add_book(store, 'El Aleph', 'XXX-4', borges['id'])

    book = get_book_by_title(store, 'The Raven')
    assert book['title'] == 'The Raven'
    assert book['isbn'] == 'XXX-1'
    assert book['author_id'] == poe['id']

    book = get_book_by_id(store, ulysses['id'])

    assert book['title'] == 'Ulysses'
    assert book['isbn'] == 'XXX-2'
    assert book['author_id'] == joyce['id']

    books = get_books_by_author(store, borges['id'])
    assert len(books) == 2

    book1 = books[0]
    assert book1['title'] == 'Ficciones'
    assert book1['isbn'] == 'XXX-3'
    assert book1['author_id'] == borges['id']

    book2 = books[1]
    assert book2['title'] == 'El Aleph'
    assert book2['isbn'] == 'XXX-4'
    assert book1['author_id'] == borges['id']
