import numpy as np

# Reading the text file
file = open("corpus2.txt", "r")
lines = file.readlines()
file.close()


# calculating the entropy for the segment of the array
def ent_segment(seg):
    pass
    ent_seg = 0
    unique, counts = np.unique(seg, return_counts=True)
    # calculating the number of occurrences of a unique dialogue type
    occ1 = np.array(list(dict(zip(unique, counts)).values()))
    # loop to access each occurrence value from the array of occurrences
    for index in range(0, occ1.size):
        prob = np.divide(occ1[index], seg.size)
        ent = prob * (np.log10(prob))
        ent_seg = ent_seg + ent
    return ent_seg


# segmentation of the input array and the maximum entropy calculation
def maximum_ent(single_row_array):
    pass
    max_ent = 0
    pos = 0
    for x in range(0, single_row_array.size-1):
        first_segment = single_row_array[:x + 1]   # division of the single row(first segment)
        second_segment = single_row_array[x + 1:]   # division of the single row(second segment)
        first_ent_sum = ent_segment(first_segment)  # function call for first segment
        second_ent_sum = ent_segment(second_segment)  # function call for second segment
        final_ent = abs(first_ent_sum) + abs(second_ent_sum)
        if final_ent > max_ent:
            max_ent = final_ent
            pos = x
    print("index of an element for segment break:" + str(pos) + "\t " + "Max_ent:" + str(max_ent))


# main loop read the text from the file line by line and calling the function to calculate max_ent and position for
# critical change
for line in lines[::]:
    single_row = line.rstrip('\n')
    # getting the required information from the single read record
    delimiter = " "
    single_row = delimiter.join(single_row.split(delimiter, 3)[3:])[:-2]
    single_row_arr = np.array(list(single_row.split(" ")))
    # function call for maximum entropy
    maximum_ent(single_row_arr)

