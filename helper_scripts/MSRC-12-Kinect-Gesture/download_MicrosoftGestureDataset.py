#taken from this StackOverflow answer: https://stackoverflow.com/a/39225039
import requests
import os
import sys
from tqdm import tqdm

def download_file(id, destination):
    URL = "https://download.microsoft.com/download/A/D/F/ADFCE572-617F-4FD0-A822-AF6F05CBE61F/MicrosoftGestureDataset.zip"
    
    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    total_size_in_bytes = int(response.headers.get('content-length',0)) or None

    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)      

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    
    CHUNK_SIZE = 32768
    
    with open(destination, "wb") as f:
      for chunk in response.iter_content(CHUNK_SIZE):
        progress_bar.update(len(chunk))
        if chunk: # filter out keep-alive new chunks
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
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

sep = os.path.sep
if(not os.path.isdir('..' + sep + '..' + sep + 'RawDatasets' + sep + 'MSRC-Kinect')):
  os.mkdir('..' + sep + '..' + sep + 'RawDatasets' + sep + 'MSRC-Kinect')

file_id = '0B20a4UzO-OyMQW9wVHhlVmZBR0k'
destination = os.path.abspath('..' + sep + '..' + sep + 'RawDatasets' + sep + 'MSRC-Kinect') + sep + 'MicrosoftGesture.zip'
print('Downloading MSRC dataset zip to ' + destination)
download_file(file_id, destination)
print('Finished\nFind the zip at ' + destination)

