import os
import sys
import time

import click
import requests
import urllib.parse


API_ENDPOINT = '/api'
VERSION = '1.1.4'


def is_valid_url(url):
    """
    Checks if a given URL is valid and reachable.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is valid and reachable, False otherwise.
    """
    try:
        result = urllib.parse.urlparse(url)
        # Try to reach url with a `HEAD` call
        response = requests.head(url)
        response.raise_for_status()
        return all([result.scheme, result.netloc])

    except (ValueError, requests.exceptions.RequestException):
        return False

def exit_with_error(message):
    """
    Prints an error message and exits the program with a non-zero exit code.

    Args:
        message (str): The error message to print.
    """
    print(f"Error: {message}")
    sys.exit(1)


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
    # ensure host_url starts with http://
    if not host_url.startswith('http://'):
        host_url = 'http://' + host_url

    # check if file path folder exist
    if not os.path.isfile(file_path):
        exit_with_error(f"File {file_path} does not exist!")

    # check if the `host_url` is a valid URL
    if not is_valid_url(host_url):
        exit_with_error(f"Invalid URL or unreachable host: {host_url}")

    # try to upload the file
    try:
        with open(file_path, 'rb') as file: #Opens the file in binary read mode `rb` to ensure proper handling of different file types
            req = requests.post(host_url + API_ENDPOINT, files={'file': file})
            req.raise_for_status() #Raise an exception for bad status code
            print('File ', file_path, 'was uploaded with success to ', host_url)

    except requests.exceptions.RequestException as e:
        exit_with_error(f"Error during upload: {e}")

if __name__ == '__main__':
    print("------------------------------")
    print(f"API Manual Upload File v-{VERSION}")
    print("Date/Time: {}".format(time.asctime(time.localtime(time.time()))))
    print("------------------------------")

    main()
