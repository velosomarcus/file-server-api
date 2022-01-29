# Upload Download Files
A Web Server and a CLI to Upload and Download Files.

You can copy files between any machines as long as 
they can communicate with each other over TCP/IP, 
and the port you choose is not blocked by a firewall.

## Install

```bash
git clone https://github.com/velosomarcus/upload-download-files.git
cd upload-download-files
pip3 install -r requirements.txt
```


## Usage

Let's say we want to transfer files between two machines, 
for instance, host A and host B.
First, we need to install this application on both machines.

### Use Case 1 
#### Upload a file saved on host A (IP 192.168.1.10) to host B (IP 1.23.45.67).

- Run the command below on the host B to start the 
  "server part" of the application:
```bash
python3 main.py -p 8888
```

Now that the host B "server" is ready to receive your files, 
you can use either a *web browser* or a *terminal window* to 
upload your file saved on host A.

- Upload your file opening a *web browser* on the host A:
```bash
http://1.23.45.67:8888
```
- Upload your file using a *terminal window* on the host A:
```bash
cd <folder-where-you-installed-the-application>
python3 upload_file.py -f <path-to-file-to-upload> -h http://1.23.45.67:8888
```

### Use Case 2 
#### Download a file stored on host A (IP 1.23.45.67) to host B (IP 192.168.1.20).

- Run the command below on the host A to start the 
  "server part" of the application:
```bash
python3 main.py -p 8888
```

Now that the host A "server" is ready to serve your files, 
you can use either a *web browser* or a *terminal window* to 
download your file stored on host A.

- Download your file opening a *web browser* on the host B:
```bash
http://1.23.45.67:8888
```
- Download your file using a *terminal window* on the host A:
```bash
curl http://1.23.45.67:8888/<filename> --output <filename>
wget http://1.23.45.67:8888/<filename>
```
