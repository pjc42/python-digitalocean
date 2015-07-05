__author__ = 'pjc'

import os

# get your digitalocean token from $Env:DO_TOKEN
# restart pycharm to get new os process and new environment
DO_TOKEN = os.getenv("DO_TOKEN")
assert DO_TOKEN is not None


import digitalocean
manager = digitalocean.Manager(token=DO_TOKEN)

# get a list of my images, backups and snapshots
my_images = manager.get_my_images()

# make a dict of them, keyed by img name
imgObjs = my_images
imgNames = [img.name for img in my_images]
my_images = dict(zip(imgNames, imgObjs))
print(type(my_images))

print('My Images (backups and snapshots) on Digital Ocean')
for name, img in my_images.items():
    print('{name:} : {id:} {type:}'.format(name=name, id=img.id, type=img.distribution))

print('Attributes of an Image')
for key, val in list(my_images.values())[0].__dict__.items():
    print('{} : {}'.format(key, val))
