# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44 # n Объёма
pages = 100 # n страниц
lines = 50 # n строк
characters = 25 # n символов
bytes_one_char = 4 # n байтов в символе

disk_size_in_kb = disk_size * 1024 * 1024
t_char = characters * lines  * pages
size_of_book = bytes_one_char * t_char
numbers_of_books = int(disk_size_in_kb // size_of_book)

print("Количество книг, помещающихся на дискету:", numbers_of_books)
