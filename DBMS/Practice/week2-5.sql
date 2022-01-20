select student_fname, student_lname from students s, members m
where s.roll_no = m.roll_no and member_type = ’PG’