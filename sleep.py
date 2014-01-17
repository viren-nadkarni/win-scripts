__author__ = 'viren'

import sys, os, time, subprocess, argparse

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', help = 'set the time-out period in minutes', type = int)
        parser.add_argument('-z', '--hibernate', help = 'hibernate instead of sleeping', action = 'store_true')
        args = parser.parse_args()

        c = args.t if args.t else 0
        d = int(c) * 60

        if not c:
            print 'No time-out specified'
            sys.exit()
        
        for i in range(0, d):
        	sys.stdout.write('Suspending in %d minutes %d seconds...\r'%((d - i) / 60, (d - i) % 60 ))
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

    except:
        sys.exit()

if __name__ == '__main__':
    if os.name == 'nt':
        main()
    else:
        sys.exit()
