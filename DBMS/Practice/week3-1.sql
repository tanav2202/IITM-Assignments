select name from teams t, matches k
where team_id = host_team_id
group by name 
having count(match_num) > 3
union
select name from teams t, matches k
where team_id = guest_team_id
group by name 
having count(match_num) > 3
