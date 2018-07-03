import baseclasses


shaft = baseclasses.shaft()

# Define cylinder 1
cylinder1 = baseclasses.cylinder(5,10)
shaft.features.append(cylinder1)

# Define cylinder 2
cylinder2 = baseclasses.cylinder(10,20)
shaft.features.append(cylinder2)

# Define cylinder 3
cylinder3 = baseclasses.cylinder()
cylinder3.diameter = 5
cylinder3.length = 10

shaft.features.append(cylinder3)

count = 0 

for feature in shaft.features:
    count = count + 1
    print("Cylinder " + str(count) + " => " + "Dia: " + str(feature.diameter) + " Length: " + str(feature.length))
    print("  volume = ", feature.get_volume)

#-- Display some info about the Shaft, which are derived from the Cylinder objects
#-- of which it is made of.
print("\nTotal Volume: %f cubic units" % shaft.get_volume())
print("\nOverall Length: %s" % shaft.get_length())