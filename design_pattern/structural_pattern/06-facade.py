"""
外观模式
"""


class CDPlayer:
    def play_cd(self):
        print("CD播放器正在播放CD...")

    def stop_cd(self):
        print("CD播放器停止播放CD...")


class DVDPlayer:
    def play_dvd(self):
        print("DVD播放器正在播放DVD...")

    def stop_dvd(self):
        print("DVD播放器停止播放DVD...")


class MediaPlayer:
    def __init__(self):
        self.cd_player = CDPlayer()
        self.dvd_player = DVDPlayer()

    def play_media(self, media_type):
        if media_type == 'cd':
            self.cd_player.play_cd()
        elif media_type == 'dvd':
            self.dvd_player.play_dvd()
        else:
            print("不支持的媒体类型")

    def stop_media(self, media_type):
        if media_type == 'cd':
            self.cd_player.stop_cd()
        elif media_type == 'dvd':
            self.dvd_player.stop_dvd()
        else:
            print("不支持的媒体类型")


if __name__ == '__main__':
    media_player = MediaPlayer()
    media_player.play_media('cd')
    media_player.play_media('dvd')
    media_player.stop_media('cd')
    media_player.stop_media('dvd')
