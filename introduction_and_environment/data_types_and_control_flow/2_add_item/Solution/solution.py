from provided_code import d
# Code your solution here
key_list = d.keys()
for i in range(0, 5):
    if key_list[i] != (i + 1):
        d[i + 1] = "found it!"
        break