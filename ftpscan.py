#! /usr/bin/env python3

import ftplib
import ipaddress
import socket
import argparse
import os
from contextlib import closing
from multiprocessing import Pool, freeze_support
import threading
from sys import exit


def _parse_arguments():
    """
    Initialize CLI arguments
    """
    global args
    parser = argparse.ArgumentParser(
        description='Scans for ftp-servers with provided user / password'
    )
    parser.add_argument('cidr', help='Subnet to scan <192.168.0.0/24>')
    parser.add_argument('user', help='<username> to attempt login.')
    parser.add_argument('password', help='<password> to attempt login.')
    parser.add_argument('-f', '--file', help='Filename to store results.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    args = parser.parse_args()


def main():
    """ Main Program """

    _parse_arguments()

    try:
        targets = ipaddress.ip_network(args.cidr)
        target_data_list = [
            [str(ip), args.user, args.password]
            for ip in targets.hosts()
        ]
    except:
        print('Invalid CIDR...')
        exit(1)

    workers = 256
    result = multiprocessor(attempt_ftp_login, target_data_list, workers)
    if result:
        print_banner()
        for ip in result:
            print('{} login success!'.format(ip))
    else:
        print('No results...')

    if args.file:
        write_results(result, os.path.join(os.getcwd(), args.file))


def multiprocessor(funktion, data, workers):
    """
    Multiprocessing function. Passes the function and data along with the number of workers.

    :param funktion: The function to multiprocess.
    :param data: The data to pass to the function that's being multiprocess'd.
    :param workers: The number of workers.
    :return: A cleaned list of successful login's.
    """
    freeze_support()
    p = Pool(processes=workers)
    result = p.map(funktion, data)
    clean_list = [
        ip
        for ip in result
        if ip
    ]
    return clean_list


def print_banner():
    print('')
    print('###########################')
    print('#        RESULTS          #')
    print('###########################')
    print('')


def attempt_ftp_login(login_info: list):
    """
    Attempts FTP login and returns IP of successful login.
    :param login_info: list: IP,USER,PASSWORD
    :return: str: IP of successful login
    """
    if len(login_info) != 3:
        raise Exception('attempt_ftp_login: Wrong number of arguments given')

    ip = login_info[0]
    user = login_info[1]
    password = login_info[2]

    try:
        with closing(ftplib.FTP(host=str(ip), timeout=2))as ftp:
            feedback = ftp.login(user, password)
            ftp.quit()
        if feedback == '230 User logged in, proceed.':
            if args.verbose:
                print('{} Successful login.'.format(ip))
            return ip

    except KeyboardInterrupt:
        exit()
    except ConnectionRefusedError:
        if args.verbose:
            print('{} Connection refused.'.format(ip))
    except ftplib.error_perm:
        if args.verbose:
            print('{} Wrong user/password.'.format(ip))
    except socket.timeout:
        if args.verbose:
            print("{} Timeout.".format(ip))
    except:
        if args.verbose:
            print("{} Unknown error.".format(ip))


def write_results(result, filename):
    """
    Writes a list / tuple item by item to a file.
    :param result: IP list of successful login's.
    :param filename: Filename to write results.
    """
    print("Writing list of successful login's to: {}".format(filename))
    with open(filename, 'w') as f:
        for ip in result:
            f.writelines(ip + '\n')


if __name__ == '__main__':
    main()
