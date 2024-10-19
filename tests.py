from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_over_40_symbols(self):
        collector = BooksCollector()
        collector.add_new_book('Клуб любителей книг и пирогов из картофельных очистков')
        assert len(collector.get_books_genre()) != 3

    def test_add_new_book_two_times(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector

    def test_set_book_genre_existing_book_and_existing_genre(self):
        collector = BooksCollector()
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert 'Гордость и предубеждение и зомби' == 'Фантастика'

    def test_set_book
