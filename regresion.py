from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

with SB(uc=True, test=True) as toiaow:

    url = "https://kick.com/brutalles"
    toiaow.uc_open_with_reconnect(url, 4)
    toiaow.sleep(4)
    toiaow.uc_gui_click_captcha()
    toiaow.sleep(1)
    toiaow.uc_gui_handle_captcha()
    toiaow.sleep(4)
    if toiaow.is_element_present('button:contains("Accept")'):
        toiaow.uc_click('button:contains("Accept")', reconnect_time=4)
    if toiaow.is_element_visible('#injected-channel-player'):
        toiaow2 = toiaow.get_new_driver(undetectable=True)
        toiaow2.uc_open_with_reconnect(url, 5)
        toiaow2.uc_gui_click_captcha()
        toiaow2.uc_gui_handle_captcha()
        toiaow.sleep(10)
        if toiaow2.is_element_present('button:contains("Accept")'):
            toiaow2.uc_click('button:contains("Accept")', reconnect_time=4)
        toiaow.quit_extra_driver()
    toiaow.sleep(00)
    if True:
        url = "https://www.twitch.tv/brutalles"
        toiaow.uc_open_with_reconnect(url, 5)
        if toiaow.is_element_present('button:contains("Accept")'):
            toiaow.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            toiaow2 = toiaow.get_new_driver(undetectable=True)
            toiaow2.uc_open_with_reconnect(url, 5)
            toiaow.sleep(10)
            if toiaow2.is_element_present('button:contains("Accept")'):
                toiaow2.uc_click('button:contains("Accept")', reconnect_time=4)
            toiaow.quit_extra_driver()
    toiaow.sleep(10)
