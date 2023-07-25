# noinspection PyUnusedLocal
import os

APPS = ['Camera High Frequency', 'Cpu Medium Frequency', 'GPS Low Frequency', 'Local Storage High Frequency', 'Networking Medium Frequency']

def main(device, *args, **kwargs):
    path = '/home/radu/usb/android-apps-benchmark/APKs'
    
    for app in APPS:
        for apk in os.listdir(path + '/' + app):
            device.install(path + '/' + app + '/' + apk)

    device.install('/home/radu/usb/com.example.batterymanager_utility.apk')
