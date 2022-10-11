from pythonping import ping

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
    avg=sum(jitter)/int(n)
    print("jitter is:",avg)


for i in range(10):
    jitt_cal(10,"192.168.1.1")
