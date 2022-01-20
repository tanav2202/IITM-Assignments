select faculty_fname,faculty_lname
from faculty
where faculty.id not in
(select members.id from members natural join book_issue
where members.id is not null)