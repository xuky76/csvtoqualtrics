import pandas as pd

questionset = pd.read_csv('sample.csv')

numquestions = len(questionset)

#open a file to put in the question
f = open('out.txt', 'wt')
for i in range(numquestions):
    f.write(str(i + 1) + '. ' + questionset['Questiontext'][i] + '\n')
    if questionset['Type'][i] == 'multipleanswer':
        for n in range(questionset['NAnswers'][i]):
            f.write('\n')
            txt = "sample answer" + str(n)
            f.write(txt)
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
        for n in range(questionset['NAnswers'][i]):
            txt = "statement" + str(n)
            f.write(txt)
            f.write('\n')
        f.write('\n')
        for s in range(int(questionset['NScale'][i])):
            f.write('scale' + str(i)+'\n')
    f.write('\n')
f.close()

