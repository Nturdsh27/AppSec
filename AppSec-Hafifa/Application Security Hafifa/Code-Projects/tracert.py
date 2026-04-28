from multiprocessing.pool import ThreadPool
from scapy.layers.inet import IP, ICMP
from scapy.all import ls
from scapy.sendrecv import sr1, sr
import argparse
import socket
tracert_parser = argparse.ArgumentParser(prog='tracert',\
    description='Track the pathway and the Rouand-Trip between the source to a destenation'\
    ,epilog='Wrote in python')
tracert_parser.add_argument('tracert')
tracert_parser.add_argument('-d', help='Do not resolve addresses to hostnames.',required=False,action='store_true')
tracert_parser.add_argument('-hops',dest='maximum_hops', help='Maximum number of hops to search for target.',type=int,default=30,required=False)
tracert_parser.add_argument('-j',dest='host_list', help='Loose source route along host-list (IPv4-only).',type=str,required=False)
tracert_parser.add_argument('-w',dest='timeout', help='Wait timeout milliseconds for each reply.',type=int,default=2,required=False)
tracert_parser.add_argument('-R', help='Trace round-trip path (IPv6-only).',type=str,required=False)
tracert_parser.add_argument('-S',dest='srcaddr', help='Source address to use (IPv6-only).',type=str,required=False)
tracert_parser.add_argument('-f4', help='Force using IPv4.',type=bool,required=False)
tracert_parser.add_argument('-f6', help='Force using IPv6.',type=bool,required=False)
tracert_args = tracert_parser.parse_args()
# print(tracert_args.tracert, tracert_args.destenation, tracert_args.maximun_hops,\
#     tracert_args.host_list,tracert_args.timeout,tracert_args.R,tracert_args.srcaddr,tracert_args.f4,tracert_args.f6)


def trace_packet(packet,resolution,timeout,):
    ans = sr1(packet,verbose=0,timeout=timeout)
    if ans is None:
        print("*".rjust(10),end=" ")
        reply_ip = ""
    else:
        if not resolution:
            try:
                hostname = socket.gethostbyaddr(ans.src)[0]
            except:
                hostname = ans.src
            reply_ip = hostname
        else:
            reply_ip = ans.src
        timestamp = int((ans.time - packet.sent_time)*1000)
        if timestamp == 0:
            print(f"<1 ms".rjust(10),end=" ")
        else:
            print(f"{timestamp}ms".rjust(10),end=" ")
    return reply_ip


def tracert(args):
    ip = args.tracert
    hostname = ip
    resolution = args.d
    timeout = args.timeout
    if not resolution:
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = ip
    ttl = args.maximum_hops
    print(f"Tracing route to {hostname} [{ip}]")
    print(f"over a maximum of {ttl} hops:")
    count = 1
    reply_ip = ""
    for index in range(ttl):
        packet = IP(dst=ip,ttl=index)/ICMP()
        print(f" {count}" , end =" ")
        for _ in range(3):
            pool = ThreadPool(processes=1)
            thread = pool.apply_async(trace_packet,(packet,resolution,timeout))
            reply_ip = thread.get()
        if reply_ip == ip or reply_ip == hostname:
                print(f"{hostname}".rjust(20))
                print("Done!")
                return
        if reply_ip != "":
            print(f"{reply_ip}".rjust(20))    
        else:
            print("Request time out.".rjust(20))    
        reply_ip = ""
        count+=1
        
        
def main():
    tracert(tracert_args)
main()