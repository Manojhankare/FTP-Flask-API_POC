
# FTP Flask Demo

## Overview

This project is a Flask-based web application that interacts with an FTP server. It provides a set of RESTful APIs for performing common file operations on the FTP server, including uploading, downloading, listing, deleting, renaming files and directories, and more. 

## Features

- **Upload Files**: Upload files to the FTP server.
- **Download Files**: Download files from the FTP server.
- **List Files**: List files in a specified directory.
- **Delete Files**: Delete files from the FTP server.
- **Rename/Move Files**: Rename or move files on the FTP server.
- **Create/Remove Directories**: Create or remove directories on the FTP server.
- **Rename/Move Directories**: Rename or move directories on the FTP server.
- **File Size**: Get the size of a file on the FTP server.
- **Check File Existence**: Check if a file exists on the FTP server.
- **File Modification Time**: Get the last modification time of a file.
- **Set File Permissions**: Set permissions for a file on the FTP server.
- **Search Files**: Search for files on the FTP server based on a pattern.
- **Health Check**: Check the health status of the FTP server.

## Setup

### Prerequisites

- Python 3.7 or later
- Flask
- An FTP server to connect to

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/username/FTP-Flask-Demo.git
   cd FTP-Flask-Demo
   

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Create Environment Variables**

   Create a `.env` file in the root directory of the project and add the following content:

   ```
   FTP_SERVER=your_ftp_server
   FTP_PORT=21
   FTP_USERNAME=your_username
   FTP_PASSWORD=your_password
   ```

6. **Run the Application**

   ```bash
   python run.py
   ```

   The application will start and be accessible at `http://127.0.0.1:5000`.

## API Endpoints

### Upload File

- **Endpoint**: `/upload`
- **Method**: `POST`
- **Parameters**:
  - `filepath`: Path to the file on the local system.
  - `destination`: Path on the FTP server where the file should be uploaded.
- **Response**: JSON with a message indicating success or failure.

### Download File

- **Endpoint**: `/download`
- **Method**: `POST`
- **Parameters**:
  - `filepath`: Path to the file on the FTP server.
  - `destination`: Path on the local system where the file should be downloaded.
- **Response**: JSON with a message indicating success or failure.

### List Files

- **Endpoint**: `/list`
- **Method**: `POST`
- **Parameters**:
  - `path`: Directory path on the FTP server to list files.
- **Response**: JSON with a list of files in the specified directory.

### Delete File

- **Endpoint**: `/delete`
- **Method**: `POST`
- **Parameters**:
  - `filepath`: Path to the file on the FTP server to be deleted.
- **Response**: JSON with a message indicating success or failure.

### Rename/Move File

- **Endpoint**: `/rename`
- **Method**: `POST`
- **Parameters**:
  - `old_path`: Current path of the file on the FTP server.
  - `new_path`: New path or name of the file on the FTP server.
- **Response**: JSON with a message indicating success or failure.

### Create Directory

- **Endpoint**: `/create_directory`
- **Method**: `POST`
- **Parameters**:
  - `path`: Path of the directory to be created on the FTP server.
- **Response**: JSON with a message indicating success or failure.

### Remove Directory

- **Endpoint**: `/remove_directory`
- **Method**: `POST`
- **Parameters**:
  - `path`: Path of the directory to be removed on the FTP server.
- **Response**: JSON with a message indicating success or failure.

### Rename/Move Directory

- **Endpoint**: `/rename_directory`
- **Method**: `POST`
- **Parameters**:
  - `old_path`: Current path of the directory on the FTP server.
  - `new_path`: New path or name of the directory on the FTP server.
- **Response**: JSON with a message indicating success or failure.

### Get File Size

- **Endpoint**: `/file_size`
- **Method**: `POST`
- **Parameters**:
  - `filepath`: Path to the file on the FTP server.
- **Response**: JSON with the size of the file.

### Check File Existence

- **Endpoint**: `/file_exists`
- **Method**: `POST`
- **Parameters**:
  - `filepath`: Path to the file on the FTP server.
- **Response**: JSON with a boolean indicating whether the file exists.

### Get File Modification Time

- **Endpoint**: `/file_mtime`
- **Method**: `POST`
- **Parameters**:
  - `filepath`: Path to the file on the FTP server.
- **Response**: JSON with the last modification time of the file.

### Set File Permissions

- **Endpoint**: `/set_permissions`
- **Method**: `POST`
- **Parameters**:
  - `filepath`: Path to the file on the FTP server.
  - `permissions`: Permissions to be set (e.g., '755').
- **Response**: JSON with a message indicating success or failure.

### Search Files

- **Endpoint**: `/search`
- **Method**: `POST`
- **Parameters**:
  - `pattern`: Search pattern for file names.
- **Response**: JSON with a list of files matching the pattern.

### Health Check

- **Endpoint**: `/health`
- **Method**: `GET`
- **Response**: JSON indicating whether the FTP server is healthy.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.


## Contact

For any questions or issues, please contact the repository owner at `manojhankare2@gmail.com`.
```
