# This is where all the colors are mapped in the GUI

# CLEAR
CLEAR_DAY = '#000'
CLEAR_DAY_ACCENT = '#000'
CLEAR_NIGHT = '#000'
CLEAR_NIGHT_ACCENT = '#000'

# SEMI CLOUDY
SEMI_CLOUDY_DAY = '#000'
SEMI_CLOUDY_DAY_ACCENT = '#000'
SEMI_CLOUDY_NIGHT = '#000'
SEMI_CLOUDY_NIGHT_ACCENT = '#000'

# CLOUDY
CLOUDY_DAY = '#000'
CLOUDY_DAY_ACCENT = '#000'
CLOUDY_NIGHT = '#000'
CLOUDY_NIGHT_ACCENT = '#000'

# BROKEN CLOUDS
BROKEN_CLOUDY_DAY = '#000'
BROKEN_CLOUDY_DAY_ACCENT = '#000'
BROKEN_CLOUDY_NIGHT = '#000'
BROKEN_CLOUDY_NIGHT_ACCENT = '#000'

# RAIN
RAIN_DAY = '#000'
RAIN_DAY_ACCENT = '#000'
RAIN_NIGHT = '#000'
RAIN_NIGHT_ACCENT = '#000'

# THUNDERSTORM
THUNDERSTORM_DAY = '#000'
THUNDERSTORM_DAY_ACCENT = '#000'
THUNDERSTORM_NIGHT = '#000'
THUNDERSTORM_NIGHT_ACCENT = '#000'

# SNOW
SNOW_DAY = '#000'
SNOW_DAY_ACCENT = '#000'
SNOW_NIGHT = '#000'
SNOW_NIGHT_ACCENT = '#000'

# MIST
MIST_DAY = '#000'
MIST_DAY_ACCENT = '#000'
MIST_NIGHT = '#000'
MIST_NIGHT_ACCENT = '#000'

# OTHERS
WHITE = '#FFF'
BLACK = '#000'

ui_map = {
    'foreground' : WHITE,
    'clear sky' : {
        'day' : {
            'background' : CLEAR_DAY,
            'accent' : CLEAR_DAY_ACCENT,
            'image' : 'assets/image/sun.png'
        },
        'night' : {
            'background' : CLEAR_NIGHT,
            'accent' : CLEAR_NIGHT_ACCENT,
            'image' : 'assets/image/moon.png'
        }
    },
    'few clouds' : {
        'day' : {
            'background' : SEMI_CLOUDY_DAY,
            'accent' : SEMI_CLOUDY_DAY_ACCENT,
            'image' : 'assets/image/semicloudday.png'
        },
        'night' : {
            'background' : SEMI_CLOUDY_NIGHT,
            'accent' : SEMI_CLOUDY_NIGHT_ACCENT,
            'image' : 'assets/image/semicloudnight.png'
        }
    },
    'scattered clouds' : {
        'day' : {
            'background' : CLOUDY_DAY,
            'accent' : CLOUDY_DAY_ACCENT,
            'image' : 'assets/image/cloud.png'
        },
        'night' : {
            'background' : CLOUDY_NIGHT,
            'accent' : CLOUDY_NIGHT_ACCENT,
            'image' : 'assets/image/cloud.png'
        }
    },
    'broken clouds' : {
        'day' : {
            'background' : BROKEN_CLOUDY_DAY,
            'accent' : BROKEN_CLOUDY_DAY_ACCENT,
            'image' : 'assets/image/brokencloud.png'
        },
        'night' : {
            'background' : BROKEN_CLOUDY_NIGHT,
            'accent' : BROKEN_CLOUDY_NIGHT_ACCENT,
            'image' : 'assets/image/brokencloud.png'
        }
    },
    'shower rain' : {
        'day' : {
            'background' : RAIN_DAY,
            'accent_color' : RAIN_DAY_ACCENT,
            'image' : 'assets/image/rain.png'
        },
        'night' : {
            'background' : RAIN_NIGHT,
            'accent' : RAIN_NIGHT_ACCENT,
            'image' : 'assets/image/rain.png'
        }
    },
    'rain' : {
        'day' : {
            'background' : CLOUDY_DAY,
            'accent' : CLOUDY_DAY_ACCENT,
            'image' : 'assets/image/rain.png'
        },
        'night' : {
            'background' : CLOUDY_NIGHT,
            'accent' : CLOUDY_NIGHT_ACCENT,
            'image' : 'assets/image/rain.png'
        }
    },
    'thunderstorm' : {
        'day' : {
            'background' : THUNDERSTORM_DAY,
            'accent' : THUNDERSTORM_DAY_ACCENT,
            'image' : 'assets/image/rain.png'
        },
        'night' : {
            'background' : THUNDERSTORM_NIGHT,
            'accent' : THUNDERSTORM_NIGHT_ACCENT,
            'image' : 'assets/image/rain.png'
        }
    },
    'snow' : {
        'day' : {
            'background' : SNOW_DAY,
            'accent' : SNOW_DAY_ACCENT,
            'image' : 'assets/image/rain.png'
        },
        'night' : {
            'background' : SNOW_NIGHT,
            'accent' : SNOW_NIGHT_ACCENT,
            'image' : 'assets/image/rain.png'
        }
    },
    'mist' : {
        'day' : {
            'background' : MIST_DAY,
            'accent' : MIST_DAY_ACCENT,
            'image' : 'assets/image/rain.png'
        },
        'night' : {
            'background' : MIST_NIGHT,
            'accent' : MIST_NIGHT_ACCENT,
            'image' : 'assets/image/rain.png'
        }
    }
}


# This maps the code ranges
weather_code_range = [
    (range(200,233), 'thunderstorm'),
    (range(300, 322), 'shower rain'),
    (range(500, 532), 'rain'),
    (range(600, 622), 'snow'),
    (range(701,782), 'mist'),
    ([800], 'clear sky'),
    ([801], 'few clouds'),
    ([802], 'scattered clouds'),
    ([803,804], 'broken clouds')
]
