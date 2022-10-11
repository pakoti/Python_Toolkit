from pythonping import ping
import matplotlib.pyplot as plt
import numpy as np


#func that sends only a packet
def ping_host(host):

    ping_result = ping(target=host, count=1, timeout=2)
    output=ping_result.rtt_avg_ms
    return output


#function that calculate jitter
#inputs:packets to be sent and also ip
def jitt_cal(n,ip):
    jitter=[]
    for i in range(int(n)):
        d1=ping_host(ip)
        d2=ping_host(ip)
        dd=abs(d1-d2)
        jitter.append(dd)
    avg=float(sum(jitter))/float(n)
    return avg


x=[1,2,3,4,5,6,7,8,9,10]
y=[]

for j in range(10):
    y1=[]
    for i in range(10):
        a=jitt_cal(10,"192.168.1.1")
        y1.append(a)
        #y=float(sum(y1))/float(10)
    #print(y1)
    y.append(float(sum(y1))/float(10))

    #print(y)
print(x)
print(y)

plt.plot(x,y,color='green', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='blue', markersize=8)

#plt.ylim(1,5)
#plt.xlim(1,10)

# number of earrayxpriement
plt.xlabel('number of 10 jitts')
# jitter over time label
plt.ylabel('jitter in ms')
# plot title
plt.title('How 10 jitter tests changes WHY!')

plt.show()


