import socket

def is_valid_ip(ip_str: str) -> bool:
    ip_sub_list = ip_str.split(sep='.')

    if len(ip_sub_list) != 4:
        return False
    
    for sub in ip_sub_list:
        if 3 < len(sub) or len(sub) < 1 or sub.isdigit() is False:
            return False

    return True

def sop_one():
    ip_str = input('Enter the IP addr: ')

    if is_valid_ip(ip_str) == False:
        return      
    
    ports = int(input('Enter a number of ports: '))

    scan_port(ip_str, ports)

def scan_port(ip_str, ports):
    print(f'\tStart scanning for {ip_str}')
    for port in range(1, ports):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((ip_str, port))
            print(f'The port {port} is open')

        except (TimeoutError, ConnectionRefusedError):
            pass
        
        finally:
            s.close()

def sop_group():
    clean_list = []
    with open('devices.txt', 'r') as devices_text:
        ip_list = devices_text.readlines()

    for ip in ip_list:
        ip = ip.removesuffix('\n')
        clean_list.append(ip)
        
    for ip in clean_list:
        if is_valid_ip(ip) is False: 
            print(f'invalid ip: {ip}\n' ) 
            continue

        print(f'For ip {ip} -->')
        ports = int(input('Enter a number of ports: '))
        scan_port(ip, ports)

def print_file():
    try:
        with open('devices.txt', 'r') as devices_text:
            text = devices_text.read()
            print('The file content is:')
            print(text)
    except FileNotFoundError:
        print('Failed to open the file devices.txt.\n')
        exit()


while True:
    print('\nPort Scanner Menu:')
    print('\t1- Print the file contents.')
    print('\t2- Search Open Ports for one single device.')
    print('\t3- Search Open Ports for a group of devices.')
    print('\t4- Quit.')

    numb = input()

    if numb == '1':
        print_file()

    elif numb == '2':
        sop_one()

    elif numb == '3':
        sop_group()

    elif numb == '4':
        print('The program is closed')
        break


