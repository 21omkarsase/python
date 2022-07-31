import enum


l = ["bhindi", "aaloo", "tomato", "chopsticks", "chowmein"]

# for item in l:
#     if(l.index(item) % 2 != 0):
#         continue
#     print(item)


# using enumerate function
for index, item in enumerate(l):
    if(index % 2 == 0):
        print(item, end=" ")
