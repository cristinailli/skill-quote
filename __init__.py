from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'chris & cristina'

LOGGER = getLogger(__name__)


class QuotingSkill(MycroftSkill):
    def __init__(self):
        super(QuotingSkill, self).__init__(name="QuotingSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        quote_intent = IntentBuilder("QuoteIntent").\
            require("QuoteKeyword").build()
        self.register_intent(quote_intent, self.handle_quote_intent)

    def handle_thank_you_intent(self, message):
        self.speak_dialog("quote")

    def stop(self):
        pass

def create_skill():
    return QuotingSkill()