import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('genre', ['Ужасы'])
    def test_set_book_genre_if_genre_exists(
        self,
        book_name_exists_in_list_books_genre,
        collector_example,
        genre
        ):

        collector_example.set_book_genre(book_name_exists_in_list_books_genre, genre)
        assert collector_example.books_genre[book_name_exists_in_list_books_genre] == genre

    @pytest.mark.parametrize('genre', ['Казино'])
    def test_set_book_genre_if_genre_not_exists(
        self,
        book_name_exists_in_list_books_genre,
        collector_example,
        genre
        ):

        collector_example.set_book_genre(book_name_exists_in_list_books_genre, genre)
        assert collector_example.books_genre[book_name_exists_in_list_books_genre] != genre

    @pytest.mark.parametrize('name, genre', [['Дюна', 'Фантастика']])
    def test_get_book_genre_success(
        self,
        collector_example,
        name,
        genre
        ):

        assert genre == collector_example.get_book_genre(name)

    @pytest.mark.parametrize('genre, books', [['Комедии', ['Аэроплан']]])
    def test_get_books_with_specific_genre_success(
        self,
        collector_example,
        genre,
        books
        ):

        assert books == collector_example.get_books_with_specific_genre(genre)

    def test_get_books_genre_success(
            self,
            collector_example,
            dict_books_genre
            ):

        assert dict_books_genre == collector_example.get_books_genre()

    def test_get_books_for_children_success(
            self,
            collector_example,
            children_books
            ):
        
        assert children_books == collector_example.get_books_for_children()

    def test_add_book_in_favorites_success(
            self,
            book_name_exists_in_list_books_genre,
            collector_example
            ):
        
        collector_example.add_book_in_favorites(book_name_exists_in_list_books_genre)
        assert book_name_exists_in_list_books_genre in collector_example.get_list_of_favorites_books()

    def test_delete_book_from_favorites_if_book_exists(
            self,
            book_name_favorite_exists,
            collector_example
            ):
        
        collector_example.delete_book_from_favorites(book_name_favorite_exists)
        assert book_name_favorite_exists not in collector_example.get_list_of_favorites_books()

    def test_delete_book_from_favorites_if_book_not_exists(
            self,
            book_name_favorite_exists,
            collector_example
            ):
        
        collector_example.delete_book_from_favorites(book_name_favorite_exists)
        assert book_name_favorite_exists not in collector_example.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(
            self,
            collector_example,
            list_books_favorites
            ):

        assert collector_example.get_list_of_favorites_books() == list_books_favorites
