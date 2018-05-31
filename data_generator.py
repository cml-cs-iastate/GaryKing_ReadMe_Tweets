import os
import csvfile


with open('new_ground_truth.csv', newline = '') as csvfile:
    data = csv.reader(csvfile)
    row_id = 1
    for row in data:
        tweet = row[0]
        truth = row[2]
        if id != 'hand_topic_id':
            filename = './tweets/' + str(row_id) + '.txt'
            file = open(filename, 'w')
            file.write(tweet)
            file.close()

            row_id += 1
