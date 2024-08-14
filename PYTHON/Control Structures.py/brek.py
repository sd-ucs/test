counter = 0
for i in range(1, 50):
 if i % 2 == 0:  
    counter += 1
 if counter > 10:
    print ("C", (counter))
    break