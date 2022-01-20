select distinct faculty_fname, faculty_lname
from faculty natural join members natural join book_issue
where faculty.department_code = ’ME’