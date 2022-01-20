select p.name
from players p, teams t
where p.team_id = t.team_id and t.name = ’All Stars’