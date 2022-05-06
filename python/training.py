#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import json
import pickle
import numpy as np


# In[2]:


import nltk
from nltk.stem import WordNetLemmatizer


# In[3]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD


# In[4]:


lemmatizer= WordNetLemmatizer()


# In[6]:


intents = json.loads(open('C:/Users/gokul/Downloads/python/intents.json').read())


# In[10]:


nltk.download('punkt')
nltk.download('wordnet')
words=[]
classes=[]
documents=[]
ignore_letters=['?','!','.',',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
           
words=[lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words=sorted(set(words))


# In[11]:


classes=sorted(set(classes))
classes[0:5]

# In[12]:


pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))
           
training=[]
output_empty=[0] * len(classes)


# In[13]:


for document in documents:
    bag = []
    word_patterns=document[0]
    word_patterns=[lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
       
    output_row=list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])
   
random.shuffle(training)
training=np.array(training)


# In[14]:


train_x=list(training[:, 0])
train_y=list(training[:, 1])


# In[16]:


model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),),activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))


# In[21]:


sgd=SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])


# In[22]:


hist=model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.h5',hist)
print("\n\ndone")


# In[ ]:




