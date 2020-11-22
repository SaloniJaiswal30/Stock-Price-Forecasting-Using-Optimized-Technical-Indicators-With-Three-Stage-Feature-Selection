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

def relative_strength_index2(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=2,center=False).mean()
    roll_down2 = down.abs().rolling(window=2,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
def relative_strength_index3(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=3,center=False).mean()
    roll_down2 = down.abs().rolling(window=3,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
def relative_strength_index4(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=4,center=False).mean()
    roll_down2 = down.abs().rolling(window=4,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
def relative_strength_index5(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=5,center=False).mean()
    roll_down2 = down.abs().rolling(window=5,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
def relative_strength_index6(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=6,center=False).mean()
    roll_down2 = down.abs().rolling(window=6,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
def relative_strength_index7(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=7,center=False).mean()
    roll_down2 = down.abs().rolling(window=7,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
def relative_strength_index8(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=8,center=False).mean()
    roll_down2 = down.abs().rolling(window=8,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
def relative_strength_index9(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=9,center=False).mean()
    roll_down2 = down.abs().rolling(window=9,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
def relative_strength_index10(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=10,center=False).mean()
    roll_down2 = down.abs().rolling(window=10,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
def relative_strength_index11(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=11,center=False).mean()
    roll_down2 = down.abs().rolling(window=11,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
def relative_strength_index12(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=12,center=False).mean()
    roll_down2 = down.abs().rolling(window=12,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
def relative_strength_index13(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=13,center=False).mean()
    roll_down2 = down.abs().rolling(window=13,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
def relative_strength_index14(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=14,center=False).mean()
    roll_down2 = down.abs().rolling(window=14,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
def relative_strength_index15(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=15,center=False).mean()
    roll_down2 = down.abs().rolling(window=15,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2

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
            temp="0"
        label.append(temp)
    date=pandas.DataFrame(date)
    label=pandas.DataFrame(label)
    return date,label
        
        
    
dataset=LoadCsv("TCS.csv")
#print(dataset)
dataset=str_to_float(dataset)
rsi2=relative_strength_index2(dataset)
rsi3=relative_strength_index3(dataset)
rsi4=relative_strength_index4(dataset)
rsi5=relative_strength_index5(dataset)
rsi6=relative_strength_index6(dataset)
rsi7=relative_strength_index7(dataset)
rsi8=relative_strength_index8(dataset)
rsi9=relative_strength_index9(dataset)
rsi10=relative_strength_index10(dataset)
rsi11=relative_strength_index11(dataset)
rsi12=relative_strength_index12(dataset)
rsi13=relative_strength_index13(dataset)
rsi14=relative_strength_index14(dataset)
rsi15=relative_strength_index15(dataset)

#print(numpy.max(sma))
#print(numpy.min(sma))
#print(numpy.mean(sma))
#print(numpy.std((sma)))
"""print(sma)
print("-----")
print(ema)
print("-----")
print(mom)
print("-----")
print(stck)
print("-----")
print(stcd)
print("-----")
print(rsi)
print("-----")
print(macd)
print("-----")
print(lwr)
print("-----")
print(ado)
print("-----")
print(cci)
print("-----")
print(len(dataset))"""

rsi2.index=numpy.arange(0,len(rsi2)) 
rsi3.index=numpy.arange(0,len(rsi3))
rsi4.index=numpy.arange(0,len(rsi4))
rsi5.index=numpy.arange(0,len(rsi5))
rsi6.index=numpy.arange(0,len(rsi6))
rsi7.index=numpy.arange(0,len(rsi7)) 
rsi8.index=numpy.arange(0,len(rsi8))
rsi9.index=numpy.arange(0,len(rsi9))
rsi10.index=numpy.arange(0,len(rsi10))
rsi11.index=numpy.arange(0,len(rsi11))
rsi12.index=numpy.arange(0,len(rsi12)) 
rsi13.index=numpy.arange(0,len(rsi13))
rsi14.index=numpy.arange(0,len(rsi14))
rsi15.index=numpy.arange(0,len(rsi15))

"""print(sma)
print("-----")
print(ema)
print("-----")
print(mom)
print("-----")"""
#print(len(sma),len(ema),len(mom),len(stck),len(stcd),len(rsi),len(macd),len(lwr),len(ado),len(cci))
rsi_norm2=pandas.Series(rsi2)
rsi_norm3=pandas.Series(rsi3)
rsi_norm4=pandas.Series(rsi4)
rsi_norm5=pandas.Series(rsi5)
rsi_norm6=pandas.Series(rsi6)
rsi_norm7=pandas.Series(rsi7)
rsi_norm8=pandas.Series(rsi8)
rsi_norm9=pandas.Series(rsi9)
rsi_norm10=pandas.Series(rsi10)
rsi_norm11=pandas.Series(rsi11)
rsi_norm12=pandas.Series(rsi12)
rsi_norm13=pandas.Series(rsi13)
rsi_norm14=pandas.Series(rsi14)
rsi_norm15=pandas.Series(rsi15)

date,label=classlabel(dataset)
date=date[len(date)-len(rsi2):]
date.index=numpy.arange(0,len(date))
label=label[len(label)-len(rsi2):]
label.index=numpy.arange(0,len(label))
"""print(sma_norm)
print("-----")
print(ema_norm)
print("-----")
print(mom_norm)
print("-----")"""

final=pandas.concat([date,rsi_norm2,rsi_norm3,rsi_norm4,rsi_norm5,rsi_norm6,rsi_norm7,rsi_norm8,rsi_norm9,rsi_norm10,rsi_norm11,rsi_norm12,rsi_norm13,rsi_norm14,rsi_norm15,label],axis=1)
final.to_csv("TCSRSI.csv",encoding="UTF-8",index=False,header=False)

