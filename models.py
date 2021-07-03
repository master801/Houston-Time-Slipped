#!/usr/bin/env python3

# Created by Master
# On: 6/27/2021 at 8:19 PM
from dataclasses import dataclass


@dataclass
class TrackManagerData:

    def __init__(self,
                 track_name: str,
                 track_manager: str,
                 local_time_zone: int,
                 track_address: str,
                 track_city: str,
                 track_state: str,
                 track_zip: str,
                 website: str,
                 footer_note: str
                 ):
        self.track_name = track_name
        self.track_manager = track_manager
        self.local_time_zone = local_time_zone
        self.track_address = track_address
        self.track_city = track_city
        self.track_state = track_state
        self.track_zip = track_zip
        self.website = website
        self.footer_note = footer_note
        return


@dataclass
class TrackURLs:

    def __init__(self,
                 last_single_race,
                 compu_link_last_race,
                 compu_link_car_last_race,
                 car_last_race_no_time,
                 streaming_url,
                 tracking_url,
                 weather_url,
                 android_registration_url,
                 track_msg_url,
                 main_logo_img_url,
                 left_lane_img_url,
                 right_lane_img_url,
                 weather_sponsor_img_url,
                 streaming_sponsor_img_url,
                 main_logo_web_url,
                 weather_sponsor_url,
                 streaming_sponsor_url,
                 left_lane_web_url,
                 right_lane_web_url,
                 training_vid_en_url,
                 encryption_key,
                 iv_key
                 ):
        self.last_single_race = last_single_race
        self.compu_link_last_race = compu_link_last_race
        self.compu_link_car_last_race = compu_link_car_last_race
        self.car_last_race_no_time = car_last_race_no_time

        self.streaming_url = streaming_url
        self.tracking_url = tracking_url
        self.weather_url = weather_url
        self.android_registration_url = android_registration_url
        self.track_msg_url = track_msg_url

        self.main_logo_img_url = main_logo_img_url
        self.left_lane_img_url = left_lane_img_url
        self.right_lane_img_url = right_lane_img_url
        self.weather_sponsor_img_url = weather_sponsor_img_url

        self.streaming_sponsor_img_url = streaming_sponsor_img_url
        self.left_lane_web_url = left_lane_web_url
        self.right_lane_web_url = right_lane_web_url
        self.training_vid_en_url = training_vid_en_url

        self.encryption_key = encryption_key
        self.iv_key = iv_key
        return


@dataclass
class RaceData:

    def __init__(self,
                 race_date,
                 car_number_left,
                 team_left,
                 class_left,
                 dial_in_left,
                 reaction_left,
                 feet_60_left,
                 feet_330_left,
                 feet_1000_left,
                 mph_660_left,
                 feet_660_left,
                 mph_1320_left,
                 feet_1320_left,
                 first_left,
                 mov_left,
                 idx_rec_left,
                 ovun_left,
                 round_left,

                 winner,
                 round_id,

                 car_number_right,
                 team_right,
                 class_right,
                 dial_in_right,
                 reaction_right,
                 feet_60_right,
                 feet_330_right,
                 mph_660_right,
                 feet_660_right,
                 feet_1000_right,
                 mph_1320_right,
                 feet_1320_right,
                 first_right,
                 mov_right,
                 idxrec_right,
                 ovun_right,
                 round_right,

                 temp,
                 pressure,
                 da,
                 rh
                 ):
        self.race_date = race_date,
        self.car_number_left = car_number_left,
        self.team_left = team_left,
        self.class_left = class_left,
        self.dial_in_left = dial_in_left,
        self.reaction_left = reaction_left,
        self.feet_60_left = feet_60_left,
        self.feet_330_left = feet_330_left,
        self.feet_1000_left = feet_1000_left,
        self.mph_660_left = mph_660_left,
        self.feet_660_left = feet_660_left,
        self.mph_1320_left = mph_1320_left,
        self.feet_1320_left = feet_1320_left,
        self.first_left = first_left,
        self.mov_left = mov_left,
        self.idx_rec_left = idx_rec_left,
        self.ovun_left = ovun_left,
        self.round_left = round_left,

        self.winner = winner,
        self.round_id = round_id,

        self.car_number_right = car_number_right,
        self.team_right = team_right,
        self.class_right = class_right,
        self.dial_in_right = dial_in_right,
        self.reaction_right = reaction_right,
        self.feet_60_right = feet_60_right,
        self.feet_330_right = feet_330_right,
        self.mph_660_right = mph_660_right,
        self.feet_660_right = feet_660_right,
        self.feet_1000_right = feet_1000_right,
        self.mph_1320_right = mph_1320_right,
        self.feet_1320_right = feet_1320_right,
        self.first_right = first_right,
        self.mov_right = mov_right,
        self.idxrec_right = idxrec_right,
        self.ovun_right = ovun_right,
        self.round_right = round_right,

        self.temp = temp,
        self.pressure = pressure,
        self.da = da,
        self.rh = rh
        return


