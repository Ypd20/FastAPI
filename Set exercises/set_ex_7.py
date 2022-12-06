set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90,10}
if set1.isdisjoint(set2):
    print ("Set does not have common elements")
else:
    new_set=set1.intersection(set2)
    print("The common element set is:",new_set)