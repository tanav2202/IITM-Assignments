select p.name from teams t, players p
where t.team_id = p.team_id and t.name = 'All Stars' and dob in 
(select max(dob)from players p,teams t
where p.team_id = t.team_id and t.name = 'All Stars')