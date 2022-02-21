import gmsh
import sys
import os
import math

gmsh.initialize()

path = os.path.dirname(os.path.abspath(__file__))
gmsh.merge(os.path.join(path, 'h.stl'))

angle = 40

forceParametrizablePatches = False
includeBoundary = False

curveAngle = 180

gmsh.model.mesh.classifySurfaces(angle * math.pi / 180., includeBoundary,
                                 forceParametrizablePatches,
                                 curveAngle * math.pi / 180.)

gmsh.model.mesh.createGeometry()

s = gmsh.model.getEntities(2)
l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

f = gmsh.model.mesh.field.add("MathEval")

gmsh.model.mesh.field.setString(f, "F", "4")
gmsh.model.mesh.field.setAsBackgroundMesh(f)

gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 1)

gmsh.model.mesh.generate(2)

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
