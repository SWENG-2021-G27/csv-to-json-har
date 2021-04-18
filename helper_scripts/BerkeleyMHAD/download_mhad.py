# taken from this StackOverflow answer: https://stackoverflow.com/a/39225039
import requests
import os
import sys
from tqdm import tqdm


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    total_size_in_bytes = int(
        response.headers.get('content-length', 0)) or None

    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            progress_bar.update(len(chunk))
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")
    progress_bar.close()


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


file_id = '1uomG5szmcaTsUy6w7CPTLsgBa2by1h3s'
sep = os.path.sep
destination_folder = os.path.abspath(
    '..' + sep + '..' + sep + 'RawDatasets' + sep + 'BerkeleyMHAD')
os.mkdir(destination_folder)
destination = destination_folder + sep + 'BerkeleyMHAD.7z'
print('Downloading BerkeleyMHAD zip to ' + destination)
download_file_from_google_drive(file_id, destination)
