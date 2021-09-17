import sys
import subprocess


def exitting():
    print('[-] Exiting')
    print('Press any key to exit')
    _ = input()
    sys.exit(1)


def script():
    cmd1_output = str(subprocess.check_output(
        'netsh wlan show drivers', shell=True))
    if 'Hosted network supported  : Yes' in cmd1_output:
        print('[+] Driver supported')

    # print('Name for your hotspot: ')
    # hot_name = input()
    hot_name = 'Canon'
    print(f'Hotspot Name: {hot_name}')
    # print('Enter your password (include alphanumeric, > 8 characters): ')
    # password = input()
    password = 'Canon110022'
    print(f'Password: {password}')

    # while(len(password) < 8):
    #    print('\n[-] Insufficient password strength. Try again ')
    #    print('Enter your password (include alphanumeric, > 8 characters): ')
    #    password = input()

    cmd2 = "netsh wlan set hostednetwork mode=allow ssid="+hot_name+" key="+password
    cmd2_output = str(subprocess.check_output(cmd2, shell=True))
    if 'successfully changed' in cmd2_output:
        print('[+] Hotspot created')
        cmd3_output = str(subprocess.check_output(
            "netsh wlan start hostednetwork", shell=True))
        if 'started' in cmd3_output:
            print('[+] The hotspot is up and running')
            print('Press any key to stop hotspot ')
            stat = input()

            cmd4_output = subprocess.check_output(
                'netsh wlan stop hostednetwork', shell=True)
            print('\n[+] Hotspot has been stopped')
            print('[+] Thanks for using')
            print('Press any key to exit')
            input()
        else:
            print('[-] Oops, Something went wrong')
            exitting()

    sys.exit(0)


def Main():
    print('[+] Checking for admin status')
    try:
        output = str(subprocess.check_output(
            "whoami /groups | find \"S-1-16-12288\"", shell=True))
    except:
        print('[-] You are not admin :( ')
        exitting()
    if('S-1-16-12288' in output):
        print('[+] The program is running with Admin priv :)')
        print('[+] Initiating the script')
        script()


if __name__ == '__main__':
    Main()
