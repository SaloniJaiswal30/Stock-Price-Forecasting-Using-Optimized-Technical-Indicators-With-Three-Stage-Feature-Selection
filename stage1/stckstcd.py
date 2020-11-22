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



def stochastic_k2(dataset):
    stoc=[]
    for i in range(1,len(dataset)):
        data=[j[2] for j in dataset[i-1:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-1:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc
def stochastic_k3(dataset):
    stoc=[]
    for i in range(2,len(dataset)):
        data=[j[2] for j in dataset[i-2:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-2:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc

def stochastic_k4(dataset):
    stoc=[]
    for i in range(3,len(dataset)):
        data=[j[2] for j in dataset[i-3:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-3:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc

def stochastic_k5(dataset):
    stoc=[]
    for i in range(4,len(dataset)):
        data=[j[2] for j in dataset[i-4:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-4:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc

def stochastic_k6(dataset):
    stoc=[]
    for i in range(5,len(dataset)):
        data=[j[2] for j in dataset[i-5:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-5:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc

def stochastic_k7(dataset):
    stoc=[]
    for i in range(6,len(dataset)):
        data=[j[2] for j in dataset[i-6:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-6:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc

def stochastic_k8(dataset):
    stoc=[]
    for i in range(7,len(dataset)):
        data=[j[2] for j in dataset[i-7:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-7:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc

def stochastic_k9(dataset):
    stoc=[]
    for i in range(8,len(dataset)):
        data=[j[2] for j in dataset[i-8:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-8:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc
def stochastic_k10(dataset):
    stoc=[]
    for i in range(9,len(dataset)):
        data=[j[2] for j in dataset[i-9:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-9:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc

def stochastic_k11(dataset):
    stoc=[]
    for i in range(10,len(dataset)):
        data=[j[2] for j in dataset[i-10:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-10:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc

def stochastic_k12(dataset):
    stoc=[]
    for i in range(11,len(dataset)):
        data=[j[2] for j in dataset[i-11:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-11:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc
def stochastic_k13(dataset):
    stoc=[]
    for i in range(12,len(dataset)):
        data=[j[2] for j in dataset[i-12:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-12:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc

def stochastic_k14(dataset):
    stoc=[]
    for i in range(13,len(dataset)):
        data=[j[2] for j in dataset[i-13:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-13:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc
def stochastic_k15(dataset):
    stoc=[]
    for i in range(14,len(dataset)):
        data=[j[2] for j in dataset[i-14:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-14:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc

def stochastic_d2(stochastick2):
    stocd=[]
    for i in range(1,len(stochastick2)):
        temp=0
        for j in range(i-1,i+1):
            temp=temp+stochastick2[j]
        temp=temp/2
        stocd.append(temp)
    return stocd
def stochastic_d3(stochastick3):
    stocd=[]
    for i in range(2,len(stochastick3)):
        temp=0
        for j in range(i-2,i+1):
            temp=temp+stochastick3[j]
        temp=temp/3
        stocd.append(temp)
    return stocd
def stochastic_d4(stochastick4):
    stocd=[]
    for i in range(3,len(stochastick4)):
        temp=0
        for j in range(i-3,i+1):
            temp=temp+stochastick4[j]
        temp=temp/4
        stocd.append(temp)
    return stocd
def stochastic_d5(stochastick5):
    stocd=[]
    for i in range(4,len(stochastick5)):
        temp=0
        for j in range(i-4,i+1):
            temp=temp+stochastick5[j]
        temp=temp/5
        stocd.append(temp)
    return stocd
def stochastic_d6(stochastick6):
    stocd=[]
    for i in range(5,len(stochastick6)):
        temp=0
        for j in range(i-5,i+1):
            temp=temp+stochastick6[j]
        temp=temp/6
        stocd.append(temp)
    return stocd
def stochastic_d7(stochastick7):
    stocd=[]
    for i in range(6,len(stochastick7)):
        temp=0
        for j in range(i-6,i+1):
            temp=temp+stochastick7[j]
        temp=temp/7
        stocd.append(temp)
    return stocd
def stochastic_d8(stochastick8):
    stocd=[]
    for i in range(7,len(stochastick8)):
        temp=0
        for j in range(i-7,i+1):
            temp=temp+stochastick8[j]
        temp=temp/8
        stocd.append(temp)
    return stocd
def stochastic_d9(stochastick9):
    stocd=[]
    for i in range(8,len(stochastick9)):
        temp=0
        for j in range(i-8,i+1):
            temp=temp+stochastick9[j]
        temp=temp/9
        stocd.append(temp)
    return stocd
def stochastic_d10(stochastick10):
    stocd=[]
    for i in range(9,len(stochastick10)):
        temp=0
        for j in range(i-9,i+1):
            temp=temp+stochastick10[j]
        temp=temp/10
        stocd.append(temp)
    return stocd
def stochastic_d11(stochastick11):
    stocd=[]
    for i in range(10,len(stochastick11)):
        temp=0
        for j in range(i-10,i+1):
            temp=temp+stochastick11[j]
        temp=temp/11
        stocd.append(temp)
    return stocd
def stochastic_d12(stochastick12):
    stocd=[]
    for i in range(11,len(stochastick12)):
        temp=0
        for j in range(i-11,i+1):
            temp=temp+stochastick12[j]
        temp=temp/12
        stocd.append(temp)
    return stocd
def stochastic_d13(stochastick13):
    stocd=[]
    for i in range(12,len(stochastick13)):
        temp=0
        for j in range(i-12,i+1):
            temp=temp+stochastick13[j]
        temp=temp/13
        stocd.append(temp)
    return stocd
def stochastic_d14(stochastick14):
    stocd=[]
    for i in range(13,len(stochastick14)):
        temp=0
        for j in range(i-13,i+1):
            temp=temp+stochastick14[j]
        temp=temp/14
        stocd.append(temp)
    return stocd
def stochastic_d15(stochastick15):
    stocd=[]
    for i in range(14,len(stochastick15)):
        temp=0
        for j in range(i-14,i+1):
            temp=temp+stochastick15[j]
        temp=temp/15
        stocd.append(temp)
    return stocd


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
stck2=stochastic_k2(dataset)
stcd2=stochastic_d2(stck2)
stck3=stochastic_k3(dataset)
stcd3=stochastic_d3(stck3)
stck4=stochastic_k4(dataset)
stcd4=stochastic_d4(stck4)
stck5=stochastic_k5(dataset)
stcd5=stochastic_d5(stck5)
stck6=stochastic_k6(dataset)
stcd6=stochastic_d6(stck6)
stck7=stochastic_k7(dataset)
stcd7=stochastic_d7(stck7)
stck8=stochastic_k8(dataset)
stcd8=stochastic_d8(stck8)
stck9=stochastic_k9(dataset)
stcd9=stochastic_d9(stck9)
stck10=stochastic_k10(dataset)
stcd10=stochastic_d10(stck10)
stck11=stochastic_k11(dataset)
stcd11=stochastic_d11(stck11)
stck12=stochastic_k12(dataset)
stcd12=stochastic_d12(stck12)
stck13=stochastic_k13(dataset)
stcd13=stochastic_d13(stck13)
stck14=stochastic_k14(dataset)
stcd14=stochastic_d14(stck14)
stck15=stochastic_k15(dataset)
stcd15=stochastic_d15(stck15)


stck2=stck2[len(stck2)-len(stck15):]
stcK3=stck3[len(stck3)-len(stck15):]
stck4=stck4[len(stck4)-len(stck15):]
stck5=stck5[len(stck5)-len(stck15):]
stck6=stck6[len(stck6)-len(stck15):]
stck7=stck7[len(stck7)-len(stck15):]
stck8=stck8[len(stck8)-len(stck15):]
stck9=stck9[len(stck9)-len(stck15):]
stck10=stck10[len(stck10)-len(stck15):]
stck11=stck11[len(stck11)-len(stck15):]
stck12=stck12[len(stck12)-len(stck15):]
stck13=stck13[len(stck13)-len(stck15):]
stck14=stck14[len(stck14)-len(stck15):]


stcd2=stcd2[len(stcd2)-len(stcd15):]
stcd3=stcd3[len(stcd3)-len(stcd15):]
stcd4=stcd4[len(stcd4)-len(stcd15):]
stcd5=stcd5[len(stcd5)-len(stcd15):]
stcd6=stcd6[len(stcd6)-len(stcd15):]
stcd7=stcd7[len(stcd7)-len(stcd15):]
stcd8=stcd8[len(stcd8)-len(stcd15):]
stcd9=stcd9[len(stcd9)-len(stcd15):]
stcd10=stcd10[len(stcd10)-len(stcd15):]
stcd11=stcd11[len(stcd11)-len(stcd15):]
stcd12=stcd12[len(stcd12)-len(stcd15):]
stcd13=stcd13[len(stcd13)-len(stcd15):]
stcd14=stcd14[len(stcd14)-len(stcd15):]
#print(len(sma),len(ema),len(mom),len(stck),len(stcd),len(rsi),len(macd),len(lwr),len(ado),len(cci))

stck_norm2=pandas.Series(stck2)
stck_norm3=pandas.Series(stck3)
stck_norm4=pandas.Series(stck4)
stck_norm5=pandas.Series(stck5)
stck_norm6=pandas.Series(stck6)
stck_norm7=pandas.Series(stck7)
stck_norm8=pandas.Series(stck8)
stck_norm9=pandas.Series(stck9)
stck_norm10=pandas.Series(stck10)
stck_norm11=pandas.Series(stck11)
stck_norm12=pandas.Series(stck12)
stck_norm13=pandas.Series(stck13)
stck_norm14=pandas.Series(stck14)
stck_norm15=pandas.Series(stck15)

stcd_norm2=pandas.Series(stcd2)
stcd_norm3=pandas.Series(stcd3)
stcd_norm4=pandas.Series(stcd4)
stcd_norm5=pandas.Series(stcd5)
stcd_norm6=pandas.Series(stcd6)
stcd_norm7=pandas.Series(stcd7)
stcd_norm8=pandas.Series(stcd8)
stcd_norm9=pandas.Series(stcd9)
stcd_norm10=pandas.Series(stcd10)
stcd_norm11=pandas.Series(stcd11)
stcd_norm12=pandas.Series(stcd12)
stcd_norm13=pandas.Series(stcd13)
stcd_norm14=pandas.Series(stcd14)
stcd_norm15=pandas.Series(stcd15)
date,label=classlabel(dataset)
date=date[len(date)-len(stck15):]
date.index=numpy.arange(0,len(date))
label=label[len(label)-len(stck15):]
label.index=numpy.arange(0,len(label))

final=pandas.concat([date,stck_norm2,stck_norm3,stck_norm4,stck_norm5,stck_norm6,stck_norm7,stck_norm8,stck_norm9,stck_norm10,stck_norm11,stck_norm12,stck_norm13,stck_norm14,stck_norm15,label],axis=1)
final.to_csv("TCSstck.csv",encoding="UTF-8",index=False,header=False)
date,label=classlabel(dataset)
date=date[len(date)-len(stcd15):]
date.index=numpy.arange(0,len(date))
label=label[len(label)-len(stcd15):]
label.index=numpy.arange(0,len(label))
final=pandas.concat([date,stcd_norm2,stcd_norm3,stcd_norm4,stcd_norm5,stcd_norm6,stcd_norm7,stcd_norm8,stcd_norm9,stcd_norm10,stcd_norm11,stcd_norm12,stcd_norm13,stcd_norm14,stcd_norm15,label],axis=1)
final.to_csv("TCSstcd.csv",encoding="UTF-8",index=False,header=False)
