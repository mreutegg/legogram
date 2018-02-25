# Copyright 2018 Marcel Reutegger
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pyrogram import Client
from pyrogram.api import types


def update_handler(client, update, users, chats):
    if isinstance(update, types.UpdateNewMessage):
        message = update.message

        # Filter by Message to exclude MessageService and MessageEmpty
        if isinstance(message, types.Message):
            # Private Messages (Message from user)
            if isinstance(message.to_id, types.PeerUser):
                text = message.message
                user = users[message.from_id].first_name
                if user == 'IFTTT' and text.startswith('lego-sorter:'):
                    log.write(text)
                    log.write('\n')
                    log.flush()


with open('/home/pi/legogram/command.log', 'a') as log:
    c = Client("lego-sorter")
    c.set_update_handler(update_handler)
    c.start()
    c.idle()
