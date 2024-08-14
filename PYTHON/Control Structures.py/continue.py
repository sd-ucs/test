counter = 0
for i in range(1, 50):
 if i % 2 != 0:
  continue
print ("I"), i
counter += 1
print ("c"),counter