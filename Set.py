# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.

# Sets are written with curly brackets.
Aset = {"ali","ahmad","shabib","ibtesam","mauzam","mukaram"}
print(Aset)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
# And Duplicate values will be ignored:
thisset = {"apple","orange","cherry","apple",True,1,2,False,0}
print(thisset,len(thisset))

# It is also possible to use the set() constructor to make a set.
myset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(myset,type(myset)) 