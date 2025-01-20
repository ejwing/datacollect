import requests, progressbar, os
from datetime import date

def download_all_realestate():
    start_year = 101
    current_year = date.today().year - 1911
    for year in range(start_year, current_year):
        for season in range(1, 5):
            filename = download_realestate(year, season)

def download_latest_lestate():
    url = "http://plvr.land.moi.gov.tw/Download?type=zip&fileName=lvr_landcsv.zip"
    if not os.path.exists("./download"):
        os.makedirs("./download")
    print("download latest season. today is", date.today())
    return download_file(url, "./download/{date}.zip".format(date=date.today()))

def download_realestate(year:int, season:int):
    year_season:str = str(year) + "S" + str(season)
    url = "http://plvr.land.moi.gov.tw/DownloadSeason?season=" + year_season + "&type=zip&fileName=lvr_landcsv.zip"
    if not os.path.exists("./download"):
        os.makedirs("./download")
    print("download year: {year} season: {season}".format(year=year,season=season))
    return download_file(url, "./download/" + year_season + ".zip")


def download_file(url, fileName):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        if r.headers['Content-Type'] == 'application/octet-stream': # streaming data
            size = r.headers['Content-Length'] # file size
            print('file size: {} bytes'.format(size))
            # write into file
            with open(fileName, 'wb') as f, progressbar.ProgressBar(max_value=int(size)) as bar:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        bar.increment(f.write(chunk))
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
