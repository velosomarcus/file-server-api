# File Server API
An API to Upload and Download Files and a CLI Client to upload files manually.

## Install

These instructions assume that you already have Python3 installed on you machine.

```bash
git clone https://github.com/velosomarcus/file-server-api.git
cd file-server-api
python3 -m pip install -r requirements.txt
```

## Run the API

```bash
cd file-server-api
python3 main.py -p 8888 [-o]  # see the help running "python3 main.py --help"
```

## Usage

### API Endpoints
<hr />

URL:
- http://host:port/api

Description:
- Endpoint to upload a file. It is necessary to send in the Http request the image file.

Method:
- POST

Return:
- Result of the upload process.

<hr />

URL:
- http://host:port/api/filename

Description:
- Endpoint to download a file.

Method:
- GET

Return:
- The file itself.

<hr />

URL:
- http://host:port/api/filename

Description:
- Endpoint to delete an uploaded file.

Method:
- DELETE

Return:
- Result of the delete process.

<hr />

### Use Case 1
Upload a file manually using the CLI client.

- Install the repository on the machine you have a file to upload to the API.
- Run the command below:
```bash
cd <folder-where-you-installed-the-application>
python3 api_client.py -f <path-to-file-to-upload> -h http://1.23.45.67:8888
```

### Use Case 2 
Download a file manually.

You can use a *web browser* or a *terminal window* to 
download your file stored on the API.

- Download your file opening a *web browser*:
```bash
http://host:port/api/filename
```
- Download your file using a *terminal window*, using one of the commands below:
```bash
wget http://host:port/api/filename
curl http://host:port/api/filename --output <filename>
```
