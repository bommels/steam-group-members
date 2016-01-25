"""
Author: TerryDEV
This code is used on https://www.steamladder.com

Read the README for requirements.
"""

import time

import requests
from requests.exceptions import Timeout, RequestException

import xml.etree.ElementTree as ET

class SteamGroup:
    """
	This Python class fetches the SteamID64's of all the Steam group members. Use run() to fetch and print the ID's.
    """
    XML_URL = 'http://steamcommunity.com/groups/SteamLadder' + '/memberslistxml?xml=1' # Add your custom group URL here
    XML_NEXT_PAGE = False
    XML_PAGE = 1

    REQUEST_TIMEOUT = 3.00  # in seconds

    STEAM_IDS = []

    def __init__(self):
        pass

    def get_steam_ids(self, page=XML_PAGE):
        """
        Proccessed the response from the get function (xml in text) and save the SteamID64's to an array.
        Uses get_steam_ids as a recurive function to fetch all the pages.
        :param page: the XML page, max is 1000 members per page.
        :return: the response XML in text format.
        """
        response = self.get(page)
        if response is None:
            return None

        root = ET.fromstring(response)
        members = root.find('members')
        if members is None:
            return None

        for steamid in members.findall('steamID64'):
            self.STEAM_IDS.append(int(steamid.text))

        if root.findall('nextPageLink'):
            page += 1
            return self.get_steam_ids(page)

        print('[OK!] Fetched ' + str(len(self.STEAM_IDS)) + ' SteamIDs')

        steamids = self.STEAM_IDS
        self.STEAM_IDS = []

        return steamids

    def get(self, page):
        """
        Get's the XML GroupMembers from Steam, no API key required.
        :param page: the page, max 1000 members per page.
        :return: the reponse, return None is not a valid response.
        """
        url = self.XML_URL + '&p=%s' % page

        response = None
        try:
            response = requests.get(url, timeout=self.REQUEST_TIMEOUT)

            print('[%s] %s' % (response.status_code, response.url))

            if response.status_code != 200:
                return None
        except Timeout as e:
            print(e)
        except RequestException as e:
            print(e)

        if response is None:
            return None

        return response.text

steamgroup = SteamGroup()
