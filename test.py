import pytest
from books_collector import BooksCollector

class TestBooksCollector():
    
    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()
        return self.collector
    
    @pytest.mark.parametrize('name', ['1', 'Три мушкетёра', '1234567890123456789012345678901234567890'])
    def test_add_new_book_name_added(self, name):
        self.collector.add_new_book(name)
        assert name in self.collector.books_genre

    @pytest.mark.parametrize('name', ['', '12345678901234567890123456789012345678901'])
    def test_add_new_book_incorrect_name_not_added(self, name):
        self.collector.add_new_book(name)
        assert name not in self.collector.books_genre

    def test_set_book_genre_genre_in_dictionary_and_in_list_genre(self):
        name = 'Тачки'
        genre = 'Мультфильмы'
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        assert self.collector.books_genre[name] == genre

    def test_get_book_genre_return_genre(self):
        name = 'Вверх'
        genre = 'Мультфильмы'
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        assert self.collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_existing_genre_return_books(self):
        genre = 'Фантастика'
        name1 = 'Терминатор'
        name2 = 'Терминатор 2: Судный день'
        self.collector.add_new_book(name1)
        self.collector.add_new_book(name2)
        self.collector.set_book_genre(name1, genre)
        self.collector.set_book_genre(name2, genre)
        assert self.collector.get_books_with_specific_genre(genre) == ['Терминатор', 'Терминатор 2: Судный день']

    def test_get_books_genre_return_dictionary(self):
        name1 = 'Джордж из Джунглей'
        name2 = 'Индиана Джонс и Храм Судьбы'
        self.collector.add_new_book(name1)
        self.collector.add_new_book(name2)
        assert self.collector.get_books_genre() == {'Джордж из Джунглей': '', 'Индиана Джонс и Храм Судьбы': ''}

    def test_get_books_for_children_return_books_without_age_rating(self):
        name1 = 'Вокруг света за 80 дней'
        name2 = 'Затерянный мир'
        genre1 = 'Комедии'
        genre2 = 'Фантастика'
        self.collector.add_new_book(name1)
        self.collector.add_new_book(name2)
        self.collector.set_book_genre(name1, genre1)
        self.collector.set_book_genre(name2, genre2)
        assert self.collector.get_books_for_children() == ['Вокруг света за 80 дней', 'Затерянный мир']

    def test_add_book_in_favorites_name_added_in_favorites(self):
        name = 'Дети Капитана Гранта'
        genre = 'Фантастика'
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        self.collector.add_book_in_favorites(name)
        assert 'Дети Капитана Гранта' in self.collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_name_deleted_from_favorites(self):
        name = '200 лье под водой'
        genre = 'Фантастика'
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        self.collector.add_book_in_favorites(name)
        self.collector.delete_book_from_favorites(name)
        assert '200 лье под водой' not in self.collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_return_list(self):
        name = 'Стальная крыса'
        genre = 'Фантастика'
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        self.collector.add_book_in_favorites(name) 
        assert self.collector.get_list_of_favorites_books() == ['Стальная крыса']