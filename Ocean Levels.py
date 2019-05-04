ocean levels
rpy = 1.6
total_risen = 0
for i in range(1,26):
    total_risen += rpy
    print("In year {} the ocean level will rise {:.1f} mm".format(i,total_risen))
