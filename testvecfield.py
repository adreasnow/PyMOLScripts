import numpy as np
from csv import reader

from pymol.cgo import *
from pymol import cmd


def loadvecfield(vecCSV, bubble=5, radius=0.2, alpha=1, pointcolour="a0a0a0"):
    def hex2rgb(hex):
        r = (int(hex[0:2], 16))/255
        g = (int(hex[2:4], 16))/255
        b = (int(hex[4:6], 16))/255
        return([r, g, b])

    def cart2sph(x, y, z):
        hxy = np.hypot(x, y)
        r = np.hypot(hxy, z)
        el = np.arctan2(z, hxy)
        az = np.arctan2(y, x)
        return az, el, r

    def sph2cart(az, el, r):
        rcos_theta = r * np.cos(el)
        x = rcos_theta * np.cos(az)
        y = rcos_theta * np.sin(az)
        z = r * np.sin(el)
        return x, y, z

    # reads in the CSV of x, y, z, energy
    with open(vecCSV, "r") as f:
        vecs = list(reader(f))[1:]

    # extracts only the energy
    e = []
    for i in vecs[1:]:
        e += [float(i[3])]
    # shifts all the values up to make them positive
    e = np.add(0 - min(e), e)

    # builds the cgo sphere opbjects
    sphere = []
    for i in range(1, len(vecs)):
        r, g, b = hex2rgb(pointcolour)
        az, el, rad = cart2sph(float(vecs[i][0]), float(vecs[i][1]), float(vecs[i][2]))
        # inverts the data so that the points are showing where the valuse are coming from 
        x, y, z = sph2cart(az, el, -bubble)
        sphere += [BEGIN, POINTS]
        sphere += [END]
        sphere += [ALPHA, alpha]
        sphere += [COLOR, r, g, b]
        sphere += [SPHERE, x, y, z, radius]


    cmd.load_cgo(sphere,'field_points2')
    
    cmd.reset()
