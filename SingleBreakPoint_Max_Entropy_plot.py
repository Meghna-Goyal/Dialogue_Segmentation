import re

import numpy as np
#import xlsxwriter
from matplotlib import pyplot as plt


# workbook = xlsxwriter.Workbook('./Max_ent.xlsx')
# worksheet = workbook.add_worksheet('Ent_brkpnt')
#row = 0


# Reading the text file
file = open("corpus2.txt", "r")
lines = file.readlines()
file.close()


# def writetoexcel(pos, entropy):
#     global row
#     worksheet.write(row, 0, pos)
#     worksheet.write(row, 1, entropy)
#     row += 1


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
def maximum_ent(single_row_array, dialogue_typ, dia_count):
    pass
    position = []
    entropy = []
    for x in range(0, single_row_array.size-1):
        first_segment = single_row_array[:x + 1]  # division of the single row(first segment)
        second_segment = single_row_array[x + 1:]  # division of the single row(second segment)
        first_ent_sum = ent_segment(first_segment)  # function call for first segment
        second_ent_sum = ent_segment(second_segment)  # function call for second segment
        final_ent = abs(first_ent_sum) + abs(second_ent_sum)
        #writetoexcel(x, final_ent)
        position.append(x+1)
        entropy.append(final_ent)
    print("(" + dialogue_typ + str(entropy) + ")")
    plt.figure(figsize=(15, 7))
    plt.plot(position, entropy, '-o')
    plt.xlabel("Segmentation Break Point")
    plt.ylabel("Entropy")
    plt.title(dialogue_typ)
    plt.xticks(np.arange(0, len(position)+1, 1))
    plt.savefig('SingleBP_plots/' + "Dialogue" + str(dia_count), figurewidth='25cm')
    plt.clf()


# main loop read the text from the file line by line and calling the function to calculate max_ent and position for
# critical change
count = 1
for line in lines:
    single_row1 = line.rstrip('\n')
    # getting the required information from the single read record
    delimiter = " "
    single_row = delimiter.join(single_row1.split(delimiter, 3)[3:])[:-2]
    #single_row = delimiter.join(single_row1.split(delimiter, 3)[3:])[-6:]
    dialogue_str = str(re.findall(r'"([^"]*)"', single_row1))
    single_row_arr = np.array(list(single_row.split(" ")))
    # function call for maximum entropy
    maximum_ent(single_row_arr, dialogue_str, count)
    count = count +1
#workbook.close()