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