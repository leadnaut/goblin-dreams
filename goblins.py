import world as w
from data import *
import tools as tls
import random as r

r.seed("hny")
test = w.World("test")
test.generate_terrain(75, 5)
tls.tmap_to_png(test)
