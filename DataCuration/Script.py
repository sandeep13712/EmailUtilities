import py_common_subseq
import pandas as pd
import os 
import re
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
os.chdir('//labdata2.ad.mshri.on.ca\wrana_lab\skumar\Computational\COMP11_DataCuration')
fileName = 'data_ijor_all'

def findCorrectName(lcsValues):
    scores = list()
    for lenCS in lcsValues:
        noOfRelevantCommonSequences = len(np.where(lenCS>1)[0])
        lengthOfLargestCS = np.max(lenCS)
        scores.append(sqrt(noOfRelevantCommonSequences**2 + lengthOfLargestCS**2))
        
    #print(scores)
        
    return np.where(scores == np.max(scores))[0][0]

data = pd.read_csv(fileName+'.csv')

print(data.shape)

data['validity'] = [0]*len(data[data.columns[0]])
data['CorrectedName'] = ['']*len(data[data.columns[0]])
data['invalidNames'] = [0]*len(data[data.columns[0]])
#print(data['validity'])

emailPattern = '.*@.*[.].*'
for i,email in zip(range(len(data['validity'])),data['email']):
    #print(email)
    nameString= str(data['name'][i])
    if(re.match(string=email, pattern=emailPattern) and len(nameString)>0):
        data['validity'][i] = 1
        names = nameString.split(';')
        
        if(len(names)<2 and len(names[0])>15):
            data['invalidNames'][i]  = 1
        
        
        lcsValues = list()
        
        #print('Len: '+str(len(names)))
        for name in names:
            lenCommonSeq = [len(seq) for seq in py_common_subseq.find_common_subsequences(name, email)]
            lcsValues.append(lenCommonSeq)
        
        correctNameIndex = findCorrectName(lcsValues)
        
        #print(email+'->'+names[correctNameIndex])
        
        data['CorrectedName'][i]  = names[correctNameIndex]
     
    print(i)
data.to_csv(fileName+'_Corrected.csv')
# test_seq_1 = 'Singh Rishan'
# test_seq_2 = 'rshnsingh1@yahoo.com'
# #py_common_subseq.count_common_subsequences(test_seq_1, test_seq_2)
# subSeq = py_common_subseq.find_common_subsequences(test_seq_1, test_seq_2)

data_removeJunk = data.copy(deep=True)
rowsToDrop = np.where(data_removeJunk['validity'] ==0)[0]
print(len(rowsToDrop))

data_removeJunk.drop(data_removeJunk.index[rowsToDrop], inplace=True)

data_removeJunk.to_csv(fileName+'Final.csv')