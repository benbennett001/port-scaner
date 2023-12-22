
import socket

# ip validation 
def is_valid_ip(ip_str: str) -> bool:
    ip_sub_list = ip_str.split(sep='.')

    if len(ip_sub_list) != 4:
        return False
    
    for sub in ip_sub_list:
        if 3 < len(sub) or len(sub) < 1 or sub.isdigit() is False:
            return False

    return True

# scan for one ip add
def sop_one():
    ip_str = input('Enter the IP addr: ')

    # call ip validation
    if is_valid_ip(ip_str) == False:
        return      
    
    # get ports number
    ports = int(input('Enter a number of ports: '))

    scan_port(ip_str, ports)

# scan function using socket library
def scan_port(ip_str, ports):
    print(f'\tStart scanning for >> {ip_str}  <<')

    for port in range(1, ports):
        try:
            # af_inet and sock_stream are the simplest functions
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            # host and port pair >> touple 
            s.connect((ip_str, port))
            print(f'The port {port} is open')

        # TODO: 
        # add the no route to host error code for not assing ips
        except (TimeoutError, ConnectionRefusedError):
            pass
        
        finally:
            s.close()

# scan for a list of ips
def sop_group():
    file_name = input('Name of the list of ips to scan: ')
    clean_list = []
    with open(file_name, 'r') as devices_text:
        ip_list = devices_text.readlines()

    for ip in ip_list:
        # cleaning the list
        ip = ip.removesuffix('\n')
        clean_list.append(ip)
        
    #goin through the list
    for ip in clean_list:

        if is_valid_ip(ip) is False: 
            print(f'invalid ip: {ip}\n' ) 
            continue

        print(f'#\tFor ip --> {ip}:')
        ports = int(input('#\tEnter a number of ports: '))
        scan_port(ip, ports)

# display the file with the list of ips 
def print_file():
    try:
        file_name = input('\tName of the file you want to read: ')
        with open(file_name, 'r') as devices_text:
            text = devices_text.read()
            print('The file content is:')
            print(text)
    except FileNotFoundError:
        print('### Failed to open the file devices.txt. ###\n')
        exit()

# MAIN MENU
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


