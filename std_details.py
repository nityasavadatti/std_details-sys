import sys
if len(sys.argv)==3:
   script_name=sys.argv[0]
   name=sys.argv[1]
   rollno=sys.argv[2]
   print("User provided input values:")
else:
   script_name=sys.argv[0]
   name="nitya"
   rollno="174"
   print("No input given-using default values:")
print("script_name:",script_name)
print( "Student Name:",name)
print("Roll Number:",rollno)
