import pandas as pd

questionset = pd.read_csv('sample2.csv')

numquestions = len(questionset)

#open a file to put in the question
f = open('out2.txt', 'wt')
for i in range(numquestions):
    f.write(str(i + 1) + '. ' + questionset['Questiontext'][i] + '\n')
    if questionset['Type'][i] == 'multipleanswer':
        for answer in questionset['NAnswers'][i].split(';'):
            f.write('\n')
            f.write(answer)
        f.write('\n')
    elif questionset['Type'][i] == 'matrix':
        '''format
        
        1. sample question
        
        statement 1
        statement 2
        statement 3
        
        scale 1
        scale 2
        scale 3
        '''
        f.write('\n')
        for statement in questionset['NAnswers'][i].split(';'):
            f.write(statement)
            f.write('\n')
        f.write('\n')
        for scale in questionset['NScale'][i].split(';'):
            f.write(scale +'\n')
    f.write('\n')
f.close()

