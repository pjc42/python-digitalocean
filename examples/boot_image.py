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
    print('{} : {}'.format(name, img))


target_img_name = 'tiny-docker-initial'
target_img = my_images[target_img_name]
assert target_img is not None

# create an example droplet
# droplet = digitalocean.Droplet(
#    token=DO_TOKEN,
#    name='Example',
#    region='nyc2', # New York 2
#    image='ubuntu-14-04-x64', # Ubuntu 14.04 x64
#    size_slug='512mb',  # 512MB
#    backups=False)


droplet = digitalocean.Droplet(
            token=DO_TOKEN,
            name=target_img.name,
            region=target_img.regions[0],
            image=target_img.id,
            size_slug='512mb',  # 512MB
            backups=False)



assert droplet is not None

help(droplet)

res = droplet.create()

