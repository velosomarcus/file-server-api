import os
import sys
import time

import click
import requests


@click.command()
@click.option('-f', '--file-path', 'file_path', required=True)
@click.option('-h', '--host-url', 'host_url', required=True)
def main(file_path, host_url):
    """
    Upload a file to server using the flask server defined in main.py

    :param file_path: The full path and filename of file to upload
    :param host_url: The host and port where to upload file (e.g: http://192.168.1.100:8888)
    :return:
    """
    # check if file path folder exist
    if not os.path.isfile(file_path):
        print('Error: File', file_path, 'does not exist!')
        sys.exit(1)
    # ToDo: check if the `host_url` is a valid URL

    # try to upload the file
    with open(file_path, 'rb') as file:
        req = requests.post(host_url, files={'file': open(file_path, 'rb')})
        if req.status_code == 200:
            print('File ', file_path, 'was uploaded with success to ', host_url)
        else:
            print('Upload failed')


if __name__ == '__main__':
    print("---------------------------------------------")
    print("Upload Download Files - Upload Script v-1.0.3")
    print("Date/Time: {}".format(time.asctime(time.localtime(time.time()))))
    print("---------------------------------------------")

    main()
