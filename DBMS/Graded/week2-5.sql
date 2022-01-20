select f.faculty_fname, f.faculty_lname
from faculty f, departments d
where f.department_code = d.department_code
and department_name = ‘Computer Science’