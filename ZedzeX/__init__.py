from ZedzeX.core.bot import ZedzeXBot
from ZedzeX.core.dir import dirr
from ZedzeX.core.git import git
from ZedzeX.core.userbot import Userbot
from ZedzeX.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ZedzeXBot()
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

