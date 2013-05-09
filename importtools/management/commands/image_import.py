#!/usr/bin/env python
# vim: fileencoding=utf-8 shiftwidth=4 tabstop=4 expandtab softtabstop=4 ai
from __future__ import print_function

import os
import datetime

from armstrong.apps.images.models import Image
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

obj = ""

class Command(BaseCommand):
    args = '<folder to search>'
    help = 'Import images from filesystem to database'

    def handle(self, *args, **options):
        os.chdir(settings.MEDIA_ROOT)
        image_dir = './'
        if args:
            if not os.path.isdir(args[0]):
                raise CommandError("'{}' is no directory".format(args[0]))
            image_dir += args[0]

        for root, dirs, files in os.walk(image_dir):
            if 'cache' in root:
                continue
            root = root[2:]
            if Image.objects.filter(image__startswith=root).exists():
                print("Skipping", root)
                continue
            for f in files:
                fn = f.decode('utf-8')
                image = Image(image=os.path.join(root, fn), pub_date=datetime.datetime.now(), title=fn)
                image.save()

    def out(self, msg):
        self.stderr.write((unicode(msg.decode('utf-8')) + "\n").encode('utf-8'))

