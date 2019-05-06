
# i=1 #while loop practice
# while i<=5:
#     print("Tamil",end= " ")
#     j=1
#     while j<=5:
#         print("Rockers", end=" ")
#         j=j+1
#
#     i=i+1
#     print()

# Print all the numbers between 1 to 100 and skip the numbers which are divisible by 3 or 5

# i=1
# while i<=100:
#     i%3!=0 or i%5!=0
#     print(i)
#     i = i + 1



#print pattern #####  using while loop
               #####
               #####
               #####

# i=1
# while i<=5:
#     print('#',end=" ")
#     # j=1
#     # while j<=4:
#     #     print('#')
#     #     j=j+1
#     i=i+1
# print()

# Print perfect square between 1 to 500 using FOR loop
# for j in range(1,500,10): # range(start,end, iteration(increment))
#     #if j(%!=10):
#
#     print (j)

# Print pattern   1 2 3 4           A P Q R       # # # #      # # # #            #
#                 2 3 4             A B Q R       # # # #      # # #              # #
#                 3 4               A B C R       # # # #      # #                # # #
#                 4                 A B C D       # # # #      #                  # # # #

for i in range(1,5):

    for j in range(1-i):
        print("j",end=" ")
    print(+i)

