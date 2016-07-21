from numpy import *
import matplotlib
import matplotlib.pyplot as plt

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines) #get file total lines
    returnMat = zeros((numberOfLines, 3)) #create matrix
    classLabelVector = []
    index = 0
    #parse file
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split("\t")
        returnMat[index, :] = listFromLine[0:3]
        intLabel = 1;
        if listFromLine[-1] == 'largeDoses':
            intLabel = 3
        elif listFromLine[-1] == 'smallDoses':
            intLabel = 2
        classLabelVector.append(intLabel)
        index += 1
    return returnMat, classLabelVector

if __name__ == "__main__":
    datingDataMat, datingLabels = file2matrix("./datingTestSet.txt")
    print datingDataMat
    print "===================="
    print datingLabels
    #Mat convert to scattergram
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1],
               15.0*array(datingLabels), 15.0*array(datingLabels))
    plt.show()