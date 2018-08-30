import time
import ftplib
import socket
from contextlib import closing
from multiprocessing import Process, Manager, Pool, freeze_support
import ipaddress

# function head for manager
# def attempt_ftp_login(ip, user, password, result_list: list):
#
#     try:
#         with closing(ftplib.FTP(host=str(ip), timeout=2))as ftp:
#             feedback = ftp.login(user, password)
#             ftp.quit()
#         if feedback == '230 User logged in, proceed.':
#             print('{} Successful login.'.format(ip))
#             result_list.append(ip)


# rebuilt function to take a list for pool
def attempt_ftp_login(info: list):
    if len(info) != 3:
        raise Exception('attempt_ftp_login: Wrong number of arguments given')

    ip = info[0]
    user = info[1]
    password = info[2]

    try:
        with closing(ftplib.FTP(host=str(ip), timeout=2))as ftp:
            feedback = ftp.login(user, password)
            ftp.quit()
        if feedback == '230 User logged in, proceed.':
            print('{} Successful login.'.format(ip))
            return ip

    except KeyboardInterrupt:
        exit()
    except ConnectionRefusedError:
        print('{} Connection refused.'.format(ip))
    except ftplib.error_perm:
        print('{} Wrong user/password.'.format(ip))
    except socket.timeout:
        print("{} Timeout.".format(ip))
    # except:
    #     print("{} Unknown error.".format(ip))


targets = ipaddress.ip_network('10.168.1.0/24')
hosts = [
    [str(ip), 'root', 'pass']
    for ip in targets.hosts()
]

if __name__ == '__main__':

    # with a pool
    start = time.time()
    freeze_support()  # necessary for windows
    p = Pool(processes=254)
    result_list = p.map(attempt_ftp_login, hosts)
    result_list = [
        ip
        for ip in result_list
        if ip
    ]
    print()
    print('Results:')
    for ip in result_list:
        print(f'{ip} login success!')
    end = time.time()
    print(end - start)


# With a manager
# with Manager() as manager:
#     Result = manager.list()
#     processes = []
#     for host in targets.hosts():
#         processes.append(Process(target=attempt_ftp_login, args=(host, 'root', 'pass', Result)))
#
#     start = time.time()
#     for p in processes:
#         p.start()
#     for p in processes:
#         p.join()
#     end = time.time()
#
#     print('Time spent: {}sec'.format(round(end - start, 2)))
#     print()
#     # for ip in result:
#     #     print(ip)
#     print(type(Result))

# Without multiprocessing
# start = time.time()
# for ip in ip_list:
#     attempt_ftp_login(ip, 'root', 'pass')
# end = time.time()
# print('Time spent: {}sec'.format(round(end - start, 2)))
