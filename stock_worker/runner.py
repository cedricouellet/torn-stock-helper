#!/usr/bin/env python3

'''
Runner and initializer for the stock worker cron job.
'''

import os
import subprocess
import fileinput

def write(value):
    '''
    Output a value in the console, without a line break.

        Parameters:
            `value`: The string value to output
    '''
    print(value, end='')

def main():
    '''
    `runner.py` entrypoint method
    '''

    # Replace cron file placeholders with env variable values
    for line in fileinput.input('/etc/cron.d/worker_cron', inplace=True):
        if 'DB_HOST_PLACEHOLDER' in line:
            write(line.replace('DB_HOST_PLACEHOLDER', os.environ['DB_HOST']))
        elif 'DB_DATABASE_PLACEHOLDER' in line: 
            write(line.replace('DB_DATABASE_PLACEHOLDER', os.environ['DB_DATABASE'])) 
        elif 'DB_USER_PLACEHOLDER' in line:
            write(line.replace('DB_USER_PLACEHOLDER', os.environ['DB_USER']))
        elif 'DB_PASS_PLACEHOLDER' in line:
            write(line.replace('DB_PASS_PLACEHOLDER', os.environ['DB_PASS']))
        elif 'DB_PORT_PLACEHOLDER' in line:
            write(line.replace('DB_PORT_PLACEHOLDER', os.environ['DB_PORT']))
        elif 'TORN_API_URL_PLACEHOLDER' in line:
            write(line.replace('TORN_API_URL_PLACEHOLDER', os.environ['TORN_API_URL']))
        elif 'TORN_API_KEY_PLACEHOLDER' in line:
            write(line.replace('TORN_API_KEY_PLACEHOLDER', os.environ['TORN_API_KEY']))
        else:
            write(line)

    # Add cron to crontab
    subprocess.call(["crontab", "/etc/cron.d/worker_cron"])

    # Start cron 
    subprocess.call(["cron"])

    # Attach log file
    subprocess.call(["tail", "-f", "/var/log/worker/log.txt"])

if __name__ == '__main__':
    main()