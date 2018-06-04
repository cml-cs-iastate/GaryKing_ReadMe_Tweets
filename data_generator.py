import os
import csv


with open('../new_ground_truth.csv', newline = '') as csvfile:
    data = csv.reader(csvfile)

    row_id = 1
    control_file = open('./tweets/control.txt', 'w')
    control_file.write('ROWID,TRUTH,TRAININGSET\n')
    for row in data:
        tweet = row[0]
        truth = row[2]
        if truth != '0':
            if truth != 'hand_topic_id':
                filename = './tweets/' + str(row_id) + '.txt'
                short_filename = str(row_id) + '.txt'
                file = open(filename, 'w')
                file.write(tweet)
                file.close()
                control_file.write(short_filename + ',' + str(truth) + ',')
                trainingset = 0
                if row_id < 15190 * 0.9:
                    trainingset = 1
                control_file.write(str(trainingset) + '\n')
                row_id += 1
    control_file.close()
