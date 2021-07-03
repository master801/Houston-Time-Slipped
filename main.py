#!/usr/bin/env python3

# Created by Master
# On: 6/26/2021 at 1:36 PM

import requests
import json

import models
import aes
from models import TrackManagerData, TrackURLs, RaceData

URL = 'https://8oqnxh7tm3.execute-api.us-east-2.amazonaws.com/getUrl/houston'
URL_TRACK_MANAGER = 'https://8r3r22va42.execute-api.us-east-2.amazonaws.com/getTrackManager/houston'

# USER_AGENT = 'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0'

HEADER = {
    'Accept': 'application/json',
    'X-Dynogeeks-Version': '2.2.5'
}
AUTH = {
    'raceusername': 'racingslips',
    'racepassword': 'racingslips94',
    'deviceId': 'TRASH_SECURITY_OBFUSCATE_YOUR_SHIT'
}


def scrape_track_manager() -> TrackManagerData:
    with requests.get(URL_TRACK_MANAGER, headers=HEADER) as post:
        tmd = json.loads(post.text, object_hook=models.deserialize_track_manager_data)
        post.close()
        pass

    if tmd == None:
        print('FUCK, FAILED TO SCRAPE')
        return None
    return tmd


def generate_encryption_key(tmd: TrackManagerData) -> str:  # com/dynogeek/houstonrp/Main$RetrieveTrackManager
    return '{:s}{:02d}{:s}'.format(
        tmd.track_name,
        int(tmd.local_time_zone / 86400 % 100),
        tmd.track_manager
    )[0:16]


def get_track_urls() -> dict:
    with requests.get(URL, headers=HEADER) as req_tt:
        json_data = json.loads(req_tt.text)
        req_tt.close()
        pass
    return json_data


def decrypt_track_urls(json_obj: dict, encryption_key: str) -> TrackURLs:
    return json.loads(
        aes.decrypt(
            json_obj['json'].encode(),
            encryption_key.encode()
        ).decode(encoding='utf-8'),
        object_hook=models.deserialize_track_urls
    )


def scrape_last_race(track_urls: TrackURLs) -> dict:
    with requests.get(track_urls.compu_link_last_race, headers=HEADER) as req_tr:
        json_last_race = json.loads(req_tr.text)
        req_tr.close()
        pass
    return json_last_race


def decrypt_last_race(json_obj: dict, encryption_key: str):
    return json.loads(
        aes.decrypt(
            json_obj['json'].encode(),
            encryption_key.encode()
        ).decode(encoding='utf-8'),
        object_hook=models.deserialize_race_data
    )


def scrape_last_race_no_time(track_urls: TrackURLs) -> dict:
    # TODO
    # Doesn't work since it needs an auth token - qr code created locally on the device
    with requests.get(track_urls.car_last_race_no_time, headers=HEADER) as req_tr:
        json_last_race = json.loads(req_tr.text)
        req_tr.close()
        pass
    return json_last_race


def decrypt_last_race_no_time(json_obj: dict, encryption_key: str) -> RaceData:
    if 'json' not in json_obj and 'message' in json_obj:  # rip
        print('FAILED TO GET NO TIME RACE')
        print('MESSAGE: \"{}\"'.format(json_obj['message']))
        return None

    decrypted_no_time = aes.decrypt_no_time(
        json_obj['json'].encode(),
        encryption_key
    )
    breakpoint()
    return None


def main():
    tmd: TrackManagerData = scrape_track_manager()
    encryption_key = generate_encryption_key(tmd)

    if encryption_key == None:
        print('FAILED TO GENERATE ENCRYPTION KEY')
        return

    print(f'ENCRYPTION KEY: {encryption_key}')

    json_track_urls: dict = get_track_urls()
    if json_track_urls == None:
        print('FAILED TO GET TRACK TIMES')
        return
    track_urls: TrackURLs = decrypt_track_urls(json_track_urls, encryption_key)

    enc_last_race: dict = scrape_last_race(track_urls)
    last_races = decrypt_last_race(enc_last_race, encryption_key)

    # enc_last_race_no_time: dict = scrape_last_race_no_time(track_urls)
    # last_race_no_time: RaceData = decrypt_last_race_no_time(enc_last_race_no_time, encryption_key)

    breakpoint()
    return


if __name__ == '__main__':
    main()
    pass
