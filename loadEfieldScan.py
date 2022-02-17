# run /Users/adrea/gdrive/Scripts/PyMol/loadEfieldScan.py
path = "/Volumes/MonARCH/honours/na1/benchmarking/field-strength/static-gas"
for i in range(1, 14):
    for j in ["r", "t", "p"]:
        try:
            cmd.load("{}/{}-efield-strength-bench-sg/{}-efield-strength-bench-sg_job{}.xyz".format(path, j, j, i), object=j, state=i-1)
        except:
            pass

preset.simple(selection='all')
cmd.color("grey40", "all")
cmd.color("atomic", "(not elem C)")

cmd.set("grid_slot", 1, "r")
# cmd.set("grid_slot", 2, "t")
# cmd.set("grid_slot", 3, "p")