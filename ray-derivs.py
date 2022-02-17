namelist = ["o-o", "o-nh", "o-no", "nh-o", "nh-nh", "nh-no", "no-o", "no-nh", "no-no"]
# namelist = ["o-o"]
for i in namelist:
    for j in ["r", "s"]:
        cmd.set_view((\
            0.125949576,   -0.907993615,    0.399601609,\
            0.285401076,    0.418947816,    0.861990750,\
            -0.950097322,    0.005480183,    0.311910778,\
            0.000000218,   -0.000000216,  -44.463024139,\
            0.766749442,   -0.583470941,    0.062541738,\
        -28834.845703125, 28923.759765625,  -20.000000000 ))
        cmd.disable(name='*')
        cmd.enable(name=f'{i}-{j}-group')
        cmd.enable(name=f'{i}-{j}-geom')
        cmd.enable(name=f'{i}-{j}-surf')
        cmd.enable(name=f'{i}-{j}-arrow')
        cmd.png(f'/Users/adrea/gdrive/Monash/BsC Chemistry Honours/Milestones/Writing/Figures/Deriv-EDD/{i}-{j}.png', width=580, height=814, dpi=50, ray=1, quiet=0)
        # cmd.ray(1740, 2442, renderer=-1)