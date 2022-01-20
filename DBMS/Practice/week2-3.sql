select c.title
from book_catalogue c, book_authors a
where c.isbn_no = a.isbn_no
and author_fname = ’Joh Paul’ and author_lname = ’Mueller’