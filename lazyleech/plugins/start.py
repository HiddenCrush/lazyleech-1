# lazyleech - Telegram bot primarily to leech from torrents and upload to Telegram
# Copyright (c) 2021 lazyleech developers <theblankx protonmail com, meliodas_bot protonmail com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from pyrogram import Client, filters

@Client.on_message(filters.command('start'))
async def start_cmd(client, message):
    await message.reply_text('''<b>Hi, I am Torrent King.</b>
Sorry But Due to some 18+ Leechers I am no longer working for Public, If you want to leech/mirror torrents then please join @Gautams_mirror.

<b>18+ Content = Direct Ban</b>'''.strip())
