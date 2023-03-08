#!/usr/bin/env python3

'''
Runner and initializer for the stock worker cron job.
'''

import os
from datetime import datetime
import subprocess
import fileinput


def output(value):
    print(value, end='')

def main():
    # Replace cron file placeholders with env variable values
    for line in fileinput.input('/etc/cron.d/worker_cron', inplace=True):
        if 'DB_HOST_PLACEHOLDER' in line:
            output(line.replace('DB_HOST_PLACEHOLDER', os.environ['DB_HOST']))
        elif 'DB_DATABASE_PLACEHOLDER' in line: 
            output(line.replace('DB_DATABASE_PLACEHOLDER', os.environ['DB_DATABASE'])) 
        elif 'DB_USER_PLACEHOLDER' in line:
            output(line.replace('DB_USER_PLACEHOLDER', os.environ['DB_USER']))
        elif 'DB_PASS_PLACEHOLDER' in line:
            output(line.replace('DB_PASS_PLACEHOLDER', os.environ['DB_PASS']))
        elif 'DB_PORT_PLACEHOLDER' in line:
            output(line.replace('DB_PORT_PLACEHOLDER', os.environ['DB_PORT']))
        elif 'TORN_API_URL_PLACEHOLDER' in line:
            output(line.replace('TORN_API_URL_PLACEHOLDER', os.environ['TORN_API_URL']))
        elif 'TORN_API_KEY_PLACEHOLDER' in line:
            output(line.replace('TORN_API_KEY_PLACEHOLDER', os.environ['TORN_API_KEY']))
        else:
            output(line)

    # Register cron job
    subprocess.call(["crontab", "/etc/cron.d/worker_cron"])

    # Start cron jobs
    subprocess.call(["cron"])

    # Attach log file
    subprocess.call(["tail", "-f", "/var/log/worker/log.txt"])

if __name__ == '__main__':
    main()