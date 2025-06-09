import pytest
from main import BooksCollector


@pytest.fixture
def book_name_not_exists():
    return 'Трава у дома'

@pytest.fixture
def book_name_exists_in_list_books_genre():
    return "Дюна"

@pytest.fixture
def book_name_not_exists():
    return "Тотошка"

@pytest.fixture
def children_books():
    return ["Дюна", "Остров сокровищ", "Аэроплан"]

@pytest.fixture
def list_books_favorites():
    return [
        'Я и мои друзья',
        'Тотошка',
        'Дерево'
    ]

@pytest.fixture
def dict_books_genre():
    return {
        "Дюна": "Фантастика",
        "Оно": "Ужасы",
        "Шерлок Холмс": "Детективы",
        "Остров сокровищ": "Мультфильмы",
        "Аэроплан": "Комедии"
        }

@pytest.fixture
def collector_example(
    dict_books_genre,
    list_books_favorites
    ):

    collector = BooksCollector()
    collector.books_genre = dict_books_genre
    collector.favorites = list_books_favorites
    return collector
