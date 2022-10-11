from pythonping import ping
import subprocess

#ONLY FOR EXERCISES PURPOSES
#THIS PYTHONPING IS SO GREAT BUT I NEED ONE FOR MY SELF NOT A 3RD PARTY SOFTWARE
#SO TRIED TWO OTHER WAYS BUT IT NEEDS A LOT OF TIME TO WRITE ONE SO I USE IT ANYWAY
#THANK YOU DEVELOPER





#func that sends only a packet
def ping_host(host):
    ping_result = ping(target=host, count=1, timeout=2)
    output=ping_result.rtt_avg_ms
    return output
'''
    return {
        'host': host,
        'avg_latency': ping_result.rtt_avg_ms,
        'min_latency': ping_result.rtt_min_ms,
        'max_latency': ping_result.rtt_max_ms,
        'packet_loss': ping_result.packet_loss
    }
    '''
def jitt_cal(n,ip):
    jitter=[]
    for i in range(int(n)):
        d1=ping_host(ip)
        d2=ping_host(ip)
        dd=abs(d1-d2)
        jitter.append(dd)
        print(dd)
    print(jitter)
    avg=sum(jitter)/int(n)
    print("average is:",avg)

'''

output = subprocess.getoutput("ping -n 1 192.168.1.1")
#print(type(output[13]))
print(output[5:18])
print(len(output))
result = subprocess.run(["ping","-n","1","1.1.1.1"], capture_output=True, text=True)
#print(repr(result.stdout))

'''




jitt_cal(10,"192.168.1.1")