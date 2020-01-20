# -*- coding: utf-8 -*-
"""decisition tree VS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mnELfhBgy2xMfQZ6jm59YItlt_YgfLwR
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd 
import numpy as np 
from sklearn import tree 
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt 
import seaborn as sns 
import io
from scipy import misc
# %matplotlib inline

import graphviz

import pydotplus

data = pd.read_csv("H:\\python jupyter\\aa\\data.csv")

data

data.head()

data.describe()

type(data)

data.max()

data.min()

data.mean()

data.info()

train, test = train_test_split(data, test_size=0.15)

train, test = train_test_split(data, test_size=0.15)

print("Training size {}; Test size: {} ".format(len(train),len(test)))

pos_tempo = data[data['target'] == 1]['tempo']
neg_tempo = data[data['target'] == 0]['tempo']

fig = plt.figure(figsize=(12,8))
plt.title("song Tempo Like / Dislike Distribution")
pos_tempo.hist(alpha = 0.7, bins = 30, label='positive')
neg_tempo.hist(alpha = 0.7, bins = 30, label='negative')
plt.legend(loc= "upper right")

red_blue = ["#195B5E","#EF4836"]
palette = sns.color_palette(red_blue)
sns.set_palette(palette)
sns.set_style("white")

pos_tempo = data[data['target'] == 1]['tempo']
neg_tempo = data[data['target'] == 0]['tempo']

fig = plt.figure(figsize=(12,8))
plt.title("song Tempo Like / Dislike Distribution")
pos_tempo.hist(alpha = 0.7, bins = 30, label='positive')
neg_tempo.hist(alpha = 0.7, bins = 30, label='negative')
plt.legend(loc= "upper right")

pos_tempo = data[data['target'] == 1]['tempo']
neg_tempo = data[data['target'] == 0]['tempo']

fig = plt.figure(figsize=(12,8))
plt.title("song Tempo Like / Dislike Distribution")
pos_tempo.hist(alpha = 0.7, bins = 30, label='positive')
neg_tempo.hist(alpha = 0.7, bins = 30, label='negative')
plt.legend(loc= "upper right")

pos_tempo

fig = plt.figure(figsize=(12,8))
plt.title("song Tempo Like / Dislike Distribution")
pos_tempo.hist(alpha = 0.7, bins = 30, label='positive')
neg_tempo.hist(alpha = 0.7, bins = 30, label='negative')
plt.legend(loc= "upper right")

pos_tempo = data[data['target'] == 1]['tempo']
neg_tempo = data[data['target'] == 0]['tempo']

pos_dance = data[data['target'] == 1]['danceability']
neg_dance = data[data['target'] == 0]['danceability']

pos_duration = data[data['target'] == 1]['duration_ms']
neg_duration = data[data['target'] == 0]['duration_ms']

pos_loudness = data[data['target'] == 1]['loudness']
neg_loudness = data[data['target'] == 0]['loudness']

pos_speechiness = data[data['target'] == 1]['speechiness']
neg_speechiness = data[data['target'] == 0]['speechiness']

pos_valence = data[data['target'] == 1]['valence']
neg_valence = data[data['target'] == 0]['valence']

pos_energy = data[data['target'] == 1]['energy']
neg_energy = data[data['target'] == 0]['energy']

pos_acousticness = data[data['target'] == 1]['acousticness']
neg_acousticness = data[data['target'] == 0]['acousticness']

pos_key = data[data['target'] == 1]['key']
neg_key = data[data['target'] == 0]['key']

pos_instrumentalness = data[data['target'] == 1]['instrumentalness']
neg_instrumentalness = data[data['target'] == 0]['instrumentalness']

pos_tempo

fig = plt.figure(figsize=(12,8))
plt.title("song Tempo Like / Dislike Distribution")
pos_tempo.hist(alpha = 0.7, bins = 30, label='positive')
neg_tempo.hist(alpha = 0.7, bins = 30, label='negative')
plt.legend(loc= "upper right")

fig2 = plt.figure(figsize=(15,15))
ax3 = fig2.add_subplot(331)
ax3.set_xlabel('Danceability')
ax3.set_ylabel('Count')
ax3.set_title('Song Daneability Like Distribution')
pos_dance.hist(alpha = 0.5, bins = 30)
ax4 = fig2.add_subplot(331)
neg_dance.hist(alpha = 0.5, bins = 30)

fig2 = plt.figure(figsize=(15,15))
ax3 = fig2.add_subplot(331)
ax3.set_xlabel('Danceability')
ax3.set_ylabel('Count')
ax3.set_title('Song Daneability Like Distribution')
pos_duration.hist(alpha = 0.5, bins = 30)
ax4 = fig2.add_subplot(331)
neg_duration.hist(alpha = 0.5, bins = 30)

fig2 = plt.figure(figsize=(15,15))
ax3 = fig2.add_subplot(331)
ax3.set_xlabel('Danceability')
ax3.set_ylabel('Count')
ax3.set_title('Song Daneability Like Distribution')
pos_loudness.hist(alpha = 0.5, bins = 30)
ax4 = fig2.add_subplot(331)
neg_loudness.hist(alpha = 0.5, bins = 30)

fig2 = plt.figure(figsize=(15,15))
ax3 = fig2.add_subplot(331)
ax3.set_xlabel('Danceability')
ax3.set_ylabel('Count')
ax3.set_title('Song Daneability Like Distribution')
pos_speechiness.hist(alpha = 0.5, bins = 30)
ax4 = fig2.add_subplot(331)
neg_speechiness.hist(alpha = 0.5, bins = 30)

fig2 = plt.figure(figsize=(15,15))
ax3 = fig2.add_subplot(331)
ax3.set_xlabel('Danceability')
ax3.set_ylabel('Count')
ax3.set_title('Song Daneability Like Distribution')
pos_valence.hist(alpha = 0.5, bins = 30)
ax4 = fig2.add_subplot(331)
neg_valence.hist(alpha = 0.5, bins = 30)

fig2 = plt.figure(figsize=(15,15))
ax3 = fig2.add_subplot(331)
ax3.set_xlabel('Danceability')
ax3.set_ylabel('Count')
ax3.set_title('Song Daneability Like Distribution')
pos_energy.hist(alpha = 0.5, bins = 30)
ax4 = fig2.add_subplot(331)
neg_energy.hist(alpha = 0.5, bins = 30)

fig2 = plt.figure(figsize=(15,15))
ax3 = fig2.add_subplot(331)
ax3.set_xlabel('Danceability')
ax3.set_ylabel('Count')
ax3.set_title('Song Daneability Like Distribution')
pos_key.hist(alpha = 0.5, bins = 30)
ax4 = fig2.add_subplot(331)
neg_key.hist(alpha = 0.5, bins = 30)

fig2 = plt.figure(figsize=(15,15))
ax3 = fig2.add_subplot(331)
ax3.set_xlabel('Danceability')
ax3.set_ylabel('Count')
ax3.set_title('Song Daneability Like Distribution')
pos_acousticness.hist(alpha = 0.5, bins = 30)
ax4 = fig2.add_subplot(331)
neg_acousticness.hist(alpha = 0.5, bins = 30)

fig2 = plt.figure(figsize=(15,15))
ax3 = fig2.add_subplot(331)
ax3.set_xlabel('Danceability')
ax3.set_ylabel('Count')
ax3.set_title('Song Daneability Like Distribution')
pos_instrumentalness.hist(alpha = 0.5, bins = 30)
ax4 = fig2.add_subplot(331)
neg_instrumentalness.hist(alpha = 0.5, bins = 30)

#danceability
fig2 = plt.figure(figsize=(15,15))
ax3 = fig2.add_subplot(331)
ax3.set_xlabel('Danceability')
ax3.set_ylabel('Count')
ax3.set_title('Song Daneability Like Distribution')
pos_dance.hist(alpha = 0.5, bins = 30)
ax4 = fig2.add_subplot(331)
neg_dance.hist(alpha = 0.5, bins = 30)



#Duration
ax5= fig2.add_subplot(332)
pos_duration.hist(alpha = 0.5, bins = 30)
ax5.set_xlabel('Duration(ms)')
ax5.set_ylabel('Count')
ax5.set_title('Song Duration(ms) Like Distribution')
ax6 = fig2.add_subplot(332)
neg_duration.hist(alpha = 0.5, bins = 30)



#Loudness
ax7= fig2.add_subplot(333)
pos_loudness.hist(alpha = 0.5, bins = 30)
ax7.set_xlabel('Loudness(ms)')
ax7.set_ylabel('Count')
ax7.set_title('Song Loudness(ms) Like Distribution')
ax8 = fig2.add_subplot(333)
neg_loudness.hist(alpha = 0.5, bins = 30)


#Speechiness
ax9= fig2.add_subplot(334)
pos_speechiness.hist(alpha = 0.5, bins = 30)
ax9.set_xlabel('Speechiness')
ax9.set_ylabel('Count')
ax9.set_title('Song Speechiness Like Distribution')
ax10 = fig2.add_subplot(334)
neg_speechiness.hist(alpha = 0.5, bins = 30)





#valence
ax11= fig2.add_subplot(335)
pos_valence.hist(alpha = 0.5, bins = 30)
ax11.set_xlabel('valence')
ax11.set_ylabel('Count')
ax11.set_title('Song valence Like Distribution')
ax12 = fig2.add_subplot(335)
neg_valence.hist(alpha = 0.5, bins = 30)


#Energy
ax13= fig2.add_subplot(336)
pos_energy.hist(alpha = 0.5, bins = 30)
ax13.set_xlabel('Energy')
ax13.set_ylabel('Count')
ax13.set_title('Song Energy Like Distribution')
ax14 = fig2.add_subplot(336)
neg_energy.hist(alpha = 0.5, bins = 30)


#Key
ax15= fig2.add_subplot(337)
pos_key.hist(alpha = 0.5, bins = 30)
ax15.set_xlabel('Key')
ax15.set_ylabel('Count')
ax15.set_title('Song Key Like Distribution')
ax15 = fig2.add_subplot(337)
neg_key.hist(alpha = 0.5, bins = 30)



#Acousticness
ax16= fig2.add_subplot(338)
pos_acousticness.hist(alpha = 0.5, bins = 30)
ax16.set_xlabel('Acousticness')
ax16.set_ylabel('Count')
ax16.set_title('Song Acousticness Like Distribution')
ax16 = fig2.add_subplot(338)
neg_acousticness.hist(alpha = 0.5, bins = 30)


#Instrumentalness
ax17= fig2.add_subplot(339)
pos_instrumentalness.hist(alpha = 0.5, bins = 30)
ax17.set_xlabel('Instrumentalness')
ax17.set_ylabel('Count')
ax17.set_title('Song Instrumentalness Like Distribution')
ax17 = fig2.add_subplot(339)
neg_instrumentalness.hist(alpha = 0.5, bins = 30)

#danceability
fig2 = plt.figure(figsize=(15,15))
ax3 = fig2.add_subplot(331)
ax3.set_xlabel('Danceability')
ax3.set_ylabel('Count')
ax3.set_title('Song Daneability Like Distribution')
pos_dance.hist(alpha = 0.5, bins = 30)

neg_dance.hist(alpha = 0.5, bins = 30)



#Duration
ax5= fig2.add_subplot(332)
pos_duration.hist(alpha = 0.5, bins = 30)
ax5.set_xlabel('Duration(ms)')
ax5.set_ylabel('Count')
ax5.set_title('Song Duration(ms) Like Distribution')

neg_duration.hist(alpha = 0.5, bins = 30)



#Loudness
ax7= fig2.add_subplot(333)
pos_loudness.hist(alpha = 0.5, bins = 30)
ax7.set_xlabel('Loudness(ms)')
ax7.set_ylabel('Count')
ax7.set_title('Song Loudness(ms) Like Distribution')

neg_loudness.hist(alpha = 0.5, bins = 30)


#Speechiness
ax9= fig2.add_subplot(334)
pos_speechiness.hist(alpha = 0.5, bins = 30)
ax9.set_xlabel('Speechiness')
ax9.set_ylabel('Count')
ax9.set_title('Song Speechiness Like Distribution')

neg_speechiness.hist(alpha = 0.5, bins = 30)





#valence
ax11= fig2.add_subplot(335)
pos_valence.hist(alpha = 0.5, bins = 30)
ax11.set_xlabel('valence')
ax11.set_ylabel('Count')
ax11.set_title('Song valence Like Distribution')

neg_valence.hist(alpha = 0.5, bins = 30)


#Energy
ax13= fig2.add_subplot(336)
pos_energy.hist(alpha = 0.5, bins = 30)
ax13.set_xlabel('Energy')
ax13.set_ylabel('Count')
ax13.set_title('Song Energy Like Distribution')

neg_energy.hist(alpha = 0.5, bins = 30)


#Key
ax15= fig2.add_subplot(337)
pos_key.hist(alpha = 0.5, bins = 30)
ax15.set_xlabel('Key')
ax15.set_ylabel('Count')
ax15.set_title('Song Key Like Distribution')

neg_key.hist(alpha = 0.5, bins = 30)



#Acousticness
ax16= fig2.add_subplot(338)
pos_acousticness.hist(alpha = 0.5, bins = 30)
ax16.set_xlabel('Acousticness')
ax16.set_ylabel('Count')
ax16.set_title('Song Acousticness Like Distribution')

neg_acousticness.hist(alpha = 0.5, bins = 30)


#Instrumentalness
ax17= fig2.add_subplot(339)
pos_instrumentalness.hist(alpha = 0.5, bins = 30)
ax17.set_xlabel('Instrumentalness')
ax17.set_ylabel('Count')
ax17.set_title('Song Instrumentalness Like Distribution')

neg_instrumentalness.hist(alpha = 0.5, bins = 30)

fig2 = plt.figure(figsize=(15,15))
ax3 = fig2.add_subplot(331)
ax3.set_xlabel('Danceability')
ax3.set_ylabel('Count')
ax3.set_title('Song Daneability Like Distribution')
pos_dance.hist(alpha = 0.5, bins = 30)
ax4 = fig2.add_subplot(331)
neg_dance.hist(alpha = 0.5, bins = 30)

fig2 = plt.figure(figsize=(15,15))
ax5 = fig2.add_subplot(332)
ax5.set_xlabel('Danceability')
ax5.set_ylabel('Count')
ax5.set_title('Song Daneability Like Distribution')
pos_dance.hist(alpha = 0.5, bins = 30)

neg_dance.hist(alpha = 0.5, bins = 30)

c = DecisionTreeClassifier(min_samples_split=100)

c = DecisionTreeClassifier(min_samples_split=100)

features = ["danceability","loudness","speechiness","valence","energy","key","acousticness","instrumentalness"]

x_train = train[features]
y_train = train["target"]

x_test = test[features]
y_test = test["target"]

features = ["danceability","loudness","speechiness","valence","energy","key","acousticness","instrumentalness"]

x_train = train[features]
y_train = train["target"]

x_test = test[features]
y_test = test["target"]

y_test

y_test

dt = c.fit(x_train,y_train)

import pydot
from io import StringIO
from io import BytesIO as StringIO

def show_tree(tree, features, path):
    f = io.StringIO()
    export_graphviz(tree, out_file=f, feature_names=features)
    pydotplus.graph_from_dot_data(f.getvalue()).write_png(path)
    img = misc.imread(path)
    plt.rcParams["figure.figsize"] = (20,20)
    plt.imshow(img)

show_tree(dt, features, 'dec_tree_01.png')

def show_tree(tree, features, path):
    f = io.StringIO()
    export_graphviz(tree, out_file=f, feature_names=features)
    pydotplus.graph_from_dot_data(f.getvalue()).write_png(path)
    img = misc.imread(path)
    plt.rcParams["figure.figsize"] = (20,20)
    plt.imshow(img)

show_tree(dt,features,'dec_tree_01.png')

