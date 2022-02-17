def diff(r, s):
    rpath = r + "/geoms"
    spath = s + "/geoms"
    rcsv = r + "/efield_perturbation.csv"
    scsv = s + "/efield_perturbation.csv"
    rbest = 0

    # 
    cmd.set("grid_mode", 1)
    highlightrvec = plotEField(rcsv, vecCSVS=scsv, name="-2", highlightstereo="r", diff=True)
    highlightsvec = plotEField(rcsv, vecCSVS=scsv, name="-3", highlightstereo="s", diff=True)
    highlightvec = plotEField(rcsv, vecCSVS=scsv, name="-1", diff=True)

    cmd.load("{}/{}/geom_{}.xyz".format(rpath, highlightrvec, highlightrvec), object="na1t-r")
    cmd.load("{}/{}/geom_{}.xyz".format(spath, highlightsvec, highlightsvec), object="na1t-s")
    cmd.load("{}/geom_0.xyz".format(spath), object="na1t")


    # cmd.load("{}/geom_{}.xyz".format(spath, highlightrvec), object="na1t-r")
    # cmd.load("{}/geom_{}.xyz".format(spath, highlightsvec), object="na1t-s")
    # cmd.load("{}/geom_{}.xyz".format(spath, highlightvec), object="na1t")
    preset.simple(selection='all')
    cmd.color("grey40", "all")
    cmd.color("atomic", "(not elem C)")




    cmd.load("{}/{}/Dt.cube".format(rpath, highlightrvec), object="Dt-r")
    cmd.load("{}/{}/Dt.cube".format(spath, highlightsvec), object="Dt-s")
    cmd.load("{}/{}/ESP.cube".format(rpath, highlightrvec), object="ESP-r")
    cmd.load("{}/{}/ESP.cube".format(spath, highlightsvec), object="ESP-s")

    cmd.isosurface("Dt2-r", "Dt-r", level=0.002)
    cmd.isosurface("Dt2-s", "Dt-s", level=0.002)

    cmd.ramp_new("espcol-r", "ESP-r", range=[-.05,-.025,0,.025,.05], color=["red", "orange", "yellow", "green", "blue"])
    cmd.ramp_new("espcol-s", "ESP-s", range=[-.05,-.025,0,.025,.05], color=["red", "orange", "yellow", "green", "blue"])
    cmd.disable("espcol-r espcol-s")

    cmd.set("surface_color", "espcol-r", "Dt2-r")
    cmd.set("surface_color", "espcol-s", "Dt2-s")
    cmd.set("transparency", 0.3)

    cmd.group("diff", "max_perturbed_dipole-1 molecular_dipole-1 max_stabilisation-1 field_points-1 ramplabel-1 rampmin-1 rampmax-1 ramp-1 na1t max_perturbed_dipole-1 molecular_dipole_label-1 diff-1 rlabel-1 slabel-1 best_r_selection-1 best_s_selection-1  molecular_dipole_label-1 perturbed_dipole_label-1 max_perturbed_dipole_label-1")
    cmd.group("R", "max_perturbed_dipole-2 molecular_dipole-2 max_stabilisation-2 field_points-2 ramplabel-2 rampmin-2 rampmax-2 ramp-2 na1t-r Dt-r Dt2-r ESP-r espcol-r diff-2 rlabel-2 molecular_dipole_label-2 perturbed_dipole_label-2 max_perturbed_dipole_label-2 best_r_selection-2")
    cmd.group("S", "max_perturbed_dipole-3 molecular_dipole-3 max_stabilisation-3 field_points-3 ramplabel-3 rampmin-3 rampmax-3 ramp-3 na1t-s Dt-s Dt2-s ESP-s espcol-s diff-3 rlabel-3 molecular_dipole_label-3 perturbed_dipole_label-3 max_perturbed_dipole_label-3 best_s_selection-3 slabel-3")

    cmd.set("grid_slot", 1, "all")
    cmd.set("grid_slot", 2, "diff")
    cmd.set("grid_slot", 3, "S")
    cmd.reset()


