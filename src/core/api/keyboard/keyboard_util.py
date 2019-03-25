# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
import logging
import time

import pyperclip

from src.core.api.errors import FindError
from src.core.api.keyboard.key import Key, KeyModifier
from src.core.api.os_helpers import OSHelper
from src.core.api.settings import Settings
from src.core.util.arg_parser import parse_args


logger = logging.getLogger(__name__)


def get_active_modifiers(key):
    """Gets all the active modifiers depending on the used OS.

    :param key: Key modifier.
    :return: Returns an array with all the active modifiers.
    """
    all_modifiers = [
        Key.SHIFT,
        Key.CTRL]
    if OSHelper.is_mac():
        all_modifiers.append(Key.CMD)
    elif OSHelper.is_windows():
        all_modifiers.append(Key.WIN)
    else:
        all_modifiers.append(Key.META)

    all_modifiers.append(Key.ALT)

    active_modifiers = []
    for item in all_modifiers:
        try:
            for key_value in key:

                if item == key_value.value:
                    active_modifiers.append(item)
        except TypeError:
            if item == key.value:
                active_modifiers.append(item)

    return active_modifiers


def paste(text: str):
    """
    :param text: Text to be pasted.
    :return: None.
    """

    pyperclip.copy(text)
    if parse_args().virtual_keyboard:
        from src.core.api.keyboard.Xkeyboard import type
    else:
        from src.core.api.keyboard.keyboard_api import type

    text_copied = False
    wait_scan_rate = float(Settings.wait_scan_rate)
    interval = 1 / wait_scan_rate
    max_attempts = int(Settings.auto_wait_timeout * wait_scan_rate)
    attempt = 0

    while not text_copied and attempt < max_attempts:
        if pyperclip.paste() == text:
            text_copied = True
        else:
            time.sleep(interval)
            attempt += 1

    if not text_copied:
        raise FindError('Paste method failed.')

    if OSHelper.is_mac():
        type(text='v', modifier=KeyModifier.CMD)
    else:
        type(text='v', modifier=KeyModifier.CTRL)

    pyperclip.copy('')
