perturbations = ['c', 'r', 's']
species = ['ethanol', 'ethanol-2', 'ethanol-deriv', 'ethanol-deriv-2', 'ethanol-nh2', 'ethanol-nh2-2']
species_dict = {'ethanol' : "h-1-",
                'ethanol-2' : "h-2-",
                'ethanol-deriv': "no2-1",
                'ethanol-deriv-2': "no2-2",
                'ethanol-nh2': "nh2-1",
                'ethanol-nh2-2': "nh2-2"
                }

for i in species:
    for j in perturbations:
        cmd.disable("all")
        cmd.enable(f"*-{i}-{j}")
        cmd.ray()
        cmd.png(f'/Users/adrea/gdrive/Monash/BsC\ Chemistry\ Honours/Milestones/Writing/Figures/final-geoms/{species_dict[i]}-{j}.png')