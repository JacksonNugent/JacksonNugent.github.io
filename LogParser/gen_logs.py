import random
import calendar

names = ["alice", "john", "bob", "jimmy"]
events = ["FAIL", "SUCCESS"]
max_count = 100
workstation = {}



def gen_random_logs(file):

    #Generate random unique IP to tie per user
    ip_set = set()
    for name in names:
        while True:
            ip_addr = "10.1.1." + str(random.randint(2, 15))
            if ip_addr not in ip_set:
                ip_set.add(ip_addr)
                break
        workstation[name] = ip_addr

    print(workstation)

gen_random_logs("log.txt")