def deserialize_track_urls(json_object: dict) -> TrackURLs:
    return TrackURLs(
        last_single_race=json_object['lastsinglerace'],
        compu_link_last_race=json_object['compulinklastrace'],
        compu_link_car_last_race=json_object['compulinkcarlastrace'],
        car_last_race_no_time=json_object['carlastracenotime'],
        streaming_url=json_object['streamingUrl'],
        tracking_url=json_object['trackingUrl'],
        weather_url=json_object['weatherUrl'],
        android_registration_url=json_object['androidRegistrationUrl'],
        track_msg_url=json_object['trackMessageUrl'],
        main_logo_img_url=json_object['mainLogoImageUrl'],
        left_lane_img_url=json_object['leftLaneImageUrl'],
        right_lane_img_url=json_object['rightLaneImageUrl'],
        weather_sponsor_img_url=json_object['weatherSponsorImageUrl'],
        streaming_sponsor_img_url=json_object['streamingSponsorImageUrl'],
        main_logo_web_url=json_object['mainLogoWebUrl'],
        weather_sponsor_url=json_object['weatherSponsorUrl'],
        streaming_sponsor_url=json_object['streamingSponsorUrl'],
        left_lane_web_url=json_object['leftLaneWebUrl'],
        right_lane_web_url=json_object['rightLaneWebUrl'],
        training_vid_en_url=json_object['trainingVideoEnUrl'],
        encryption_key=json_object['encryptionKey'],
        iv_key=json_object['ivKey']
    )


def deserialize_track_manager_data(json_object: dict) -> TrackManagerData:
    return TrackManagerData(
        json_object['trackname'],
        json_object['trackmanager'],
        json_object['localtimezone'],
        json_object['trackaddress'],
        json_object['trackcity'],
        json_object['trackstate'],
        json_object['trackzip'],
        json_object['website'],
        json_object['footernote']
    )


def deserialize_race_data(json_object: dict) -> RaceData:
    return RaceData(
        json_object['raceDate'],
        json_object['carNumberLeft'],
        json_object['teamLeft'],
        json_object['classLeft'],
        json_object['dialInLeft'],
        json_object['reactionLeft'],
        json_object['feet60Left'],
        json_object['feet330Left'],
        json_object['feet1000Left'],
        json_object['mph660Left'],
        json_object['feet660Left'],
        json_object['mph1320Left'],
        json_object['feet1320Left'],
        json_object['firstLeft'],
        json_object['movLeft'],
        json_object['idxrecLeft'],
        json_object['ovunLeft'],
        json_object['roundLeft'],
        json_object['winner'],
        json_object['roundId'],
        json_object['carNumberRight'],
        json_object['teamRight'],
        json_object['classRight'],
        json_object['dialInRight'],
        json_object['reactionRight'],
        json_object['feet60Right'],
        json_object['feet330Right'],
        json_object['mph660Right'],
        json_object['feet660Right'],
        json_object['feet1000Right'],
        json_object['mph1320Right'],
        json_object['feet1320Right'],
        json_object['firstRight'],
        json_object['movRight'],
        json_object['idxrecRight'],
        json_object['ovunRight'],
        json_object['roundRight'],
        json_object['temp'],
        json_object['pressure'],
        json_object['da'],
        json_object['rh'],
    )
