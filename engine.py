import os
from random import choice


def send_photo(bot, address, directory):
    all_files = list()
    for root, _, files in os.walk(directory):
        all_files.extend([os.path.normpath(os.path.join(root, file)) for file in files])

    with open(file=choice(all_files), mode="rb") as photo:
        bot.send_photo(address, photo)
