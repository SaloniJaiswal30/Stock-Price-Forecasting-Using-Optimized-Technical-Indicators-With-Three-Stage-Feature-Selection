import csv
import numpy
import pandas

def LoadCsv(filename):
    file=open(filename,"r")
    reader=csv.reader(file)
    next(reader)
    dataset=[r for r in reader]
    return dataset

def str_to_float(dataset):
    print(len(dataset))
    for i in range(len(dataset)):
        for j in range(1,len(dataset[i])):
            dataset[i][j]=float(dataset[i][j])
    return dataset

def simple_moving_average2(dataset):
    moving_average=[]
    for i in range(1,len(dataset)):
        temp=0
        for j in range(i-1,i+1):
            temp=temp+dataset[j][4]
        temp=temp/2
        moving_average.append(temp)
    return moving_average

def simple_moving_average3(dataset):
    moving_average=[]
    for i in range(2,len(dataset)):
        temp=0
        for j in range(i-2,i+1):
            temp=temp+dataset[j][4]
        temp=temp/3
        moving_average.append(temp)
    return moving_average
def simple_moving_average4(dataset):
    moving_average=[]
    for i in range(3,len(dataset)):
        temp=0
        for j in range(i-3,i+1):
            temp=temp+dataset[j][4]
        temp=temp/4
        moving_average.append(temp)
    return moving_average
def simple_moving_average5(dataset):
    moving_average=[]
    for i in range(4,len(dataset)):
        temp=0
        for j in range(i-4,i+1):
            temp=temp+dataset[j][4]
        temp=temp/5
        moving_average.append(temp)
    return moving_average
def simple_moving_average6(dataset):
    moving_average=[]
    for i in range(5,len(dataset)):
        temp=0
        for j in range(i-5,i+1):
            temp=temp+dataset[j][4]
        temp=temp/6
        moving_average.append(temp)
    return moving_average
def simple_moving_average7(dataset):
    moving_average=[]
    for i in range(6,len(dataset)):
        temp=0
        for j in range(i-6,i+1):
            temp=temp+dataset[j][4]
        temp=temp/7
        moving_average.append(temp)
    return moving_average
def simple_moving_average8(dataset):
    moving_average=[]
    for i in range(7,len(dataset)):
        temp=0
        for j in range(i-7,i+1):
            temp=temp+dataset[j][4]
        temp=temp/8
        moving_average.append(temp)
    return moving_average
def simple_moving_average9(dataset):
    moving_average=[]
    for i in range(8,len(dataset)):
        temp=0
        for j in range(i-8,i+1):
            temp=temp+dataset[j][4]
        temp=temp/9
        moving_average.append(temp)
    return moving_average
def simple_moving_average10(dataset):
    moving_average=[]
    for i in range(9,len(dataset)):
        temp=0
        for j in range(i-9,i+1):
            temp=temp+dataset[j][4]
        temp=temp/10
        moving_average.append(temp)
    return moving_average
def simple_moving_average11(dataset):
    moving_average=[]
    for i in range(10,len(dataset)):
        temp=0
        for j in range(i-10,i+1):
            temp=temp+dataset[j][4]
        temp=temp/11
        moving_average.append(temp)
    return moving_average
def simple_moving_average12(dataset):
    moving_average=[]
    for i in range(11,len(dataset)):
        temp=0
        for j in range(i-11,i+1):
            temp=temp+dataset[j][4]
        temp=temp/12
        moving_average.append(temp)
    return moving_average
def simple_moving_average13(dataset):
    moving_average=[]
    for i in range(12,len(dataset)):
        temp=0
        for j in range(i-12,i+1):
            temp=temp+dataset[j][4]
        temp=temp/13
        moving_average.append(temp)
    return moving_average
def simple_moving_average14(dataset):
    moving_average=[]
    for i in range(13,len(dataset)):
        temp=0
        for j in range(i-13,i+1):
            temp=temp+dataset[j][4]
        temp=temp/14
        moving_average.append(temp)
    return moving_average
def simple_moving_average15(dataset):
    moving_average=[]
    for i in range(14,len(dataset)):
        temp=0
        for j in range(i-14,i+1):
            temp=temp+dataset[j][4]
        temp=temp/15
        moving_average.append(temp)
    return moving_average
def simple_moving_average16(dataset):
    moving_average=[]
    for i in range(15,len(dataset)):
        temp=0
        for j in range(i-15,i+1):
            temp=temp+dataset[j][4]
        temp=temp/16
        moving_average.append(temp)
    return moving_average
def simple_moving_average17(dataset):
    moving_average=[]
    for i in range(16,len(dataset)):
        temp=0
        for j in range(i-16,i+1):
            temp=temp+dataset[j][4]
        temp=temp/17
        moving_average.append(temp)
    return moving_average
def simple_moving_average18(dataset):
    moving_average=[]
    for i in range(17,len(dataset)):
        temp=0
        for j in range(i-17,i+1):
            temp=temp+dataset[j][4]
        temp=temp/18
        moving_average.append(temp)
    return moving_average
