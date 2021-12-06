import numpy as np

# Reading the text file
file = open("corpus_test.txt", "r")
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
        ent = prob * (np.log(prob))
        ent_seg = ent_seg + ent
    return ent_seg


# segmentation of the input array and the maximum entropy calculation
def maximum_ent(single_row_array, dialogue_str):
    pass
    max_ent = 0
    pos1 = 0
    pos2 = 0
    count = 0
    for x in range(0, single_row_array.size - 2):
        first_segment = single_row_array[:x + 1]  # division of the single row(first segment)
        second_segment = single_row_array[x + 1:]  # division of the single row(second segment)
        for y in range(0, second_segment.size - 1):
            middle_segment = second_segment[:y + 1]  # division of the second segment(middle segment)
            third_segment = second_segment[y + 1:]  # division of the second segment(third   segment)
            first_ent_sum = ent_segment(first_segment)  # function call for first segment
            middle_ent_sum = ent_segment(middle_segment)  # function call for middle segment
            third_ent_sum = ent_segment(third_segment)  # function call for third segment
            final_ent = abs(first_ent_sum) + abs(middle_ent_sum) + abs(third_ent_sum)
            print("(" + dialogue_str + " " + str(x + 1) + " " + str(x+y+2) + " " + str(final_ent) + ")")
            if final_ent > max_ent:
                max_ent = final_ent
                pos1 = x
                pos2 = x + y + 2
            count = count + 1  # number of permutation combinations for 2 segmentation
    print("(" + dialogue_str + " " + str(pos1 + 1) + " " + str(pos2) + " " + str(max_ent) + ")")
    print(count)


# main loop read the text from the file line by line and calling the function to calculate max_ent and position for
# critical change
for line in lines:
    single_row1 = line.rstrip('\n')
    # getting the required information from the single read record
    delimiter = " "
    single_row = delimiter.join(single_row1.split(delimiter, 3)[3:])[:-2]
    dialogue_str = delimiter.join(single_row1.split(delimiter, 3)[:3])[-7:]
    single_row_arr = np.array(list(single_row.split(" ")))
    # function call for maximum entropy
    maximum_ent(single_row_arr, dialogue_str)
