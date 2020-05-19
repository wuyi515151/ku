import matplotlib.pyplot as plt
import numpy as np
import seaborn



Fs = 150.0;                 # sampling rate采样率
Ts = 1.0/Fs;                # sampling interval 采样区间
t = np.arange(0,1,Ts)       # time vector,这里Ts也是步长

ff = 25;                    # frequency of the signal信号频率
y = np.sin(2*np.pi*ff*t)

n = len(y)                  # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T                   # two sides frequency range
frq1 = frq[range(int(n/2))] # one side frequency range

YY = np.fft.fft(y)          # 未归一化
Y = np.fft.fft(y)/n         # fft computing and normalization 归一化
Y1 = Y[range(int(n/2))]

fig, ax = plt.subplots(4, 1)

ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')

ax[1].plot(frq,abs(YY),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')

ax[2].plot(frq,abs(Y),'G')  # plotting the spectrum
ax[2].set_xlabel('Freq (Hz)')
ax[2].set_ylabel('|Y(freq)|')

ax[3].plot(frq1,abs(Y1),'B') # plotting the spectrum
ax[3].set_xlabel('Freq (Hz)')
ax[3].set_ylabel('|Y(freq)|')

plt.show()





#这是音频传入进行采样的代码
# -*- coding: UTF-8 -*-
import wave
import numpy as np
import matplotlib.pyplot as plt

# 打开wav文件 ，open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据。
f = wave.open(r"D:\VS\ccc\999.wav","rb")
# 读取格式信息
# 一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采
# 样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
params = f.getparams()
[nchannels, sampwidth, framerate, nframes] = params[:4]
# 读取波形数据
# 读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）
str_data = f.readframes(nframes)
f.close()
# 将波形数据转换成数组
# 需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
wave_data = np.fromstring(str_data,dtype = np.short)
# 将wave_data数组改为2列，行数自动匹配。在修改shape属的性时，需使得数组的总长度不变。
wave_data.shape = -1,2
# 转置数据
wave_data = wave_data.T
# 通过取样点数和取样频率计算出每个取样的时间。
time=np.arange(0,nframes/2)/framerate
# print(params)
plt.figure(1)
# time 也是一个数组，与wave_data[0]或wave_data[1]配对形成系列点坐标
plt.subplot(211)
plt.plot(time,wave_data[0])
plt.xlabel("time/s")
plt.title('Wave')


N=44100
start=0
# 开始采样位置
df = framerate/(N-1)
# 分辨率
freq = [df*n for n in range(0,N)]
# N个元素
wave_data2=wave_data[0][start:start+N]
c=np.fft.fft(wave_data2)*2/N
# 常规显示采样频率一半的频谱
plt.subplot(212)
plt.plot(freq[:round(len(freq)/2)],abs(c[:round(len(c)/2)]),'r')
plt.title('Freq')
plt.xlabel("Freq/Hz")
plt.show()
