def get_media_type(file_name):
    media_types = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }
    file_extension = file_name.lower().strip().split('.')[-1]
    if file_extension in media_types:
        return media_types[file_extension]
    else:
        return 'application/octet-stream'

def main():
    file_name = input('File name')
    media_type = get_media_type(file_name)
    print(media_type)
if __name__ == "__main__":
    main()
