select title from book_catalogue
where isbn_no in
(select isbn_no from book_copies natural join book_issue natural join members
where member_type = 'PG'
except
select isbn_no from book_copies natural join book_issue natural join members
where member_type = 'UG')

