from flask import Flask, request, jsonify
from ftphelper import *

app = Flask(__name__)

printdetails()

@app.route('/upload', methods=['POST'])
def upload():
    """Handle file upload requests."""
    try:
        filepath = request.form['filepath']
        destination_path = request.form['destination']
        upload_file(filepath, destination_path)
        return jsonify({"message": "File uploaded successfully"})
    except Exception as e:
        logging.error(f"Error in upload route: {e}")
        return jsonify({"message": "File upload failed"}), 500

@app.route('/download', methods=['POST'])
def download():
    """Handle file download requests."""
    try:
        filepath = request.form['filepath']
        destination_path = request.form['destination']
        download_file(filepath, destination_path)
        return jsonify({"message": "File downloaded successfully"})
    except Exception as e:
        logging.error(f"Error in download route: {e}")
        return jsonify({"message": "File download failed"}), 500

@app.route('/list', methods=['POST'])
def list_files():
    """List files in the specified directory."""
    try:
        directory_path = request.form['path']
        files = list_directory(directory_path)
        return jsonify({"files": files})
    except Exception as e:
        logging.error(f"Error in list route: {e}")
        return jsonify({"message": "Failed to list directory contents"}), 500

@app.route('/delete', methods=['POST'])
def delete():
    """Delete a file from the server."""
    try:
        filepath = request.form['filepath']
        delete_file(filepath)
        return jsonify({"message": "File deleted successfully"})
    except Exception as e:
        logging.error(f"Error in delete route: {e}")
        return jsonify({"message": "File deletion failed"}), 500

@app.route('/rename', methods=['POST'])
def rename():
    """Rename or move a file on the server."""
    try:
        old_path = request.form['old_path']
        new_path = request.form['new_path']
        rename_file(old_path, new_path)
        return jsonify({"message": "File renamed/moved successfully"})
    except Exception as e:
        logging.error(f"Error in rename route: {e}")
        return jsonify({"message": "File renaming/moving failed"}), 500

@app.route('/create_directory', methods=['POST'])
def create_dir():
    """Create a directory on the server."""
    try:
        directory_path = request.form['path']
        create_directory(directory_path)
        return jsonify({"message": "Directory created successfully"})
    except Exception as e:
        logging.error(f"Error in create directory route: {e}")
        return jsonify({"message": "Directory creation failed"}), 500

@app.route('/remove_directory', methods=['POST'])
def remove_dir():
    """Remove a directory from the server."""
    try:
        directory_path = request.form['path']
        remove_directory(directory_path)
        return jsonify({"message": "Directory removed successfully"})
    except Exception as e:
        logging.error(f"Error in remove directory route: {e}")
        return jsonify({"message": "Directory removal failed"}), 500

@app.route('/rename_directory', methods=['POST'])
def rename_directory_route():
    """Rename or move a directory on the server."""
    try:
        old_path = request.form['old_path']
        new_path = request.form['new_path']
        rename_directory(old_path, new_path)
        return jsonify({"message": "Directory renamed/moved successfully"})
    except Exception as e:
        logging.error(f"Error in rename directory route: {e}")
        return jsonify({"message": "Directory renaming/moving failed"}), 500

@app.route('/file_size', methods=['POST'])
def file_size():
    """Get the size of a file on the server."""
    try:
        filepath = request.form['filepath']
        size = get_file_size(filepath)
        return jsonify({"size": size})
    except Exception as e:
        logging.error(f"Error in file size route: {e}")
        return jsonify({"message": "Failed to get file size"}), 500

@app.route('/file_exists', methods=['POST'])
def check_file():
    """Check if a file exists on the server."""
    try:
        filepath = request.form['filepath']
        exists = file_exists(filepath)
        return jsonify({"exists": exists})
    except Exception as e:
        logging.error(f"Error in file exists route: {e}")
        return jsonify({"message": "Failed to check file existence"}), 500

@app.route('/file_mtime', methods=['POST'])
def file_mtime():
    """Get the last modification time of a file on the server."""
    try:
        filepath = request.form['filepath']
        mtime = get_file_mtime(filepath)
        return jsonify({"mtime": mtime})
    except Exception as e:
        logging.error(f"Error in file mtime route: {e}")
        return jsonify({"message": "Failed to get file modification time"}), 500

@app.route('/set_permissions', methods=['POST'])
def set_permissions():
    """Set permissions for a file on the server."""
    try:
        filepath = request.form['filepath']
        permissions = request.form['permissions']
        set_file_permissions(filepath, permissions)
        return jsonify({"message": "File permissions set successfully"})
    except Exception as e:
        logging.error(f"Error in set permissions route: {e}")
        return jsonify({"message": "Failed to set file permissions"}), 500

@app.route('/search', methods=['POST'])
def search():
    """Search for files on the server."""
    try:
        pattern = request.form['pattern']
        files = search_files(pattern)
        return jsonify({"files": files})
    except Exception as e:
        logging.error(f"Error in search route: {e}")
        return jsonify({"message": "File search failed"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Check the health of the FTP server."""
    try:
        is_healthy = check_ftp_health()
        if is_healthy:
            return jsonify({"message": "FTP server is healthy"})
        else:
            return jsonify({"message": "FTP server is not healthy"}), 503
    except Exception as e:
        logging.error(f"Error in health check route: {e}")
        return jsonify({"message": "Health check failed"}), 500

if __name__ == '__main__':
    app.run(debug=True)

