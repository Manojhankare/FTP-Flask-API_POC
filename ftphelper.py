from ftplib import FTP
import os
import logging

import fnmatch

FTP_SERVER = os.getenv('FTP_SERVER')
FTP_PORT = int(os.getenv('FTP_PORT', 21))  # Default to port 21 if not set
FTP_USERNAME = os.getenv('FTP_USERNAME')
FTP_PASSWORD = os.getenv('FTP_PASSWORD')

logging.basicConfig(level=logging.INFO)

def printdetails():
    """Print FTP connection details."""
    if not FTP_SERVER or not FTP_USERNAME:
        logging.warning("FTP_SERVER or FTP_USERNAME environment variable is not set.")
        return
    
    logging.info("FTP Server: %s", FTP_SERVER)
    logging.info("FTP Port: %d", FTP_PORT)
    logging.info("FTP Username: %s", FTP_USERNAME)
    logging.info("FTP Password: [Hidden]")

def connect_ftp():
    """Connect to the FTP server and return the connection object."""
    logging.info("Connecting to FTP server at %s:%d", FTP_SERVER, FTP_PORT)
    ftp = FTP()
    try:
        ftp.connect(host=FTP_SERVER, port=FTP_PORT)
        ftp.login(user=FTP_USERNAME, passwd=FTP_PASSWORD)
        logging.info("Connected to FTP server")
    except Exception as e:
        logging.error("Failed to connect to FTP server: %s", e)
        raise
    return ftp

def close_ftp(ftp):
    """Close the FTP connection."""
    logging.info("Closing FTP connection")
    try:
        ftp.quit()
        logging.info("FTP connection closed")
    except Exception as e:
        logging.error("Failed to close FTP connection: %s", e)

def upload_file(filepath, destination_path):
    """Upload a file to the FTP server."""
    ftp = None
    try:
        ftp = connect_ftp()
        with open(filepath, 'rb') as file:
            logging.info("Uploading file %s to %s", filepath, destination_path)
            ftp.storbinary(f'STOR {destination_path}', file)
            logging.info("File uploaded successfully")
    except Exception as e:
        logging.error("Upload failed: %s", e)
        raise
    finally:
        if ftp:
            close_ftp(ftp)

def download_file(filepath, destination_path):
    """Download a file from the FTP server."""
    ftp = None
    try:
        ftp = connect_ftp()
        with open(destination_path, 'wb') as file:
            logging.info("Downloading file %s to %s", filepath, destination_path)
            ftp.retrbinary(f'RETR {filepath}', file.write)
            logging.info("File downloaded successfully")
    except Exception as e:
        logging.error("Download failed: %s", e)
        raise
    finally:
        if ftp:
            close_ftp(ftp)

def list_directory(path):
    """List files and directories in the specified path."""
    ftp = None
    try:
        ftp = connect_ftp()
        files = ftp.nlst(path)
        logging.info("Listed files in %s: %s", path, files)
        return files
    except Exception as e:
        logging.error("Failed to list directory contents: %s", e)
        raise
    finally:
        if ftp:
            close_ftp(ftp)

def delete_file(filepath):
    """Delete a file from the FTP server."""
    ftp = None
    try:
        ftp = connect_ftp()
        ftp.delete(filepath)
        logging.info("File %s deleted successfully", filepath)
    except Exception as e:
        logging.error("Failed to delete file: %s", e)
        raise
    finally:
        if ftp:
            close_ftp(ftp)

def rename_file(old_path, new_path):
    """Rename or move a file on the FTP server."""
    ftp = None
    try:
        ftp = connect_ftp()
        ftp.rename(old_path, new_path)
        logging.info("File renamed/moved from %s to %s", old_path, new_path)
    except Exception as e:
        logging.error("Failed to rename/move file: %s", e)
        raise
    finally:
        if ftp:
            close_ftp(ftp)

