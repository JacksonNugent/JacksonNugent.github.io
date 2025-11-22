import random, datetime, os



workstation = {} # Name = Key; IP = Value
names = {'James', 'Dean', 'Alice', 'Doe'}
events = {'LOGON', 'LOGON_FAILED', 'LOGOFF', 'FILE_ACCESS'}
ips = set()
log_file = 'logs.txt'
max_count = 100


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    input('Press enter to continue...')
    clear_console()
    gen_ips()
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
            name = random.choice(list(names))
            ip = workstation[name]
            event = random.choice(list(events))
            f.write(f'{ts},{name},{ip},{event}\n')

# Generate IPs and add to ips set to choose
def gen_ips():
    for i in range(2, 15):
        ips.add('10.1.1.' + str(i))
    for name in names:
        workstation[name] = random.choice(list(ips)) 


    


if __name__ == '__main__':    main()