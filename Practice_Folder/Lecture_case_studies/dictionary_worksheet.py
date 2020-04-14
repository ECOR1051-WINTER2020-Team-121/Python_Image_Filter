# 1.
stud_data = {
    10: 55,
    23: 66.7,
    14: 87
}

# 2.
stud_data[99] = 55
# stud_data.update({900: 4})

# 3.
if 38 in stud_data.keys():
    print("38 is in")
else:
    print("38 is not in")

# 4.
stud_10 = stud_data[10]

# 5.
# stud_38 = stud_data[38]
stud_38 = stud_data.get(38) # Returns None

# 6.



print(stud_data)
