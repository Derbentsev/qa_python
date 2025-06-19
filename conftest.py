import pytest
from main import BooksCollector


@pytest.fixture
def book_name_not_exists():
    return 'Трава у дома'

@pytest.fixture
def book_name_exists_in_list_books_genre():
    return 'Дюна'

@pytest.fixture
def children_books():
    return ['Дюна', 'Остров сокровищ', 'Аэроплан']

@pytest.fixture
def list_books_favorites():
    return [
        'Дюна',
        'Оно',
        'Шерлок Холмс'
    ]

@pytest.fixture
def dict_books_genre():
    return {
        'Дюна': 'Фантастика',
        'Оно': 'Ужасы',
        'Шерлок Холмс': 'Детективы',
        'Остров сокровищ': 'Мультфильмы',
        'Аэроплан': 'Комедии'
        }

@pytest.fixture
def collector_example(
    dict_books_genre,
    list_books_favorites
    ):

    collector = BooksCollector()
    for name, genre in dict_books_genre.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

    for book_name in list_books_favorites:
        collector.add_book_in_favorites(book_name)

    return collector
