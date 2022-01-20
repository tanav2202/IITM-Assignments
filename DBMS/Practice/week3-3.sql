select count(title) from book_catalogue where isbn_no in
(select isbn_no
from book_issue a, book_copies b
where a.accession_no=b.accession_no and
a.doi=’2021-08-11’
)