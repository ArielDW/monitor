import os
import time
import subprocess
import signal


def ping_google():
    while True:
        try:
            subprocess.check_output(['ping', '-c 1', 'google.com'])
            print("Google ping successful")
            time.sleep(10)
        except subprocess.CalledProcessError as e:
            print("Google ping failed. Stopping daemon.")
            break


def start_daemon():
    # Fork the process
    try:
        pid = os.fork()
        if pid > 0:
            # Exit first parent
            exit(0)
    except OSError as e:
        exit(1)

    # Decouple from parent environment
    os.chdir('/')
    os.setsid()
    os.umask(0)

    # Do second fork
    try:
        pid = os.fork()
        if pid > 0:
            with open('daemon.pid', 'w') as f:
                f.write(str(pid))
            print(f"Daemon started successfully with PID: {pid}")
            return pid
    except OSError as e:
        exit(1)

    # Start the daemon
    ping_google()


def stop_daemon():
    with open('daemon.pid', 'r') as f:
        pid = int(f.read())
    os.kill(pid, signal.SIGTERM)
    os.remove('daemon.pid')
