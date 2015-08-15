import cProfile, pstats, StringIO, introspect
from introspect import whatsin 

s = StringIO.StringIO()

pr = cProfile.Profile()

pr.enable()
whatsin(introspect);
pr.disable()

ps = pstats.Stats(pr, stream=s).sort_stats('calls')
ps.print_stats()
print s.getvalue()
