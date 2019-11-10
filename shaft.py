import baseclasses


shaft = baseclasses.shaft()


def _input(message,in_type=float):
    while True:
      try:
        return in_type (input(message))
      except:
        shaft_input()


def shaft_input():
    in_diameter = _input("Please enter cylinder diameter: ", float)
    in_length = _input("Please enter cylinder length: ", float)
    cylinder = baseclasses.cylinder(in_diameter, in_length)
    shaft.add_feature(cylinder)
    in_continue = input("Would you like to enter another cylinder? (y/n): ")
    if in_continue == "y":
        shaft_input()
    else:
        display_results()


#-- Display some info about the Shaft, which are derived from the Cylinder objects
#-- of which it is made of.
def display_results():
    count = 0

    for feature in shaft.features:
        count = count + 1
        print("Cylinder " + str(count) + " => " + "Dia: " + str(feature.diameter) + " Length: " + str(feature.length))
        print("  volume = ", feature.get_volume())

    print("\nTotal Volume: %f cubic units" % shaft.get_volume())
    print("\nOverall Length: %s" % shaft.get_length())
    print("\nWeight: %f (lbs): " % shaft.weight)


if __name__ == '__main__':
    shaft_input()

