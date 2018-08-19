#! /usr/bin/env python3

import ftplib
import ipaddress
import socket
import argparse
import os


def main():
    """ Main Program """

    # todo: implement multiprocessing

    result = scan(args.cidr, args.user, args.password)
    if args.file:
        _write_results(result, os.path.join(os.getcwd(), args.file))


def scan(cidr, user, password):
    """
    Scan provided subnet for ftp access with provided user/password.
    :param cidr: Subnet, <192.168.0.0/24>
    :param user: Username to attempt login.
    :param password: Password to attempt login
    :return: IP [list] of successful login's.
    """
    network = ipaddress.ip_network(cidr)
    result = []

    for ip in network.hosts():
        try:
            ftp = ftplib.FTP(host=str(ip), timeout=2)
            feedback = ftp.login(user, password)
            ftp.quit()
            if feedback == '230 User logged in, proceed.':
                result.append(str(ip))
                print('{} Successful login.'.format(ip))

        except KeyboardInterrupt:
            exit()
        except ConnectionRefusedError:
            print('{} Connection refused.'.format(ip))
        except ftplib.error_perm:
            print('{} Wrong user/password.'.format(ip))
        except socket.timeout:
            print("{} Timeout.".format(ip))
        except:
            print("{} Unknown error.".format(ip))

    return result


def _write_results(result, filename):
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

    # Initialize CLI arguments

    parser = argparse.ArgumentParser(
        description='Scans for ftp-servers with provided user / password'
    )
    parser.add_argument('cidr', help='Subnet to scan <192.168.0.0/24>')
    parser.add_argument('user', help='<username> to attempt login.')
    parser.add_argument('password', help='<password> to attempt login.')
    parser.add_argument('-f', '--file', help='Filename to store results.')
    args = parser.parse_args()
    main()
