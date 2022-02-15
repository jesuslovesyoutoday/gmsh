import gmsh
import sys
import math

gmsh.initialize()

gmsh.model.add('torus')

gmsh.model.occ.addTorus(0, 0, 0, 20, 10)

gmsh.model.occ.addPlaneSurface([1], 2)
gmsh.model.occ.addThickSolid(1, [2], offset = 3)

gmsh.model.occ.synchronize()

f = gmsh.model.mesh.field.add("MathEval")

gmsh.model.mesh.field.setString(f, "F", "1")
gmsh.model.mesh.field.setAsBackgroundMesh(f)

gmsh.model.mesh.generate(2)

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()
    
gmsh.finalize()
