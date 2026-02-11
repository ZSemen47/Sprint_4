# Sprint_4
Фикстура collector создает объект класса перед каждым тестом

Тест 1.  
Название: test_add_new_book_name_added  
Описание: add_new_book добавляет книгу с именем name. При помщи параметризации проверяю граничные значения  

Тест 2.  
Название: test_add_new_book_incorrect_name_not_added  
Описание: add_new_book НЕ добавляет книгу с некорректным названием. При помощи параметризации проверяются разные невалидные значения.  

Тест 3.  
Название: test_set_book_genre_add_genre_in_dictionary  
Описание: set_book_genre добавляет жанр в словарь  

Тест 4.  
Название: test_get_book_genre_return_genre  
Описание: get_book_genre возвращает жанр  

Тест 5.  
Название: test_get_books_with_specific_genre_existing_genre_return_books  
Описание: get_books_with_specific_genre получает на вход существующий жанр и возвращает список книг  

Тест 6.  
Название: test_get_books_genre_return_dictionary  
Описание: проверяю что get_books_genre возвращает словарь с добавленными туда именами и жанрами  
 
Тест 7.  
Название: test_get_books_for_children_return_books_without_age_rating  
Описание: get_books_for_children возвращает книги у которых отсутствует возрастной рейтинг  

Тест 8.  
Название: test_add_book_in_favorites_name_added_in_favorites  
Описание: add_book_in_favorites добавляет name в список избранного  

Тест 9.  
Название: test_delete_book_from_favorites_name_deleted_from_favorites  
Описание: delete_book_from_favorites удаляет name из избранного  

Тест 10.  
Название: test_get_list_of_favorites_books_return_list  
Описание: get_list_of_favorites_books возвращает список  