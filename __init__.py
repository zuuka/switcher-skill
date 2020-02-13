from mycroft import MycroftSkill, intent_file_handler


class Switcher(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('switcher.intent')
    def handle_switcher(self, message):
        self.speak_dialog('switcher')


def create_skill():
    return Switcher()

