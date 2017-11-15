from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'chris & cristina'

LOGGER = getLogger(__name__)


class QuotingSkill(MycroftSkill):
    def __init__(self):
        super(QuotingSkill, self).__init__(name="QuotingSkill")

    @intent_handler(IntentBuilder("QuoteIntent").require("QuoteKeyword"))
    def handle_quote_intent(self, message):
        self.speak_dialog("quote")

    def stop(self):
        pass

def create_skill():
    return QuotingSkill()