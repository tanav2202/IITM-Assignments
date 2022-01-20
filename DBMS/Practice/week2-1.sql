select m.name
from managers m, teams t
where m.team_id = t.team_id and t.name = ’All Stars’