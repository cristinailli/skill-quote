import random
import time
import webbrowser
from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft.messagebus.message import Message
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'chris & cristina'

LOGGER = getLogger(__name__)


class QuotingSkill(MycroftSkill):
    def __init__(self):
        super(QuotingSkill, self).__init__(name="QuotingSkill")
        self.process = None
        quoteone = "Don't worry about what anybody else is going to do. The best way to predict the future is to invent it. By Alan Kay"

    def initialize(self):
        intent = IntentBuilder("QuotingSkill").require(
            "QuotingKeyword").build()
        self.register_intent(intent, self.handle_intent)
        self.add_event("mycroft.quote", self.quote, False)

    def quote(self, quoteone):
        self.speak = quoteone

    def handle_intent(self, message):
        quotetwo = "Premature optimization is the root of all evil (or at least most of it) in programming. By Donald Knuth"
        try:
            self.speak_dialog('quoting')
            time.sleep(3)
            self.speak = quotetwo

        except Exception as e:
            LOGGER.error("Error: {0}".format(e))
            
    def stop(self):
        if self.process and self.process.poll() is None:
            self.speak_dialog('quoting.stop')
            self.process.terminate()
            self.process.wait()

def create_skill():
    return QuotingSkill()