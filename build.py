import os
import shutil

path = os.path.dirname(os.path.realpath(__file__))

shutil.make_archive(
    path + '/export/resources',
    'zip',
    path + '/resources'
)