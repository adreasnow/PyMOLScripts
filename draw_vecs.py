import numpy as np

cmd.set("grid_mode", 1)
cmd.bg_color("white")

def drawarrow(vec, name, color, multiplier):
    az, el, r = cart2sph(float(vec[0]), float(vec[1]), float(vec[2]))
    magnitude = r*multiplier
    endxyz = sph2cart(az, el, (4))
    startxyz = sph2cart(az, el, (5.5+magnitude))
    conexyz = sph2cart(az, el, (3.5))
    endxyz = [endxyz[0]-1, endxyz[1]+1, endxyz[2]]
    startxyz = [startxyz[0]-1, startxyz[1]+1, startxyz[2]]
    conexyz = [conexyz[0]-1, conexyz[1]+1, conexyz[2]]

    color = list(np.divide(color, 256))
    conergb = color
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

fieldcolour=[252, 186, 3]
dipolecolour=[3, 140, 252]
perturbeddipolecolour=[245, 66, 132]

perturbations = ['c', 'r', 's']
species = ['ethanol', 'ethanol-2', 'ethanol-deriv', 'ethanol-deriv-2', 'ethanol-nh2', 'ethanol-nh2-2']

# /Volumes/MonARCH/honours/na1/benchmarking/relaxed/ethanol-2/na1t-s/scratch/c/c_trj.xyz

fields = {
    'c' : [0.00106120124951941, -0.0036990209183248154, 0.0005642507137444658],
    'r' : [-0.0006753838835499315, 0.0, -0.003830292328790097],
    's' : [-0.0006753838835499315, 0.0, 0.003830292328790097]
}

dipoles = {
    'ethanol-deriv' : [
        [-0.62990, -3.89763, 1.86070], #uncatalysed
        [-0.24166, -6.41074, 1.43790], #catalysed
        [-0.91853, -5.66925, 0.21301], #R
        [-1.10702, -3.96064, 2.38391] #S
    ],
    'ethanol-deriv-2' : [
        [-0.62990, -3.89763, 1.86070], #uncatalysed
        [ 0.20440, -5.50034, 2.37580], #catalysed
        [-1.16221, -3.71160, 0.73176], #R
        [-1.31626, -4.25653, 2.74679] #S
    ],
    'ethanol' : [
        [-0.62990, -3.89763, 1.86070], #uncatalysed
        [-0.47155, -4.69582, 2.02231], #catalysed
        [-0.82177, -4.34462, 0.89730], #R
        [-0.75087, -4.28613, 2.04706] #S
    ],
    'ethanol-2' : [
        [-0.63345, -4.38667, 1.32953], #uncatalysed
        [-0.68278, -4.65056, 2.95153], #catalysed
        [-1.02214, -4.24760, 0.55887], #R
        [-0.87107, -4.17219, 2.85358] #S
    ],
    'ethanol-nh2' : [
        [-0.44258, -5.32601, 1.08900], #uncatalysed
        [-0.05952, -5.88581, 2.19393], #catalysed
        [-0.75630, -5.22033, 0.46885], #R
        [-0.52595, -5.22306, 2.15186] #S
    ],
    'ethanol-nh2-2' : [
        [-0.44258, -5.32601, 1.08900], #uncatalysed
        [ 0.97963, -6.65455, 1.98421], #catalysed
        [-1.10803, -5.07803, 0.01016], #R
        [-0.44867, -5.06848, 3.31936] #S
    ],
}

for i in species:
    for j in perturbations:
        try:
            cmd.load(f"/Volumes/MonARCH/honours/na1/benchmarking/relaxed/{i}/na1t-s/scratch/{j}/{j}.xyz", f"geom-{i}-{j}")
        except:
            pass


for i in species:
    for j in perturbations:
        # cmd.load(f"/Volumes/MonARCH/honours/na1/benchmarking/relaxed/{i}/na1t-s/scratch/{j}/{j}.xyz", f"geom-{i}-{j}")
        drawarrow(fields[j], f"oeef-{i}-{j}", fieldcolour, 200)
        drawarrow(dipoles[i][0], f"u-u-{i}-{j}", dipolecolour, 0.1)
        try:
            if j == 'c':
                drawarrow(dipoles[i][1], f"u-p-{i}-{j}", perturbeddipolecolour, 0.3)
            elif j == 'r':
                drawarrow(dipoles[i][2], f"u-p-{i}-{j}", perturbeddipolecolour, 0.3)
            elif j == 's':
                drawarrow(dipoles[i][3], f"u-p-{i}-{j}", perturbeddipolecolour, 0.3)
        except:
            pass

for i in species:
    for j in perturbations:
        cmd.group(f"group-{i}-{j}", f"geom-{i}-{j} oeef-{i}-{j} u-u-{i}-{j} u-p-{i}-{j}")
        
preset.simple(selection='all')
cmd.color("grey40", "all")
cmd.color("atomic", "(not elem C)")
cmd.remove("elem -")
cmd.valence("guess", "all")
cmd.reset()
cmd.set_view((\
     0.870013416,   -0.073984385,    0.487444848,\
    -0.001913203,    0.988160372,    0.153397292,\
    -0.493023008,   -0.134389311,    0.859572709,\
     0.000001709,    0.000005405,  -34.945766449,\
     0.742949963,   -0.863646269,    0.933203876,\
  -4040.973876953, 4110.864257812,  -20.000000000 ))

# for i in species:
#     for j in perturbations:
#         cmd.disable("all")
#         cmd.enable(f"*-{i}-{j}")

cmd.set("label_position", [0, -1.5, 0])
cmd.set("label_digits",  3)
cmd.set("label_size",  30)
cmd.set("label_font_id",  9)