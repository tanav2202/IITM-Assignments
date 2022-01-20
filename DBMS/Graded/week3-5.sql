select c.title, count(*) from book_catalogue c natural join book_copies k
where title like '%Database%'
group by isbn_no, c.title