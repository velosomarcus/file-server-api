# File Server API
A simple API to Upload and Download Files and a CLI Client to upload files manually.

## Install

### Running on your local machine

These instructions assume that we already have Python3 installed on our machine.

```bash
git clone https://github.com/velosomarcus/file-server-api.git
cd file-server-api
python3 -m pip install -r requirements.txt
```

#### Run the API

```bash
cd file-server-api
python3 main.py -p 8888 [-o]  # see the help running "python3 main.py --help"
```
Now this machine is serving the files under the folder `file-server-api/files`.

### Running as a Docker container

We can use the existing image on Docker Hub, at:
https://hub.docker.com/repository/docker/marcusveloso/file-server-api

Or we can build the image following these instructions

#### How to build the image:
```bash
docker build --no-cache -t file-server-api:<tag> . -f ./docker/Dockerfile
```

#### How to create and run the container:
```bash
docker run --name <file-server-api-container-name> -p 8888:8888 -d file-server-api:<tag>
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
Upload a file manually.

You can use a *web browser* or a *terminal window* to 
upload your file to the API.

- Upload your file using a *web browser*:
  - Point you browser to the URL below, select your file and click the *Upload* button.
```bash
http://host:port/api/filename
```

- To upload your file using a *terminal window*, 
  you first need to install the repository on 
  the machine where you have a file to upload to the API.
  And then run the command below:
```bash
cd <folder-where-you-installed-the-application>
python3 api_client.py -f filename -h host:port
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
curl http://host:port/api/filename --output filename
```


### Note:

In these instructions, the words *host*, *port* and *filename* 
must be replaced with their current values of you project. 
For example: 
- *host* is the IP of your API server machine
- *port* is the port you choose when you run the API
- *filename* is the name of the file you are uploading, downloading or deleting
