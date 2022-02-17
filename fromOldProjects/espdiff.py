import numpy as np
from pymol.cgo import *
from pymol import cmd
namelist = ["o-o", "o-nh", "o-no", "nh-o", "nh-nh", "nh-no", "no-o", "no-nh", "no-no"]
vecnumlist = [76, 23, 76, 84, 84, 76, 76, 76, 76] 
vecdict = {76 : [-0.000337691941, 4.13553354e-20, -0.00191514616], 84 : [0.000330312562, -0.000404323865, 0.00187329563], 23 : [-0.00117110771, 0.000404323865, -0.00149894951]}

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
    for j in ["r", "s"]:
        cmd.load(f"/Volumes/MonARCH/honours/na1/benchmarking/derivative-edd/{i}/S/geom.xyz", object=f"{i}-{j}-geom")
        preset.simple(selection='all')
        # preset.default(selection='all')
        cmd.color("grey40", "all")
        cmd.color("atomic", "(not elem C)")
for i in namelist:
    for j in ["r", "s"]:
        cmd.load(f"/Volumes/MonARCH/honours/na1/benchmarking/derivative-edd/{i}/{j}diff.cube", object=f'{i}-{j}-cube')
        cmd.isosurface(f"{i}-{j}-surf", f"{i}-{j}-cube", level=0.0002)
        cmd.color("tv_red", f"{i}-{j}-surf")
        cmd.set("surface_negative_color", "tv_blue")
        cmd.set("surface_negative_visible")
        cmd.set("transparency", 0.1)
        cmd.group(f"{i}-{j}-group", f"{i}-{j}-surf {i}-{j}-cube {i}-{j}geom")
        cmd.set("state", counter, f"{i}-{j}-group")
        counter += 1

for i in range(len(namelist)):
    vecnum = vecnumlist[i]
    vec = vecdict[vecnum]
    name = namelist[i]
    drawarrow(vec, f'{name}-s-arrow')
    az, el, r = cart2sph(vec[0], vec[1], vec[2])
    x, y, z = sph2cart(az, el, -r)
    drawarrow([x, y, z], f'{name}-r-arrow')
    cmd.group(f"{name}-s-group", f'{name}-s-arrow')
    cmd.group(f"{name}-r-group", f'{name}-r-arrow')
    
counter = 1
for i in namelist:
    for j in ["s", "r"]:
        cmd.set("state", counter, f"{i}-{j}-group")
        counter += 1

cmd.reset()

cmd.set_view((\
     0.782635033,   -0.234382242,    0.576667368,\
     0.082216680,    0.957210958,    0.277468204,\
    -0.617026389,   -0.169743255,    0.768418312,\
     0.000000000,    0.000000000,  -36.820232391,\
     0.085400105,   -0.267166615,    0.062833309,\
  -32051.296875000, 32124.933593750,  -20.000000000 ))

