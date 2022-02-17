derivs = ['o', 'nh', 'no']
names = []
minnums = []

counter = 1
cmd.set("grid_mode", 1)
for i in derivs:
    for j in derivs:
        if f'{i}{j}' != 'oo':
            scsv = f'/Volumes/MonARCH/honours/na1/na1-efield/relaxed-derivatives/s-na1t-{i}-{j}-1/efield_perturbation.csv'
            rcsv = f'/Volumes/MonARCH/honours/na1/na1-efield/relaxed-derivatives/r-na1t-{i}-{j}-1/efield_perturbation.csv'
            minnum = plotEField(rcsv, vecCSVS=scsv, diff=True, name=f'-{i}-{j}', highlightstereo="s")
            # cmd.load(f'/Volumes/MonARCH/honours/na1/na1-efield/relaxed-derivatives/r-na1t-{i}-{j}-1/geoms/{minnum}/geom_{minnum}.xyz', object=f"r-na1t-{i}-{j}")
            cmd.load(f'/Volumes/MonARCH/honours/na1/na1-efield/relaxed-derivatives/s-na1t-{i}-{j}-1/geoms/{minnum}/geom_{minnum}.xyz', object=f"s-na1t-{i}-{j}")
            preset.simple(selection='all')
            cmd.color("grey40", "all")
            cmd.color("atomic", "(not elem C)")
            cmd.group(f'{i}-{j}', f'max_perturbed_dipole-{i}-{j} molecular_dipole-{i}-{j} max_stabilisation-{i}-{j} field_points-{i}-{j} ramplabel-{i}-{j} rampmin-{i}-{j} rampmax-{i}-{j} ramp-{i}-{j} r-na1t-{i}-{j} s-na1t-{i}-{j} diff-{i}-{j} max_perturbed_dipole-{i}-{j} molecular_dipole_label-{i}-{j} diff-{i}-{j} max_perturbed_dipole_label-{i}-{j} molecular_dipole_label-{i}-{j} best_s_selection-{i}-{j} slabel-{i}-{j}')
            # cmd.set(f'{i}-{j}', state=counter)
            cmd.set("grid_slot", counter, f'{i}-{j}')
            counter += 1
            names += [f'{i}-{j}']
            minnums += [minnum]

cmd.reset()

for i in range(len(names)):
    print(f'{names[i]}: {minnums[i]}')

# for i in range(1,33):
#     cmd.set("grid_mode", 1)
#     cmd.load("{}/{}/geom_{}.xyz".format(rpath, i, i), object="na1t-r", state=i)
#     cmd.load("{}/{}/geom_{}.xyz".format(spath, i, i), object="na1t-s", state=i)
#     preset.simple(selection='all')
#     cmd.color("grey40", "all")
#     cmd.color("atomic", "(not elem C)")
#     plotEField(rcsv, name="-2", state=i, highlightvec=i)
#     plotEField(scsv, name="-3", state=i, highlightvec=i)

#     cmd.group("R", "max_perturbed_dipole-2 molecular_dipole-2 max_stabilisation-2 field_points-2 ramplabel-2 rampmin-2 rampmax-2 ramp-2 na1t-r Dt-r Dt2-r ESP-r espcol-r diff-2 max_perturbed_dipole-2 molecular_dipole_label-2 diff-2 max_perturbed_dipole_label-2 molecular_dipole_label-2")
#     cmd.group("S", "max_perturbed_dipole-3 molecular_dipole-3 max_stabilisation-3 field_points-3 ramplabel-3 rampmin-3 rampmax-3 ramp-3 na1t-s Dt-s Dt2-s ESP-s espcol-s diff-3 max_perturbed_dipole-3 molecular_dipole_label-3 diff-3 max_perturbed_dipole_label-3 molecular_dipole_label-3")

#     cmd.set("grid_slot", 1, "all")
#     cmd.set("grid_slot", 2, "S")
#     cmd.reset()


