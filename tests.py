import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('name', ['Гордость и предубеждение', 'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_add_two_books(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    def test_add_new_book_over_40_symbols(self, collector):
        collector.add_new_book('Клуб любителей книг и пирогов из картофельных очистков')
        assert collector.get_books_genre() == {}

    def test_add_new_book_two_times(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')
        assert len(collector.get_books_genre()) != 2

    def test_set_book_genre_existing_book_and_existing_genre(self, collector):
        collector.add_new_book('Divergent')
        collector.set_book_genre('Divergent', 'Фантастика')
        assert collector.get_books_genre() == {'Divergent': 'Фантастика'}

    def test_set_book_genre_existing_book_no_genre(self, collector):
        collector.add_new_book('Holy Bible')
        collector.set_book_genre('Holy Bible', 'History')
        assert collector.get_books_genre() == {'Holy Bible': ''}

    def test_get_book_genre_existing_book(self, collector):
        collector.add_new_book('Divergent')
        collector.set_book_genre('Divergent', 'Фантастика')
        assert collector.get_book_genre('Divergent') == 'Фантастика'

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Divergent')
        collector.set_book_genre('Divergent', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Divergent']

    def test_get_books_genre_get_names(self, collector):
        collector.add_new_book('Divergent')
        assert collector.get_books_genre() == {'Divergent': ''}

    @pytest.mark.parametrize('name', ['Cinderella', 'Beauty and The Beast'])
    def test_get_books_for_children_without_rating(self, collector, name):
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Мультфильмы')
        assert name in collector.get_books_for_children()

    def test_add_book_in_favorites_one_book(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')
        assert 'Гордость и предубеждение' in collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites_one_book(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.delete_book_from_favorites('Гордость и предубеждение')
        assert 'Гордость и предубеждение' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_new_book(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')
        assert len(collector.get_list_of_favorites_books()) == 1

