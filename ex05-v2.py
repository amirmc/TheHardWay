name = 'Amir Chaudhry'
age = 31.0 # not a lie
height_cm = 175.0 # cm
weight_kg = 76.0 # kgs
eyes = 'brown'
teeth = 'white'
hair = 'black'

height_in = height_cm*0.3937008
weight_lb = weight_kg*2.20462

print "Let's talk about %s." % name
print "He's %d cm tall." % height_cm
print "That's", height_in, "in imperial units"
print "That's {0:g} inches, in imperial units" .format(height_in)
print "He's %d kgs heavy." % weight_kg
print "Also known as {0:g}lbs." .format(weight_lb)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add {0:g}, {1:g}, and {2:g} I get {3:g}.".format(age, height_cm, weight_kg,
                                                             age + height_cm + weight_kg)
