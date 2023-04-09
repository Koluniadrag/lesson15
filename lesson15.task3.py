
class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.current_channel()

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.current_channel()

    def turn_channel(self, n):
        if n < 1 or n > len(self.channels):
            return "No"
        else:
            self.current_channel_index = n - 1
            return self.current_channel()

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def is_exist(self, query):
        if type(query) == int:
            return "Yes" if query >= 1 and query <= len(self.channels) else "No"
        else:
            return "Yes" if query in self.channels else "No"

CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

print(controller.last_channel())
print(controller.first_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
