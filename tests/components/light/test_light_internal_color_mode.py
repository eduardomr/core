class ColorMode:
    HS = "HS"
    COLOR_TEMP = "COLOR_TEMP"
    BRIGHTNESS = "BRIGHTNESS"
    ONOFF = "ONOFF"
    UNKNOWN = "UNKNOWN"


class Light:
    def __init__(self):
        self.color_mode = None
        self._light_internal_supported_color_modes = []
        self.hs_color = None
        self.color_temp_kelvin = None
        self.brightness = None

    def _light_internal_color_mode(self) -> str:

        if (color_mode := self.color_mode) is None:

            supported = self._light_internal_supported_color_modes

            if ColorMode.HS in supported and self.hs_color is not None:
                return ColorMode.HS
            if ColorMode.COLOR_TEMP in supported and self.color_temp_kelvin is not None:
                return ColorMode.COLOR_TEMP
            if ColorMode.BRIGHTNESS in supported and self.brightness is not None:
                return ColorMode.BRIGHTNESS
            if ColorMode.ONOFF in supported:
                return ColorMode.ONOFF
            return ColorMode.UNKNOWN

        return color_mode


def test_light_internal_color_mode_hs():
    light = Light()
    light.color_mode = None
    light._light_internal_supported_color_modes = [ColorMode.HS]
    light.hs_color = [50, 60]
    assert light._light_internal_color_mode() == "HS"


def test_light_internal_color_mode_color_temp():
    light = Light()
    light.color_mode = None
    light._light_internal_supported_color_modes = [ColorMode.COLOR_TEMP]
    light.color_temp_kelvin = 5000
    assert light._light_internal_color_mode() == "COLOR_TEMP"


def test_light_internal_color_mode_brightness():
    light = Light()
    light.color_mode = None
    light._light_internal_supported_color_modes = [ColorMode.BRIGHTNESS]
    light.brightness = 75
    assert light._light_internal_color_mode() == "BRIGHTNESS"


def test_light_internal_color_mode_onoff():
    light = Light()
    light.color_mode = None
    light._light_internal_supported_color_modes = [ColorMode.ONOFF]
    assert light._light_internal_color_mode() == "ONOFF"


def test_light_internal_color_mode_unknown():
    light = Light()
    light.color_mode = None
    light._light_internal_supported_color_modes = []
    assert light._light_internal_color_mode() == "UNKNOWN"


def test_light_internal_color_mode_color_mode():
    light = Light()
    light.color_mode = "HS"
    assert light._light_internal_color_mode() == "HS"
