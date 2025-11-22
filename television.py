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