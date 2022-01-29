import os
import logging

from flask import Flask, request, redirect, jsonify, send_file
from werkzeug.utils import secure_filename
import click


# configure the logging
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s][%(levelname)s] %(message)s')
# create the logger
logger = logging.getLogger()

UP_DOWN_FOLDER = os.getcwd() + '/files'
os.makedirs(UP_DOWN_FOLDER, mode=0o777, exist_ok=True)

app = Flask(__name__)

overwrite = False

@click.command()
@click.option('-p', '--port-number', 'port', required=True)
@click.option('-o', '--overwrite-existing-file', 'ow', is_flag=True)
def main(port, ow):
    """
    A minimal Flask server to upload and download files.

    :param port: The port number to be used by the server.
    :param ow: This parameter allows the server to overwrite existing files during the upload.
    :return:
    """
    global overwrite
    overwrite = ow
    print()
    logger.info("------------------------")
    logger.info("File Server API v-1.0.10")
    logger.info("Files Folder: {}/files".format(os.getcwd()))
    logger.info("Allow overwrite existing files: {}".format(ow))
    logger.info("------------------------\n")

    app.run("0.0.0.0", port=port, debug=False)


@app.route('/api/<filename>', methods=['GET', 'DELETE'])
def download_file(filename):
    if request.method == 'GET':
        path_and_filename = os.path.join(UP_DOWN_FOLDER, filename)
        if os.path.isfile(path_and_filename):
            if path_and_filename[:1] == ".":  # required to avoid error when call send_file() function
                path_and_filename = os.getcwd() + path_and_filename[1:]

            return send_file(path_and_filename, attachment_filename=filename)
        else:
            app.logger.info('File not found: %s  Client-IP: %s', filename, request.remote_addr)
            return 'File not found', 404

    elif request.method == 'DELETE':
        path_and_filename = os.path.join(UP_DOWN_FOLDER, filename)
        if os.path.isfile(path_and_filename):
            os.unlink(path_and_filename)
            return jsonify(
                {
                    'delete_success': True,
                    'message': 'File is deleted'
                }
            )
        else:
            app.logger.info('File not found: %s  Client-IP: %s', filename, request.remote_addr)
            return 'File not found', 404


@app.route('/api', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return '''
            <!doctype html>
            <title>Upload a File</title>
            <h1>Upload a File</h1>
            <form method=post enctype=multipart/form-data>
              <input type=file name=file>
              <input type=submit value=Upload>
            </form>
        '''

    if request.method == 'POST':
        # check if the post request has the file part
        file = request.files.get('file')
        if not file:
            logger.info('not file')
            return redirect(request.url)
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            logger.info('file == ""')
            return redirect(request.url)

        filename = secure_filename(file.filename)

        # file part is ok
        upload_path_and_filename = os.path.join(UP_DOWN_FOLDER, filename)
        # if file already exist
        if os.path.isfile(upload_path_and_filename) and not overwrite:
            app.logger.info('File already exists. Use -o option to allow overwrite')
            return 'File already exists', 403

        # save file
        file.save(upload_path_and_filename)
        app.logger.info('File uploaded: %s  Size: %i bytes  Client-IP: %s',
                        filename, os.path.getsize(upload_path_and_filename), request.remote_addr)

        return jsonify(
            {
                'upload_success': True,
                'filename': filename
            }
        )


if __name__ == "__main__":
    main()
