import gmsh
import sys
import math

gmsh.initialize()

gmsh.model.add('torus')
gmsh.model.occ.addTorus(0, 0, 0, 20, 10)

gmsh.model.occ.synchronize()
gmsh.model.mesh.generate(2)

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()
    
gmsh.finalize()
