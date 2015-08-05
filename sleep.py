__author__ = 'viren'

import sys
import os
import time
import subprocess
import argparse

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('timeout', help='Timeout in minutes')
        parser.add_argument('-s', '--sleep', help='Sleep (default)', action='store_true')
        parser.add_argument('-z', '--hibernate', help='Hibernate', action='store_true')
        args = parser.parse_args()

        timeout_minutes = args.timeout if args.timeout else 0
        timeout_seconds = int(timeout_minutes) * 60

        if args.hibernate:
            action = 'Hibernating'
        else:
            action = 'Sleeping'
            
        for i in range(0, timeout_seconds):
            sys.stdout.write('{} in {} minutes {} seconds...\r'.format(action, 
                                                                       (timeout_seconds-i)/60, 
                                                                       (timeout_seconds-i)%60 ))
            sys.stdout.flush()
            time.sleep(1)

        path = 'C:\\Windows\\System32\\rundll32.exe PowrProf.dll, SetSuspendState '
        if args.hibernate:
            path += '1,0,0'
        else:
            path += '0,0,0'
        subprocess.call(path)

    except KeyboardInterrupt:
        print '\nKeyboardInterrupt: Operation cancelled'
        sys.exit()

    except Exception as e:
        sys.stderr.write('Exception: ' + str(e) + '\n')
        sys.exit()


if __name__ == '__main__':
    if os.name == 'nt':
        main()
    else:
        sys.stderr.write('Unsupported OS\n')
        sys.exit()

