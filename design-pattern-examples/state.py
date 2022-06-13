from abc import ABC, abstractmethod


# context
class LightBulb:
    def __init__(self, switch_state):
        self._switch_state = None
        self.set_switch_state(switch_state)

    def set_switch_state(self, switch_state):
        self._switch_state = switch_state
        self._switch_state.set_light_bulb(self)

    def flip_switch(self):
        self._switch_state.flip()


# state interface
class SwitchState(ABC):
    def __init__(self):
        self._light_bulb = None

    def get_light_bulb(self):
        return self._light_bulb

    def set_light_bulb(self, light_bulb):
        self._light_bulb = light_bulb

    @abstractmethod
    def flip(self):
        pass


# state implementation
class SwitchStateOff(SwitchState):
    def flip(self):
        print("The light is now turned on")
        self.get_light_bulb().set_switch_state(SwitchStateOn())


class SwitchStateOn(SwitchState):
    def flip(self):
        print("The light is now turned off")
        self.get_light_bulb().set_switch_state(SwitchStateOff())


bulb = LightBulb(SwitchStateOff())
bulb.flip_switch()
bulb.flip_switch()
bulb.flip_switch()
bulb.flip_switch()
bulb.flip_switch()
bulb.flip_switch()
bulb.flip_switch()
bulb.flip_switch()
