import numpy as np
from pymol.cgo import *
from pymol import cmd
namelist = ['r', 's', 'c']
vecdict = {'c' : [2.728e-3, -9.513e-2, 1.451e-2],
           'r' : [-1.731e-2, 0.0, 6.145e-2],
           's' : [-1.731e-2, 0.0, -6.145e-2]}

def cart2sph(x, y, z):
    hxy = np.hypot(x, y)
    r = np.hypot(hxy, z)
    el = np.arctan2(z, hxy)
    az = np.arctan2(y, x)
    return(az, el, r)

def sph2cart(az, el, r):
    rcos_theta = r * np.cos(el)
    x = rcos_theta * np.cos(az)
    y = rcos_theta * np.sin(az)
    z = r * np.sin(el)
    return(x, y, z)

def drawarrow(vec, name):
    #inverts this to the other side of the origin
    az, el, r = cart2sph(float(vec[0]), float(vec[1]), float(vec[2]))
    endxyz = sph2cart(az, el, -(4))
    startxyz = sph2cart(az, el, -(5.5))
    conexyz = sph2cart(az, el, -(3.5))

    conergb = [1.0, 1.0, 0.0]
    arrow = []
    # arrow += [BEGIN, POINTS]
    arrow += [CYLINDER]
    arrow += startxyz
    arrow += endxyz
    arrow += [0.1] # arrow radius
    arrow += conergb
    arrow += conergb
    arrow += [CONE]
    arrow += endxyz
    arrow += conexyz
    arrow += [0.4, 0.0] #cone radius
    arrow += conergb
    arrow += conergb
    arrow += [1.0, 0.0]
    # arrow += [END]
    cmd.load_cgo(arrow, name)

cmd.set("grid_mode", 1)
cmd.bg_color("white")
counter = 1
for i in namelist:
    cmd.load(f"/Volumes/MonARCH/honours/na1/na1-efield/density-diff/geom.pdb", object=f"{i}-geom")
    preset.simple(selection='all')
    # preset.default(selection='all')
    cmd.color("grey40", "all")
    cmd.color("atomic", "(not elem C)")
for i in namelist:
        cmd.load(f"/Volumes/MonARCH/honours/na1/na1-efield/density-diff/{i}diff.cube", object=f'{i}-cube')
        cmd.isosurface(f"{i}-surf", f"{i}-cube", level=0.0002)
        cmd.color("tv_red", f"{i}-surf")
        cmd.set("surface_negative_color", "tv_blue")
        cmd.set("surface_negative_visible")
        cmd.set("transparency", 0.1)
        vec = vecdict[i]
        az, el, r = cart2sph(vec[0], vec[1], vec[2])
        x, y, z = sph2cart(az, el, -r)
        drawarrow([x, y, z], f'{i}-arrow')
        cmd.group(f"{i}-group", f"{i}-surf {i}-cube {i}-geom {i}-arrow")
        cmd.set("state", counter, f"{i}-group")
        counter += 1

cmd.reset()

cmd.set_view((\
     0.782635033,   -0.234382242,    0.576667368,\
     0.082216680,    0.957210958,    0.277468204,\
    -0.617026389,   -0.169743255,    0.768418312,\
     0.000000546,   -0.000000177,  -30.818422318,\
     0.044756040,   -0.442756981,    0.156704724,\
  -32057.304687500, 32118.925781250,  -20.000000000 ))

