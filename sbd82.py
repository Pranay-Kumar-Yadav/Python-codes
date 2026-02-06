#iterator or iterable
object1 = iter(eval(input("enter object")))
object_dir = dir(object1)
if '__iter__' in object_dir and '__next__' in object_dir:
    print("iterable operations goes here")
elif '__iter__' in object_dir:
    print("iterable operations goes here")
else:
    print("not supported")