def create_directory(path):
    """Create a directory on the FTP server."""
    ftp = None
    try:
        ftp = connect_ftp()
        ftp.mkd(path)
        logging.info("Directory %s created successfully", path)
    except Exception as e:
        logging.error("Failed to create directory: %s", e)
        raise
    finally:
        if ftp:
            close_ftp(ftp)

def remove_directory(path):
    """Remove a directory from the FTP server."""
    ftp = None
    try:
        ftp = connect_ftp()
        ftp.rmd(path)
        logging.info("Directory %s removed successfully", path)
    except Exception as e:
        logging.error("Failed to remove directory: %s", e)
        raise
    finally:
        if ftp:
            close_ftp(ftp)

def rename_directory(old_path, new_path):
    """Rename or move a directory on the FTP server."""
    ftp = None
    try:
        ftp = connect_ftp()
        # List contents of old directory and move them to the new directory
        files = ftp.nlst(old_path)
        ftp.mkd(new_path)  # Create new directory
        for file in files:
            if file != old_path:
                ftp.rename(file, os.path.join(new_path, os.path.basename(file)))
        ftp.rmd(old_path)  # Remove old directory
        logging.info("Directory renamed/moved from %s to %s", old_path, new_path)
    except Exception as e:
        logging.error("Failed to rename/move directory: %s", e)
        raise
    finally:
        if ftp:
            close_ftp(ftp)

def get_file_size(filepath):
    """Get the size of a file on the FTP server."""
    ftp = None
    try:
        ftp = connect_ftp()
        size = ftp.size(filepath)
        logging.info("File size of %s: %d bytes", filepath, size)
        return size
    except Exception as e:
        logging.error("Failed to get file size: %s", e)
        raise
    finally:
        if ftp:
            close_ftp(ftp)

def file_exists(filepath):
    """Check if a file exists on the FTP server."""
    ftp = None
    try:
        ftp = connect_ftp()
        files = ftp.nlst()  # List files in the current directory
        exists = filepath in files
        logging.info("File %s exists: %s", filepath, exists)
        return exists
    except Exception as e:
        logging.error("Failed to check file existence: %s", e)
        raise
    finally:
        if ftp:
            close_ftp(ftp)

def get_file_mtime(filepath):
    """Get the last modification time of a file on the FTP server."""
    ftp = None
    try:
        ftp = connect_ftp()
        mtime = ftp.sendcmd(f'MDTM {filepath}')
        logging.info("File modification time of %s: %s", filepath, mtime)
        return mtime
    except Exception as e:
        logging.error("Failed to get file modification time: %s", e)
        raise
    finally:
        if ftp:
            close_ftp(ftp)

def set_file_permissions(filepath, permissions):
    """Set permissions for a file on the FTP server."""
    ftp = None
    try:
        ftp = connect_ftp()
        # Example command, adjust according to FTP server's capabilities
        ftp.sendcmd(f'SITE CHMOD {permissions} {filepath}')
        logging.info("File permissions set to %s for %s", permissions, filepath)
    except Exception as e:
        logging.error("Failed to set file permissions: %s", e)
        raise
    finally:
        if ftp:
            close_ftp(ftp)

def search_files(pattern):
    """Search for files matching the pattern on the FTP server."""
    ftp = None
    try:
        ftp = connect_ftp()
        all_files = ftp.nlst()  # List all files
        matched_files = fnmatch.filter(all_files, pattern)
        logging.info("Files matching pattern %s: %s", pattern, matched_files)
        return matched_files
    except Exception as e:
        logging.error("Failed to search files: %s", e)
        raise
    finally:
        if ftp:
            close_ftp(ftp)

def check_ftp_health():
    """Check if the FTP server is reachable."""
    ftp = None
    try:
        ftp = connect_ftp()
        ftp.quit()
        logging.info("FTP server is reachable")
        return True
    except Exception as e:
        logging.error("FTP server is not reachable: %s", e)
        return False
    finally:
        if ftp:
            close_ftp(ftp)
