print "decodes core loaded"

VERBOSE_FS = False # determines if we verify file system loaded right
VERBOSE = True

EPSILON = 1.0e-10

from dc_interval import *
from dc_color import *

from dc_base import *
from dc_vec import *
from dc_point import *

"""
VECTOR CONSTANTS
"""
UX = Vec(1,0,0)
UY = Vec(0,1,0)
UZ = Vec(0,0,1)

from dc_bounds import *

from dc_plane import *
from dc_cs import *

from dc_line import *
from dc_circle import *
from dc_tri import *

from dc_raster import *
from dc_grid import *

from dc_has_pts import *
from dc_pline import *
from dc_mesh import *
from dc_pgon import *

from dc_xform import *
from dc_intersection import *

from dc_curve import *
from dc_surface import *


