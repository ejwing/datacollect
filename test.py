import sys
import requests

def download_file(url, fileName):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        if r.headers['Content-Type'] == 'application/octet-stream': # streaming data
            size = r.headers['Content-Length'] # file size
            print('file size: {} bytes'.format(size))
            # write into file
            with open(fileName, 'wb') as f:
                count = 0
                process_rate = 0
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        count += len(chunk)
                        pr = int(count / int(size) * 100)
                        if process_rate != pr:
                            process_rate = pr
                            print('{}: {:3d}%'.format(fileName, process_rate))
                    else:
                        print('no chunk')
            r.close()
            return fileName
        else:
            print('content type is not zip file.')
            r.close()
            return None
    else:
        print('request failed')
        r.close()
        return None
