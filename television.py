class Television:
    """

    """

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Initializes the television object to start off, starts not muted, volume starts at 0, channel starts at 0 and just logging the volume.
        """
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL
        self._previous_volume = self._volume

    def power(self):
        """
        The switch for the tv whether its on or off
        """
        self._status = not self._status

    def mute(self):
        """
        It allows for muting on the volume, it cheks the to see if its muted, if not then it will remember the volume and then change it to 0,
        else it will restore the volume to previous volume
        """
        if self._status:
            self._muted = not self._muted
            if self._muted:
                self._previous_volume = self._volume
                self._volume = 0
            else:
                self._volume = self._previous_volume

    def channel_up(self):
        """
        Allows for the channel to be raised, checks the status of the channel and increases the channel by 1 and if its already at max it will switch
        to min which is 0
        """
        if self._status:
            if self._channel == self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL
            else:
                self._channel += 1

    def channel_down(self):
        """
        Allows for the channel to be decreased, checks the status of the channel and decreases the channel by 1 and if its already at min it will switch
        to max channel which is 3
        """
        if self._status:
            if self._channel == self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self):
        """
        Checks the status for on, if mute turn off, restores previous volume and if it is less than max it will add 1 volume if its less than max
        """
        if self._status:
            if self._muted:
                self._muted = False
                if self._previous_volume < self.MAX_VOLUME:
                    self._previous_volume += 1
                    self._volume = self._previous_volume
            elif self._volume < self.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        """
        Checks the status for on, if mute turn off, restores previous volume and if greater than min it will decrease by 1 volume if its greater than min
        """
        if self._status:
            if self._muted:
                self._muted = False
                if self._previous_volume > self.MIN_VOLUME:
                    self._previous_volume -= 1
                    self._volume = self._previous_volume
            elif self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        """
         returns the power status, channel number, and volume in the form of a string for verifying
        """
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"














