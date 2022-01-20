select distinct t.name from players p,teams t
where t.team_id = p.team_id and jersey_no != 74
except
select distinct t.name from players p,teams t
where t.team_id = p.team_id and jersey_no = 74