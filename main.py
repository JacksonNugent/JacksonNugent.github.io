import random, datetime

workstation = {} # Name = Key; IP = Value
names = {'James', 'Dean', 'Alice', 'Doe'}
ips = set()
log_file = 'logs.txt'
max_count = 100

def main():
    input('Press enter to continue...')
    gen_ips()
    assign_ips()
    for user, ip in workstation.items():
        print(f'{user} has {ip}')
    gen_logs(log_file)
  
  
# Provide a datetime log for gen_logs   
def gen_datetime(user:str, ip:str):
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return datetime.datetime(2025, 12, 1, hour, minute, second)
     

# Generate logs for scanning     
def gen_logs(file):
    timestamps = set()
    for _ in range(max_count):
        timestamps.add(gen_datetime('test', 'test'))
    timestamps = list(timestamps)
    timestamps.sort()
    
    with open(file, 'w') as f:
        for ts in timestamps:
            f.write(f'{ts}\n')

# Generate IPs and add to ips set to choose
def gen_ips():
    for i in range(2, 15):
        ips.add('10.1.1.' + str(i))


# Assign users to workstation dictionary with a value of ip randomly chosen from ips
def assign_ips():
    for name in names:
        workstation[name] = random.choice(list(ips))


main()