import subprocess
from functools import partial
from libqtile.widget import base
from libqtile.log_utils import logger

class Spt(base.ThreadPoolText):
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ('update_interval',0.5),
    ]

    def __init__(self, **config):
        base.ThreadPoolText.__init__(self,"", **config)
        self.add_defaults(Spt.defaults)
        self.add_callbacks({
            'Button1': partial(subprocess.Popen,['sp','play']),
            'Button4': partial(subprocess.Popen,['sp','next']),
            'Button5': partial(subprocess.Popen,['sp','prev']),
        })

    def get_info(self):
        try:
            output = self.call_process(['sp','current'])
        except subprocess.CalledProcessError as err:
            output = err.output.decode()

        if output.startswith("Album"):
            output = output.splitlines()
            info = {'Album':        "",
                    'AlbumArtist':  "",
                    'Artist':       "",
                    'Title':        "",
                    }
            for line in output:
                for data in info:
                    if data in line:
                        index = line.index(data)
                        if index < 5:
                            info[data] = line[len(data) + index:].strip()
                            break
                    elif line.startswith("set"):
                        return info
            return info

    def now_playing(self):
        """return a string with the now playing info (Artist - Song Title)."""
        info = self.get_info()
        now_playing = "Not running "
        if info:
            title = info['Title']
            artist = info['Artist']
            now_playing = " {0} - {1}".format(artist,title)
        return now_playing


    def poll(self):
        """Pool content for the text box"""
        return self.now_playing()

