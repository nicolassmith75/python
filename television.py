class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False # Turns power off
        self._muted = False  # Shows not muted
        self._volume = self.MIN_VOLUME # min volume is 2
        self._channel = self.MIN_CHANNEL # min channel is 0
        self._previous_volume = self._volume  # previous volume sync

    def power(self):
        self._status = not self._status # the status of if the tv is on or off

    def mute(self):
        if self._status:
            self._muted = not self._muted # checks the mute
            if self._muted:
                self._previous_volume = self._volume  # remembers what volume number before muting
                self._volume = 0
            else:
                self._volume = self._previous_volume # restores the volume that was remembered

    def channel_up(self):
        if self._status:
            if self._channel == self.MAX_CHANNEL:  #checks the status of the channel for it at max
                self._channel = self.MIN_CHANNEL   # and min
            else:
                self._channel += 1       # increases the channel number by 1

    def channel_down(self):
        if self._status:
            if self._channel == self.MIN_CHANNEL:   # checks the channel if at min
                self._channel = self.MAX_CHANNEL    # and max
            else:
                self._channel -= 1                 # decreases the channel by 1

    def volume_up(self):
        if self._status:
            if self._muted:
                self._muted = False                             # if it is not muted
                if self._previous_volume < self.MAX_VOLUME:
                    self._previous_volume += 1                  # adds a volume if the
                    self._volume = self._previous_volume        # max has not been reached
            elif self._volume < self.MAX_VOLUME:            # if the current volume is less than 2 it will add 1 to reach max
                self._volume += 1

    def volume_down(self):
        if self._status:
            if self._muted:
                self._muted = False                                 # decreases volume by 1
                if self._previous_volume > self.MIN_VOLUME:         # when volume reaches 0 it will go back to previous volume
                    self._previous_volume -= 1
                    self._volume = self._previous_volume
            elif self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"     # returns the power status, channel number, and volume in the form of a string.














