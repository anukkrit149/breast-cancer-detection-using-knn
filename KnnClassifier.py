import numpy as np
# from sklearn import preprocessing,neighbors,model_selection
import pandas as pd
from collections import Counter
import random
# import math
import warnings


def k_nearest_neighbours(train_data, predict, k=3):
    if len(train_data) >= k:
        warnings.warn('K is lower than total classes')
    dist = list()
    for data_class in train_data:
        for features in train_data[data_class]:
            euclidean_dist = np.linalg.norm(np.array(features) - np.array(predict))
            dist.append([euclidean_dist, data_class])
    votes = [i[1] for i in sorted(dist)[:k]]
    print('Prediction')
    print("Class-", Counter(votes).most_common(1)[0][0])
    print("Confidence-", Counter(votes).most_common(1)[0][1] / k)
    # votes_result = Counter.most_common(1)[0][0]
    # confidence = int(Counter.most_common(1)[0][1]) / k
    #
    # print(votes_result,confidence)
    # #
    # return votes_result, confidence


df = pd.read_csv('breast-cancer-wisconsin.txt')

df.replace('?', -9999999, True)
df.replace('0', 2, True)

df = df.drop(columns='id')

data = df.astype(float).values.tolist()

random.shuffle(data)

test_size = 0.2

train_set = {2: [], 4: []}
test_set = {2: [], 4: []}

train_data = data[:-int(test_size * len(data))]
test_data = data[-int(test_size * len(data)):]

for i in train_data:
    train_set[i[-1]].append(i[:-1])
for i in test_data:
    test_set[i[-1]].append(i[:-1])

# correct = 0
# total = 0

for data_class in test_set:
    for data in test_set[data_class]:
        # vote, confidence =\
        k_nearest_neighbours(train_set, data, k=3)
    # if data_class == vote:
    #     correct += 1
    # else:
    #     print(confidence)
    # total += 1
# print('Accuracy:', correct / total)

predict = [5,1,1,1,2,1,3,1,1]
k_nearest_neighbours(train_set, predict, k=5)