def simple_moving_average19(dataset):
    moving_average=[]
    for i in range(18,len(dataset)):
        temp=0
        for j in range(i-18,i+1):
            temp=temp+dataset[j][4]
        temp=temp/19
        moving_average.append(temp)
    return moving_average
def simple_moving_average20(dataset):
    moving_average=[]
    for i in range(19,len(dataset)):
        temp=0
        for j in range(i-19,i+1):
            temp=temp+dataset[j][4]
        temp=temp/20
        moving_average.append(temp)
    return moving_average


def classlabel(dataset):
    date=[]
    label=[]
    for i in range(len(dataset)):
        date.append(dataset[i][0])
        diff=dataset[i][4]-dataset[i][1]
        if(diff>0):
            temp=1
        elif(diff<0):
            temp=0
        else:
            temp=0
        label.append(temp)
    date=pandas.DataFrame(date)
    label=pandas.DataFrame(label)
    return date,label
        
        
    
dataset=LoadCsv("TCS.csv")
dataset=str_to_float(dataset)
sma2=simple_moving_average2(dataset)
sma3=simple_moving_average3(dataset)
sma4=simple_moving_average4(dataset)
sma5=simple_moving_average5(dataset)
sma6=simple_moving_average6(dataset)
sma7=simple_moving_average7(dataset)
sma8=simple_moving_average8(dataset)
sma9=simple_moving_average9(dataset)
sma10=simple_moving_average10(dataset)
sma11=simple_moving_average11(dataset)
sma12=simple_moving_average12(dataset)
sma13=simple_moving_average13(dataset)
sma14=simple_moving_average14(dataset)
sma15=simple_moving_average15(dataset)
sma16=simple_moving_average16(dataset)
sma17=simple_moving_average17(dataset)
sma18=simple_moving_average18(dataset)
sma19=simple_moving_average19(dataset)
sma20=simple_moving_average20(dataset)

#print(len(sma),len(ema),len(mom),len(stck),len(stcd),len(rsi),len(macd),len(lwr),len(ado),len(cci))
sma2=sma2[len(sma2)-len(sma20):]
sma3=sma3[len(sma3)-len(sma20):]
sma4=sma4[len(sma4)-len(sma20):]
sma5=sma5[len(sma5)-len(sma20):]
sma6=sma6[len(sma6)-len(sma20):]
sma7=sma7[len(sma7)-len(sma20):]
sma8=sma8[len(sma8)-len(sma20):]
sma9=sma9[len(sma9)-len(sma20):]
sma10=sma10[len(sma10)-len(sma20):]
sma11=sma11[len(sma11)-len(sma20):]
sma12=sma12[len(sma12)-len(sma20):]
sma13=sma13[len(sma13)-len(sma20):]
sma14=sma14[len(sma14)-len(sma20):]
sma15=sma15[len(sma15)-len(sma20):]
sma16=sma16[len(sma16)-len(sma20):]
sma17=sma17[len(sma17)-len(sma20):]
sma18=sma18[len(sma18)-len(sma20):]
sma19=sma19[len(sma19)-len(sma20):]
sma_norm2=pandas.Series(sma2)
sma_norm3=pandas.Series(sma3)
sma_norm4=pandas.Series(sma4)
sma_norm5=pandas.Series(sma5)
sma_norm6=pandas.Series(sma6)
sma_norm7=pandas.Series(sma7)
sma_norm8=pandas.Series(sma8)
sma_norm9=pandas.Series(sma9)
sma_norm10=pandas.Series(sma10)
sma_norm11=pandas.Series(sma11)
sma_norm12=pandas.Series(sma12)
sma_norm13=pandas.Series(sma13)
sma_norm14=pandas.Series(sma14)
sma_norm15=pandas.Series(sma15)
sma_norm16=pandas.Series(sma16)
sma_norm17=pandas.Series(sma17)
sma_norm18=pandas.Series(sma18)
sma_norm19=pandas.Series(sma19)
sma_norm20=pandas.Series(sma20)

date,label=classlabel(dataset)
date=date[len(date)-len(sma2):]
date.index=numpy.arange(0,len(date))
label=label[len(label)-len(sma2):]
label.index=numpy.arange(0,len(label))
"""print(sma_norm)
print("-----")
print(ema_norm)
print("-----")
print(mom_norm)
print("-----")"""

final=pandas.concat([date,sma_norm2,sma_norm3,sma_norm4,sma_norm5,sma_norm6,sma_norm7,sma_norm8,sma_norm9,sma_norm10,sma_norm11,sma_norm12,sma_norm13,sma_norm14,sma_norm15,sma_norm16,sma_norm17,sma_norm18,sma_norm19,sma_norm20,label],axis=1)
final.to_csv("TCSsma.csv",encoding="UTF-8",index=False,header=False)