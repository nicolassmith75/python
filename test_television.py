import pytest
from television import Television

def test_init():
    """
    The status, channel, and volume values
    """
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power_on():
    """
    Tests the power is on
    """
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_power_off():
    """
    Tests the power is off
    """
    tv = Television()
    tv.power()
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute_after_volume_up():
    """
    The tv details when the tv is on, value increased 1 time,
    then tv muted
    """
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_unmuted_tv_on():
    """
    Tv is on and it shows the details of the tv when it is unmuted
    """
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_mute_tv_off():
    """
    TV details when it is off and muted
    """
    tv = Television()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_unmuted_tv_off():
    """
    Tv details when it tv is off and unmuted
    """
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"



def test_channel_up_increase_tv_off():
    """
    tv details tv is off, channel is increased
    """
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_up_increase_tv_on():
    """
    tv details tv is on, channel is increased
    """
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"


def test_channel_up_increase_max_tv_on():
    """
    tv details tv is on, increases channel past max value
    """
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down_tv_off_channel_decrease():
    """
    tv details tv is off, channel is decreased
    """
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_down_tv_on_():
    """
    tv details tv is on, channel is decreased past min value
    """
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

def test_volume_up_tv_off_volume_increase():
    """
    tv details tv is off, volume is increased
    """
    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_volume_up_tv_on_volume_increase():
    """
    tv details tv is on, volume is increased
    """
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_volume_up_tv_on_muted_volume_increase():
    """
    Tv details tv is on, muted, then volume is increased, to 2 from previous volume before mute
    """
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_up_tv_on_volume_increase_max():     #11
    """
    tv details tv is on, volume is increased past the max value which is 2, cannot go past 2
    """
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down_tv_off_volume_decrease():
    """
    tv details tv is off and the volume is decreased
    """
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_volume_down_tv_on_volume_decrease_at_max():
    """
    tv details tv is on, volume turned to max and decreased by 1
    """
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_volume_down_tv_on_muted_volume_decrease():
    """
    tv details tv is on, muted, then volume is decreased
    """
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_volume_down_tv_on_volume_decrease_min():
    """
    tv details tv is on, volume decreased past min value
    """
    tv = Television()
    tv.power()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"