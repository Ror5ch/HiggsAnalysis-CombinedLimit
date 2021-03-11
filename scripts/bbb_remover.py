import sys

card_name = sys.argv[1]

original = open(card_name, "r")
skimmed = open(card_name+".skim", "w")

for line in original.readlines():
    if line.find("_bin_") != -1:
        if line.find("group") != -1:
            line = line.replace(syst_name, "")
        else:
            continue

    skimmed.write(line)

original.close()
skimmed.close()