# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

def on_error_speak_dialog(dialog_file):
    def decorator(function):
        def wrapper(self, message):
            try:
                try:
                    function(self, message)
                except TypeError:
                    function(self)
            except Exception:
                self.log.exception('In safe wrapped function')
                self.speak_dialog(dialog_file)
        return wrapper
    return decorator


class FarmSkill(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__()
        self.learning = True

        

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')


    @intent_handler(IntentBuilder('HowIsMyFarmDoingIntent').require('HowIsMyFarmDoingKeyword'))
    @on_error_speak_dialog('test')
    def handle_how_is_my_farm_doing(self, message):
        """ This is a Padatious intent handler.
        It is triggered using a list of sample phrases."""
        self.speak_dialog("how.is.my.farm.doing")
    
    def stop(self):
        pass


def create_skill():
    return FarmSkill()
