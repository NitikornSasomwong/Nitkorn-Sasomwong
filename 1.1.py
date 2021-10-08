
all = "ddhjdghhdf"
AA = "N"
for i in range(len(all)):

    threeCharChk = "fgh"
    threeall = all[i:i+3]

    if (threeCharChk == threeall):
        AA ="Y"
        print("1")
        break;
    else:
        AA = "Z"
        print("-1")



