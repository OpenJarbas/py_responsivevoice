from responsive_voice import ResponsiveVoice


class UkEnglishFemale(ResponsiveVoice):
    uri = "UkEnglishFemale"
    name = "UK English Female"
    voiceIDs = [7, 171, 201, 5, 1, 528, 257, 286, 342, 258, 287, 343, 8]
    _raw = {'flag': 'gb', 'gender': 'f', 'lang': 'en-GB',
            'voiceIDs': [7, 171, 201, 5, 1, 528, 257, 286, 342, 258, 287, 343, 8], 'name': 'UK English Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='UK English Female', service="")


class UkEnglishMale(ResponsiveVoice):
    uri = "UkEnglishMale"
    name = "UK English Male"
    voiceIDs = [277, 202, 75, 4, 2, 256, 285, 341, 159]
    _raw = {'flag': 'gb', 'gender': 'm', 'lang': 'en-GB', 'voiceIDs': [277, 202, 75, 4, 2, 256, 285, 341, 159],
            'name': 'UK English Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='UK English Male', service="")


class UsEnglishFemale(ResponsiveVoice):
    uri = "UsEnglishFemale"
    name = "US English Female"
    voiceIDs = [433, 434, 40, 41, 42, 383, 205, 204, 43, 481, 173, 235, 283, 339, 408, 44]
    _raw = {'flag': 'us', 'gender': 'f', 'lang': 'en-US',
            'voiceIDs': [433, 434, 40, 41, 42, 383, 205, 204, 43, 481, 173, 235, 283, 339, 408, 44],
            'name': 'US English Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='US English Female', service="")


class UsEnglishMale(ResponsiveVoice):
    uri = "UsEnglishMale"
    name = "US English Male"
    voiceIDs = [39, 234, 282, 338, 236, 284, 340, 2, 4, 0, 75, 195, 169]
    _raw = {'flag': 'us', 'gender': 'm', 'lang': 'en-US',
            'voiceIDs': [39, 234, 282, 338, 236, 284, 340, 2, 4, 0, 75, 195, 169], 'name': 'US English Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='US English Male', service="")


class ArabicMale(ResponsiveVoice):
    uri = "ArabicMale"
    name = "Arabic Male"
    voiceIDs = [95, 97, 196, 388]
    _raw = {'flag': 'ar', 'gender': 'm', 'lang': 'ar-SA', 'voiceIDs': [95, 97, 196, 388], 'name': 'Arabic Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar-SA", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Arabic Male', service="")


class ArabicFemale(ResponsiveVoice):
    uri = "ArabicFemale"
    name = "Arabic Female"
    voiceIDs = [98]
    _raw = {'flag': 'ar', 'gender': 'f', 'lang': 'ar-SA', 'voiceIDs': [98], 'name': 'Arabic Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar-SA", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Arabic Female', service="")


class ArmenianMale(ResponsiveVoice):
    uri = "ArmenianMale"
    name = "Armenian Male"
    voiceIDs = [99]
    _raw = {'flag': 'hy', 'gender': 'f', 'lang': 'hy-AM', 'voiceIDs': '99', 'name': 'Armenian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hy-AM", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Armenian Male', service="")


class AustralianFemale(ResponsiveVoice):
    uri = "AustralianFemale"
    name = "Australian Female"
    voiceIDs = [415, 276, 201, 87, 5, 88]
    _raw = {'flag': 'au', 'gender': 'f', 'lang': 'en-AU', 'voiceIDs': [415, 276, 201, 87, 5, 88],
            'name': 'Australian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Australian Female', service="")


class AustralianMale(ResponsiveVoice):
    uri = "AustralianMale"
    name = "Australian Male"
    voiceIDs = [386]
    _raw = {'flag': 'au', 'gender': 'm', 'lang': 'en-AU', 'voiceIDs': [386], 'name': 'Australian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Australian Male', service="")


class BanglaBangladeshFemale(ResponsiveVoice):
    uri = "BanglaBangladeshFemale"
    name = "Bangla Bangladesh Female"
    voiceIDs = [435]
    _raw = {'flag': 'bd', 'gender': 'f', 'lang': 'bn-BD', 'voiceIDs': '435', 'name': 'Bangla Bangladesh Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bn-BD", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Bangla Bangladesh Female', service="")


class BanglaBangladeshMale(ResponsiveVoice):
    uri = "BanglaBangladeshMale"
    name = "Bangla Bangladesh Male"
    voiceIDs = [410, 436]
    _raw = {'flag': 'bd', 'gender': 'm', 'lang': 'bn-BD', 'voiceIDs': [410, 436], 'name': 'Bangla Bangladesh Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bn-BD", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Bangla Bangladesh Male', service="")


class BanglaIndiaFemale(ResponsiveVoice):
    uri = "BanglaIndiaFemale"
    name = "Bangla India Female"
    voiceIDs = [447]
    _raw = {'flag': 'bd', 'gender': 'f', 'lang': 'bn-IN', 'voiceIDs': '447', 'name': 'Bangla India Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bn-IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Bangla India Female', service="")


class BanglaIndiaMale(ResponsiveVoice):
    uri = "BanglaIndiaMale"
    name = "Bangla India Male"
    voiceIDs = [411, 448]
    _raw = {'flag': 'bd', 'gender': 'm', 'lang': 'bn-IN', 'voiceIDs': [411, 448], 'name': 'Bangla India Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bn-IN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Bangla India Male', service="")


class BrazilianPortugueseFemale(ResponsiveVoice):
    uri = "BrazilianPortugueseFemale"
    name = "Brazilian Portuguese Female"
    voiceIDs = [124, 123, 125, 499, 186, 223, 126]
    _raw = {'flag': 'br', 'gender': 'f', 'lang': 'pt-BR', 'voiceIDs': [124, 123, 125, 499, 186, 223, 126],
            'name': 'Brazilian Portuguese Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Brazilian Portuguese Female', service="")


class BrazilianPortugueseMale(ResponsiveVoice):
    uri = "BrazilianPortugueseMale"
    name = "Brazilian Portuguese Male"
    voiceIDs = [332, 371, 399]
    _raw = {'flag': 'br', 'gender': 'm', 'lang': 'pt-BR', 'voiceIDs': [332, 371, 399], 'deprecated': True,
            'name': 'Brazilian Portuguese Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Brazilian Portuguese Male', service="")


class ChineseFemale(ResponsiveVoice):
    uri = "ChineseFemale"
    name = "Chinese Female"
    voiceIDs = [58, 59, 452, 380, 281, 231, 155, 60, 513, 191, 268, 297, 353, 269, 298, 354, 409, 61]
    _raw = {'flag': 'cn', 'gender': 'f', 'lang': 'zh-CN',
            'voiceIDs': [58, 59, 452, 380, 281, 231, 155, 60, 513, 191, 268, 297, 353, 269, 298, 354, 409, 61],
            'name': 'Chinese Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese Female', service="")


class ChineseMale(ResponsiveVoice):
    uri = "ChineseMale"
    name = "Chinese Male"
    voiceIDs = [334, 373, 389]
    _raw = {'flag': 'cn', 'gender': 'm', 'lang': 'zh-CN', 'voiceIDs': [334, 373, 389], 'name': 'Chinese Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese Male', service="")


class ChineseHongKongFemale(ResponsiveVoice):
    uri = "ChineseHongKongFemale"
    name = "Chinese (Hong Kong) Female"
    voiceIDs = [464, 192, 193, 232, 250, 251, 270, 299, 355, 409, 444, 252]
    _raw = {'flag': 'hk', 'gender': 'f', 'lang': 'zh-HK',
            'voiceIDs': [464, 192, 193, 232, 250, 251, 270, 299, 355, 409, 444, 252],
            'name': 'Chinese (Hong Kong) Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese (Hong Kong) Female', service="")


class ChineseHongKongMale(ResponsiveVoice):
    uri = "ChineseHongKongMale"
    name = "Chinese (Hong Kong) Male"
    voiceIDs = [318, 335, 374, 445, 390]
    _raw = {'flag': 'hk', 'gender': 'm', 'lang': 'zh-HK', 'voiceIDs': [318, 335, 374, 445, 390],
            'name': 'Chinese (Hong Kong) Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese (Hong Kong) Male', service="")


class ChineseTaiwanFemale(ResponsiveVoice):
    uri = "ChineseTaiwanFemale"
    name = "Chinese Taiwan Female"
    voiceIDs = [194, 233, 253, 254, 305, 322, 361, 384, 319, 336, 375, 409, 255]
    _raw = {'flag': 'tw', 'gender': 'f', 'lang': 'zh-TW',
            'voiceIDs': [194, 233, 253, 254, 305, 322, 361, 384, 319, 336, 375, 409, 255],
            'name': 'Chinese Taiwan Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese Taiwan Female', service="")


class ChineseTaiwanMale(ResponsiveVoice):
    uri = "ChineseTaiwanMale"
    name = "Chinese Taiwan Male"
    voiceIDs = [337, 376, 391]
    _raw = {'flag': 'tw', 'gender': 'm', 'lang': 'zh-TW', 'voiceIDs': [337, 376, 391], 'name': 'Chinese Taiwan Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese Taiwan Male', service="")


class CzechFemale(ResponsiveVoice):
    uri = "CzechFemale"
    name = "Czech Female"
    voiceIDs = [412, 101, 100, 102, 197, 103]
    _raw = {'flag': 'cz', 'gender': 'f', 'lang': 'cs-CZ', 'voiceIDs': [412, 101, 100, 102, 197, 103],
            'name': 'Czech Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs-CZ", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Czech Female', service="")


class CzechMale(ResponsiveVoice):
    uri = "CzechMale"
    name = "Czech Male"
    voiceIDs = [161]
    _raw = {'flag': 'cz', 'gender': 'm', 'lang': 'cs-CZ', 'voiceIDs': '161', 'deprecated': True, 'name': 'Czech Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs-CZ", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Czech Male', service="")


class DanishFemale(ResponsiveVoice):
    uri = "DanishFemale"
    name = "Danish Female"
    voiceIDs = [413, 105, 104, 106, 198, 107]
    _raw = {'flag': 'dk', 'gender': 'f', 'lang': 'da-DK', 'voiceIDs': [413, 105, 104, 106, 198, 107],
            'name': 'Danish Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da-DK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Danish Female', service="")


class DanishMale(ResponsiveVoice):
    uri = "DanishMale"
    name = "Danish Male"
    voiceIDs = [162]
    _raw = {'flag': 'da', 'gender': 'm', 'lang': 'da-DK', 'voiceIDs': '162', 'deprecated': True, 'name': 'Danish Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da-DK", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Danish Male', service="")


class DeutschFemale(ResponsiveVoice):
    uri = "DeutschFemale"
    name = "Deutsch Female"
    voiceIDs = [28, 29, 30, 78, 170, 275, 199, 31, 502, 261, 290, 346, 262, 291, 347, 32]
    _raw = {'flag': 'de', 'gender': 'f', 'lang': 'de-DE',
            'voiceIDs': [28, 29, 30, 78, 170, 275, 199, 31, 502, 261, 290, 346, 262, 291, 347, 32],
            'name': 'Deutsch Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Deutsch Female', service="")


class DeutschMale(ResponsiveVoice):
    uri = "DeutschMale"
    name = "Deutsch Male"
    voiceIDs = [324, 363, 377, 393]
    _raw = {'flag': 'de', 'gender': 'm', 'lang': 'de-DE', 'voiceIDs': [324, 363, 377, 393], 'name': 'Deutsch Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Deutsch Male', service="")


class DutchFemale(ResponsiveVoice):
    uri = "DutchFemale"
    name = "Dutch Female"
    voiceIDs = [219, 84, 157, 158, 496, 184, 45]
    _raw = {'flag': 'nl', 'gender': 'f', 'lang': 'nl-NL', 'voiceIDs': [219, 84, 157, 158, 496, 184, 45],
            'name': 'Dutch Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-NL", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Dutch Female', service="")


class DutchMale(ResponsiveVoice):
    uri = "DutchMale"
    name = "Dutch Male"
    voiceIDs = [220, 407]
    _raw = {'flag': 'nl', 'gender': 'm', 'lang': 'nl-NL', 'voiceIDs': [220, 407], 'name': 'Dutch Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-NL", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Dutch Male', service="")


class EstonianMale(ResponsiveVoice):
    uri = "EstonianMale"
    name = "Estonian Male"
    voiceIDs = [416, 446]
    _raw = {'flag': 'ee', 'gender': 'm', 'lang': 'et-EE', 'voiceIDs': [416, 446], 'name': 'Estonian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="et-EE", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Estonian Male', service="")


class FilipinoFemale(ResponsiveVoice):
    uri = "FilipinoFemale"
    name = "Filipino Female"
    voiceIDs = [418, 437]
    _raw = {'flag': 'ph', 'gender': 'f', 'lang': 'fil-PH', 'voiceIDs': [418, 437], 'name': 'Filipino Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fil-PH", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Filipino Female', service="")


class FinnishFemale(ResponsiveVoice):
    uri = "FinnishFemale"
    name = "Finnish Female"
    voiceIDs = [417, 90, 89, 91, 209, 92]
    _raw = {'flag': 'fi', 'gender': 'f', 'lang': 'fi-FI', 'voiceIDs': [417, 90, 89, 91, 209, 92],
            'name': 'Finnish Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi-FI", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Finnish Female', service="")


class FinnishMale(ResponsiveVoice):
    uri = "FinnishMale"
    name = "Finnish Male"
    voiceIDs = [160]
    _raw = {'flag': 'fi', 'gender': 'm', 'lang': 'fi-FI', 'voiceIDs': '160', 'deprecated': True, 'name': 'Finnish Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi-FI", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Finnish Male', service="")


class FrenchFemale(ResponsiveVoice):
    uri = "FrenchFemale"
    name = "French Female"
    voiceIDs = [21, 22, 23, 77, 178, 279, 210, 493, 266, 295, 351, 304, 321, 360, 26]
    _raw = {'flag': 'fr', 'gender': 'f', 'lang': 'fr-FR',
            'voiceIDs': [21, 22, 23, 77, 178, 279, 210, 493, 266, 295, 351, 304, 321, 360, 26], 'name': 'French Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='French Female', service="")


class FrenchMale(ResponsiveVoice):
    uri = "FrenchMale"
    name = "French Male"
    voiceIDs = [328, 367, 378, 392]
    _raw = {'flag': 'fr', 'gender': 'm', 'lang': 'fr-FR', 'voiceIDs': [328, 367, 378, 392], 'name': 'French Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='French Male', service="")


class FrenchCanadianFemale(ResponsiveVoice):
    uri = "FrenchCanadianFemale"
    name = "French Canadian Female"
    voiceIDs = [419, 210, 449]
    _raw = {'flag': 'ca', 'gender': 'f', 'lang': 'fr-CA', 'voiceIDs': [419, 210, 449], 'name': 'French Canadian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-CA", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='French Canadian Female', service="")


class FrenchCanadianMale(ResponsiveVoice):
    uri = "FrenchCanadianMale"
    name = "French Canadian Male"
    voiceIDs = [450]
    _raw = {'flag': 'ca', 'gender': 'm', 'lang': 'fr-CA', 'voiceIDs': '450', 'name': 'French Canadian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-CA", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='French Canadian Male', service="")


class GreekFemale(ResponsiveVoice):
    uri = "GreekFemale"
    name = "Greek Female"
    voiceIDs = [414, 62, 63, 80, 200, 64]
    _raw = {'flag': 'gr', 'gender': 'f', 'lang': 'el-GR', 'voiceIDs': [414, 62, 63, 80, 200, 64],
            'name': 'Greek Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el-GR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Greek Female', service="")


class GreekMale(ResponsiveVoice):
    uri = "GreekMale"
    name = "Greek Male"
    voiceIDs = [163]
    _raw = {'flag': 'gr', 'gender': 'm', 'lang': 'el-GR', 'voiceIDs': '163', 'deprecated': True, 'name': 'Greek Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el-GR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Greek Male', service="")


class HindiFemale(ResponsiveVoice):
    uri = "HindiFemale"
    name = "Hindi Female"
    voiceIDs = [66, 154, 179, 213, 489, 259, 288, 344, 67]
    _raw = {'flag': 'hi', 'gender': 'f', 'lang': 'hi-IN', 'voiceIDs': [66, 154, 179, 213, 489, 259, 288, 344, 67],
            'name': 'Hindi Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Hindi Female', service="")


class HindiMale(ResponsiveVoice):
    uri = "HindiMale"
    name = "Hindi Male"
    voiceIDs = [394]
    _raw = {'flag': 'hi', 'gender': 'm', 'lang': 'hi-IN', 'voiceIDs': '394', 'name': 'Hindi Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Hindi Male', service="")


class HungarianFemale(ResponsiveVoice):
    uri = "HungarianFemale"
    name = "Hungarian Female"
    voiceIDs = [420, 9, 10, 81, 214, 11]
    _raw = {'flag': 'hu', 'gender': 'f', 'lang': 'hu-HU', 'voiceIDs': [420, 9, 10, 81, 214, 11],
            'name': 'Hungarian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu-HU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Hungarian Female', service="")


class HungarianMale(ResponsiveVoice):
    uri = "HungarianMale"
    name = "Hungarian Male"
    voiceIDs = [164]
    _raw = {'flag': 'hu', 'gender': 'm', 'lang': 'hu-HU', 'voiceIDs': '164', 'deprecated': True,
            'name': 'Hungarian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu-HU", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Hungarian Male', service="")


class IndonesianFemale(ResponsiveVoice):
    uri = "IndonesianFemale"
    name = "Indonesian Female"
    voiceIDs = [111, 112, 524, 180, 215, 113]
    _raw = {'flag': 'id', 'gender': 'f', 'lang': 'id-ID', 'voiceIDs': [111, 112, 524, 180, 215, 113],
            'name': 'Indonesian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id-ID", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Indonesian Female', service="")


class IndonesianMale(ResponsiveVoice):
    uri = "IndonesianMale"
    name = "Indonesian Male"
    voiceIDs = [395]
    _raw = {'flag': 'id', 'gender': 'm', 'lang': 'id-ID', 'voiceIDs': '395', 'name': 'Indonesian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id-ID", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Indonesian Male', service="")


class ItalianFemale(ResponsiveVoice):
    uri = "ItalianFemale"
    name = "Italian Female"
    voiceIDs = [33, 34, 35, 36, 37, 79, 181, 216, 508, 271, 300, 356, 38]
    _raw = {'flag': 'it', 'gender': 'f', 'lang': 'it-IT',
            'voiceIDs': [33, 34, 35, 36, 37, 79, 181, 216, 508, 271, 300, 356, 38], 'name': 'Italian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Italian Female', service="")


class ItalianMale(ResponsiveVoice):
    uri = "ItalianMale"
    name = "Italian Male"
    voiceIDs = [329, 368, 406]
    _raw = {'flag': 'it', 'gender': 'm', 'lang': 'it-IT', 'voiceIDs': [329, 368, 406], 'name': 'Italian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Italian Male', service="")


class JapaneseFemale(ResponsiveVoice):
    uri = "JapaneseFemale"
    name = "Japanese Female"
    voiceIDs = [280, 217, 52, 153, 517, 182, 273, 302, 358, 274, 303, 359, 53]
    _raw = {'flag': 'jp', 'gender': 'f', 'lang': 'ja-JP',
            'voiceIDs': [280, 217, 52, 153, 517, 182, 273, 302, 358, 274, 303, 359, 53], 'name': 'Japanese Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Japanese Female', service="")


class JapaneseMale(ResponsiveVoice):
    uri = "JapaneseMale"
    name = "Japanese Male"
    voiceIDs = [50, 313, 330, 369, 396]
    _raw = {'flag': 'jp', 'gender': 'm', 'lang': 'ja-JP', 'voiceIDs': [50, 313, 330, 369, 396], 'name': 'Japanese Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Japanese Male', service="")


class KoreanFemale(ResponsiveVoice):
    uri = "KoreanFemale"
    name = "Korean Female"
    voiceIDs = [55, 56, 156, 183, 218, 466, 306, 323, 362, 384, 57]
    _raw = {'flag': 'kr', 'gender': 'f', 'lang': 'ko-KR',
            'voiceIDs': [55, 56, 156, 183, 218, 466, 306, 323, 362, 384, 57], 'name': 'Korean Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Korean Female', service="")


class KoreanMale(ResponsiveVoice):
    uri = "KoreanMale"
    name = "Korean Male"
    voiceIDs = [397]
    _raw = {'flag': 'kr', 'gender': 'm', 'lang': 'ko-KR', 'voiceIDs': '397', 'name': 'Korean Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Korean Male', service="")


class LatinFemale(ResponsiveVoice):
    uri = "LatinFemale"
    name = "Latin Female"
    voiceIDs = [114]
    _raw = {'flag': 'va', 'gender': 'f', 'lang': 'la', 'voiceIDs': '114', 'deprecated': True, 'name': 'Latin Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="la", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Latin Female', service="")


class LatinMale(ResponsiveVoice):
    uri = "LatinMale"
    name = "Latin Male"
    voiceIDs = [165]
    _raw = {'flag': 'va', 'gender': 'm', 'lang': 'la', 'voiceIDs': '165', 'name': 'Latin Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="la", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Latin Male', service="")


class Nepali(ResponsiveVoice):
    uri = "Nepali"
    name = "Nepali"
    voiceIDs = [423, 441]
    _raw = {'flag': 'np', 'gender': 'f', 'lang': 'ne-NP', 'voiceIDs': [423, 441], 'name': 'Nepali'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ne-NP", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Nepali', service="")


class NorwegianFemale(ResponsiveVoice):
    uri = "NorwegianFemale"
    name = "Norwegian Female"
    voiceIDs = [422, 72, 73, 221, 74]
    _raw = {'flag': 'no', 'gender': 'f', 'lang': 'nb-NO', 'voiceIDs': [422, 72, 73, 221, 74],
            'name': 'Norwegian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nb-NO", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Norwegian Female', service="")


class NorwegianMale(ResponsiveVoice):
    uri = "NorwegianMale"
    name = "Norwegian Male"
    voiceIDs = [166]
    _raw = {'flag': 'no', 'gender': 'm', 'lang': 'nb-NO', 'voiceIDs': '166', 'name': 'Norwegian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nb-NO", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Norwegian Male', service="")


class PolishFemale(ResponsiveVoice):
    uri = "PolishFemale"
    name = "Polish Female"
    voiceIDs = [120, 119, 121, 185, 222, 505, 267, 296, 352, 122]
    _raw = {'flag': 'pl', 'gender': 'f', 'lang': 'pl-PL',
            'voiceIDs': [120, 119, 121, 185, 222, 505, 267, 296, 352, 122], 'name': 'Polish Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Polish Female', service="")


class PolishMale(ResponsiveVoice):
    uri = "PolishMale"
    name = "Polish Male"
    voiceIDs = [331, 370, 398]
    _raw = {'flag': 'pl', 'gender': 'm', 'lang': 'pl-PL', 'voiceIDs': [331, 370, 398], 'name': 'Polish Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Polish Male', service="")


class PortugueseFemale(ResponsiveVoice):
    uri = "PortugueseFemale"
    name = "Portuguese Female"
    voiceIDs = [127, 129, 187, 224, 479, 272, 301, 357, 130]
    _raw = {'flag': 'br', 'gender': 'f', 'lang': 'pt-BR', 'voiceIDs': [127, 129, 187, 224, 479, 272, 301, 357, 130],
            'name': 'Portuguese Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Portuguese Female', service="")


class PortugueseMale(ResponsiveVoice):
    uri = "PortugueseMale"
    name = "Portuguese Male"
    voiceIDs = [400]
    _raw = {'flag': 'br', 'gender': 'm', 'lang': 'pt-BR', 'voiceIDs': '400', 'name': 'Portuguese Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Portuguese Male', service="")


class RomanianFemale(ResponsiveVoice):
    uri = "RomanianFemale"
    name = "Romanian Female"
    voiceIDs = [424, 151, 150, 152, 225, 46]
    _raw = {'flag': 'ro', 'gender': 'f', 'lang': 'ro-RO', 'voiceIDs': [424, 151, 150, 152, 225, 46],
            'name': 'Romanian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ro-RO", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Romanian Female', service="")


class RussianFemale(ResponsiveVoice):
    uri = "RussianFemale"
    name = "Russian Female"
    voiceIDs = [47, 48, 83, 468, 188, 226, 260, 289, 345, 49]
    _raw = {'flag': 'ru', 'gender': 'f', 'lang': 'ru-RU', 'voiceIDs': [47, 48, 83, 468, 188, 226, 260, 289, 345, 49],
            'name': 'Russian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Russian Female', service="")


class RussianMale(ResponsiveVoice):
    uri = "RussianMale"
    name = "Russian Male"
    voiceIDs = [333, 372, 387]
    _raw = {'flag': 'ru', 'gender': 'm', 'lang': 'ru-RU', 'voiceIDs': [333, 372, 387], 'deprecated': True,
            'name': 'Russian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Russian Male', service="")


class Sinhala(ResponsiveVoice):
    uri = "Sinhala"
    name = "Sinhala"
    voiceIDs = [425, 442]
    _raw = {'flag': 'lk', 'gender': 'f', 'lang': 'si-LK', 'voiceIDs': [425, 442], 'name': 'Sinhala'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="si-LK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Sinhala', service="")


class SlovakFemale(ResponsiveVoice):
    uri = "SlovakFemale"
    name = "Slovak Female"
    voiceIDs = [426, 133, 132, 134, 227, 135]
    _raw = {'flag': 'sk', 'gender': 'f', 'lang': 'sk-SK', 'voiceIDs': [426, 133, 132, 134, 227, 135],
            'name': 'Slovak Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk-SK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Slovak Female', service="")


class SlovakMale(ResponsiveVoice):
    uri = "SlovakMale"
    name = "Slovak Male"
    voiceIDs = [167]
    _raw = {'flag': 'sk', 'gender': 'm', 'lang': 'sk-SK', 'voiceIDs': '167', 'deprecated': True, 'name': 'Slovak Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk-SK", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Slovak Male', service="")


class SpanishFemale(ResponsiveVoice):
    uri = "SpanishFemale"
    name = "Spanish Female"
    voiceIDs = [238, 16, 17, 18, 20, 76, 174, 207, 514, 521, 263, 292, 348, 264, 293, 349, 15]
    _raw = {'flag': 'es', 'gender': 'f', 'lang': 'es-ES',
            'voiceIDs': [238, 16, 17, 18, 20, 76, 174, 207, 514, 521, 263, 292, 348, 264, 293, 349, 15],
            'name': 'Spanish Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Spanish Female', service="")


class SpanishMale(ResponsiveVoice):
    uri = "SpanishMale"
    name = "Spanish Male"
    voiceIDs = [326, 365, 401]
    _raw = {'flag': 'es', 'gender': 'm', 'lang': 'es-ES', 'voiceIDs': [326, 365, 401], 'deprecated': True,
            'name': 'Spanish Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Spanish Male', service="")


class SpanishLatinAmericanFemale(ResponsiveVoice):
    uri = "SpanishLatinAmericanFemale"
    name = "Spanish Latin American Female"
    voiceIDs = [137, 136, 138, 175, 208, 265, 294, 350, 139]
    _raw = {'flag': 'es', 'gender': 'f', 'lang': 'es-MX', 'voiceIDs': [137, 136, 138, 175, 208, 265, 294, 350, 139],
            'name': 'Spanish Latin American Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Spanish Latin American Female', service="")


class SpanishLatinAmericanMale(ResponsiveVoice):
    uri = "SpanishLatinAmericanMale"
    name = "Spanish Latin American Male"
    voiceIDs = [310, 327, 366, 402]
    _raw = {'flag': 'es', 'gender': 'm', 'lang': 'es-MX', 'voiceIDs': [310, 327, 366, 402],
            'name': 'Spanish Latin American Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Spanish Latin American Male', service="")


class SwedishFemale(ResponsiveVoice):
    uri = "SwedishFemale"
    name = "Swedish Female"
    voiceIDs = [427, 85, 149, 228, 65]
    _raw = {'flag': 'sv', 'gender': 'f', 'lang': 'sv-SE', 'voiceIDs': [427, 85, 149, 228, 65], 'name': 'Swedish Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sv-SE", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Swedish Female', service="")


class SwedishMale(ResponsiveVoice):
    uri = "SwedishMale"
    name = "Swedish Male"
    voiceIDs = [168]
    _raw = {'flag': 'sv', 'gender': 'm', 'lang': 'sv-SE', 'voiceIDs': [168], 'name': 'Swedish Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sv-SE", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Swedish Male', service="")


class TamilFemale(ResponsiveVoice):
    uri = "TamilFemale"
    name = "Tamil Female"
    voiceIDs = [516, 451]
    _raw = {'flag': 'hi', 'gender': 'm', 'lang': 'hi-IN', 'voiceIDs': [516, 451], 'name': 'Tamil Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Tamil Female', service="")


class TamilMale(ResponsiveVoice):
    uri = "TamilMale"
    name = "Tamil Male"
    voiceIDs = [141]
    _raw = {'flag': 'hi', 'gender': 'm', 'lang': 'hi-IN', 'voiceIDs': '141', 'name': 'Tamil Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Tamil Male', service="")


class ThaiFemale(ResponsiveVoice):
    uri = "ThaiFemale"
    name = "Thai Female"
    voiceIDs = [142, 144, 471, 189, 229, 145]
    _raw = {'flag': 'th', 'gender': 'f', 'lang': 'th-TH', 'voiceIDs': [142, 144, 471, 189, 229, 145],
            'name': 'Thai Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th-TH", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Thai Female', service="")


class ThaiMale(ResponsiveVoice):
    uri = "ThaiMale"
    name = "Thai Male"
    voiceIDs = [403]
    _raw = {'flag': 'th', 'gender': 'm', 'lang': 'th-TH', 'voiceIDs': '403', 'name': 'Thai Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th-TH", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Thai Male', service="")


class TurkishFemale(ResponsiveVoice):
    uri = "TurkishFemale"
    name = "Turkish Female"
    voiceIDs = [70, 82, 475, 190, 230, 71]
    _raw = {'flag': 'tr', 'gender': 'f', 'lang': 'tr-TR', 'voiceIDs': [70, 82, 475, 190, 230, 71],
            'name': 'Turkish Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr-TR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Turkish Female', service="")


class TurkishMale(ResponsiveVoice):
    uri = "TurkishMale"
    name = "Turkish Male"
    voiceIDs = [404]
    _raw = {'flag': 'tr', 'gender': 'm', 'lang': 'tr-TR', 'voiceIDs': [404], 'name': 'Turkish Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr-TR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Turkish Male', service="")


class UkrainianFemale(ResponsiveVoice):
    uri = "UkrainianFemale"
    name = "Ukrainian Female"
    voiceIDs = [428, 443]
    _raw = {'flag': 'ua', 'gender': 'f', 'lang': 'uk-UA', 'voiceIDs': [428, 443], 'name': 'Ukrainian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="uk-UA", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ukrainian Female', service="")


class VietnameseFemale(ResponsiveVoice):
    uri = "VietnameseFemale"
    name = "Vietnamese Female"
    voiceIDs = [429, 405]
    _raw = {'flag': 'vi', 'gender': 'f', 'lang': 'vi-VN', 'voiceIDs': [429, 405], 'name': 'Vietnamese Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="vi-VN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Vietnamese Female', service="")


class VietnameseMale(ResponsiveVoice):
    uri = "VietnameseMale"
    name = "Vietnamese Male"
    voiceIDs = [146]
    _raw = {'flag': 'vi', 'gender': 'm', 'lang': 'vi-VN', 'voiceIDs': '146', 'name': 'Vietnamese Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="vi-VN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Vietnamese Male', service="")


class AfrikaansMale(ResponsiveVoice):
    uri = "AfrikaansMale"
    name = "Afrikaans Male"
    voiceIDs = [93]
    _raw = {'flag': 'af', 'gender': 'm', 'lang': 'af-ZA', 'voiceIDs': '93', 'name': 'Afrikaans Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="af-ZA", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Afrikaans Male', service="")


class AlbanianMale(ResponsiveVoice):
    uri = "AlbanianMale"
    name = "Albanian Male"
    voiceIDs = [94]
    _raw = {'flag': 'sq', 'gender': 'm', 'lang': 'sq-AL', 'voiceIDs': '94', 'name': 'Albanian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sq-AL", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Albanian Male', service="")


class BosnianMale(ResponsiveVoice):
    uri = "BosnianMale"
    name = "Bosnian Male"
    voiceIDs = [14]
    _raw = {'flag': 'bs', 'gender': 'm', 'lang': 'bs', 'voiceIDs': '14', 'name': 'Bosnian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bs", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Bosnian Male', service="")


class CatalanMale(ResponsiveVoice):
    uri = "CatalanMale"
    name = "Catalan Male"
    voiceIDs = [68]
    _raw = {'flag': 'catalonia', 'gender': 'm', 'lang': 'ca-ES', 'voiceIDs': '68', 'name': 'Catalan Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ca-ES", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Catalan Male', service="")


class CroatianMale(ResponsiveVoice):
    uri = "CroatianMale"
    name = "Croatian Male"
    voiceIDs = [13]
    _raw = {'flag': 'hr', 'gender': 'm', 'lang': 'hr-HR', 'voiceIDs': '13', 'name': 'Croatian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hr-HR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Croatian Male', service="")


class EsperantoMale(ResponsiveVoice):
    uri = "EsperantoMale"
    name = "Esperanto Male"
    voiceIDs = [108]
    _raw = {'flag': 'eo', 'gender': 'm', 'lang': 'eo', 'voiceIDs': '108', 'name': 'Esperanto Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="eo", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Esperanto Male', service="")


class IcelandicMale(ResponsiveVoice):
    uri = "IcelandicMale"
    name = "Icelandic Male"
    voiceIDs = [110]
    _raw = {'flag': 'is', 'gender': 'm', 'lang': 'is-IS', 'voiceIDs': '110', 'deprecated': True,
            'name': 'Icelandic Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="is-IS", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Icelandic Male', service="")


class IcelandicFemale(ResponsiveVoice):
    uri = "IcelandicFemale"
    name = "Icelandic Female"
    voiceIDs = [110]
    _raw = {'flag': 'is', 'gender': 'm', 'lang': 'is-IS', 'voiceIDs': '110', 'name': 'Icelandic Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="is-IS", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Icelandic Female', service="")


class LatvianMale(ResponsiveVoice):
    uri = "LatvianMale"
    name = "Latvian Male"
    voiceIDs = [115]
    _raw = {'flag': 'lv', 'gender': 'm', 'lang': 'lv-LV', 'voiceIDs': '115', 'name': 'Latvian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="lv-LV", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Latvian Male', service="")


class MacedonianMale(ResponsiveVoice):
    uri = "MacedonianMale"
    name = "Macedonian Male"
    voiceIDs = [116]
    _raw = {'flag': 'mk', 'gender': 'm', 'lang': 'mk-MK', 'voiceIDs': '116', 'name': 'Macedonian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="mk-MK", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Macedonian Male', service="")


class MoldavianFemale(ResponsiveVoice):
    uri = "MoldavianFemale"
    name = "Moldavian Female"
    voiceIDs = [117]
    _raw = {'flag': 'md', 'gender': 'f', 'lang': 'md', 'voiceIDs': '117', 'name': 'Moldavian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="md", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Moldavian Female', service="")


class MoldavianMale(ResponsiveVoice):
    uri = "MoldavianMale"
    name = "Moldavian Male"
    voiceIDs = [117]
    _raw = {'flag': 'md', 'gender': 'm', 'lang': 'md', 'voiceIDs': '117', 'deprecated': True, 'name': 'Moldavian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="md", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Moldavian Male', service="")


class MontenegrinMale(ResponsiveVoice):
    uri = "MontenegrinMale"
    name = "Montenegrin Male"
    voiceIDs = [118]
    _raw = {'flag': 'me', 'gender': 'm', 'lang': 'me', 'voiceIDs': '118', 'name': 'Montenegrin Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="me", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Montenegrin Male', service="")


class SerbianMale(ResponsiveVoice):
    uri = "SerbianMale"
    name = "Serbian Male"
    voiceIDs = [12]
    _raw = {'flag': 'sr', 'gender': 'm', 'lang': 'sr-RS', 'voiceIDs': '12', 'name': 'Serbian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sr-RS", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Serbian Male', service="")


class SerbocroatianMale(ResponsiveVoice):
    uri = "SerbocroatianMale"
    name = "Serbo-Croatian Male"
    voiceIDs = [131]
    _raw = {'flag': 'hr', 'gender': 'm', 'lang': 'hr-HR', 'voiceIDs': '131', 'name': 'Serbo-Croatian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hr-HR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Serbo-Croatian Male', service="")


class SwahiliMale(ResponsiveVoice):
    uri = "SwahiliMale"
    name = "Swahili Male"
    voiceIDs = [140]
    _raw = {'flag': 'sw', 'gender': 'm', 'lang': 'sw-KE', 'voiceIDs': '140', 'name': 'Swahili Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sw-KE", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Swahili Male', service="")


class WelshMale(ResponsiveVoice):
    uri = "WelshMale"
    name = "Welsh Male"
    voiceIDs = [147]
    _raw = {'flag': 'cy', 'gender': 'm', 'lang': 'cy', 'voiceIDs': '147', 'name': 'Welsh Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cy", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Welsh Male', service="")


class FallbackUkFemale(ResponsiveVoice):
    uri = "FallbackUkFemale"
    name = "Fallback UK Female"
    voiceIDs = []
    _raw = {'flag': 'gb', 'gender': 'f', 'lang': 'en-GB', 'voiceIDs': '', 'name': 'Fallback UK Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback UK Female', service="")


class FallbackEngbFemale(ResponsiveVoice):
    uri = "FallbackEngbFemale"
    name = "Fallback en-GB Female"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female',
            'name': 'Fallback en-GB Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback en-GB Female', service="g1")


class FallbackHungarianFemale(ResponsiveVoice):
    uri = "FallbackHungarianFemale"
    name = "Fallback Hungarian Female"
    voiceIDs = []
    _raw = {'lang': 'hu', 'fallbackvoice': True, 'service': 'g1', 'name': 'Fallback Hungarian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Hungarian Female', service="g1")


class FallbackSerbianMale(ResponsiveVoice):
    uri = "FallbackSerbianMale"
    name = "Fallback Serbian Male"
    voiceIDs = []
    _raw = {'lang': 'sr', 'fallbackvoice': True, 'service': 'g1', 'gender': 'male', 'name': 'Fallback Serbian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sr", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Serbian Male', service="g1")


class FallbackCroatianMale(ResponsiveVoice):
    uri = "FallbackCroatianMale"
    name = "Fallback Croatian Male"
    voiceIDs = []
    _raw = {'lang': 'hr', 'rate': '.5', 'fallbackvoice': True, 'service': 'g2', 'gender': 'male',
            'name': 'Fallback Croatian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hr", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Croatian Male', service="g2")


class FallbackBosnianMale(ResponsiveVoice):
    uri = "FallbackBosnianMale"
    name = "Fallback Bosnian Male"
    voiceIDs = []
    _raw = {'lang': 'bs', 'fallbackvoice': True, 'service': 'g2', 'gender': 'male', 'name': 'Fallback Bosnian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bs", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Bosnian Male', service="g2")


class FallbackSpanishFemale(ResponsiveVoice):
    uri = "FallbackSpanishFemale"
    name = "Fallback Spanish Female"
    voiceIDs = []
    _raw = {'lang': 'es', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Spanish Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Spanish Female', service="g1")


class FallbackFrenchFemale(ResponsiveVoice):
    uri = "FallbackFrenchFemale"
    name = "Fallback French Female"
    voiceIDs = []
    _raw = {'lang': 'fr', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback French Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback French Female', service="g1")


class FallbackDeutschFemale(ResponsiveVoice):
    uri = "FallbackDeutschFemale"
    name = "Fallback Deutsch Female"
    voiceIDs = []
    _raw = {'lang': 'de', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Deutsch Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Deutsch Female', service="g1")


class FallbackItalianFemale(ResponsiveVoice):
    uri = "FallbackItalianFemale"
    name = "Fallback Italian Female"
    voiceIDs = []
    _raw = {'lang': 'it', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Italian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Italian Female', service="g1")


class FallbackUsEnglish(ResponsiveVoice):
    uri = "FallbackUsEnglish"
    name = "Fallback US English"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g1', 'gender': 'female',
            'name': 'Fallback US English'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback US English', service="g1")


class FallbackDutchFemale(ResponsiveVoice):
    uri = "FallbackDutchFemale"
    name = "Fallback Dutch Female"
    voiceIDs = []
    _raw = {'lang': 'nl', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g1', 'gender': 'female',
            'name': 'Fallback Dutch Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Dutch Female', service="g1")


class FallbackRomanian(ResponsiveVoice):
    uri = "FallbackRomanian"
    name = "Fallback Romanian"
    voiceIDs = []
    _raw = {'lang': 'ro', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Romanian'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ro", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Romanian', service="g1")


class FallbackRussian(ResponsiveVoice):
    uri = "FallbackRussian"
    name = "Fallback Russian"
    voiceIDs = []
    _raw = {'lang': 'ru', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Russian'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Russian', service="g1")


class FallbackJapaneseFemale(ResponsiveVoice):
    uri = "FallbackJapaneseFemale"
    name = "Fallback Japanese Female"
    voiceIDs = []
    _raw = {'lang': 'ja', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female',
            'name': 'Fallback Japanese Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Japanese Female', service="g1")


class FallbackKoreanFemale(ResponsiveVoice):
    uri = "FallbackKoreanFemale"
    name = "Fallback Korean Female"
    voiceIDs = []
    _raw = {'lang': 'ko', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Korean Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Korean Female', service="g1")


class FallbackChinese(ResponsiveVoice):
    uri = "FallbackChinese"
    name = "Fallback Chinese"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Chinese'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Chinese', service="g1")


class FallbackGreek(ResponsiveVoice):
    uri = "FallbackGreek"
    name = "Fallback Greek"
    voiceIDs = []
    _raw = {'lang': 'el', 'fallbackvoice': True, 'service': 'g3', 'gender': 'female', 'name': 'Fallback Greek'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Greek', service="g3")


class FallbackSwedish(ResponsiveVoice):
    uri = "FallbackSwedish"
    name = "Fallback Swedish"
    voiceIDs = []
    _raw = {'lang': 'sv', 'fallbackvoice': True, 'service': 'g3', 'gender': 'female', 'name': 'Fallback Swedish'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sv", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Swedish', service="g3")


class FallbackHindiFemale(ResponsiveVoice):
    uri = "FallbackHindiFemale"
    name = "Fallback Hindi Female"
    voiceIDs = []
    _raw = {'lang': 'hi', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Hindi Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Hindi Female', service="g1")


class FallbackCatalan(ResponsiveVoice):
    uri = "FallbackCatalan"
    name = "Fallback Catalan"
    voiceIDs = []
    _raw = {'lang': 'ca', 'fallbackvoice': True, 'service': 'g1', 'gender': 'male', 'name': 'Fallback Catalan'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ca", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Catalan', service="g1")


class FallbackTurkish(ResponsiveVoice):
    uri = "FallbackTurkish"
    name = "Fallback Turkish"
    voiceIDs = []
    _raw = {'lang': 'tr', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Turkish'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Turkish', service="g1")


class FallbackNorwegian(ResponsiveVoice):
    uri = "FallbackNorwegian"
    name = "Fallback Norwegian"
    voiceIDs = []
    _raw = {'lang': 'no', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Norwegian'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="no", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Norwegian', service="g1")


class FallbackAustralianFemale(ResponsiveVoice):
    uri = "FallbackAustralianFemale"
    name = "Fallback Australian Female"
    voiceIDs = []
    _raw = {'lang': 'en-AU', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female',
            'name': 'Fallback Australian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Australian Female', service="g1")


class FallbackFinnish(ResponsiveVoice):
    uri = "FallbackFinnish"
    name = "Fallback Finnish"
    voiceIDs = []
    _raw = {'lang': 'fi', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Finnish'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Finnish', service="g1")


class FallbackAfrikans(ResponsiveVoice):
    uri = "FallbackAfrikans"
    name = "Fallback Afrikans"
    voiceIDs = []
    _raw = {'lang': 'af', 'fallbackvoice': True, 'service': 'g1', 'gender': 'male', 'name': 'Fallback Afrikans'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="af", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Afrikans', service="g1")


class FallbackAlbanian(ResponsiveVoice):
    uri = "FallbackAlbanian"
    name = "Fallback Albanian"
    voiceIDs = []
    _raw = {'lang': 'sq', 'fallbackvoice': True, 'service': 'g2', 'gender': 'male', 'name': 'Fallback Albanian'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sq", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Albanian', service="g2")


class FallbackArabic(ResponsiveVoice):
    uri = "FallbackArabic"
    name = "Fallback Arabic"
    voiceIDs = []
    _raw = {'lang': 'ar', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Arabic'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Arabic', service="g1")


class FallbackArmenian(ResponsiveVoice):
    uri = "FallbackArmenian"
    name = "Fallback Armenian"
    voiceIDs = []
    _raw = {'lang': 'hy', 'fallbackvoice': True, 'service': 'g2', 'gender': 'male', 'name': 'Fallback Armenian'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hy", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Armenian', service="g2")


class FallbackCzech(ResponsiveVoice):
    uri = "FallbackCzech"
    name = "Fallback Czech"
    voiceIDs = []
    _raw = {'lang': 'cs', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Czech'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Czech', service="g1")


class FallbackDanish(ResponsiveVoice):
    uri = "FallbackDanish"
    name = "Fallback Danish"
    voiceIDs = []
    _raw = {'lang': 'da', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Danish'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Danish', service="g1")


class FallbackEsperanto(ResponsiveVoice):
    uri = "FallbackEsperanto"
    name = "Fallback Esperanto"
    voiceIDs = []
    _raw = {'lang': 'eo', 'fallbackvoice': True, 'service': 'g2', 'gender': 'male', 'name': 'Fallback Esperanto'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="eo", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Esperanto', service="g2")


class FallbackHaitianCreole(ResponsiveVoice):
    uri = "FallbackHaitianCreole"
    name = "Fallback Haitian Creole"
    voiceIDs = []
    _raw = {'lang': 'ht', 'fallbackvoice': True, 'name': 'Fallback Haitian Creole'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ht", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Haitian Creole', service="")


class FallbackIcelandic(ResponsiveVoice):
    uri = "FallbackIcelandic"
    name = "Fallback Icelandic"
    voiceIDs = []
    _raw = {'lang': 'is', 'fallbackvoice': True, 'service': 'g1', 'gender': 'male', 'name': 'Fallback Icelandic'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="is", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Icelandic', service="g1")


class FallbackIndonesianFemale(ResponsiveVoice):
    uri = "FallbackIndonesianFemale"
    name = "Fallback Indonesian Female"
    voiceIDs = []
    _raw = {'lang': 'id', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female',
            'name': 'Fallback Indonesian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Indonesian Female', service="g1")


class FallbackLatinFemale(ResponsiveVoice):
    uri = "FallbackLatinFemale"
    name = "Fallback Latin Female"
    voiceIDs = []
    _raw = {'lang': 'la', 'fallbackvoice': True, 'service': 'g2', 'gender': 'female', 'name': 'Fallback Latin Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="la", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Latin Female', service="g2")


class FallbackLatvianMale(ResponsiveVoice):
    uri = "FallbackLatvianMale"
    name = "Fallback Latvian Male"
    voiceIDs = []
    _raw = {'lang': 'lv', 'fallbackvoice': True, 'service': 'g1', 'gender': 'male', 'name': 'Fallback Latvian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="lv", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Latvian Male', service="g1")


class FallbackMacedonianMale(ResponsiveVoice):
    uri = "FallbackMacedonianMale"
    name = "Fallback Macedonian Male"
    voiceIDs = []
    _raw = {'lang': 'mk', 'fallbackvoice': True, 'service': 'g2', 'gender': 'male', 'name': 'Fallback Macedonian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="mk", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Macedonian Male', service="g2")


class FallbackMoldavianFemale(ResponsiveVoice):
    uri = "FallbackMoldavianFemale"
    name = "Fallback Moldavian Female"
    voiceIDs = []
    _raw = {'lang': 'mo', 'fallbackvoice': True, 'service': 'g2', 'gender': 'female',
            'name': 'Fallback Moldavian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="mo", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Moldavian Female', service="g2")


class FallbackMontenegrinMale(ResponsiveVoice):
    uri = "FallbackMontenegrinMale"
    name = "Fallback Montenegrin Male"
    voiceIDs = []
    _raw = {'lang': 'sr-ME', 'fallbackvoice': True, 'service': 'g1', 'gender': 'male',
            'name': 'Fallback Montenegrin Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sr-ME", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Montenegrin Male', service="g1")


class FallbackPolishFemale(ResponsiveVoice):
    uri = "FallbackPolishFemale"
    name = "Fallback Polish Female"
    voiceIDs = []
    _raw = {'lang': 'pl', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Polish Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Polish Female', service="g1")


class FallbackBrazilianPortugueseFemale(ResponsiveVoice):
    uri = "FallbackBrazilianPortugueseFemale"
    name = "Fallback Brazilian Portuguese Female"
    voiceIDs = []
    _raw = {'lang': 'pt-BR', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female',
            'name': 'Fallback Brazilian Portuguese Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Brazilian Portuguese Female', service="g1")


class FallbackPortuguese(ResponsiveVoice):
    uri = "FallbackPortuguese"
    name = "Fallback Portuguese"
    voiceIDs = []
    _raw = {'lang': 'pt-PT', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Portuguese'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-PT", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Portuguese', service="g1")


class FallbackSerbocroation(ResponsiveVoice):
    uri = "FallbackSerbocroation"
    name = "Fallback Serbo-Croation"
    voiceIDs = []
    _raw = {'lang': 'sh', 'fallbackvoice': True, 'service': 'g2', 'gender': 'male', 'name': 'Fallback Serbo-Croation'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sh", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Serbo-Croation', service="g2")


class FallbackSlovak(ResponsiveVoice):
    uri = "FallbackSlovak"
    name = "Fallback Slovak"
    voiceIDs = []
    _raw = {'lang': 'sk', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Slovak'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Slovak', service="g1")


class FallbackSpanishLatinAmericanFemale(ResponsiveVoice):
    uri = "FallbackSpanishLatinAmericanFemale"
    name = "Fallback Spanish (Latin American) Female"
    voiceIDs = []
    _raw = {'lang': 'es-419', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female',
            'name': 'Fallback Spanish (Latin American) Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-419", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Spanish (Latin American) Female', service="g1")


class FallbackSwahili(ResponsiveVoice):
    uri = "FallbackSwahili"
    name = "Fallback Swahili"
    voiceIDs = []
    _raw = {'lang': 'sw', 'fallbackvoice': True, 'service': 'g2', 'gender': 'male', 'name': 'Fallback Swahili'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sw", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Swahili', service="g2")


class FallbackTamil(ResponsiveVoice):
    uri = "FallbackTamil"
    name = "Fallback Tamil"
    voiceIDs = []
    _raw = {'lang': 'ta', 'fallbackvoice': True, 'service': 'g1', 'gender': 'male', 'name': 'Fallback Tamil'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ta", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Tamil', service="g1")


class FallbackThaiFemale(ResponsiveVoice):
    uri = "FallbackThaiFemale"
    name = "Fallback Thai Female"
    voiceIDs = []
    _raw = {'lang': 'th', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Thai Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Thai Female', service="g1")


class FallbackVietnameseMale(ResponsiveVoice):
    uri = "FallbackVietnameseMale"
    name = "Fallback Vietnamese Male"
    voiceIDs = []
    _raw = {'lang': 'vi', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback Vietnamese Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="vi", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Vietnamese Male', service="g3")


class FallbackWelsh(ResponsiveVoice):
    uri = "FallbackWelsh"
    name = "Fallback Welsh"
    voiceIDs = []
    _raw = {'lang': 'cy', 'fallbackvoice': True, 'service': 'g2', 'gender': 'male', 'name': 'Fallback Welsh'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cy", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Welsh', service="g2")


class FallbackUkEnglishMale(ResponsiveVoice):
    uri = "FallbackUkEnglishMale"
    name = "Fallback UK English Male"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'fallbackvoice': True, 'service': 'g1', 'voicename': 'rjs', 'gender': 'male',
            'name': 'Fallback UK English Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback UK English Male', service="g1")


class FinnishMaleAlt(ResponsiveVoice):
    uri = "FinnishMaleAlt"
    name = "Finnish Male"
    voiceIDs = []
    _raw = {'lang': 'fi', 'fallbackvoice': True, 'service': 'g3', 'voicename': '', 'gender': 'male', 'deprecated': True,
            'name': 'Finnish Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Finnish Male', service="g3")


class CzechMaleAlt(ResponsiveVoice):
    uri = "CzechMaleAlt"
    name = "Czech Male"
    voiceIDs = []
    _raw = {'lang': 'cs', 'fallbackvoice': True, 'service': 'g3', 'voicename': '', 'gender': 'male', 'deprecated': True,
            'name': 'Czech Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Czech Male', service="g3")


class DanishMaleAlt(ResponsiveVoice):
    uri = "DanishMaleAlt"
    name = "Danish Male"
    voiceIDs = []
    _raw = {'lang': 'da', 'fallbackvoice': True, 'service': 'g3', 'voicename': '', 'gender': 'male', 'deprecated': True,
            'name': 'Danish Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Danish Male', service="g3")


class GreekMaleAlt(ResponsiveVoice):
    uri = "GreekMaleAlt"
    name = "Greek Male"
    voiceIDs = []
    _raw = {'lang': 'el', 'fallbackvoice': True, 'service': 'g3', 'voicename': '', 'gender': 'male', 'deprecated': True,
            'name': 'Greek Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Greek Male', service="g3")


class HungarianMaleAlt(ResponsiveVoice):
    uri = "HungarianMaleAlt"
    name = "Hungarian Male"
    voiceIDs = []
    _raw = {'lang': 'hu', 'fallbackvoice': True, 'service': 'g3', 'voicename': '', 'gender': 'male', 'deprecated': True,
            'name': 'Hungarian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Hungarian Male', service="g3")


class LatinMaleAlt(ResponsiveVoice):
    uri = "LatinMaleAlt"
    name = "Latin Male"
    voiceIDs = []
    _raw = {'lang': 'la', 'fallbackvoice': True, 'service': 'g2', 'voicename': '', 'gender': 'male',
            'name': 'Latin Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="la", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Latin Male', service="g2")


class NorwegianMaleAlt(ResponsiveVoice):
    uri = "NorwegianMaleAlt"
    name = "Norwegian Male"
    voiceIDs = []
    _raw = {'lang': 'no', 'fallbackvoice': True, 'service': 'g3', 'voicename': '', 'gender': 'male',
            'name': 'Norwegian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="no", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Norwegian Male', service="g3")


class SlovakMaleAlt(ResponsiveVoice):
    uri = "SlovakMaleAlt"
    name = "Slovak Male"
    voiceIDs = []
    _raw = {'lang': 'sk', 'fallbackvoice': True, 'service': 'g3', 'voicename': '', 'gender': 'male', 'deprecated': True,
            'name': 'Slovak Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Slovak Male', service="g3")


class SwedishMaleAlt(ResponsiveVoice):
    uri = "SwedishMaleAlt"
    name = "Swedish Male"
    voiceIDs = []
    _raw = {'lang': 'sv', 'fallbackvoice': True, 'service': 'g3', 'voicename': '', 'gender': 'male',
            'name': 'Swedish Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sv", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Swedish Male', service="g3")


class FallbackUsEnglishMale(ResponsiveVoice):
    uri = "FallbackUsEnglishMale"
    name = "Fallback US English Male"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'fallbackvoice': True, 'service': 'g3', 'voicename': '', 'gender': 'male',
            'name': 'Fallback US English Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback US English Male', service="g3")


class GermanGermany(ResponsiveVoice):
    uri = "GermanGermany"
    name = "German Germany"
    voiceIDs = []
    _raw = {'lang': 'de_DE', 'name': 'German Germany'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de_DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='German Germany', service="")


class EnglishUnitedKingdom(ResponsiveVoice):
    uri = "EnglishUnitedKingdom"
    name = "English United Kingdom"
    voiceIDs = []
    _raw = {'lang': 'en_GB', 'name': 'English United Kingdom'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en_GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='English United Kingdom', service="")


class EnglishIndia(ResponsiveVoice):
    uri = "EnglishIndia"
    name = "English India"
    voiceIDs = []
    _raw = {'lang': 'en_IN', 'name': 'English India'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en_IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='English India', service="")


class EnglishUnitedStates(ResponsiveVoice):
    uri = "EnglishUnitedStates"
    name = "English United States"
    voiceIDs = []
    _raw = {'lang': 'en_US', 'name': 'English United States'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en_US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='English United States', service="")


class SpanishSpain(ResponsiveVoice):
    uri = "SpanishSpain"
    name = "Spanish Spain"
    voiceIDs = []
    _raw = {'lang': 'es_ES', 'name': 'Spanish Spain'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es_ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Spanish Spain', service="")


class SpanishMexico(ResponsiveVoice):
    uri = "SpanishMexico"
    name = "Spanish Mexico"
    voiceIDs = []
    _raw = {'lang': 'es_MX', 'name': 'Spanish Mexico'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es_MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Spanish Mexico', service="")


class SpanishUnitedStates(ResponsiveVoice):
    uri = "SpanishUnitedStates"
    name = "Spanish United States"
    voiceIDs = []
    _raw = {'lang': 'es_US', 'name': 'Spanish United States'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es_US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Spanish United States', service="")


class FrenchBelgium(ResponsiveVoice):
    uri = "FrenchBelgium"
    name = "French Belgium"
    voiceIDs = []
    _raw = {'lang': 'fr_BE', 'name': 'French Belgium'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr_BE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='French Belgium', service="")


class FrenchFrance(ResponsiveVoice):
    uri = "FrenchFrance"
    name = "French France"
    voiceIDs = []
    _raw = {'lang': 'fr_FR', 'name': 'French France'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr_FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='French France', service="")


class HindiIndia(ResponsiveVoice):
    uri = "HindiIndia"
    name = "Hindi India"
    voiceIDs = []
    _raw = {'lang': 'hi_IN', 'name': 'Hindi India'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi_IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Hindi India', service="")


class IndonesianIndonesia(ResponsiveVoice):
    uri = "IndonesianIndonesia"
    name = "Indonesian Indonesia"
    voiceIDs = []
    _raw = {'lang': 'in_ID', 'name': 'Indonesian Indonesia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="in_ID", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Indonesian Indonesia', service="")


class ItalianItaly(ResponsiveVoice):
    uri = "ItalianItaly"
    name = "Italian Italy"
    voiceIDs = []
    _raw = {'lang': 'it_IT', 'name': 'Italian Italy'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it_IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Italian Italy', service="")


class JapaneseJapan(ResponsiveVoice):
    uri = "JapaneseJapan"
    name = "Japanese Japan"
    voiceIDs = []
    _raw = {'lang': 'ja_JP', 'name': 'Japanese Japan'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja_JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Japanese Japan', service="")


class KoreanSouthKorea(ResponsiveVoice):
    uri = "KoreanSouthKorea"
    name = "Korean South Korea"
    voiceIDs = []
    _raw = {'lang': 'ko_KR', 'name': 'Korean South Korea'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko_KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Korean South Korea', service="")


class DutchNetherlands(ResponsiveVoice):
    uri = "DutchNetherlands"
    name = "Dutch Netherlands"
    voiceIDs = []
    _raw = {'lang': 'nl_NL', 'name': 'Dutch Netherlands'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl_NL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Dutch Netherlands', service="")


class PolishPoland(ResponsiveVoice):
    uri = "PolishPoland"
    name = "Polish Poland"
    voiceIDs = []
    _raw = {'lang': 'pl_PL', 'name': 'Polish Poland'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl_PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Polish Poland', service="")


class PortugueseBrazil(ResponsiveVoice):
    uri = "PortugueseBrazil"
    name = "Portuguese Brazil"
    voiceIDs = []
    _raw = {'lang': 'pt_BR', 'name': 'Portuguese Brazil'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt_BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Portuguese Brazil', service="")


class PortuguesePortugal(ResponsiveVoice):
    uri = "PortuguesePortugal"
    name = "Portuguese Portugal"
    voiceIDs = []
    _raw = {'lang': 'pt_PT', 'name': 'Portuguese Portugal'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt_PT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Portuguese Portugal', service="")


class RussianRussia(ResponsiveVoice):
    uri = "RussianRussia"
    name = "Russian Russia"
    voiceIDs = []
    _raw = {'lang': 'ru_RU', 'name': 'Russian Russia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru_RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Russian Russia', service="")


class ThaiThailand(ResponsiveVoice):
    uri = "ThaiThailand"
    name = "Thai Thailand"
    voiceIDs = []
    _raw = {'lang': 'th_TH', 'name': 'Thai Thailand'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th_TH", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Thai Thailand', service="")


class TurkishTurkey(ResponsiveVoice):
    uri = "TurkishTurkey"
    name = "Turkish Turkey"
    voiceIDs = []
    _raw = {'lang': 'tr_TR', 'name': 'Turkish Turkey'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr_TR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Turkish Turkey', service="")


class ChineseChina(ResponsiveVoice):
    uri = "ChineseChina"
    name = "Chinese China"
    voiceIDs = []
    _raw = {'lang': 'zh_CN_#Hans', 'name': 'Chinese China'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh_CN_#Hans", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese China', service="")


class ChineseHongKong(ResponsiveVoice):
    uri = "ChineseHongKong"
    name = "Chinese Hong Kong"
    voiceIDs = []
    _raw = {'lang': 'zh_HK_#Hans', 'name': 'Chinese Hong Kong'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh_HK_#Hans", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese Hong Kong', service="")


class ChineseHongKongAlt(ResponsiveVoice):
    uri = "ChineseHongKongAlt"
    name = "Chinese Hong Kong"
    voiceIDs = []
    _raw = {'lang': 'zh_HK_#Hant', 'name': 'Chinese Hong Kong'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh_HK_#Hant", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese Hong Kong', service="")


class ChineseTaiwan(ResponsiveVoice):
    uri = "ChineseTaiwan"
    name = "Chinese Taiwan"
    voiceIDs = []
    _raw = {'lang': 'zh_TW_#Hant', 'name': 'Chinese Taiwan'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh_TW_#Hant", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese Taiwan', service="")


class Maged(ResponsiveVoice):
    uri = "Maged"
    name = "Maged"
    voiceIDs = []
    _raw = {'lang': 'ar-SA', 'name': 'Maged'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar-SA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Maged', service="")


class Zuzana(ResponsiveVoice):
    uri = "Zuzana"
    name = "Zuzana"
    voiceIDs = []
    _raw = {'lang': 'cs-CZ', 'name': 'Zuzana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs-CZ", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Zuzana', service="")


class Sara(ResponsiveVoice):
    uri = "Sara"
    name = "Sara"
    voiceIDs = []
    _raw = {'lang': 'da-DK', 'name': 'Sara'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da-DK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Sara', service="")


class Anna(ResponsiveVoice):
    uri = "Anna"
    name = "Anna"
    voiceIDs = []
    _raw = {'lang': 'de-DE', 'name': 'Anna'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Anna', service="")


class Melina(ResponsiveVoice):
    uri = "Melina"
    name = "Melina"
    voiceIDs = []
    _raw = {'lang': 'el-GR', 'name': 'Melina'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el-GR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Melina', service="")


class Karen(ResponsiveVoice):
    uri = "Karen"
    name = "Karen"
    voiceIDs = []
    _raw = {'lang': 'en-AU', 'name': 'Karen'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Karen', service="")


class Daniel(ResponsiveVoice):
    uri = "Daniel"
    name = "Daniel"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'name': 'Daniel'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Daniel', service="")


class Moira(ResponsiveVoice):
    uri = "Moira"
    name = "Moira"
    voiceIDs = []
    _raw = {'lang': 'en-IE', 'name': 'Moira'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Moira', service="")


class SamanthaEnhanced(ResponsiveVoice):
    uri = "SamanthaEnhanced"
    name = "Samantha (Enhanced)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'name': 'Samantha (Enhanced)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Samantha (Enhanced)', service="")


class Samantha(ResponsiveVoice):
    uri = "Samantha"
    name = "Samantha"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'name': 'Samantha'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Samantha', service="")


class Tessa(ResponsiveVoice):
    uri = "Tessa"
    name = "Tessa"
    voiceIDs = []
    _raw = {'lang': 'en-ZA', 'name': 'Tessa'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-ZA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Tessa', service="")


class Monica(ResponsiveVoice):
    uri = "Monica"
    name = "Monica"
    voiceIDs = []
    _raw = {'lang': 'es-ES', 'name': 'Monica'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Monica', service="")


class Paulina(ResponsiveVoice):
    uri = "Paulina"
    name = "Paulina"
    voiceIDs = []
    _raw = {'lang': 'es-MX', 'name': 'Paulina'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Paulina', service="")


class Satu(ResponsiveVoice):
    uri = "Satu"
    name = "Satu"
    voiceIDs = []
    _raw = {'lang': 'fi-FI', 'name': 'Satu'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi-FI", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Satu', service="")


class Amelie(ResponsiveVoice):
    uri = "Amelie"
    name = "Amelie"
    voiceIDs = []
    _raw = {'lang': 'fr-CA', 'name': 'Amelie'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-CA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Amelie', service="")


class Thomas(ResponsiveVoice):
    uri = "Thomas"
    name = "Thomas"
    voiceIDs = []
    _raw = {'lang': 'fr-FR', 'name': 'Thomas'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Thomas', service="")


class Carmit(ResponsiveVoice):
    uri = "Carmit"
    name = "Carmit"
    voiceIDs = []
    _raw = {'lang': 'he-IL', 'name': 'Carmit'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="he-IL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Carmit', service="")


class Lekha(ResponsiveVoice):
    uri = "Lekha"
    name = "Lekha"
    voiceIDs = []
    _raw = {'lang': 'hi-IN', 'name': 'Lekha'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Lekha', service="")


class Mariska(ResponsiveVoice):
    uri = "Mariska"
    name = "Mariska"
    voiceIDs = []
    _raw = {'lang': 'hu-HU', 'name': 'Mariska'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu-HU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Mariska', service="")


class Damayanti(ResponsiveVoice):
    uri = "Damayanti"
    name = "Damayanti"
    voiceIDs = []
    _raw = {'lang': 'id-ID', 'name': 'Damayanti'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id-ID", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Damayanti', service="")


class Alice(ResponsiveVoice):
    uri = "Alice"
    name = "Alice"
    voiceIDs = []
    _raw = {'lang': 'it-IT', 'name': 'Alice'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Alice', service="")


class Kyoko(ResponsiveVoice):
    uri = "Kyoko"
    name = "Kyoko"
    voiceIDs = []
    _raw = {'lang': 'ja-JP', 'name': 'Kyoko'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Kyoko', service="")


class Yuna(ResponsiveVoice):
    uri = "Yuna"
    name = "Yuna"
    voiceIDs = []
    _raw = {'lang': 'ko-KR', 'name': 'Yuna'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Yuna', service="")


class Ellen(ResponsiveVoice):
    uri = "Ellen"
    name = "Ellen"
    voiceIDs = []
    _raw = {'lang': 'nl-BE', 'name': 'Ellen'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-BE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ellen', service="")


class Xander(ResponsiveVoice):
    uri = "Xander"
    name = "Xander"
    voiceIDs = []
    _raw = {'lang': 'nl-NL', 'name': 'Xander'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-NL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Xander', service="")


class Nora(ResponsiveVoice):
    uri = "Nora"
    name = "Nora"
    voiceIDs = []
    _raw = {'lang': 'no-NO', 'name': 'Nora'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="no-NO", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Nora', service="")


class Zosia(ResponsiveVoice):
    uri = "Zosia"
    name = "Zosia"
    voiceIDs = []
    _raw = {'lang': 'pl-PL', 'name': 'Zosia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Zosia', service="")


class Luciana(ResponsiveVoice):
    uri = "Luciana"
    name = "Luciana"
    voiceIDs = []
    _raw = {'lang': 'pt-BR', 'name': 'Luciana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Luciana', service="")


class Joana(ResponsiveVoice):
    uri = "Joana"
    name = "Joana"
    voiceIDs = []
    _raw = {'lang': 'pt-PT', 'name': 'Joana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-PT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Joana', service="")


class Ioana(ResponsiveVoice):
    uri = "Ioana"
    name = "Ioana"
    voiceIDs = []
    _raw = {'lang': 'ro-RO', 'name': 'Ioana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ro-RO", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ioana', service="")


class Milena(ResponsiveVoice):
    uri = "Milena"
    name = "Milena"
    voiceIDs = []
    _raw = {'lang': 'ru-RU', 'name': 'Milena'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Milena', service="")


class Laura(ResponsiveVoice):
    uri = "Laura"
    name = "Laura"
    voiceIDs = []
    _raw = {'lang': 'sk-SK', 'name': 'Laura'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk-SK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Laura', service="")


class Alva(ResponsiveVoice):
    uri = "Alva"
    name = "Alva"
    voiceIDs = []
    _raw = {'lang': 'sv-SE', 'name': 'Alva'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sv-SE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Alva', service="")


class Kanya(ResponsiveVoice):
    uri = "Kanya"
    name = "Kanya"
    voiceIDs = []
    _raw = {'lang': 'th-TH', 'name': 'Kanya'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th-TH", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Kanya', service="")


class Yelda(ResponsiveVoice):
    uri = "Yelda"
    name = "Yelda"
    voiceIDs = []
    _raw = {'lang': 'tr-TR', 'name': 'Yelda'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr-TR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Yelda', service="")


class Tingting(ResponsiveVoice):
    uri = "Tingting"
    name = "Ting-Ting"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Ting-Ting'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ting-Ting', service="")


class Sinji(ResponsiveVoice):
    uri = "Sinji"
    name = "Sin-Ji"
    voiceIDs = []
    _raw = {'lang': 'zh-HK', 'name': 'Sin-Ji'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Sin-Ji', service="")


class Meijia(ResponsiveVoice):
    uri = "Meijia"
    name = "Mei-Jia"
    voiceIDs = []
    _raw = {'lang': 'zh-TW', 'name': 'Mei-Jia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Mei-Jia', service="")


class MicrosoftDavidMobileEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftDavidMobileEnglishUnitedStates"
    name = "Microsoft David Mobile - English (United States)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'name': 'Microsoft David Mobile - English (United States)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft David Mobile - English (United States)', service="")


class MicrosoftZiraMobileEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftZiraMobileEnglishUnitedStates"
    name = "Microsoft Zira Mobile - English (United States)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'name': 'Microsoft Zira Mobile - English (United States)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Zira Mobile - English (United States)', service="")


class MicrosoftMarkMobileEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftMarkMobileEnglishUnitedStates"
    name = "Microsoft Mark Mobile - English (United States)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'name': 'Microsoft Mark Mobile - English (United States)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Mark Mobile - English (United States)', service="")


class FallbackChineseHongKongFemale(ResponsiveVoice):
    uri = "FallbackChineseHongKongFemale"
    name = "Fallback Chinese (Hong Kong) Female"
    voiceIDs = []
    _raw = {'lang': 'zh-HK', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female',
            'name': 'Fallback Chinese (Hong Kong) Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Chinese (Hong Kong) Female', service="g1")


class FallbackChineseTaiwanFemale(ResponsiveVoice):
    uri = "FallbackChineseTaiwanFemale"
    name = "Fallback Chinese (Taiwan) Female"
    voiceIDs = []
    _raw = {'lang': 'zh-TW', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female',
            'name': 'Fallback Chinese (Taiwan) Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Chinese (Taiwan) Female', service="g1")


class MicrosoftGeorgeMobileEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftGeorgeMobileEnglishUnitedKingdom"
    name = "Microsoft George Mobile - English (United Kingdom)"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'name': 'Microsoft George Mobile - English (United Kingdom)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft George Mobile - English (United Kingdom)', service="")


class MicrosoftSusanMobileEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftSusanMobileEnglishUnitedKingdom"
    name = "Microsoft Susan Mobile - English (United Kingdom)"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'name': 'Microsoft Susan Mobile - English (United Kingdom)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Susan Mobile - English (United Kingdom)', service="")


class MicrosoftHazelMobileEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftHazelMobileEnglishUnitedKingdom"
    name = "Microsoft Hazel Mobile - English (United Kingdom)"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'name': 'Microsoft Hazel Mobile - English (United Kingdom)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Hazel Mobile - English (United Kingdom)', service="")


class MicrosoftHeeraMobileEnglishIndia(ResponsiveVoice):
    uri = "MicrosoftHeeraMobileEnglishIndia"
    name = "Microsoft Heera Mobile - English (India)"
    voiceIDs = []
    _raw = {'lang': 'en-In', 'name': 'Microsoft Heera Mobile - English (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-In", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Heera Mobile - English (India)', service="")


class MicrosoftIrinaMobileRussianRussia(ResponsiveVoice):
    uri = "MicrosoftIrinaMobileRussianRussia"
    name = "Microsoft Irina Mobile - Russian (Russia)"
    voiceIDs = []
    _raw = {'lang': 'ru-RU', 'name': 'Microsoft Irina Mobile - Russian (Russia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Irina Mobile - Russian (Russia)', service="")


class MicrosoftHeddaMobileGermanGermany(ResponsiveVoice):
    uri = "MicrosoftHeddaMobileGermanGermany"
    name = "Microsoft Hedda Mobile - German (Germany)"
    voiceIDs = []
    _raw = {'lang': 'de-DE', 'name': 'Microsoft Hedda Mobile - German (Germany)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Hedda Mobile - German (Germany)', service="")


class MicrosoftKatjaMobileGermanGermany(ResponsiveVoice):
    uri = "MicrosoftKatjaMobileGermanGermany"
    name = "Microsoft Katja Mobile - German (Germany)"
    voiceIDs = []
    _raw = {'lang': 'de-DE', 'name': 'Microsoft Katja Mobile - German (Germany)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Katja Mobile - German (Germany)', service="")


class MicrosoftHelenaMobileSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftHelenaMobileSpanishSpain"
    name = "Microsoft Helena Mobile - Spanish (Spain)"
    voiceIDs = []
    _raw = {'lang': 'es-ES', 'name': 'Microsoft Helena Mobile - Spanish (Spain)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Helena Mobile - Spanish (Spain)', service="")


class MicrosoftLauraMobileSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftLauraMobileSpanishSpain"
    name = "Microsoft Laura Mobile - Spanish (Spain)"
    voiceIDs = []
    _raw = {'lang': 'es-ES', 'name': 'Microsoft Laura Mobile - Spanish (Spain)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Laura Mobile - Spanish (Spain)', service="")


class MicrosoftSabinaMobileSpanishMexico(ResponsiveVoice):
    uri = "MicrosoftSabinaMobileSpanishMexico"
    name = "Microsoft Sabina Mobile - Spanish (Mexico)"
    voiceIDs = []
    _raw = {'lang': 'es-MX', 'name': 'Microsoft Sabina Mobile - Spanish (Mexico)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Sabina Mobile - Spanish (Mexico)', service="")


class MicrosoftJulieMobileFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftJulieMobileFrenchFrance"
    name = "Microsoft Julie Mobile - French (France)"
    voiceIDs = []
    _raw = {'lang': 'fr-FR', 'name': 'Microsoft Julie Mobile - French (France)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Julie Mobile - French (France)', service="")


class MicrosoftPaulinaMobilePolishPoland(ResponsiveVoice):
    uri = "MicrosoftPaulinaMobilePolishPoland"
    name = "Microsoft Paulina Mobile - Polish (Poland)"
    voiceIDs = []
    _raw = {'lang': 'pl-PL', 'name': 'Microsoft Paulina Mobile - Polish (Poland)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Paulina Mobile - Polish (Poland)', service="")


class MicrosoftHuihuiMobileChineseSimplifiedPrc(ResponsiveVoice):
    uri = "MicrosoftHuihuiMobileChineseSimplifiedPrc"
    name = "Microsoft Huihui Mobile - Chinese (Simplified PRC)"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Microsoft Huihui Mobile - Chinese (Simplified PRC)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Huihui Mobile - Chinese (Simplified PRC)', service="")


class MicrosoftYaoyaoMobileChineseSimplifiedPrc(ResponsiveVoice):
    uri = "MicrosoftYaoyaoMobileChineseSimplifiedPrc"
    name = "Microsoft Yaoyao Mobile - Chinese (Simplified PRC)"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Microsoft Yaoyao Mobile - Chinese (Simplified PRC)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Yaoyao Mobile - Chinese (Simplified PRC)', service="")


class MicrosoftTracyMobileChineseTraditionalHongKongSAR(ResponsiveVoice):
    uri = "MicrosoftTracyMobileChineseTraditionalHongKongSAR"
    name = "Microsoft Tracy Mobile - Chinese (Traditional Hong Kong S.A.R.)"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Microsoft Tracy Mobile - Chinese (Traditional Hong Kong S.A.R.)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Tracy Mobile - Chinese (Traditional Hong Kong S.A.R.)', service="")


class MicrosoftElsaMobileItalianItaly(ResponsiveVoice):
    uri = "MicrosoftElsaMobileItalianItaly"
    name = "Microsoft Elsa Mobile - Italian (Italy)"
    voiceIDs = []
    _raw = {'lang': 'it-IT', 'name': 'Microsoft Elsa Mobile - Italian (Italy)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Elsa Mobile - Italian (Italy)', service="")


class MicrosoftMariaMobilePortugueseBrazil(ResponsiveVoice):
    uri = "MicrosoftMariaMobilePortugueseBrazil"
    name = "Microsoft Maria Mobile - Portuguese (Brazil)"
    voiceIDs = []
    _raw = {'lang': 'pt-BR', 'name': 'Microsoft Maria Mobile - Portuguese (Brazil)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Maria Mobile - Portuguese (Brazil)', service="")


class MicrosoftAyumiMobileJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftAyumiMobileJapaneseJapan"
    name = "Microsoft Ayumi Mobile - Japanese (Japan)"
    voiceIDs = []
    _raw = {'lang': 'ja-JP', 'name': 'Microsoft Ayumi Mobile - Japanese (Japan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Ayumi Mobile - Japanese (Japan)', service="")


class MicrosoftHarukaMobileJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftHarukaMobileJapaneseJapan"
    name = "Microsoft Haruka Mobile - Japanese (Japan)"
    voiceIDs = []
    _raw = {'lang': 'ja-JP', 'name': 'Microsoft Haruka Mobile - Japanese (Japan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Haruka Mobile - Japanese (Japan)', service="")


class Helena(ResponsiveVoice):
    uri = "Helena"
    name = "Helena"
    voiceIDs = []
    _raw = {'lang': 'de-DE', 'name': 'Helena'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Helena', service="")


class Catherine(ResponsiveVoice):
    uri = "Catherine"
    name = "Catherine"
    voiceIDs = []
    _raw = {'lang': 'en-AU', 'name': 'Catherine'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Catherine', service="")


class Arthur(ResponsiveVoice):
    uri = "Arthur"
    name = "Arthur"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'name': 'Arthur'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Arthur', service="")


class Martha(ResponsiveVoice):
    uri = "Martha"
    name = "Martha"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'name': 'Martha'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Martha', service="")


class Marie(ResponsiveVoice):
    uri = "Marie"
    name = "Marie"
    voiceIDs = []
    _raw = {'lang': 'fr-FR', 'name': 'Marie'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Marie', service="")


class Oren(ResponsiveVoice):
    uri = "Oren"
    name = "O-ren"
    voiceIDs = []
    _raw = {'lang': 'ja-JP', 'name': 'O-ren'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='O-ren', service="")


class Yushu(ResponsiveVoice):
    uri = "Yushu"
    name = "Yu-shu"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Yu-shu'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Yu-shu', service="")


class MicrosoftDavidEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftDavidEnglishUnitedStates"
    name = "Microsoft David - English (United States)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'name': 'Microsoft David - English (United States)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft David - English (United States)', service="")


class MicrosoftZiraEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftZiraEnglishUnitedStates"
    name = "Microsoft Zira - English (United States)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'name': 'Microsoft Zira - English (United States)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Zira - English (United States)', service="")


class MicrosoftMarkEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftMarkEnglishUnitedStates"
    name = "Microsoft Mark - English (United States)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'name': 'Microsoft Mark - English (United States)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Mark - English (United States)', service="")


class MicrosoftGeorgeEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftGeorgeEnglishUnitedKingdom"
    name = "Microsoft George - English (United Kingdom)"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'name': 'Microsoft George - English (United Kingdom)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft George - English (United Kingdom)', service="")


class MicrosoftSusanEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftSusanEnglishUnitedKingdom"
    name = "Microsoft Susan - English (United Kingdom)"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'name': 'Microsoft Susan - English (United Kingdom)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Susan - English (United Kingdom)', service="")


class MicrosoftHazelEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftHazelEnglishUnitedKingdom"
    name = "Microsoft Hazel - English (United Kingdom)"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'name': 'Microsoft Hazel - English (United Kingdom)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Hazel - English (United Kingdom)', service="")


class MicrosoftHeeraEnglishIndia(ResponsiveVoice):
    uri = "MicrosoftHeeraEnglishIndia"
    name = "Microsoft Heera - English (India)"
    voiceIDs = []
    _raw = {'lang': 'en-In', 'name': 'Microsoft Heera - English (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-In", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Heera - English (India)', service="")


class MicrosoftIrinaRussianRussia(ResponsiveVoice):
    uri = "MicrosoftIrinaRussianRussia"
    name = "Microsoft Irina - Russian (Russia)"
    voiceIDs = []
    _raw = {'lang': 'ru-RU', 'name': 'Microsoft Irina - Russian (Russia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Irina - Russian (Russia)', service="")


class MicrosoftHeddaGermanGermany(ResponsiveVoice):
    uri = "MicrosoftHeddaGermanGermany"
    name = "Microsoft Hedda - German (Germany)"
    voiceIDs = []
    _raw = {'lang': 'de-DE', 'name': 'Microsoft Hedda - German (Germany)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Hedda - German (Germany)', service="")


class MicrosoftKatjaGermanGermany(ResponsiveVoice):
    uri = "MicrosoftKatjaGermanGermany"
    name = "Microsoft Katja - German (Germany)"
    voiceIDs = []
    _raw = {'lang': 'de-DE', 'name': 'Microsoft Katja - German (Germany)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Katja - German (Germany)', service="")


class MicrosoftHelenaSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftHelenaSpanishSpain"
    name = "Microsoft Helena - Spanish (Spain)"
    voiceIDs = []
    _raw = {'lang': 'es-ES', 'name': 'Microsoft Helena - Spanish (Spain)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Helena - Spanish (Spain)', service="")


class MicrosoftLauraSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftLauraSpanishSpain"
    name = "Microsoft Laura - Spanish (Spain)"
    voiceIDs = []
    _raw = {'lang': 'es-ES', 'name': 'Microsoft Laura - Spanish (Spain)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Laura - Spanish (Spain)', service="")


class MicrosoftSabinaSpanishMexico(ResponsiveVoice):
    uri = "MicrosoftSabinaSpanishMexico"
    name = "Microsoft Sabina - Spanish (Mexico)"
    voiceIDs = []
    _raw = {'lang': 'es-MX', 'name': 'Microsoft Sabina - Spanish (Mexico)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Sabina - Spanish (Mexico)', service="")


class MicrosoftJulieFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftJulieFrenchFrance"
    name = "Microsoft Julie - French (France)"
    voiceIDs = []
    _raw = {'lang': 'fr-FR', 'name': 'Microsoft Julie - French (France)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Julie - French (France)', service="")


class MicrosoftPaulinaPolishPoland(ResponsiveVoice):
    uri = "MicrosoftPaulinaPolishPoland"
    name = "Microsoft Paulina - Polish (Poland)"
    voiceIDs = []
    _raw = {'lang': 'pl-PL', 'name': 'Microsoft Paulina - Polish (Poland)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Paulina - Polish (Poland)', service="")


class MicrosoftHuihuiChineseSimplifiedPrc(ResponsiveVoice):
    uri = "MicrosoftHuihuiChineseSimplifiedPrc"
    name = "Microsoft Huihui - Chinese (Simplified PRC)"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Microsoft Huihui - Chinese (Simplified PRC)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Huihui - Chinese (Simplified PRC)', service="")


class MicrosoftYaoyaoChineseSimplifiedPrc(ResponsiveVoice):
    uri = "MicrosoftYaoyaoChineseSimplifiedPrc"
    name = "Microsoft Yaoyao - Chinese (Simplified PRC)"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Microsoft Yaoyao - Chinese (Simplified PRC)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Yaoyao - Chinese (Simplified PRC)', service="")


class MicrosoftTracyChineseTraditionalHongKongSAR(ResponsiveVoice):
    uri = "MicrosoftTracyChineseTraditionalHongKongSAR"
    name = "Microsoft Tracy - Chinese (Traditional Hong Kong S.A.R.)"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Microsoft Tracy - Chinese (Traditional Hong Kong S.A.R.)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Tracy - Chinese (Traditional Hong Kong S.A.R.)', service="")


class MicrosoftElsaItalianItaly(ResponsiveVoice):
    uri = "MicrosoftElsaItalianItaly"
    name = "Microsoft Elsa - Italian (Italy)"
    voiceIDs = []
    _raw = {'lang': 'it-IT', 'name': 'Microsoft Elsa - Italian (Italy)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Elsa - Italian (Italy)', service="")


class MicrosoftMariaPortugueseBrazil(ResponsiveVoice):
    uri = "MicrosoftMariaPortugueseBrazil"
    name = "Microsoft Maria - Portuguese (Brazil)"
    voiceIDs = []
    _raw = {'lang': 'pt-BR', 'name': 'Microsoft Maria - Portuguese (Brazil)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Maria - Portuguese (Brazil)', service="")


class MicrosoftAyumiJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftAyumiJapaneseJapan"
    name = "Microsoft Ayumi - Japanese (Japan)"
    voiceIDs = []
    _raw = {'lang': 'ja-JP', 'name': 'Microsoft Ayumi - Japanese (Japan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Ayumi - Japanese (Japan)', service="")


class MicrosoftHarukaJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftHarukaJapaneseJapan"
    name = "Microsoft Haruka - Japanese (Japan)"
    voiceIDs = []
    _raw = {'lang': 'ja-JP', 'name': 'Microsoft Haruka - Japanese (Japan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Haruka - Japanese (Japan)', service="")


class MicrosoftHortenseFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftHortenseFrenchFrance"
    name = "Microsoft Hortense - French (France)"
    voiceIDs = []
    _raw = {'lang': 'fr-FR', 'name': 'Microsoft Hortense - French (France)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Hortense - French (France)', service="")


class MicrosoftHanhanChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftHanhanChineseTraditionalTaiwan"
    name = "Microsoft Hanhan - Chinese (Traditional Taiwan)"
    voiceIDs = []
    _raw = {'lang': 'zh-TW', 'name': 'Microsoft Hanhan - Chinese (Traditional Taiwan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Hanhan - Chinese (Traditional Taiwan)', service="")


class MicrosoftHeamiKoreanKorean(ResponsiveVoice):
    uri = "MicrosoftHeamiKoreanKorean"
    name = "Microsoft Heami - Korean (Korean)"
    voiceIDs = []
    _raw = {'lang': 'ko-KR', 'name': 'Microsoft Heami - Korean (Korean)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Heami - Korean (Korean)', service="")


class MicrosoftStefanGermanGermany(ResponsiveVoice):
    uri = "MicrosoftStefanGermanGermany"
    name = "Microsoft Stefan - German (Germany)"
    voiceIDs = []
    _raw = {'lang': 'de-DE', 'name': 'Microsoft Stefan - German (Germany)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Stefan - German (Germany)', service="")


class MicrosoftRaviEnglishIndia(ResponsiveVoice):
    uri = "MicrosoftRaviEnglishIndia"
    name = "Microsoft Ravi - English (India)"
    voiceIDs = []
    _raw = {'lang': 'en-IN', 'name': 'Microsoft Ravi - English (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Ravi - English (India)', service="")


class MicrosoftPabloSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftPabloSpanishSpain"
    name = "Microsoft Pablo - Spanish (Spain)"
    voiceIDs = []
    _raw = {'lang': 'es-ES', 'name': 'Microsoft Pablo - Spanish (Spain)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Pablo - Spanish (Spain)', service="")


class MicrosoftRaulSpanishMexico(ResponsiveVoice):
    uri = "MicrosoftRaulSpanishMexico"
    name = "Microsoft Raul - Spanish (Mexico)"
    voiceIDs = []
    _raw = {'lang': 'es-MX', 'name': 'Microsoft Raul - Spanish (Mexico)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Raul - Spanish (Mexico)', service="")


class MicrosoftPaulFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftPaulFrenchFrance"
    name = "Microsoft Paul - French (France)"
    voiceIDs = []
    _raw = {'lang': 'fr-FR', 'name': 'Microsoft Paul - French (France)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Paul - French (France)', service="")


class MicrosoftCosimoItalianItaly(ResponsiveVoice):
    uri = "MicrosoftCosimoItalianItaly"
    name = "Microsoft Cosimo - Italian (Italy)"
    voiceIDs = []
    _raw = {'lang': 'it-IT', 'name': 'Microsoft Cosimo - Italian (Italy)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Cosimo - Italian (Italy)', service="")


class MicrosoftIchiroJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftIchiroJapaneseJapan"
    name = "Microsoft Ichiro - Japanese (Japan)"
    voiceIDs = []
    _raw = {'lang': 'ja-JP', 'name': 'Microsoft Ichiro - Japanese (Japan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Ichiro - Japanese (Japan)', service="")


class MicrosoftAdamPolishPoland(ResponsiveVoice):
    uri = "MicrosoftAdamPolishPoland"
    name = "Microsoft Adam - Polish (Poland)"
    voiceIDs = []
    _raw = {'lang': 'pl-PL', 'name': 'Microsoft Adam - Polish (Poland)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Adam - Polish (Poland)', service="")


class MicrosoftDanielPortugueseBrazil(ResponsiveVoice):
    uri = "MicrosoftDanielPortugueseBrazil"
    name = "Microsoft Daniel - Portuguese (Brazil)"
    voiceIDs = []
    _raw = {'lang': 'pt-BR', 'name': 'Microsoft Daniel - Portuguese (Brazil)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Daniel - Portuguese (Brazil)', service="")


class MicrosoftPavelRussianRussia(ResponsiveVoice):
    uri = "MicrosoftPavelRussianRussia"
    name = "Microsoft Pavel - Russian (Russia)"
    voiceIDs = []
    _raw = {'lang': 'ru-RU', 'name': 'Microsoft Pavel - Russian (Russia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Pavel - Russian (Russia)', service="")


class MicrosoftKangkangChineseSimplifiedPrc(ResponsiveVoice):
    uri = "MicrosoftKangkangChineseSimplifiedPrc"
    name = "Microsoft Kangkang - Chinese (Simplified PRC)"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Microsoft Kangkang - Chinese (Simplified PRC)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Kangkang - Chinese (Simplified PRC)', service="")


class MicrosoftDannyChineseTraditionalHongKongSAR(ResponsiveVoice):
    uri = "MicrosoftDannyChineseTraditionalHongKongSAR"
    name = "Microsoft Danny - Chinese (Traditional Hong Kong S.A.R.)"
    voiceIDs = []
    _raw = {'lang': 'zh-HK', 'name': 'Microsoft Danny - Chinese (Traditional Hong Kong S.A.R.)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Danny - Chinese (Traditional Hong Kong S.A.R.)', service="")


class MicrosoftYatingChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftYatingChineseTraditionalTaiwan"
    name = "Microsoft Yating - Chinese (Traditional Taiwan)"
    voiceIDs = []
    _raw = {'lang': 'zh-TW', 'name': 'Microsoft Yating - Chinese (Traditional Taiwan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Yating - Chinese (Traditional Taiwan)', service="")


class MicrosoftZhiweiChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftZhiweiChineseTraditionalTaiwan"
    name = "Microsoft Zhiwei - Chinese (Traditional Taiwan)"
    voiceIDs = []
    _raw = {'lang': 'zh-TW', 'name': 'Microsoft Zhiwei - Chinese (Traditional Taiwan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Zhiwei - Chinese (Traditional Taiwan)', service="")


class MicrosoftHortenseMobileFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftHortenseMobileFrenchFrance"
    name = "Microsoft Hortense Mobile - French (France)"
    voiceIDs = []
    _raw = {'lang': 'fr-FR', 'name': 'Microsoft Hortense Mobile - French (France)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Hortense Mobile - French (France)', service="")


class MicrosoftHanhanMobileChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftHanhanMobileChineseTraditionalTaiwan"
    name = "Microsoft Hanhan Mobile - Chinese (Traditional Taiwan)"
    voiceIDs = []
    _raw = {'lang': 'zh-TW', 'name': 'Microsoft Hanhan Mobile - Chinese (Traditional Taiwan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Hanhan Mobile - Chinese (Traditional Taiwan)', service="")


class MicrosoftHeamiMobileKoreanKorean(ResponsiveVoice):
    uri = "MicrosoftHeamiMobileKoreanKorean"
    name = "Microsoft Heami Mobile - Korean (Korean)"
    voiceIDs = []
    _raw = {'lang': 'ko-KR', 'name': 'Microsoft Heami Mobile - Korean (Korean)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Heami Mobile - Korean (Korean)', service="")


class MicrosoftStefanMobileGermanGermany(ResponsiveVoice):
    uri = "MicrosoftStefanMobileGermanGermany"
    name = "Microsoft Stefan Mobile - German (Germany)"
    voiceIDs = []
    _raw = {'lang': 'de-DE', 'name': 'Microsoft Stefan Mobile - German (Germany)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Stefan Mobile - German (Germany)', service="")


class MicrosoftRaviMobileEnglishIndia(ResponsiveVoice):
    uri = "MicrosoftRaviMobileEnglishIndia"
    name = "Microsoft Ravi Mobile - English (India)"
    voiceIDs = []
    _raw = {'lang': 'en-IN', 'name': 'Microsoft Ravi Mobile - English (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Ravi Mobile - English (India)', service="")


class MicrosoftPabloMobileSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftPabloMobileSpanishSpain"
    name = "Microsoft Pablo Mobile - Spanish (Spain)"
    voiceIDs = []
    _raw = {'lang': 'es-ES', 'name': 'Microsoft Pablo Mobile - Spanish (Spain)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Pablo Mobile - Spanish (Spain)', service="")


class MicrosoftRaulMobileSpanishMexico(ResponsiveVoice):
    uri = "MicrosoftRaulMobileSpanishMexico"
    name = "Microsoft Raul Mobile - Spanish (Mexico)"
    voiceIDs = []
    _raw = {'lang': 'es-MX', 'name': 'Microsoft Raul Mobile - Spanish (Mexico)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Raul Mobile - Spanish (Mexico)', service="")


class MicrosoftPaulMobileFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftPaulMobileFrenchFrance"
    name = "Microsoft Paul Mobile - French (France)"
    voiceIDs = []
    _raw = {'lang': 'fr-FR', 'name': 'Microsoft Paul Mobile - French (France)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Paul Mobile - French (France)', service="")


class MicrosoftCosimoMobileItalianItaly(ResponsiveVoice):
    uri = "MicrosoftCosimoMobileItalianItaly"
    name = "Microsoft Cosimo Mobile - Italian (Italy)"
    voiceIDs = []
    _raw = {'lang': 'it-IT', 'name': 'Microsoft Cosimo Mobile - Italian (Italy)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Cosimo Mobile - Italian (Italy)', service="")


class MicrosoftIchiroMobileJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftIchiroMobileJapaneseJapan"
    name = "Microsoft Ichiro Mobile - Japanese (Japan)"
    voiceIDs = []
    _raw = {'lang': 'ja-JP', 'name': 'Microsoft Ichiro Mobile - Japanese (Japan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Ichiro Mobile - Japanese (Japan)', service="")


class MicrosoftAdamMobilePolishPoland(ResponsiveVoice):
    uri = "MicrosoftAdamMobilePolishPoland"
    name = "Microsoft Adam Mobile - Polish (Poland)"
    voiceIDs = []
    _raw = {'lang': 'pl-PL', 'name': 'Microsoft Adam Mobile - Polish (Poland)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Adam Mobile - Polish (Poland)', service="")


class MicrosoftDanielMobilePortugueseBrazil(ResponsiveVoice):
    uri = "MicrosoftDanielMobilePortugueseBrazil"
    name = "Microsoft Daniel Mobile - Portuguese (Brazil)"
    voiceIDs = []
    _raw = {'lang': 'pt-BR', 'name': 'Microsoft Daniel Mobile - Portuguese (Brazil)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Daniel Mobile - Portuguese (Brazil)', service="")


class MicrosoftPavelMobileRussianRussia(ResponsiveVoice):
    uri = "MicrosoftPavelMobileRussianRussia"
    name = "Microsoft Pavel Mobile - Russian (Russia)"
    voiceIDs = []
    _raw = {'lang': 'ru-RU', 'name': 'Microsoft Pavel Mobile - Russian (Russia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Pavel Mobile - Russian (Russia)', service="")


class MicrosoftKangkangMobileChineseSimplifiedPrc(ResponsiveVoice):
    uri = "MicrosoftKangkangMobileChineseSimplifiedPrc"
    name = "Microsoft Kangkang Mobile - Chinese (Simplified PRC)"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Microsoft Kangkang Mobile - Chinese (Simplified PRC)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Kangkang Mobile - Chinese (Simplified PRC)', service="")


class MicrosoftDannyMobileChineseTraditionalHongKongSAR(ResponsiveVoice):
    uri = "MicrosoftDannyMobileChineseTraditionalHongKongSAR"
    name = "Microsoft Danny Mobile - Chinese (Traditional Hong Kong S.A.R.)"
    voiceIDs = []
    _raw = {'lang': 'zh-HK', 'name': 'Microsoft Danny Mobile - Chinese (Traditional Hong Kong S.A.R.)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Danny Mobile - Chinese (Traditional Hong Kong S.A.R.)', service="")


class MicrosoftYatingMobileChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftYatingMobileChineseTraditionalTaiwan"
    name = "Microsoft Yating Mobile - Chinese (Traditional Taiwan)"
    voiceIDs = []
    _raw = {'lang': 'zh-TW', 'name': 'Microsoft Yating Mobile - Chinese (Traditional Taiwan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Yating Mobile - Chinese (Traditional Taiwan)', service="")


class MicrosoftZhiweiMobileChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftZhiweiMobileChineseTraditionalTaiwan"
    name = "Microsoft Zhiwei Mobile - Chinese (Traditional Taiwan)"
    voiceIDs = []
    _raw = {'lang': 'zh-TW', 'name': 'Microsoft Zhiwei Mobile - Chinese (Traditional Taiwan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Zhiwei Mobile - Chinese (Traditional Taiwan)', service="")


class MicrosoftDavidDesktopEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftDavidDesktopEnglishUnitedStates"
    name = "Microsoft David Desktop - English (United States)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'name': 'Microsoft David Desktop - English (United States)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft David Desktop - English (United States)', service="")


class MicrosoftZiraDesktopEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftZiraDesktopEnglishUnitedStates"
    name = "Microsoft Zira Desktop - English (United States)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'name': 'Microsoft Zira Desktop - English (United States)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Zira Desktop - English (United States)', service="")


class MicrosoftMarkDesktopEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftMarkDesktopEnglishUnitedStates"
    name = "Microsoft Mark Desktop - English (United States)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'name': 'Microsoft Mark Desktop - English (United States)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Mark Desktop - English (United States)', service="")


class MicrosoftGeorgeDesktopEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftGeorgeDesktopEnglishUnitedKingdom"
    name = "Microsoft George Desktop - English (United Kingdom)"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'name': 'Microsoft George Desktop - English (United Kingdom)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft George Desktop - English (United Kingdom)', service="")


class MicrosoftSusanDesktopEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftSusanDesktopEnglishUnitedKingdom"
    name = "Microsoft Susan Desktop - English (United Kingdom)"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'name': 'Microsoft Susan Desktop - English (United Kingdom)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Susan Desktop - English (United Kingdom)', service="")


class MicrosoftHazelDesktopEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftHazelDesktopEnglishUnitedKingdom"
    name = "Microsoft Hazel Desktop - English (United Kingdom)"
    voiceIDs = []
    _raw = {'lang': 'en-GB', 'name': 'Microsoft Hazel Desktop - English (United Kingdom)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Hazel Desktop - English (United Kingdom)', service="")


class MicrosoftHeeraDesktopEnglishIndia(ResponsiveVoice):
    uri = "MicrosoftHeeraDesktopEnglishIndia"
    name = "Microsoft Heera Desktop - English (India)"
    voiceIDs = []
    _raw = {'lang': 'en-In', 'name': 'Microsoft Heera Desktop - English (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-In", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Heera Desktop - English (India)', service="")


class MicrosoftIrinaDesktopRussianRussia(ResponsiveVoice):
    uri = "MicrosoftIrinaDesktopRussianRussia"
    name = "Microsoft Irina Desktop - Russian (Russia)"
    voiceIDs = []
    _raw = {'lang': 'ru-RU', 'name': 'Microsoft Irina Desktop - Russian (Russia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Irina Desktop - Russian (Russia)', service="")


class MicrosoftHeddaDesktopGermanGermany(ResponsiveVoice):
    uri = "MicrosoftHeddaDesktopGermanGermany"
    name = "Microsoft Hedda Desktop - German (Germany)"
    voiceIDs = []
    _raw = {'lang': 'de-DE', 'name': 'Microsoft Hedda Desktop - German (Germany)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Hedda Desktop - German (Germany)', service="")


class MicrosoftKatjaDesktopGermanGermany(ResponsiveVoice):
    uri = "MicrosoftKatjaDesktopGermanGermany"
    name = "Microsoft Katja Desktop - German (Germany)"
    voiceIDs = []
    _raw = {'lang': 'de-DE', 'name': 'Microsoft Katja Desktop - German (Germany)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Katja Desktop - German (Germany)', service="")


class MicrosoftHelenaDesktopSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftHelenaDesktopSpanishSpain"
    name = "Microsoft Helena Desktop - Spanish (Spain)"
    voiceIDs = []
    _raw = {'lang': 'es-ES', 'name': 'Microsoft Helena Desktop - Spanish (Spain)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Helena Desktop - Spanish (Spain)', service="")


class MicrosoftLauraDesktopSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftLauraDesktopSpanishSpain"
    name = "Microsoft Laura Desktop - Spanish (Spain)"
    voiceIDs = []
    _raw = {'lang': 'es-ES', 'name': 'Microsoft Laura Desktop - Spanish (Spain)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Laura Desktop - Spanish (Spain)', service="")


class MicrosoftSabinaDesktopSpanishMexico(ResponsiveVoice):
    uri = "MicrosoftSabinaDesktopSpanishMexico"
    name = "Microsoft Sabina Desktop - Spanish (Mexico)"
    voiceIDs = []
    _raw = {'lang': 'es-MX', 'name': 'Microsoft Sabina Desktop - Spanish (Mexico)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Sabina Desktop - Spanish (Mexico)', service="")


class MicrosoftJulieDesktopFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftJulieDesktopFrenchFrance"
    name = "Microsoft Julie Desktop - French (France)"
    voiceIDs = []
    _raw = {'lang': 'fr-FR', 'name': 'Microsoft Julie Desktop - French (France)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Julie Desktop - French (France)', service="")


class MicrosoftPaulinaDesktopPolishPoland(ResponsiveVoice):
    uri = "MicrosoftPaulinaDesktopPolishPoland"
    name = "Microsoft Paulina Desktop - Polish (Poland)"
    voiceIDs = []
    _raw = {'lang': 'pl-PL', 'name': 'Microsoft Paulina Desktop - Polish (Poland)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Paulina Desktop - Polish (Poland)', service="")


class MicrosoftHuihuiDesktopChineseSimplifiedPrc(ResponsiveVoice):
    uri = "MicrosoftHuihuiDesktopChineseSimplifiedPrc"
    name = "Microsoft Huihui Desktop - Chinese (Simplified PRC)"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Microsoft Huihui Desktop - Chinese (Simplified PRC)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Huihui Desktop - Chinese (Simplified PRC)', service="")


class MicrosoftYaoyaoDesktopChineseSimplifiedPrc(ResponsiveVoice):
    uri = "MicrosoftYaoyaoDesktopChineseSimplifiedPrc"
    name = "Microsoft Yaoyao Desktop - Chinese (Simplified PRC)"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Microsoft Yaoyao Desktop - Chinese (Simplified PRC)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Yaoyao Desktop - Chinese (Simplified PRC)', service="")


class MicrosoftTracyDesktopChineseTraditionalHongKongSAR(ResponsiveVoice):
    uri = "MicrosoftTracyDesktopChineseTraditionalHongKongSAR"
    name = "Microsoft Tracy Desktop - Chinese (Traditional Hong Kong S.A.R.)"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Microsoft Tracy Desktop - Chinese (Traditional Hong Kong S.A.R.)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Tracy Desktop - Chinese (Traditional Hong Kong S.A.R.)', service="")


class MicrosoftElsaDesktopItalianItaly(ResponsiveVoice):
    uri = "MicrosoftElsaDesktopItalianItaly"
    name = "Microsoft Elsa Desktop - Italian (Italy)"
    voiceIDs = []
    _raw = {'lang': 'it-IT', 'name': 'Microsoft Elsa Desktop - Italian (Italy)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Elsa Desktop - Italian (Italy)', service="")


class MicrosoftMariaDesktopPortugueseBrazil(ResponsiveVoice):
    uri = "MicrosoftMariaDesktopPortugueseBrazil"
    name = "Microsoft Maria Desktop - Portuguese (Brazil)"
    voiceIDs = []
    _raw = {'lang': 'pt-BR', 'name': 'Microsoft Maria Desktop - Portuguese (Brazil)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Maria Desktop - Portuguese (Brazil)', service="")


class MicrosoftAyumiDesktopJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftAyumiDesktopJapaneseJapan"
    name = "Microsoft Ayumi Desktop - Japanese (Japan)"
    voiceIDs = []
    _raw = {'lang': 'ja-JP', 'name': 'Microsoft Ayumi Desktop - Japanese (Japan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Ayumi Desktop - Japanese (Japan)', service="")


class MicrosoftHarukaDesktopJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftHarukaDesktopJapaneseJapan"
    name = "Microsoft Haruka Desktop - Japanese (Japan)"
    voiceIDs = []
    _raw = {'lang': 'ja-JP', 'name': 'Microsoft Haruka Desktop - Japanese (Japan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Haruka Desktop - Japanese (Japan)', service="")


class MicrosoftHortenseDesktopFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftHortenseDesktopFrenchFrance"
    name = "Microsoft Hortense Desktop - French (France)"
    voiceIDs = []
    _raw = {'lang': 'fr-FR', 'name': 'Microsoft Hortense Desktop - French (France)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Hortense Desktop - French (France)', service="")


class MicrosoftHanhanDesktopChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftHanhanDesktopChineseTraditionalTaiwan"
    name = "Microsoft Hanhan Desktop - Chinese (Traditional Taiwan)"
    voiceIDs = []
    _raw = {'lang': 'zh-TW', 'name': 'Microsoft Hanhan Desktop - Chinese (Traditional Taiwan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Hanhan Desktop - Chinese (Traditional Taiwan)', service="")


class MicrosoftHeamiDesktopKoreanKorean(ResponsiveVoice):
    uri = "MicrosoftHeamiDesktopKoreanKorean"
    name = "Microsoft Heami Desktop - Korean (Korean)"
    voiceIDs = []
    _raw = {'lang': 'ko-KR', 'name': 'Microsoft Heami Desktop - Korean (Korean)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Heami Desktop - Korean (Korean)', service="")


class MicrosoftStefanDesktopGermanGermany(ResponsiveVoice):
    uri = "MicrosoftStefanDesktopGermanGermany"
    name = "Microsoft Stefan Desktop - German (Germany)"
    voiceIDs = []
    _raw = {'lang': 'de-DE', 'name': 'Microsoft Stefan Desktop - German (Germany)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Stefan Desktop - German (Germany)', service="")


class MicrosoftRaviDesktopEnglishIndia(ResponsiveVoice):
    uri = "MicrosoftRaviDesktopEnglishIndia"
    name = "Microsoft Ravi Desktop - English (India)"
    voiceIDs = []
    _raw = {'lang': 'en-IN', 'name': 'Microsoft Ravi Desktop - English (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Ravi Desktop - English (India)', service="")


class MicrosoftPabloDesktopSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftPabloDesktopSpanishSpain"
    name = "Microsoft Pablo Desktop - Spanish (Spain)"
    voiceIDs = []
    _raw = {'lang': 'es-ES', 'name': 'Microsoft Pablo Desktop - Spanish (Spain)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Pablo Desktop - Spanish (Spain)', service="")


class MicrosoftRaulDesktopSpanishMexico(ResponsiveVoice):
    uri = "MicrosoftRaulDesktopSpanishMexico"
    name = "Microsoft Raul Desktop - Spanish (Mexico)"
    voiceIDs = []
    _raw = {'lang': 'es-MX', 'name': 'Microsoft Raul Desktop - Spanish (Mexico)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Raul Desktop - Spanish (Mexico)', service="")


class MicrosoftPaulDesktopFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftPaulDesktopFrenchFrance"
    name = "Microsoft Paul Desktop - French (France)"
    voiceIDs = []
    _raw = {'lang': 'fr-FR', 'name': 'Microsoft Paul Desktop - French (France)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Paul Desktop - French (France)', service="")


class MicrosoftCosimoDesktopItalianItaly(ResponsiveVoice):
    uri = "MicrosoftCosimoDesktopItalianItaly"
    name = "Microsoft Cosimo Desktop - Italian (Italy)"
    voiceIDs = []
    _raw = {'lang': 'it-IT', 'name': 'Microsoft Cosimo Desktop - Italian (Italy)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Cosimo Desktop - Italian (Italy)', service="")


class MicrosoftIchiroDesktopJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftIchiroDesktopJapaneseJapan"
    name = "Microsoft Ichiro Desktop - Japanese (Japan)"
    voiceIDs = []
    _raw = {'lang': 'ja-JP', 'name': 'Microsoft Ichiro Desktop - Japanese (Japan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Ichiro Desktop - Japanese (Japan)', service="")


class MicrosoftAdamDesktopPolishPoland(ResponsiveVoice):
    uri = "MicrosoftAdamDesktopPolishPoland"
    name = "Microsoft Adam Desktop - Polish (Poland)"
    voiceIDs = []
    _raw = {'lang': 'pl-PL', 'name': 'Microsoft Adam Desktop - Polish (Poland)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Adam Desktop - Polish (Poland)', service="")


class MicrosoftDanielDesktopPortugueseBrazil(ResponsiveVoice):
    uri = "MicrosoftDanielDesktopPortugueseBrazil"
    name = "Microsoft Daniel Desktop - Portuguese (Brazil)"
    voiceIDs = []
    _raw = {'lang': 'pt-BR', 'name': 'Microsoft Daniel Desktop - Portuguese (Brazil)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Daniel Desktop - Portuguese (Brazil)', service="")


class MicrosoftPavelDesktopRussianRussia(ResponsiveVoice):
    uri = "MicrosoftPavelDesktopRussianRussia"
    name = "Microsoft Pavel Desktop - Russian (Russia)"
    voiceIDs = []
    _raw = {'lang': 'ru-RU', 'name': 'Microsoft Pavel Desktop - Russian (Russia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Pavel Desktop - Russian (Russia)', service="")


class MicrosoftKangkangDesktopChineseSimplifiedPrc(ResponsiveVoice):
    uri = "MicrosoftKangkangDesktopChineseSimplifiedPrc"
    name = "Microsoft Kangkang Desktop - Chinese (Simplified PRC)"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Microsoft Kangkang Desktop - Chinese (Simplified PRC)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Kangkang Desktop - Chinese (Simplified PRC)', service="")


class MicrosoftDannyDesktopChineseTraditionalHongKongSAR(ResponsiveVoice):
    uri = "MicrosoftDannyDesktopChineseTraditionalHongKongSAR"
    name = "Microsoft Danny Desktop - Chinese (Traditional Hong Kong S.A.R.)"
    voiceIDs = []
    _raw = {'lang': 'zh-HK', 'name': 'Microsoft Danny Desktop - Chinese (Traditional Hong Kong S.A.R.)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Danny Desktop - Chinese (Traditional Hong Kong S.A.R.)', service="")


class MicrosoftYatingDesktopChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftYatingDesktopChineseTraditionalTaiwan"
    name = "Microsoft Yating Desktop - Chinese (Traditional Taiwan)"
    voiceIDs = []
    _raw = {'lang': 'zh-TW', 'name': 'Microsoft Yating Desktop - Chinese (Traditional Taiwan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Yating Desktop - Chinese (Traditional Taiwan)', service="")


class MicrosoftZhiweiDesktopChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftZhiweiDesktopChineseTraditionalTaiwan"
    name = "Microsoft Zhiwei Desktop - Chinese (Traditional Taiwan)"
    voiceIDs = []
    _raw = {'lang': 'zh-TW', 'name': 'Microsoft Zhiwei Desktop - Chinese (Traditional Taiwan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Zhiwei Desktop - Chinese (Traditional Taiwan)', service="")


class Martin(ResponsiveVoice):
    uri = "Martin"
    name = "Martin"
    voiceIDs = []
    _raw = {'lang': 'de-DE', 'name': 'Martin'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Martin', service="")


class DanielAlt(ResponsiveVoice):
    uri = "DanielAlt"
    name = "Daniel"
    voiceIDs = []
    _raw = {'lang': 'fr-FR', 'name': 'Daniel'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Daniel', service="")


class Hattori(ResponsiveVoice):
    uri = "Hattori"
    name = "Hattori"
    voiceIDs = []
    _raw = {'lang': 'ja-JP', 'name': 'Hattori'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Hattori', service="")


class Limu(ResponsiveVoice):
    uri = "Limu"
    name = "Li-mu"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'name': 'Li-mu'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Li-mu', service="")


class Gordon(ResponsiveVoice):
    uri = "Gordon"
    name = "Gordon"
    voiceIDs = []
    _raw = {'lang': 'en-AU', 'name': 'Gordon'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Gordon', service="")


class Aaron(ResponsiveVoice):
    uri = "Aaron"
    name = "Aaron"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'name': 'Aaron'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Aaron', service="")


class Nicky(ResponsiveVoice):
    uri = "Nicky"
    name = "Nicky"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'name': 'Nicky'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Nicky', service="")


class MicrosoftHanhanDesktopChineseTaiwan(ResponsiveVoice):
    uri = "MicrosoftHanhanDesktopChineseTaiwan"
    name = "Microsoft Hanhan Desktop - Chinese (Taiwan)"
    voiceIDs = []
    _raw = {'lang': 'zh-TW', 'name': 'Microsoft Hanhan Desktop - Chinese (Taiwan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Hanhan Desktop - Chinese (Taiwan)', service="")


class MicrosoftHeamiDesktopKorean(ResponsiveVoice):
    uri = "MicrosoftHeamiDesktopKorean"
    name = "Microsoft Heami Desktop - Korean"
    voiceIDs = []
    _raw = {'lang': 'ko-KR', 'name': 'Microsoft Heami Desktop - Korean'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Heami Desktop - Korean', service="")


class FallbackAustralianMale(ResponsiveVoice):
    uri = "FallbackAustralianMale"
    name = "Fallback Australian Male"
    voiceIDs = []
    _raw = {'lang': 'en-AU', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male',
            'name': 'Fallback Australian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Australian Male', service="g3")


class FallbackRussianMale(ResponsiveVoice):
    uri = "FallbackRussianMale"
    name = "Fallback Russian Male"
    voiceIDs = []
    _raw = {'lang': 'ru', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'deprecated': True,
            'name': 'Fallback Russian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Russian Male', service="g3")


class FallbackArabicMale(ResponsiveVoice):
    uri = "FallbackArabicMale"
    name = "Fallback Arabic Male"
    voiceIDs = []
    _raw = {'lang': 'ar', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback Arabic Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Arabic Male', service="g3")


class FallbackChineseAlt(ResponsiveVoice):
    uri = "FallbackChineseAlt"
    name = "Fallback Chinese"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback Chinese'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Chinese', service="g3")


class FallbackChineseHk(ResponsiveVoice):
    uri = "FallbackChineseHk"
    name = "Fallback Chinese HK"
    voiceIDs = []
    _raw = {'lang': 'zh-HK', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback Chinese HK'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Chinese HK', service="g3")


class FallbackChineseTw(ResponsiveVoice):
    uri = "FallbackChineseTw"
    name = "Fallback Chinese TW"
    voiceIDs = []
    _raw = {'lang': 'zh-TW', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback Chinese TW'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Chinese TW', service="g3")


class FallbackFrenchMale(ResponsiveVoice):
    uri = "FallbackFrenchMale"
    name = "Fallback French Male"
    voiceIDs = []
    _raw = {'lang': 'fr', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback French Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback French Male', service="g3")


class FallbackDeutschMale(ResponsiveVoice):
    uri = "FallbackDeutschMale"
    name = "Fallback Deutsch Male"
    voiceIDs = []
    _raw = {'lang': 'de', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback Deutsch Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Deutsch Male', service="g3")


class FallbackHindiMale(ResponsiveVoice):
    uri = "FallbackHindiMale"
    name = "Fallback Hindi Male"
    voiceIDs = []
    _raw = {'lang': 'hi', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback Hindi Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Hindi Male', service="g3")


class FallbackIndonesianMale(ResponsiveVoice):
    uri = "FallbackIndonesianMale"
    name = "Fallback Indonesian Male"
    voiceIDs = []
    _raw = {'lang': 'id', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback Indonesian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Indonesian Male', service="g3")


class FallbackJapaneseMale(ResponsiveVoice):
    uri = "FallbackJapaneseMale"
    name = "Fallback Japanese Male"
    voiceIDs = []
    _raw = {'lang': 'ja', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback Japanese Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Japanese Male', service="g3")


class FallbackKoreanMale(ResponsiveVoice):
    uri = "FallbackKoreanMale"
    name = "Fallback Korean Male"
    voiceIDs = []
    _raw = {'lang': 'ko', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback Korean Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Korean Male', service="g3")


class FallbackPolishMale(ResponsiveVoice):
    uri = "FallbackPolishMale"
    name = "Fallback Polish Male"
    voiceIDs = []
    _raw = {'lang': 'pl', 'fallbackvoice': True, 'service': 'g1', 'gender': 'male', 'name': 'Fallback Polish Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Polish Male', service="g1")


class FallbackBrazilianPortugueseMale(ResponsiveVoice):
    uri = "FallbackBrazilianPortugueseMale"
    name = "Fallback Brazilian Portuguese Male"
    voiceIDs = []
    _raw = {'lang': 'pt-BR', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'deprecated': True,
            'name': 'Fallback Brazilian Portuguese Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Brazilian Portuguese Male', service="g3")


class FallbackPortugueseMale(ResponsiveVoice):
    uri = "FallbackPortugueseMale"
    name = "Fallback Portuguese Male"
    voiceIDs = []
    _raw = {'lang': 'pt-PT', 'fallbackvoice': True, 'service': 'g1', 'gender': 'male',
            'name': 'Fallback Portuguese Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-PT", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Portuguese Male', service="g1")


class FallbackSpanishMale(ResponsiveVoice):
    uri = "FallbackSpanishMale"
    name = "Fallback Spanish Male"
    voiceIDs = []
    _raw = {'lang': 'es', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'deprecated': True,
            'name': 'Fallback Spanish Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Spanish Male', service="g3")


class FallbackSpanishLatinAmericanMale(ResponsiveVoice):
    uri = "FallbackSpanishLatinAmericanMale"
    name = "Fallback Spanish (Latin American) Male"
    voiceIDs = []
    _raw = {'lang': 'es-419', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male',
            'name': 'Fallback Spanish (Latin American) Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-419", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Spanish (Latin American) Male', service="g3")


class FallbackThaiMale(ResponsiveVoice):
    uri = "FallbackThaiMale"
    name = "Fallback Thai Male"
    voiceIDs = []
    _raw = {'lang': 'th', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback Thai Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Thai Male', service="g3")


class FallbackTurkishMale(ResponsiveVoice):
    uri = "FallbackTurkishMale"
    name = "Fallback Turkish Male"
    voiceIDs = []
    _raw = {'lang': 'tr', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback Turkish Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Turkish Male', service="g3")


class FallbackVietnameseFemale(ResponsiveVoice):
    uri = "FallbackVietnameseFemale"
    name = "Fallback Vietnamese Female"
    voiceIDs = []
    _raw = {'lang': 'vi', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female',
            'name': 'Fallback Vietnamese Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="vi", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Vietnamese Female', service="g1")


class FallbackItalianMale(ResponsiveVoice):
    uri = "FallbackItalianMale"
    name = "Fallback Italian Male"
    voiceIDs = []
    _raw = {'lang': 'it', 'fallbackvoice': True, 'service': 'g3', 'gender': 'male', 'name': 'Fallback Italian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Italian Male', service="g3")


class FallbackDutchMale(ResponsiveVoice):
    uri = "FallbackDutchMale"
    name = "Fallback Dutch Male"
    voiceIDs = []
    _raw = {'lang': 'nl', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'male',
            'name': 'Fallback Dutch Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Dutch Male', service="g3")


class MicrosoftAnnaEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftAnnaEnglishUnitedStates"
    name = "Microsoft Anna - English (United States)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'gender': 'female', 'name': 'Microsoft Anna - English (United States)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Anna - English (United States)', service="")


class MicrosoftLiliChineseChina(ResponsiveVoice):
    uri = "MicrosoftLiliChineseChina"
    name = "Microsoft Lili - Chinese (China)"
    voiceIDs = []
    _raw = {'lang': 'zh-CN', 'gender': 'female', 'name': 'Microsoft Lili - Chinese (China)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Lili - Chinese (China)', service="")


class BanglaBangladesh(ResponsiveVoice):
    uri = "BanglaBangladesh"
    name = "Bangla Bangladesh"
    voiceIDs = []
    _raw = {'lang': 'bn_BD', 'gender': 'male', 'name': 'Bangla Bangladesh'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bn_BD", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Bangla Bangladesh', service="")


class BanglaIndia(ResponsiveVoice):
    uri = "BanglaIndia"
    name = "Bangla India"
    voiceIDs = []
    _raw = {'lang': 'bn_IN', 'gender': 'male', 'name': 'Bangla India'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bn_IN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Bangla India', service="")


class CzechCzechia(ResponsiveVoice):
    uri = "CzechCzechia"
    name = "Czech Czechia"
    voiceIDs = []
    _raw = {'lang': 'cs_CZ', 'gender': 'female', 'name': 'Czech Czechia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs_CZ", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Czech Czechia', service="")


class DanishDenmark(ResponsiveVoice):
    uri = "DanishDenmark"
    name = "Danish Denmark"
    voiceIDs = []
    _raw = {'lang': 'da_DK', 'gender': 'female', 'name': 'Danish Denmark'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da_DK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Danish Denmark', service="")


class GreekGreece(ResponsiveVoice):
    uri = "GreekGreece"
    name = "Greek Greece"
    voiceIDs = []
    _raw = {'lang': 'el_GR', 'gender': 'female', 'name': 'Greek Greece'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el_GR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Greek Greece', service="")


class EnglishAustralia(ResponsiveVoice):
    uri = "EnglishAustralia"
    name = "English Australia"
    voiceIDs = []
    _raw = {'lang': 'en_AU', 'gender': 'female', 'name': 'English Australia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en_AU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='English Australia', service="")


class EstonianEstonia(ResponsiveVoice):
    uri = "EstonianEstonia"
    name = "Estonian Estonia"
    voiceIDs = []
    _raw = {'lang': 'et_EE', 'gender': 'male', 'name': 'Estonian Estonia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="et_EE", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Estonian Estonia', service="")


class FinnishFinland(ResponsiveVoice):
    uri = "FinnishFinland"
    name = "Finnish Finland"
    voiceIDs = []
    _raw = {'lang': 'fi_FI', 'gender': 'female', 'name': 'Finnish Finland'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi_FI", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Finnish Finland', service="")


class FilipinoPhilippines(ResponsiveVoice):
    uri = "FilipinoPhilippines"
    name = "Filipino Philippines"
    voiceIDs = []
    _raw = {'lang': 'fil_PH', 'gender': 'female', 'name': 'Filipino Philippines'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fil_PH", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Filipino Philippines', service="")


class FrenchCanada(ResponsiveVoice):
    uri = "FrenchCanada"
    name = "French Canada"
    voiceIDs = []
    _raw = {'lang': 'fr_CAF', 'gender': 'female', 'name': 'French Canada'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr_CAF", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='French Canada', service="")


class HungarianHungary(ResponsiveVoice):
    uri = "HungarianHungary"
    name = "Hungarian Hungary"
    voiceIDs = []
    _raw = {'lang': 'hu_HU', 'gender': 'female', 'name': 'Hungarian Hungary'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu_HU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Hungarian Hungary', service="")


class KhmerCambodia(ResponsiveVoice):
    uri = "KhmerCambodia"
    name = "Khmer Cambodia"
    voiceIDs = []
    _raw = {'lang': 'km_KH', 'gender': 'female', 'name': 'Khmer Cambodia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="km_KH", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Khmer Cambodia', service="")


class NepaliNepal(ResponsiveVoice):
    uri = "NepaliNepal"
    name = "Nepali Nepal"
    voiceIDs = []
    _raw = {'lang': 'ne_NP', 'gender': 'female', 'name': 'Nepali Nepal'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ne_NP", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Nepali Nepal', service="")


class RomanianRomania(ResponsiveVoice):
    uri = "RomanianRomania"
    name = "Romanian Romania"
    voiceIDs = []
    _raw = {'lang': 'ro_RO', 'gender': 'female', 'name': 'Romanian Romania'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ro_RO", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Romanian Romania', service="")


class SinhalaSriLanka(ResponsiveVoice):
    uri = "SinhalaSriLanka"
    name = "Sinhala Sri Lanka"
    voiceIDs = []
    _raw = {'lang': 'si_LK', 'gender': 'female', 'name': 'Sinhala Sri Lanka'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="si_LK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Sinhala Sri Lanka', service="")


class SlovakSlovakia(ResponsiveVoice):
    uri = "SlovakSlovakia"
    name = "Slovak Slovakia"
    voiceIDs = []
    _raw = {'lang': 'sk_SK', 'gender': 'female', 'name': 'Slovak Slovakia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk_SK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Slovak Slovakia', service="")


class SwedishSweden(ResponsiveVoice):
    uri = "SwedishSweden"
    name = "Swedish Sweden"
    voiceIDs = []
    _raw = {'lang': 'sv_SE', 'gender': 'female', 'name': 'Swedish Sweden'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sv_SE", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Swedish Sweden', service="")


class UkrainianUkraine(ResponsiveVoice):
    uri = "UkrainianUkraine"
    name = "Ukrainian Ukraine"
    voiceIDs = []
    _raw = {'lang': 'uk_UA', 'gender': 'female', 'name': 'Ukrainian Ukraine'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="uk_UA", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ukrainian Ukraine', service="")


class VietnameseVietnam(ResponsiveVoice):
    uri = "VietnameseVietnam"
    name = "Vietnamese Vietnam"
    voiceIDs = []
    _raw = {'lang': 'vi_VN', 'gender': 'female', 'name': 'Vietnamese Vietnam'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="vi_VN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Vietnamese Vietnam', service="")


class CantoneseHongKong(ResponsiveVoice):
    uri = "CantoneseHongKong"
    name = "Cantonese Hong Kong"
    voiceIDs = []
    _raw = {'lang': 'yue_HK_#Hant', 'gender': 'female', 'name': 'Cantonese Hong Kong'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="yue_HK_#Hant", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Cantonese Hong Kong', service="")


class MicrosoftServerSpeechTextToSpeechVoiceEnusGuy24Krus(ResponsiveVoice):
    uri = "MicrosoftServerSpeechTextToSpeechVoiceEnusGuy24Krus"
    name = "Microsoft Server Speech Text to Speech Voice (en-US Guy24kRUS)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'gender': 'male', 'name': 'Microsoft Server Speech Text to Speech Voice (en-US Guy24kRUS)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Server Speech Text to Speech Voice (en-US Guy24kRUS)', service="")


class MicrosoftServerSpeechTextToSpeechVoiceEnusJessa24Krus(ResponsiveVoice):
    uri = "MicrosoftServerSpeechTextToSpeechVoiceEnusJessa24Krus"
    name = "Microsoft Server Speech Text to Speech Voice (en-US Jessa24kRUS)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'gender': 'female',
            'name': 'Microsoft Server Speech Text to Speech Voice (en-US Jessa24kRUS)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Server Speech Text to Speech Voice (en-US Jessa24kRUS)', service="")


class MicrosoftServerSpeechTextToSpeechVoiceEnusJessarus(ResponsiveVoice):
    uri = "MicrosoftServerSpeechTextToSpeechVoiceEnusJessarus"
    name = "Microsoft Server Speech Text to Speech Voice (en-US JessaRUS)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'gender': 'female',
            'name': 'Microsoft Server Speech Text to Speech Voice (en-US JessaRUS)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Server Speech Text to Speech Voice (en-US JessaRUS)', service="")


class MicrosoftServerSpeechTextToSpeechVoiceEnusZirarus(ResponsiveVoice):
    uri = "MicrosoftServerSpeechTextToSpeechVoiceEnusZirarus"
    name = "Microsoft Server Speech Text to Speech Voice (en-US ZiraRUS)"
    voiceIDs = []
    _raw = {'lang': 'en-US', 'gender': 'female', 'name': 'Microsoft Server Speech Text to Speech Voice (en-US ZiraRUS)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Server Speech Text to Speech Voice (en-US ZiraRUS)', service="")


class FallbackBanglaBangladehFemale(ResponsiveVoice):
    uri = "FallbackBanglaBangladehFemale"
    name = "Fallback Bangla Bangladeh Female"
    voiceIDs = []
    _raw = {'lang': 'bn-BD', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'female',
            'name': 'Fallback Bangla Bangladeh Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bn-BD", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Bangla Bangladeh Female', service="g3")


class FallbackBanglaBangladehMale(ResponsiveVoice):
    uri = "FallbackBanglaBangladehMale"
    name = "Fallback Bangla Bangladeh Male"
    voiceIDs = []
    _raw = {'lang': 'bn-BD', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'male',
            'name': 'Fallback Bangla Bangladeh Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bn-BD", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Bangla Bangladeh Male', service="g3")


class FallbackFilipinoFemale(ResponsiveVoice):
    uri = "FallbackFilipinoFemale"
    name = "Fallback Filipino Female"
    voiceIDs = []
    _raw = {'lang': 'fil-PH', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'female',
            'name': 'Fallback Filipino Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fil-PH", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Filipino Female', service="g3")


class FallbackFilipinoMale(ResponsiveVoice):
    uri = "FallbackFilipinoMale"
    name = "Fallback Filipino Male"
    voiceIDs = []
    _raw = {'lang': 'fil-PH', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'male',
            'name': 'Fallback Filipino Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fil-PH", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Filipino Male', service="g3")


class FallbackCambodianKhmerFemale(ResponsiveVoice):
    uri = "FallbackCambodianKhmerFemale"
    name = "Fallback Cambodian Khmer Female"
    voiceIDs = []
    _raw = {'lang': 'km-KH', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'female',
            'name': 'Fallback Cambodian Khmer Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="km-KH", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Cambodian Khmer Female', service="g3")


class FallbackCambodianKhmerMale(ResponsiveVoice):
    uri = "FallbackCambodianKhmerMale"
    name = "Fallback Cambodian Khmer Male"
    voiceIDs = []
    _raw = {'lang': 'km-KH', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'male',
            'name': 'Fallback Cambodian Khmer Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="km-KH", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Cambodian Khmer Male', service="g3")


class FallbackNepaliFemale(ResponsiveVoice):
    uri = "FallbackNepaliFemale"
    name = "Fallback Nepali Female"
    voiceIDs = []
    _raw = {'lang': 'ne-NP', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'female',
            'name': 'Fallback Nepali Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ne-NP", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Nepali Female', service="g3")


class FallbackSinhalaFemale(ResponsiveVoice):
    uri = "FallbackSinhalaFemale"
    name = "Fallback Sinhala Female"
    voiceIDs = []
    _raw = {'lang': 'si-LK', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'female',
            'name': 'Fallback Sinhala Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="si-LK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Sinhala Female', service="g3")


class FallbackUkrainianFemale(ResponsiveVoice):
    uri = "FallbackUkrainianFemale"
    name = "Fallback Ukrainian Female"
    voiceIDs = []
    _raw = {'lang': 'uk-UA', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'female',
            'name': 'Fallback Ukrainian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="uk-UA", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Ukrainian Female', service="g3")


class FallbackCantoneseHongKongFemale(ResponsiveVoice):
    uri = "FallbackCantoneseHongKongFemale"
    name = "Fallback Cantonese Hong Kong Female"
    voiceIDs = []
    _raw = {'lang': 'yue-HK', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'female',
            'name': 'Fallback Cantonese Hong Kong Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="yue-HK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Cantonese Hong Kong Female', service="g3")


class FallbackCantoneseHongKongMale(ResponsiveVoice):
    uri = "FallbackCantoneseHongKongMale"
    name = "Fallback Cantonese Hong Kong Male"
    voiceIDs = []
    _raw = {'lang': 'yue-HK', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'male',
            'name': 'Fallback Cantonese Hong Kong Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="yue-HK", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Cantonese Hong Kong Male', service="g3")


class FallbackEstonianMale(ResponsiveVoice):
    uri = "FallbackEstonianMale"
    name = "Fallback Estonian Male"
    voiceIDs = []
    _raw = {'lang': 'et-EE', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'male',
            'name': 'Fallback Estonian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="et-EE", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Estonian Male', service="g3")


class FallbackBanglaIndiaFemale(ResponsiveVoice):
    uri = "FallbackBanglaIndiaFemale"
    name = "Fallback Bangla India Female"
    voiceIDs = []
    _raw = {'lang': 'bn-IN', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'female',
            'name': 'Fallback Bangla India Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bn-IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Bangla India Female', service="g3")


class FallbackBanglaIndiaMale(ResponsiveVoice):
    uri = "FallbackBanglaIndiaMale"
    name = "Fallback Bangla India Male"
    voiceIDs = []
    _raw = {'lang': 'bn-IN', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'male',
            'name': 'Fallback Bangla India Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bn-IN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Bangla India Male', service="g3")


class FallbackFrenchCanadianFemale(ResponsiveVoice):
    uri = "FallbackFrenchCanadianFemale"
    name = "Fallback French Canadian Female"
    voiceIDs = []
    _raw = {'lang': 'fr-CA', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'female',
            'name': 'Fallback French Canadian Female'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-CA", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback French Canadian Female', service="g3")


class FallbackFrenchCanadianMale(ResponsiveVoice):
    uri = "FallbackFrenchCanadianMale"
    name = "Fallback French Canadian Male"
    voiceIDs = []
    _raw = {'lang': 'fr-CA', 'fallbackvoice': True, 'timerSpeed': '0', 'service': 'g3', 'gender': 'male',
            'name': 'Fallback French Canadian Male'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-CA", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback French Canadian Male', service="g3")


class FallbackTamilAlt(ResponsiveVoice):
    uri = "FallbackTamilAlt"
    name = "Fallback Tamil"
    voiceIDs = []
    _raw = {'lang': 'ta', 'fallbackvoice': True, 'service': 'g1', 'gender': 'female', 'name': 'Fallback Tamil'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ta", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fallback Tamil', service="g1")


class ComAppleTtsbundleTingtingcompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Ting-Ting-compact"
    name = "Tian-Tian"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Ting-Ting-compact', 'lang': 'zh-CN', 'gender': 'female',
            'name': 'Tian-Tian'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Tian-Tian', service="")


class EnglishNigeria(ResponsiveVoice):
    uri = "EnglishNigeria"
    name = "English Nigeria"
    voiceIDs = []
    _raw = {'lang': 'en_NG', 'gender': 'female', 'name': 'English Nigeria'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en_NG", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='English Nigeria', service="")


class GujaratiIndia(ResponsiveVoice):
    uri = "GujaratiIndia"
    name = "Gujarati India"
    voiceIDs = []
    _raw = {'lang': 'gu_IN', 'gender': 'female', 'name': 'Gujarati India'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="gu_IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Gujarati India', service="")


class KannadaIndia(ResponsiveVoice):
    uri = "KannadaIndia"
    name = "Kannada India"
    voiceIDs = []
    _raw = {'lang': 'kn_IN', 'gender': 'female', 'name': 'Kannada India'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="kn_IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Kannada India', service="")


class MalayalamIndia(ResponsiveVoice):
    uri = "MalayalamIndia"
    name = "Malayalam India"
    voiceIDs = []
    _raw = {'lang': 'ml_IN', 'gender': 'female', 'name': 'Malayalam India'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ml_IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Malayalam India', service="")


class MarathiIndia(ResponsiveVoice):
    uri = "MarathiIndia"
    name = "Marathi India"
    voiceIDs = []
    _raw = {'lang': 'mr_IN', 'gender': 'female', 'name': 'Marathi India'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="mr_IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Marathi India', service="")


class TamilIndia(ResponsiveVoice):
    uri = "TamilIndia"
    name = "Tamil India"
    voiceIDs = []
    _raw = {'lang': 'ta_IN', 'gender': 'female', 'name': 'Tamil India'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ta_IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Tamil India', service="")


class TeluguIndia(ResponsiveVoice):
    uri = "TeluguIndia"
    name = "Telugu India"
    voiceIDs = []
    _raw = {'lang': 'te_IN', 'gender': 'female', 'name': 'Telugu India'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="te_IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Telugu India', service="")


class UrduPakistan(ResponsiveVoice):
    uri = "UrduPakistan"
    name = "Urdu Pakistan"
    voiceIDs = []
    _raw = {'lang': 'ur_PK', 'gender': 'female', 'name': 'Urdu Pakistan'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ur_PK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Urdu Pakistan', service="")


class JavaneseIndonesia(ResponsiveVoice):
    uri = "JavaneseIndonesia"
    name = "Javanese Indonesia"
    voiceIDs = []
    _raw = {'lang': 'jv_ID', 'gender': 'female', 'name': 'Javanese Indonesia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="jv_ID", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Javanese Indonesia', service="")


class MalayMalaysia(ResponsiveVoice):
    uri = "MalayMalaysia"
    name = "Malay Malaysia"
    voiceIDs = []
    _raw = {'lang': 'ms_MY', 'gender': 'female', 'name': 'Malay Malaysia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ms_MY", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Malay Malaysia', service="")


class ChineseHongKongAltAlt(ResponsiveVoice):
    uri = "ChineseHongKongAltAlt"
    name = "Chinese Hong Kong"
    voiceIDs = []
    _raw = {'lang': 'zh_HK_#Hans', 'gender': 'female', 'name': 'Chinese Hong Kong'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh_HK_#Hans", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese Hong Kong', service="")


class ChineseHongKongAltAltAlt(ResponsiveVoice):
    uri = "ChineseHongKongAltAltAlt"
    name = "Chinese Hong Kong"
    voiceIDs = []
    _raw = {'lang': 'zh_HK_#Hant', 'gender': 'female', 'name': 'Chinese Hong Kong'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh_HK_#Hant", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese Hong Kong', service="")


class MicrosoftTolgaTurkishTurkey(ResponsiveVoice):
    uri = "MicrosoftTolgaTurkishTurkey"
    name = "Microsoft Tolga - Turkish (Turkey)"
    voiceIDs = []
    _raw = {'lang': 'tr-TR', 'gender': 'male', 'name': 'Microsoft Tolga - Turkish (Turkey)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr-TR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Microsoft Tolga - Turkish (Turkey)', service="")


class MozttsAndroidKoKr(ResponsiveVoice):
    uri = "moz-tts:android:ko_KR"
    name = "Korean (South Korea)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:ko_KR', 'lang': 'ko-KR', 'gender': 'female', 'name': 'Korean (South Korea)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Korean (South Korea)', service="")


class MozttsAndroidMrIn(ResponsiveVoice):
    uri = "moz-tts:android:mr_IN"
    name = "Marathi (India)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:mr_IN', 'lang': 'mr-IN', 'gender': 'female', 'name': 'Marathi (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="mr-IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Marathi (India)', service="")


class MozttsAndroidRuRu(ResponsiveVoice):
    uri = "moz-tts:android:ru_RU"
    name = "Russian (Russia)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:ru_RU', 'lang': 'ru-RU', 'gender': 'female', 'name': 'Russian (Russia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Russian (Russia)', service="")


class MozttsAndroidZhTw(ResponsiveVoice):
    uri = "moz-tts:android:zh_TW"
    name = "Chinese (Taiwan)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:zh_TW', 'lang': 'zh-TW', 'gender': 'female', 'name': 'Chinese (Taiwan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese (Taiwan)', service="")


class MozttsAndroidHuHu(ResponsiveVoice):
    uri = "moz-tts:android:hu_HU"
    name = "Hungarian (Hungary)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:hu_HU', 'lang': 'hu-HU', 'gender': 'female', 'name': 'Hungarian (Hungary)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu-HU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Hungarian (Hungary)', service="")


class MozttsAndroidThTh(ResponsiveVoice):
    uri = "moz-tts:android:th_TH"
    name = "Thai (Thailand)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:th_TH', 'lang': 'th-TH', 'gender': 'female', 'name': 'Thai (Thailand)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th-TH", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Thai (Thailand)', service="")


class MozttsAndroidUrPk(ResponsiveVoice):
    uri = "moz-tts:android:ur_PK"
    name = "Urdu (Pakistan)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:ur_PK', 'lang': 'ur-PK', 'gender': 'female', 'name': 'Urdu (Pakistan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ur-PK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Urdu (Pakistan)', service="")


class MozttsAndroidNbNo(ResponsiveVoice):
    uri = "moz-tts:android:nb_NO"
    name = "Norwegian Bokm\u00e5l (Norway)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:nb_NO', 'lang': 'nb-NO', 'gender': 'female',
            'name': 'Norwegian Bokm\\u00e5l (Norway)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nb-NO", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Norwegian Bokm\u00e5l (Norway)', service="")


class MozttsAndroidDaDk(ResponsiveVoice):
    uri = "moz-tts:android:da_DK"
    name = "Danish (Denmark)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:da_DK', 'lang': 'da-DK', 'gender': 'female', 'name': 'Danish (Denmark)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da-DK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Danish (Denmark)', service="")


class MozttsAndroidTrTr(ResponsiveVoice):
    uri = "moz-tts:android:tr_TR"
    name = "Turkish (Turkey)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:tr_TR', 'lang': 'tr-TR', 'gender': 'female', 'name': 'Turkish (Turkey)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr-TR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Turkish (Turkey)', service="")


class MozttsAndroidEtEe(ResponsiveVoice):
    uri = "moz-tts:android:et_EE"
    name = "Estonian (Estonia)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:et_EE', 'lang': 'et-EE', 'gender': 'male', 'name': 'Estonian (Estonia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="et-EE", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Estonian (Estonia)', service="")


class MozttsAndroidBs(ResponsiveVoice):
    uri = "moz-tts:android:bs"
    name = "Bosnian"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:bs', 'lang': 'bs', 'deprecated': True, 'name': 'Bosnian'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bs", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Bosnian', service="")


class MozttsAndroidSw(ResponsiveVoice):
    uri = "moz-tts:android:sw"
    name = "Swahili"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:sw', 'lang': 'sw', 'deprecated': True, 'name': 'Swahili'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sw", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Swahili', service="")


class MozttsAndroidPtPt(ResponsiveVoice):
    uri = "moz-tts:android:pt_PT"
    name = "Portuguese (Portugal)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:pt_PT', 'lang': 'pt-PT', 'gender': 'female', 'name': 'Portuguese (Portugal)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-PT", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Portuguese (Portugal)', service="")


class MozttsAndroidViVn(ResponsiveVoice):
    uri = "moz-tts:android:vi_VN"
    name = "Vietnamese (Vietnam)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:vi_VN', 'lang': 'vi-VN', 'gender': 'female', 'name': 'Vietnamese (Vietnam)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="vi-VN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Vietnamese (Vietnam)', service="")


class MozttsAndroidEnUs(ResponsiveVoice):
    uri = "moz-tts:android:en_US"
    name = "English (United States)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:en_US', 'lang': 'en-US', 'gender': 'female', 'name': 'English (United States)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='English (United States)', service="")


class MozttsAndroidSvSe(ResponsiveVoice):
    uri = "moz-tts:android:sv_SE"
    name = "Swedish (Sweden)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:sv_SE', 'lang': 'sv-SE', 'gender': 'female', 'name': 'Swedish (Sweden)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sv-SE", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Swedish (Sweden)', service="")


class MozttsAndroidAr(ResponsiveVoice):
    uri = "moz-tts:android:ar"
    name = "Arabic"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:ar', 'lang': 'ar', 'gender': 'female', 'name': 'Arabic'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Arabic', service="")


class MozttsAndroidSuId(ResponsiveVoice):
    uri = "moz-tts:android:su_ID"
    name = "Sundanese (Indonesia)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:su_ID', 'lang': 'su-ID', 'gender': 'female', 'name': 'Sundanese (Indonesia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="su-ID", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Sundanese (Indonesia)', service="")


class MozttsAndroidBnBd(ResponsiveVoice):
    uri = "moz-tts:android:bn_BD"
    name = "Bangla (Bangladesh)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:bn_BD', 'lang': 'bn-BD', 'gender': 'male', 'name': 'Bangla (Bangladesh)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bn-BD", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Bangla (Bangladesh)', service="")


class MozttsAndroidGuIn(ResponsiveVoice):
    uri = "moz-tts:android:gu_IN"
    name = "Gujarati (India)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:gu_IN', 'lang': 'gu-IN', 'gender': 'female', 'name': 'Gujarati (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="gu-IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Gujarati (India)', service="")


class MozttsAndroidKnIn(ResponsiveVoice):
    uri = "moz-tts:android:kn_IN"
    name = "Kannada (India)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:kn_IN', 'lang': 'kn-IN', 'gender': 'female', 'name': 'Kannada (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="kn-IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Kannada (India)', service="")


class MozttsAndroidElGr(ResponsiveVoice):
    uri = "moz-tts:android:el_GR"
    name = "Greek (Greece)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:el_GR', 'lang': 'el-GR', 'gender': 'female', 'name': 'Greek (Greece)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el-GR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Greek (Greece)', service="")


class MozttsAndroidHiIn(ResponsiveVoice):
    uri = "moz-tts:android:hi_IN"
    name = "Hindi (India)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:hi_IN', 'lang': 'hi-IN', 'gender': 'female', 'name': 'Hindi (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Hindi (India)', service="")


class MozttsAndroidFiFi(ResponsiveVoice):
    uri = "moz-tts:android:fi_FI"
    name = "Finnish (Finland)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:fi_FI', 'lang': 'fi-FI', 'gender': 'female', 'name': 'Finnish (Finland)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi-FI", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Finnish (Finland)', service="")


class MozttsAndroidKmKh(ResponsiveVoice):
    uri = "moz-tts:android:km_KH"
    name = "Khmer (Cambodia)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:km_KH', 'lang': 'km-KH', 'gender': 'female', 'name': 'Khmer (Cambodia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="km-KH", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Khmer (Cambodia)', service="")


class MozttsAndroidBnIn(ResponsiveVoice):
    uri = "moz-tts:android:bn_IN"
    name = "Bangla (India)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:bn_IN', 'lang': 'bn-IN', 'gender': 'male', 'name': 'Bangla (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bn-IN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Bangla (India)', service="")


class MozttsAndroidFrFr(ResponsiveVoice):
    uri = "moz-tts:android:fr_FR"
    name = "French (France)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:fr_FR', 'lang': 'fr-FR', 'gender': 'female', 'name': 'French (France)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='French (France)', service="")


class MozttsAndroidUkUa(ResponsiveVoice):
    uri = "moz-tts:android:uk_UA"
    name = "Ukrainian (Ukraine)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:uk_UA', 'lang': 'uk-UA', 'gender': 'female', 'name': 'Ukrainian (Ukraine)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="uk-UA", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ukrainian (Ukraine)', service="")


class MozttsAndroidEnAu(ResponsiveVoice):
    uri = "moz-tts:android:en_AU"
    name = "English (Australia)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:en_AU', 'lang': 'en-AU', 'gender': 'female', 'name': 'English (Australia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='English (Australia)', service="")


class MozttsAndroidNlNl(ResponsiveVoice):
    uri = "moz-tts:android:nl_NL"
    name = "Dutch (Netherlands)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:nl_NL', 'lang': 'nl-NL', 'gender': 'female', 'name': 'Dutch (Netherlands)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-NL", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Dutch (Netherlands)', service="")


class MozttsAndroidFrCa(ResponsiveVoice):
    uri = "moz-tts:android:fr_CA"
    name = "French (Canada)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:fr_CA', 'lang': 'fr-CA', 'gender': 'female', 'name': 'French (Canada)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-CA", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='French (Canada)', service="")


class MozttsAndroidSr(ResponsiveVoice):
    uri = "moz-tts:android:sr"
    name = "Serbian"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:sr', 'lang': 'sr', 'gender': 'female', 'name': 'Serbian'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sr", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Serbian', service="")


class MozttsAndroidPtBr(ResponsiveVoice):
    uri = "moz-tts:android:pt_BR"
    name = "Portuguese (Brazil)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:pt_BR', 'lang': 'pt-BR', 'gender': 'female', 'name': 'Portuguese (Brazil)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Portuguese (Brazil)', service="")


class MozttsAndroidMlIn(ResponsiveVoice):
    uri = "moz-tts:android:ml_IN"
    name = "Malayalam (India)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:ml_IN', 'lang': 'ml-IN', 'gender': 'female', 'name': 'Malayalam (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ml-IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Malayalam (India)', service="")


class MozttsAndroidSiLk(ResponsiveVoice):
    uri = "moz-tts:android:si_LK"
    name = "Sinhala (Sri Lanka)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:si_LK', 'lang': 'si-LK', 'gender': 'female', 'name': 'Sinhala (Sri Lanka)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="si-LK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Sinhala (Sri Lanka)', service="")


class MozttsAndroidDeDe(ResponsiveVoice):
    uri = "moz-tts:android:de_DE"
    name = "German (Germany)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:de_DE', 'lang': 'de-DE', 'gender': 'female', 'name': 'German (Germany)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='German (Germany)', service="")


class MozttsAndroidKu(ResponsiveVoice):
    uri = "moz-tts:android:ku"
    name = "Kurdish"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:ku', 'lang': 'ku', 'deprecated': True, 'name': 'Kurdish'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ku", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Kurdish', service="")


class MozttsAndroidCsCz(ResponsiveVoice):
    uri = "moz-tts:android:cs_CZ"
    name = "Czech (Czechia)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:cs_CZ', 'lang': 'cs-CZ', 'gender': 'female', 'name': 'Czech (Czechia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs-CZ", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Czech (Czechia)', service="")


class MozttsAndroidPlPl(ResponsiveVoice):
    uri = "moz-tts:android:pl_PL"
    name = "Polish (Poland)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:pl_PL', 'lang': 'pl-PL', 'gender': 'female', 'name': 'Polish (Poland)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Polish (Poland)', service="")


class MozttsAndroidSkSk(ResponsiveVoice):
    uri = "moz-tts:android:sk_SK"
    name = "Slovak (Slovakia)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:sk_SK', 'lang': 'sk-SK', 'gender': 'female', 'name': 'Slovak (Slovakia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk-SK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Slovak (Slovakia)', service="")


class MozttsAndroidFilPh(ResponsiveVoice):
    uri = "moz-tts:android:fil_PH"
    name = "Filipino (Philippines)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:fil_PH', 'lang': 'fil-PH', 'gender': 'female',
            'name': 'Filipino (Philippines)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fil-PH", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Filipino (Philippines)', service="")


class MozttsAndroidItIt(ResponsiveVoice):
    uri = "moz-tts:android:it_IT"
    name = "Italian (Italy)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:it_IT', 'lang': 'it-IT', 'gender': 'female', 'name': 'Italian (Italy)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Italian (Italy)', service="")


class MozttsAndroidNeNp(ResponsiveVoice):
    uri = "moz-tts:android:ne_NP"
    name = "Nepali (Nepal)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:ne_NP', 'lang': 'ne-NP', 'gender': 'female', 'name': 'Nepali (Nepal)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ne-NP", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Nepali (Nepal)', service="")


class MozttsAndroidMsMy(ResponsiveVoice):
    uri = "moz-tts:android:ms_MY"
    name = "Malay (Malaysia)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:ms_MY', 'lang': 'ms-MY', 'gender': 'female', 'name': 'Malay (Malaysia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ms-MY", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Malay (Malaysia)', service="")


class MozttsAndroidHr(ResponsiveVoice):
    uri = "moz-tts:android:hr"
    name = "Croatian"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:hr', 'lang': 'hr', 'deprecated': True, 'name': 'Croatian'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hr", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Croatian', service="")


class MozttsAndroidEnNg(ResponsiveVoice):
    uri = "moz-tts:android:en_NG"
    name = "English (Nigeria)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:en_NG', 'lang': 'en-NG', 'gender': 'female', 'name': 'English (Nigeria)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-NG", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='English (Nigeria)', service="")


class MozttsAndroidZhCn(ResponsiveVoice):
    uri = "moz-tts:android:zh_CN"
    name = "Chinese (China)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:zh_CN', 'lang': 'zh-CN', 'gender': 'female', 'name': 'Chinese (China)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Chinese (China)', service="")


class MozttsAndroidEsEs(ResponsiveVoice):
    uri = "moz-tts:android:es_ES"
    name = "Spanish (Spain)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:es_ES', 'lang': 'es-ES', 'gender': 'female', 'name': 'Spanish (Spain)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Spanish (Spain)', service="")


class MozttsAndroidCy(ResponsiveVoice):
    uri = "moz-tts:android:cy"
    name = "Welsh"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:cy', 'lang': 'cy', 'deprecated': True, 'name': 'Welsh'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cy", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Welsh', service="")


class MozttsAndroidTaIn(ResponsiveVoice):
    uri = "moz-tts:android:ta_IN"
    name = "Tamil (India)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:ta_IN', 'lang': 'ta-IN', 'gender': 'female', 'name': 'Tamil (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ta-IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Tamil (India)', service="")


class MozttsAndroidJaJp(ResponsiveVoice):
    uri = "moz-tts:android:ja_JP"
    name = "Japanese (Japan)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:ja_JP', 'lang': 'ja-JP', 'gender': 'female', 'name': 'Japanese (Japan)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Japanese (Japan)', service="")


class MozttsAndroidSq(ResponsiveVoice):
    uri = "moz-tts:android:sq"
    name = "Albanian"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:sq', 'lang': 'sq', 'deprecated': True, 'name': 'Albanian'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sq", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Albanian', service="")


class MozttsAndroidYueHk(ResponsiveVoice):
    uri = "moz-tts:android:yue_HK"
    name = "Cantonese (Hong Kong)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:yue_HK', 'lang': 'yue-HK', 'gender': 'female', 'name': 'Cantonese (Hong Kong)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="yue-HK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Cantonese (Hong Kong)', service="")


class MozttsAndroidEnIn(ResponsiveVoice):
    uri = "moz-tts:android:en_IN"
    name = "English (India)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:en_IN', 'lang': 'en-IN', 'gender': 'female', 'name': 'English (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='English (India)', service="")


class MozttsAndroidEsUs(ResponsiveVoice):
    uri = "moz-tts:android:es_US"
    name = "Spanish (United States)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:es_US', 'lang': 'es-US', 'gender': 'female', 'name': 'Spanish (United States)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Spanish (United States)', service="")


class MozttsAndroidJvId(ResponsiveVoice):
    uri = "moz-tts:android:jv_ID"
    name = "Javanese (Indonesia)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:jv_ID', 'lang': 'jv-ID', 'gender': 'female', 'name': 'Javanese (Indonesia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="jv-ID", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Javanese (Indonesia)', service="")


class MozttsAndroidLa(ResponsiveVoice):
    uri = "moz-tts:android:la"
    name = "Latin"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:la', 'lang': 'la', 'deprecated': True, 'name': 'Latin'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="la", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Latin', service="")


class MozttsAndroidInId(ResponsiveVoice):
    uri = "moz-tts:android:in_ID"
    name = "Indonesian (Indonesia)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:in_ID', 'lang': 'in-ID', 'gender': 'female', 'name': 'Indonesian (Indonesia)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="in-ID", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Indonesian (Indonesia)', service="")


class MozttsAndroidTeIn(ResponsiveVoice):
    uri = "moz-tts:android:te_IN"
    name = "Telugu (India)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:te_IN', 'lang': 'te-IN', 'gender': 'female', 'name': 'Telugu (India)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="te-IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Telugu (India)', service="")


class MozttsAndroidRoRo(ResponsiveVoice):
    uri = "moz-tts:android:ro_RO"
    name = "Romanian (Romania)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:ro_RO', 'lang': 'ro-RO', 'gender': 'female', 'name': 'Romanian (Romania)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ro-RO", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Romanian (Romania)', service="")


class MozttsAndroidCa(ResponsiveVoice):
    uri = "moz-tts:android:ca"
    name = "Catalan"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:ca', 'lang': 'ca', 'gender': 'female', 'name': 'Catalan'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ca", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Catalan', service="")


class MozttsAndroidEnGb(ResponsiveVoice):
    uri = "moz-tts:android:en_GB"
    name = "English (United Kingdom)"
    voiceIDs = []
    _raw = {'voiceURI': 'moz-tts:android:en_GB', 'lang': 'en-GB', 'gender': 'female',
            'name': 'English (United Kingdom)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='English (United Kingdom)', service="")


class ComAppleTtsbundleRishicompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Rishi-compact"
    name = "Rishi"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Rishi-compact', 'lang': 'en-IN', 'gender': 'male', 'name': 'Rishi'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Rishi', service="")


class Heil(ResponsiveVoice):
    uri = "he-IL"
    name = "he-IL"
    voiceIDs = []
    _raw = {'voiceURI': 'he-IL', 'lang': 'he-IL', 'name': 'he-IL'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="he-IL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='he-IL', service="")


class Thth(ResponsiveVoice):
    uri = "th-TH"
    name = "th-TH"
    voiceIDs = []
    _raw = {'voiceURI': 'th-TH', 'lang': 'th-TH', 'name': 'th-TH'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th-TH", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='th-TH', service="")


class Ptbr(ResponsiveVoice):
    uri = "pt-BR"
    name = "pt-BR"
    voiceIDs = []
    _raw = {'voiceURI': 'pt-BR', 'lang': 'pt-BR', 'name': 'pt-BR'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='pt-BR', service="")


class Sksk(ResponsiveVoice):
    uri = "sk-SK"
    name = "sk-SK"
    voiceIDs = []
    _raw = {'voiceURI': 'sk-SK', 'lang': 'sk-SK', 'name': 'sk-SK'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk-SK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='sk-SK', service="")


class Frca(ResponsiveVoice):
    uri = "fr-CA"
    name = "fr-CA"
    voiceIDs = []
    _raw = {'voiceURI': 'fr-CA', 'lang': 'fr-CA', 'name': 'fr-CA'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-CA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='fr-CA', service="")


class Roro(ResponsiveVoice):
    uri = "ro-RO"
    name = "ro-RO"
    voiceIDs = []
    _raw = {'voiceURI': 'ro-RO', 'lang': 'ro-RO', 'name': 'ro-RO'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ro-RO", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='ro-RO', service="")


class Nono(ResponsiveVoice):
    uri = "no-NO"
    name = "no-NO"
    voiceIDs = []
    _raw = {'voiceURI': 'no-NO', 'lang': 'no-NO', 'name': 'no-NO'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="no-NO", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='no-NO', service="")


class Fifi(ResponsiveVoice):
    uri = "fi-FI"
    name = "fi-FI"
    voiceIDs = []
    _raw = {'voiceURI': 'fi-FI', 'lang': 'fi-FI', 'name': 'fi-FI'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi-FI", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='fi-FI', service="")


class Plpl(ResponsiveVoice):
    uri = "pl-PL"
    name = "pl-PL"
    voiceIDs = []
    _raw = {'voiceURI': 'pl-PL', 'lang': 'pl-PL', 'name': 'pl-PL'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='pl-PL', service="")


class Dede(ResponsiveVoice):
    uri = "de-DE"
    name = "de-DE"
    voiceIDs = []
    _raw = {'voiceURI': 'de-DE', 'lang': 'de-DE', 'name': 'de-DE'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='de-DE', service="")


class Nlnl(ResponsiveVoice):
    uri = "nl-NL"
    name = "nl-NL"
    voiceIDs = []
    _raw = {'voiceURI': 'nl-NL', 'lang': 'nl-NL', 'name': 'nl-NL'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-NL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='nl-NL', service="")


class Idid(ResponsiveVoice):
    uri = "id-ID"
    name = "id-ID"
    voiceIDs = []
    _raw = {'voiceURI': 'id-ID', 'lang': 'id-ID', 'name': 'id-ID'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id-ID", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='id-ID', service="")


class Trtr(ResponsiveVoice):
    uri = "tr-TR"
    name = "tr-TR"
    voiceIDs = []
    _raw = {'voiceURI': 'tr-TR', 'lang': 'tr-TR', 'name': 'tr-TR'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr-TR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='tr-TR', service="")


class Itit(ResponsiveVoice):
    uri = "it-IT"
    name = "it-IT"
    voiceIDs = []
    _raw = {'voiceURI': 'it-IT', 'lang': 'it-IT', 'name': 'it-IT'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='it-IT', service="")


class Ptpt(ResponsiveVoice):
    uri = "pt-PT"
    name = "pt-PT"
    voiceIDs = []
    _raw = {'voiceURI': 'pt-PT', 'lang': 'pt-PT', 'name': 'pt-PT'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-PT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='pt-PT', service="")


class Frfr(ResponsiveVoice):
    uri = "fr-FR"
    name = "fr-FR"
    voiceIDs = []
    _raw = {'voiceURI': 'fr-FR', 'lang': 'fr-FR', 'name': 'fr-FR'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='fr-FR', service="")


class Ruru(ResponsiveVoice):
    uri = "ru-RU"
    name = "ru-RU"
    voiceIDs = []
    _raw = {'voiceURI': 'ru-RU', 'lang': 'ru-RU', 'name': 'ru-RU'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='ru-RU', service="")


class Esmx(ResponsiveVoice):
    uri = "es-MX"
    name = "es-MX"
    voiceIDs = []
    _raw = {'voiceURI': 'es-MX', 'lang': 'es-MX', 'name': 'es-MX'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='es-MX', service="")


class Zhhk(ResponsiveVoice):
    uri = "zh-HK"
    name = "zh-HK"
    voiceIDs = []
    _raw = {'voiceURI': 'zh-HK', 'lang': 'zh-HK', 'name': 'zh-HK'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='zh-HK', service="")


class Svse(ResponsiveVoice):
    uri = "sv-SE"
    name = "sv-SE"
    voiceIDs = []
    _raw = {'voiceURI': 'sv-SE', 'lang': 'sv-SE', 'name': 'sv-SE'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sv-SE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='sv-SE', service="")


class Huhu(ResponsiveVoice):
    uri = "hu-HU"
    name = "hu-HU"
    voiceIDs = []
    _raw = {'voiceURI': 'hu-HU', 'lang': 'hu-HU', 'name': 'hu-HU'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu-HU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='hu-HU', service="")


class Zhtw(ResponsiveVoice):
    uri = "zh-TW"
    name = "zh-TW"
    voiceIDs = []
    _raw = {'voiceURI': 'zh-TW', 'lang': 'zh-TW', 'name': 'zh-TW'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='zh-TW', service="")


class Eses(ResponsiveVoice):
    uri = "es-ES"
    name = "es-ES"
    voiceIDs = []
    _raw = {'voiceURI': 'es-ES', 'lang': 'es-ES', 'name': 'es-ES'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='es-ES', service="")


class Zhcn(ResponsiveVoice):
    uri = "zh-CN"
    name = "zh-CN"
    voiceIDs = []
    _raw = {'voiceURI': 'zh-CN', 'lang': 'zh-CN', 'name': 'zh-CN'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='zh-CN', service="")


class Nlbe(ResponsiveVoice):
    uri = "nl-BE"
    name = "nl-BE"
    voiceIDs = []
    _raw = {'voiceURI': 'nl-BE', 'lang': 'nl-BE', 'name': 'nl-BE'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-BE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='nl-BE', service="")


class Engb(ResponsiveVoice):
    uri = "en-GB"
    name = "en-GB"
    voiceIDs = []
    _raw = {'voiceURI': 'en-GB', 'lang': 'en-GB', 'name': 'en-GB'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='en-GB', service="")


class Arsa(ResponsiveVoice):
    uri = "ar-SA"
    name = "ar-SA"
    voiceIDs = []
    _raw = {'voiceURI': 'ar-SA', 'lang': 'ar-SA', 'name': 'ar-SA'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar-SA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='ar-SA', service="")


class Kokr(ResponsiveVoice):
    uri = "ko-KR"
    name = "ko-KR"
    voiceIDs = []
    _raw = {'voiceURI': 'ko-KR', 'lang': 'ko-KR', 'name': 'ko-KR'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='ko-KR', service="")


class Cscz(ResponsiveVoice):
    uri = "cs-CZ"
    name = "cs-CZ"
    voiceIDs = []
    _raw = {'voiceURI': 'cs-CZ', 'lang': 'cs-CZ', 'name': 'cs-CZ'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs-CZ", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='cs-CZ', service="")


class Enza(ResponsiveVoice):
    uri = "en-ZA"
    name = "en-ZA"
    voiceIDs = []
    _raw = {'voiceURI': 'en-ZA', 'lang': 'en-ZA', 'name': 'en-ZA'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-ZA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='en-ZA', service="")


class Enau(ResponsiveVoice):
    uri = "en-AU"
    name = "en-AU"
    voiceIDs = []
    _raw = {'voiceURI': 'en-AU', 'lang': 'en-AU', 'name': 'en-AU'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='en-AU', service="")


class Dadk(ResponsiveVoice):
    uri = "da-DK"
    name = "da-DK"
    voiceIDs = []
    _raw = {'voiceURI': 'da-DK', 'lang': 'da-DK', 'name': 'da-DK'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da-DK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='da-DK', service="")


class Enus(ResponsiveVoice):
    uri = "en-US"
    name = "en-US"
    voiceIDs = []
    _raw = {'voiceURI': 'en-US', 'lang': 'en-US', 'name': 'en-US'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='en-US', service="")


class Enie(ResponsiveVoice):
    uri = "en-IE"
    name = "en-IE"
    voiceIDs = []
    _raw = {'voiceURI': 'en-IE', 'lang': 'en-IE', 'name': 'en-IE'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='en-IE', service="")


class Hiin(ResponsiveVoice):
    uri = "hi-IN"
    name = "hi-IN"
    voiceIDs = []
    _raw = {'voiceURI': 'hi-IN', 'lang': 'hi-IN', 'name': 'hi-IN'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='hi-IN', service="")


class Elgr(ResponsiveVoice):
    uri = "el-GR"
    name = "el-GR"
    voiceIDs = []
    _raw = {'voiceURI': 'el-GR', 'lang': 'el-GR', 'name': 'el-GR'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el-GR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='el-GR', service="")


class Jajp(ResponsiveVoice):
    uri = "ja-JP"
    name = "ja-JP"
    voiceIDs = []
    _raw = {'voiceURI': 'ja-JP', 'lang': 'ja-JP', 'name': 'ja-JP'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='ja-JP', service="")


class ComAppleTtsbundleMagedcompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Maged-compact"
    name = "Maged"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Maged-compact', 'lang': 'ar-SA', 'localService': True, 'default': True,
            'name': 'Maged'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar-SA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Maged', service="")


class ComAppleTtsbundleZuzanacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Zuzana-compact"
    name = "Zuzana"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Zuzana-compact', 'lang': 'cs-CZ', 'localService': True, 'default': True,
            'name': 'Zuzana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs-CZ", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Zuzana', service="")


class ComAppleTtsbundleSaracompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Sara-compact"
    name = "Sara"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Sara-compact', 'lang': 'da-DK', 'localService': True, 'default': True,
            'name': 'Sara'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da-DK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Sara', service="")


class ComAppleTtsbundleAnnacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Anna-compact"
    name = "Anna"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Anna-compact', 'lang': 'de-DE', 'localService': True, 'default': True,
            'name': 'Anna'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Anna', service="")


class ComAppleTtsbundleMelinacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Melina-compact"
    name = "Melina"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Melina-compact', 'lang': 'el-GR', 'localService': True, 'default': True,
            'name': 'Melina'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el-GR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Melina', service="")


class ComAppleTtsbundleKarencompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Karen-compact"
    name = "Karen"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Karen-compact', 'lang': 'en-AU', 'localService': True, 'default': True,
            'name': 'Karen'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Karen', service="")


class ComAppleTtsbundleDanielcompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Daniel-compact"
    name = "Daniel"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Daniel-compact', 'lang': 'en-GB', 'localService': True, 'default': True,
            'name': 'Daniel'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Daniel', service="")


class ComAppleTtsbundleMoiracompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Moira-compact"
    name = "Moira"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Moira-compact', 'lang': 'en-IE', 'localService': True, 'default': True,
            'name': 'Moira'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Moira', service="")


class ComAppleTtsbundleSamanthapremium(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Samantha-premium"
    name = "Samantha (Enhanced)"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Samantha-premium', 'lang': 'en-US', 'localService': True, 'default': True,
            'name': 'Samantha (Enhanced)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Samantha (Enhanced)', service="")


class ComAppleTtsbundleSamanthacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Samantha-compact"
    name = "Samantha"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Samantha-compact', 'lang': 'en-US', 'localService': True, 'default': True,
            'name': 'Samantha'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Samantha', service="")


class ComAppleTtsbundleTessacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Tessa-compact"
    name = "Tessa"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Tessa-compact', 'lang': 'en-ZA', 'localService': True, 'default': True,
            'name': 'Tessa'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-ZA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Tessa', service="")


class ComAppleTtsbundleMonicacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Monica-compact"
    name = "Monica"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Monica-compact', 'lang': 'es-ES', 'localService': True, 'default': True,
            'name': 'Monica'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Monica', service="")


class ComAppleTtsbundlePaulinacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Paulina-compact"
    name = "Paulina"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Paulina-compact', 'lang': 'es-MX', 'localService': True, 'default': True,
            'name': 'Paulina'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Paulina', service="")


class ComAppleTtsbundleSatucompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Satu-compact"
    name = "Satu"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Satu-compact', 'lang': 'fi-FI', 'localService': True, 'default': True,
            'name': 'Satu'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi-FI", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Satu', service="")


class ComAppleTtsbundleAmeliecompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Amelie-compact"
    name = "Amelie"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Amelie-compact', 'lang': 'fr-CA', 'localService': True, 'default': True,
            'name': 'Amelie'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-CA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Amelie', service="")


class ComAppleTtsbundleThomascompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Thomas-compact"
    name = "Thomas"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Thomas-compact', 'lang': 'fr-FR', 'localService': True, 'default': True,
            'name': 'Thomas'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Thomas', service="")


class ComAppleTtsbundleCarmitcompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Carmit-compact"
    name = "Carmit"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Carmit-compact', 'lang': 'he-IL', 'localService': True, 'default': True,
            'name': 'Carmit'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="he-IL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Carmit', service="")


class ComAppleTtsbundleLekhacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Lekha-compact"
    name = "Lekha"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Lekha-compact', 'lang': 'hi-IN', 'localService': True, 'default': True,
            'name': 'Lekha'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Lekha', service="")


class ComAppleTtsbundleMariskacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Mariska-compact"
    name = "Mariska"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Mariska-compact', 'lang': 'hu-HU', 'localService': True, 'default': True,
            'name': 'Mariska'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu-HU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Mariska', service="")


class ComAppleTtsbundleDamayanticompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Damayanti-compact"
    name = "Damayanti"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Damayanti-compact', 'lang': 'id-ID', 'localService': True, 'default': True,
            'name': 'Damayanti'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id-ID", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Damayanti', service="")


class ComAppleTtsbundleAlicecompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Alice-compact"
    name = "Alice"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Alice-compact', 'lang': 'it-IT', 'localService': True, 'default': True,
            'name': 'Alice'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Alice', service="")


class ComAppleTtsbundleKyokocompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Kyoko-compact"
    name = "Kyoko"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Kyoko-compact', 'lang': 'ja-JP', 'localService': True, 'default': True,
            'name': 'Kyoko'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Kyoko', service="")


class ComAppleTtsbundleYunacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Yuna-compact"
    name = "Yuna"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Yuna-compact', 'lang': 'ko-KR', 'localService': True, 'default': True,
            'name': 'Yuna'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Yuna', service="")


class ComAppleTtsbundleEllencompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Ellen-compact"
    name = "Ellen"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Ellen-compact', 'lang': 'nl-BE', 'localService': True, 'default': True,
            'name': 'Ellen'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-BE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ellen', service="")


class ComAppleTtsbundleXandercompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Xander-compact"
    name = "Xander"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Xander-compact', 'lang': 'nl-NL', 'localService': True, 'default': True,
            'name': 'Xander'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-NL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Xander', service="")


class ComAppleTtsbundleNoracompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Nora-compact"
    name = "Nora"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Nora-compact', 'lang': 'no-NO', 'localService': True, 'default': True,
            'name': 'Nora'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="no-NO", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Nora', service="")


class ComAppleTtsbundleZosiacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Zosia-compact"
    name = "Zosia"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Zosia-compact', 'lang': 'pl-PL', 'localService': True, 'default': True,
            'name': 'Zosia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Zosia', service="")


class ComAppleTtsbundleLucianacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Luciana-compact"
    name = "Luciana"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Luciana-compact', 'lang': 'pt-BR', 'localService': True, 'default': True,
            'name': 'Luciana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Luciana', service="")


class ComAppleTtsbundleJoanacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Joana-compact"
    name = "Joana"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Joana-compact', 'lang': 'pt-PT', 'localService': True, 'default': True,
            'name': 'Joana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-PT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Joana', service="")


class ComAppleTtsbundleIoanacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Ioana-compact"
    name = "Ioana"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Ioana-compact', 'lang': 'ro-RO', 'localService': True, 'default': True,
            'name': 'Ioana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ro-RO", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ioana', service="")


class ComAppleTtsbundleMilenacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Milena-compact"
    name = "Milena"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Milena-compact', 'lang': 'ru-RU', 'localService': True, 'default': True,
            'name': 'Milena'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Milena', service="")


class ComAppleTtsbundleLauracompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Laura-compact"
    name = "Laura"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Laura-compact', 'lang': 'sk-SK', 'localService': True, 'default': True,
            'name': 'Laura'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk-SK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Laura', service="")


class ComAppleTtsbundleAlvacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Alva-compact"
    name = "Alva"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Alva-compact', 'lang': 'sv-SE', 'localService': True, 'default': True,
            'name': 'Alva'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sv-SE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Alva', service="")


class ComAppleTtsbundleKanyacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Kanya-compact"
    name = "Kanya"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Kanya-compact', 'lang': 'th-TH', 'localService': True, 'default': True,
            'name': 'Kanya'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th-TH", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Kanya', service="")


class ComAppleTtsbundleYeldacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Yelda-compact"
    name = "Yelda"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Yelda-compact', 'lang': 'tr-TR', 'localService': True, 'default': True,
            'name': 'Yelda'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr-TR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Yelda', service="")


class ComAppleTtsbundleTingtingcompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Ting-Ting-compact"
    name = "Ting-Ting"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Ting-Ting-compact', 'lang': 'zh-CN', 'localService': True, 'default': True,
            'name': 'Ting-Ting'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ting-Ting', service="")


class ComAppleTtsbundleSinjicompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Sin-Ji-compact"
    name = "Sin-Ji"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Sin-Ji-compact', 'lang': 'zh-HK', 'localService': True, 'default': True,
            'name': 'Sin-Ji'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Sin-Ji', service="")


class ComAppleTtsbundleMeijiacompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Mei-Jia-compact"
    name = "Mei-Jia"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Mei-Jia-compact', 'lang': 'zh-TW', 'localService': True, 'default': True,
            'name': 'Mei-Jia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Mei-Jia', service="")


class ComAppleTtsbundleMagedcompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Maged-compact"
    name = "Maged"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Maged-compact', 'lang': 'ar-SA', 'name': 'Maged'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar-SA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Maged', service="")


class ComAppleTtsbundleZuzanacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Zuzana-compact"
    name = "Zuzana"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Zuzana-compact', 'lang': 'cs-CZ', 'name': 'Zuzana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs-CZ", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Zuzana', service="")


class ComAppleTtsbundleSaracompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Sara-compact"
    name = "Sara"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Sara-compact', 'lang': 'da-DK', 'name': 'Sara'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da-DK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Sara', service="")


class ComAppleTtsbundleAnnacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Anna-compact"
    name = "Anna"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Anna-compact', 'lang': 'de-DE', 'name': 'Anna'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Anna', service="")


class ComAppleTtsbundleSiriFemaleDedeCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_de-DE_compact"
    name = "Helena"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_de-DE_compact', 'lang': 'de-DE', 'name': 'Helena'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Helena', service="")


class ComAppleTtsbundleSiriMaleDedeCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_de-DE_compact"
    name = "Martin"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_de-DE_compact', 'lang': 'de-DE', 'name': 'Martin'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Martin', service="")


class ComAppleTtsbundleNikospremium(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Nikos-premium"
    name = "Nikos (Enhanced)"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Nikos-premium', 'lang': 'el-GR', 'name': 'Nikos (Enhanced)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el-GR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Nikos (Enhanced)', service="")


class ComAppleTtsbundleMelinacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Melina-compact"
    name = "Melina"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Melina-compact', 'lang': 'el-GR', 'name': 'Melina'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el-GR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Melina', service="")


class ComAppleTtsbundleNikoscompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Nikos-compact"
    name = "Nikos"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Nikos-compact', 'lang': 'el-GR', 'name': 'Nikos'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el-GR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Nikos', service="")


class ComAppleTtsbundleSiriFemaleEnauCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_en-AU_compact"
    name = "Catherine"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_en-AU_compact', 'lang': 'en-AU', 'name': 'Catherine'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Catherine', service="")


class ComAppleTtsbundleSiriMaleEnauCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_en-AU_compact"
    name = "Gordon"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_en-AU_compact', 'lang': 'en-AU', 'name': 'Gordon'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Gordon', service="")


class ComAppleTtsbundleKarencompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Karen-compact"
    name = "Karen"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Karen-compact', 'lang': 'en-AU', 'name': 'Karen'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Karen', service="")


class ComAppleTtsbundleDanielpremium(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Daniel-premium"
    name = "Daniel (Enhanced)"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Daniel-premium', 'lang': 'en-GB', 'name': 'Daniel (Enhanced)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Daniel (Enhanced)', service="")


class ComAppleTtsbundleSiriMaleEngbCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_en-GB_compact"
    name = "Arthur"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_en-GB_compact', 'lang': 'en-GB', 'name': 'Arthur'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Arthur', service="")


class ComAppleTtsbundleDanielcompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Daniel-compact"
    name = "Daniel"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Daniel-compact', 'lang': 'en-GB', 'name': 'Daniel'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Daniel', service="")


class ComAppleTtsbundleSiriFemaleEngbCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_en-GB_compact"
    name = "Martha"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_en-GB_compact', 'lang': 'en-GB', 'name': 'Martha'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Martha', service="")


class ComAppleTtsbundleMoiracompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Moira-compact"
    name = "Moira"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Moira-compact', 'lang': 'en-IE', 'name': 'Moira'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Moira', service="")


class ComAppleTtsbundleSiriFemaleEnusPremium(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_en-US_premium"
    name = "Nicky (Enhanced)"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_en-US_premium', 'lang': 'en-US', 'name': 'Nicky (Enhanced)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Nicky (Enhanced)', service="")


class ComAppleTtsbundleSamanthapremiumAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Samantha-premium"
    name = "Samantha (Enhanced)"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Samantha-premium', 'lang': 'en-US', 'name': 'Samantha (Enhanced)'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Samantha (Enhanced)', service="")


class ComAppleTtsbundleSiriMaleEnusCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_en-US_compact"
    name = "Aaron"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_en-US_compact', 'lang': 'en-US', 'name': 'Aaron'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Aaron', service="")


class ComAppleSpeechSynthesisVoiceFred(ResponsiveVoice):
    uri = "com.apple.speech.synthesis.voice.Fred"
    name = "Fred"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.speech.synthesis.voice.Fred', 'lang': 'en-US', 'name': 'Fred'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fred', service="")


class ComAppleTtsbundleSiriFemaleEnusCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_en-US_compact"
    name = "Nicky"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_en-US_compact', 'lang': 'en-US', 'name': 'Nicky'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Nicky', service="")


class ComAppleTtsbundleSamanthacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Samantha-compact"
    name = "Samantha"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Samantha-compact', 'lang': 'en-US', 'name': 'Samantha'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Samantha', service="")


class ComAppleTtsbundleTessacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Tessa-compact"
    name = "Tessa"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Tessa-compact', 'lang': 'en-ZA', 'name': 'Tessa'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-ZA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Tessa', service="")


class ComAppleTtsbundleMonicacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Monica-compact"
    name = "Monica"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Monica-compact', 'lang': 'es-ES', 'name': 'Monica'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Monica', service="")


class ComAppleTtsbundlePaulinacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Paulina-compact"
    name = "Paulina"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Paulina-compact', 'lang': 'es-MX', 'name': 'Paulina'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Paulina', service="")


class ComAppleTtsbundleSatucompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Satu-compact"
    name = "Satu"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Satu-compact', 'lang': 'fi-FI', 'name': 'Satu'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi-FI", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Satu', service="")


class ComAppleTtsbundleAmeliecompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Amelie-compact"
    name = "Amelie"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Amelie-compact', 'lang': 'fr-CA', 'name': 'Amelie'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-CA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Amelie', service="")


class ComAppleTtsbundleSiriMaleFrfrCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_fr-FR_compact"
    name = "Daniel"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_fr-FR_compact', 'lang': 'fr-FR', 'name': 'Daniel'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Daniel', service="")


class ComAppleTtsbundleSiriFemaleFrfrCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_fr-FR_compact"
    name = "Marie"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_fr-FR_compact', 'lang': 'fr-FR', 'name': 'Marie'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Marie', service="")


class ComAppleTtsbundleThomascompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Thomas-compact"
    name = "Thomas"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Thomas-compact', 'lang': 'fr-FR', 'name': 'Thomas'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Thomas', service="")


class ComAppleTtsbundleCarmitcompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Carmit-compact"
    name = "Carmit"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Carmit-compact', 'lang': 'he-IL', 'name': 'Carmit'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="he-IL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Carmit', service="")


class ComAppleTtsbundleLekhacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Lekha-compact"
    name = "Lekha"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Lekha-compact', 'lang': 'hi-IN', 'name': 'Lekha'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Lekha', service="")


class ComAppleTtsbundleMariskacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Mariska-compact"
    name = "Mariska"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Mariska-compact', 'lang': 'hu-HU', 'name': 'Mariska'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu-HU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Mariska', service="")


class ComAppleTtsbundleDamayanticompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Damayanti-compact"
    name = "Damayanti"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Damayanti-compact', 'lang': 'id-ID', 'name': 'Damayanti'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id-ID", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Damayanti', service="")


class ComAppleTtsbundleAlicecompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Alice-compact"
    name = "Alice"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Alice-compact', 'lang': 'it-IT', 'name': 'Alice'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Alice', service="")


class ComAppleTtsbundleSiriMaleJajpCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_ja-JP_compact"
    name = "Hattori"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_ja-JP_compact', 'lang': 'ja-JP', 'name': 'Hattori'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Hattori', service="")


class ComAppleTtsbundleKyokocompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Kyoko-compact"
    name = "Kyoko"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Kyoko-compact', 'lang': 'ja-JP', 'name': 'Kyoko'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Kyoko', service="")


class ComAppleTtsbundleSiriFemaleJajpCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_ja-JP_compact"
    name = "O-ren"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_ja-JP_compact', 'lang': 'ja-JP', 'name': 'O-ren'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='O-ren', service="")


class ComAppleTtsbundleYunacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Yuna-compact"
    name = "Yuna"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Yuna-compact', 'lang': 'ko-KR', 'name': 'Yuna'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Yuna', service="")


class ComAppleTtsbundleEllencompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Ellen-compact"
    name = "Ellen"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Ellen-compact', 'lang': 'nl-BE', 'name': 'Ellen'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-BE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ellen', service="")


class ComAppleTtsbundleXandercompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Xander-compact"
    name = "Xander"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Xander-compact', 'lang': 'nl-NL', 'name': 'Xander'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-NL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Xander', service="")


class ComAppleTtsbundleNoracompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Nora-compact"
    name = "Nora"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Nora-compact', 'lang': 'no-NO', 'name': 'Nora'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="no-NO", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Nora', service="")


class ComAppleTtsbundleZosiacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Zosia-compact"
    name = "Zosia"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Zosia-compact', 'lang': 'pl-PL', 'name': 'Zosia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Zosia', service="")


class ComAppleTtsbundleLucianacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Luciana-compact"
    name = "Luciana"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Luciana-compact', 'lang': 'pt-BR', 'name': 'Luciana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Luciana', service="")


class ComAppleTtsbundleJoanacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Joana-compact"
    name = "Joana"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Joana-compact', 'lang': 'pt-PT', 'name': 'Joana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-PT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Joana', service="")


class ComAppleTtsbundleIoanacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Ioana-compact"
    name = "Ioana"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Ioana-compact', 'lang': 'ro-RO', 'name': 'Ioana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ro-RO", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ioana', service="")


class ComAppleTtsbundleMilenacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Milena-compact"
    name = "Milena"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Milena-compact', 'lang': 'ru-RU', 'name': 'Milena'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Milena', service="")


class ComAppleTtsbundleLauracompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Laura-compact"
    name = "Laura"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Laura-compact', 'lang': 'sk-SK', 'name': 'Laura'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk-SK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Laura', service="")


class ComAppleTtsbundleAlvacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Alva-compact"
    name = "Alva"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Alva-compact', 'lang': 'sv-SE', 'name': 'Alva'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sv-SE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Alva', service="")


class ComAppleTtsbundleKanyacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Kanya-compact"
    name = "Kanya"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Kanya-compact', 'lang': 'th-TH', 'name': 'Kanya'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th-TH", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Kanya', service="")


class ComAppleTtsbundleYeldacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Yelda-compact"
    name = "Yelda"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Yelda-compact', 'lang': 'tr-TR', 'name': 'Yelda'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr-TR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Yelda', service="")


class ComAppleTtsbundleSiriMaleZhcnCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_zh-CN_compact"
    name = "Li-mu"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_zh-CN_compact', 'lang': 'zh-CN', 'name': 'Li-mu'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Li-mu', service="")


class ComAppleTtsbundleTingtingcompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Ting-Ting-compact"
    name = "Ting-Ting"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Ting-Ting-compact', 'lang': 'zh-CN', 'name': 'Ting-Ting'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ting-Ting', service="")


class ComAppleTtsbundleSiriFemaleZhcnCompact(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_zh-CN_compact"
    name = "Yu-shu"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_zh-CN_compact', 'lang': 'zh-CN', 'name': 'Yu-shu'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Yu-shu', service="")


class ComAppleTtsbundleSinjicompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Sin-Ji-compact"
    name = "Sin-Ji"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Sin-Ji-compact', 'lang': 'zh-HK', 'name': 'Sin-Ji'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Sin-Ji', service="")


class ComAppleTtsbundleMeijiacompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Mei-Jia-compact"
    name = "Mei-Jia"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Mei-Jia-compact', 'lang': 'zh-TW', 'name': 'Mei-Jia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Mei-Jia', service="")


class ComAppleTtsbundleMagedcompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Maged-compact"
    name = "Maged"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Maged-compact', 'lang': 'ar-SA', 'name': 'Maged'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar-SA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Maged', service="")


class ComAppleTtsbundleZuzanacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Zuzana-compact"
    name = "Zuzana"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Zuzana-compact', 'lang': 'cs-CZ', 'name': 'Zuzana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs-CZ", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Zuzana', service="")


class ComAppleTtsbundleSaracompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Sara-compact"
    name = "Sara"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Sara-compact', 'lang': 'da-DK', 'name': 'Sara'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da-DK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Sara', service="")


class ComAppleTtsbundleAnnacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Anna-compact"
    name = "Anna"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Anna-compact', 'lang': 'de-DE', 'name': 'Anna'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Anna', service="")


class ComAppleTtsbundleSiriFemaleDedeCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_de-DE_compact"
    name = "Helena"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_de-DE_compact', 'lang': 'de-DE', 'name': 'Helena'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Helena', service="")


class ComAppleTtsbundleSiriMaleDedeCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_de-DE_compact"
    name = "Martin"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_de-DE_compact', 'lang': 'de-DE', 'name': 'Martin'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Martin', service="")


class ComAppleTtsbundleMelinacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Melina-compact"
    name = "Melina"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Melina-compact', 'lang': 'el-GR', 'name': 'Melina'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el-GR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Melina', service="")


class ComAppleTtsbundleSiriFemaleEnauCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_en-AU_compact"
    name = "Catherine"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_en-AU_compact', 'lang': 'en-AU', 'name': 'Catherine'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Catherine', service="")


class ComAppleTtsbundleSiriMaleEnauCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_en-AU_compact"
    name = "Gordon"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_en-AU_compact', 'lang': 'en-AU', 'name': 'Gordon'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Gordon', service="")


class ComAppleTtsbundleKarencompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Karen-compact"
    name = "Karen"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Karen-compact', 'lang': 'en-AU', 'name': 'Karen'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Karen', service="")


class ComAppleTtsbundleSiriMaleEngbCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_en-GB_compact"
    name = "Arthur"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_en-GB_compact', 'lang': 'en-GB', 'name': 'Arthur'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Arthur', service="")


class ComAppleTtsbundleDanielcompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Daniel-compact"
    name = "Daniel"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Daniel-compact', 'lang': 'en-GB', 'name': 'Daniel'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Daniel', service="")


class ComAppleTtsbundleSiriFemaleEngbCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_en-GB_compact"
    name = "Martha"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_en-GB_compact', 'lang': 'en-GB', 'name': 'Martha'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Martha', service="")


class ComAppleTtsbundleMoiracompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Moira-compact"
    name = "Moira"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Moira-compact', 'lang': 'en-IE', 'name': 'Moira'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Moira', service="")


class ComAppleTtsbundleSiriMaleEnusCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_en-US_compact"
    name = "Aaron"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_en-US_compact', 'lang': 'en-US', 'name': 'Aaron'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Aaron', service="")


class ComAppleSpeechSynthesisVoiceFredAlt(ResponsiveVoice):
    uri = "com.apple.speech.synthesis.voice.Fred"
    name = "Fred"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.speech.synthesis.voice.Fred', 'lang': 'en-US', 'name': 'Fred'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Fred', service="")


class ComAppleTtsbundleSiriFemaleEnusCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_en-US_compact"
    name = "Nicky"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_en-US_compact', 'lang': 'en-US', 'name': 'Nicky'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Nicky', service="")


class ComAppleTtsbundleSamanthacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Samantha-compact"
    name = "Samantha"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Samantha-compact', 'lang': 'en-US', 'name': 'Samantha'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Samantha', service="")


class ComAppleTtsbundleTessacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Tessa-compact"
    name = "Tessa"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Tessa-compact', 'lang': 'en-ZA', 'name': 'Tessa'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-ZA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Tessa', service="")


class ComAppleTtsbundleMonicacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Monica-compact"
    name = "Monica"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Monica-compact', 'lang': 'es-ES', 'name': 'Monica'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Monica', service="")


class ComAppleTtsbundlePaulinacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Paulina-compact"
    name = "Paulina"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Paulina-compact', 'lang': 'es-MX', 'name': 'Paulina'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Paulina', service="")


class ComAppleTtsbundleSatucompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Satu-compact"
    name = "Satu"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Satu-compact', 'lang': 'fi-FI', 'name': 'Satu'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi-FI", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Satu', service="")


class ComAppleTtsbundleAmeliecompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Amelie-compact"
    name = "Amelie"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Amelie-compact', 'lang': 'fr-CA', 'name': 'Amelie'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-CA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Amelie', service="")


class ComAppleTtsbundleSiriMaleFrfrCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_fr-FR_compact"
    name = "Daniel"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_fr-FR_compact', 'lang': 'fr-FR', 'name': 'Daniel'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Daniel', service="")


class ComAppleTtsbundleSiriFemaleFrfrCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_fr-FR_compact"
    name = "Marie"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_fr-FR_compact', 'lang': 'fr-FR', 'name': 'Marie'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Marie', service="")


class ComAppleTtsbundleThomascompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Thomas-compact"
    name = "Thomas"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Thomas-compact', 'lang': 'fr-FR', 'name': 'Thomas'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Thomas', service="")


class ComAppleTtsbundleCarmitcompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Carmit-compact"
    name = "Carmit"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Carmit-compact', 'lang': 'he-IL', 'name': 'Carmit'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="he-IL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Carmit', service="")


class ComAppleTtsbundleLekhacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Lekha-compact"
    name = "Lekha"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Lekha-compact', 'lang': 'hi-IN', 'name': 'Lekha'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Lekha', service="")


class ComAppleTtsbundleMariskacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Mariska-compact"
    name = "Mariska"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Mariska-compact', 'lang': 'hu-HU', 'name': 'Mariska'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu-HU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Mariska', service="")


class ComAppleTtsbundleDamayanticompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Damayanti-compact"
    name = "Damayanti"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Damayanti-compact', 'lang': 'id-ID', 'name': 'Damayanti'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id-ID", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Damayanti', service="")


class ComAppleTtsbundleAlicecompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Alice-compact"
    name = "Alice"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Alice-compact', 'lang': 'it-IT', 'name': 'Alice'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Alice', service="")


class ComAppleTtsbundleSiriMaleJajpCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_ja-JP_compact"
    name = "Hattori"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_ja-JP_compact', 'lang': 'ja-JP', 'name': 'Hattori'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Hattori', service="")


class ComAppleTtsbundleKyokocompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Kyoko-compact"
    name = "Kyoko"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Kyoko-compact', 'lang': 'ja-JP', 'name': 'Kyoko'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Kyoko', service="")


class ComAppleTtsbundleSiriFemaleJajpCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_ja-JP_compact"
    name = "O-ren"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_ja-JP_compact', 'lang': 'ja-JP', 'name': 'O-ren'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='O-ren', service="")


class ComAppleTtsbundleYunacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Yuna-compact"
    name = "Yuna"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Yuna-compact', 'lang': 'ko-KR', 'name': 'Yuna'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Yuna', service="")


class ComAppleTtsbundleEllencompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Ellen-compact"
    name = "Ellen"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Ellen-compact', 'lang': 'nl-BE', 'name': 'Ellen'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-BE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ellen', service="")


class ComAppleTtsbundleXandercompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Xander-compact"
    name = "Xander"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Xander-compact', 'lang': 'nl-NL', 'name': 'Xander'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-NL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Xander', service="")


class ComAppleTtsbundleNoracompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Nora-compact"
    name = "Nora"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Nora-compact', 'lang': 'no-NO', 'name': 'Nora'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="no-NO", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Nora', service="")


class ComAppleTtsbundleZosiacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Zosia-compact"
    name = "Zosia"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Zosia-compact', 'lang': 'pl-PL', 'name': 'Zosia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Zosia', service="")


class ComAppleTtsbundleLucianacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Luciana-compact"
    name = "Luciana"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Luciana-compact', 'lang': 'pt-BR', 'name': 'Luciana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Luciana', service="")


class ComAppleTtsbundleJoanacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Joana-compact"
    name = "Joana"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Joana-compact', 'lang': 'pt-PT', 'name': 'Joana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-PT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Joana', service="")


class ComAppleTtsbundleIoanacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Ioana-compact"
    name = "Ioana"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Ioana-compact', 'lang': 'ro-RO', 'name': 'Ioana'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ro-RO", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ioana', service="")


class ComAppleTtsbundleMilenacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Milena-compact"
    name = "Milena"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Milena-compact', 'lang': 'ru-RU', 'name': 'Milena'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Milena', service="")


class ComAppleTtsbundleLauracompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Laura-compact"
    name = "Laura"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Laura-compact', 'lang': 'sk-SK', 'name': 'Laura'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk-SK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Laura', service="")


class ComAppleTtsbundleAlvacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Alva-compact"
    name = "Alva"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Alva-compact', 'lang': 'sv-SE', 'name': 'Alva'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sv-SE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Alva', service="")


class ComAppleTtsbundleKanyacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Kanya-compact"
    name = "Kanya"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Kanya-compact', 'lang': 'th-TH', 'name': 'Kanya'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th-TH", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Kanya', service="")


class ComAppleTtsbundleYeldacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Yelda-compact"
    name = "Yelda"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Yelda-compact', 'lang': 'tr-TR', 'name': 'Yelda'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr-TR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Yelda', service="")


class ComAppleTtsbundleSiriMaleZhcnCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_male_zh-CN_compact"
    name = "Li-mu"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_male_zh-CN_compact', 'lang': 'zh-CN', 'name': 'Li-mu'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Li-mu', service="")


class ComAppleTtsbundleTingtingcompactAltAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Ting-Ting-compact"
    name = "Ting-Ting"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Ting-Ting-compact', 'lang': 'zh-CN', 'name': 'Ting-Ting'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Ting-Ting', service="")


class ComAppleTtsbundleSiriFemaleZhcnCompactAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.siri_female_zh-CN_compact"
    name = "Yu-shu"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.siri_female_zh-CN_compact', 'lang': 'zh-CN', 'name': 'Yu-shu'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Yu-shu', service="")


class ComAppleTtsbundleSinjicompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Sin-Ji-compact"
    name = "Sin-Ji"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Sin-Ji-compact', 'lang': 'zh-HK', 'name': 'Sin-Ji'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Sin-Ji', service="")


class ComAppleTtsbundleMeijiacompactAltAlt(ResponsiveVoice):
    uri = "com.apple.ttsbundle.Mei-Jia-compact"
    name = "Mei-Jia"
    voiceIDs = []
    _raw = {'voiceURI': 'com.apple.ttsbundle.Mei-Jia-compact', 'lang': 'zh-TW', 'name': 'Mei-Jia'}

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name='Mei-Jia', service="")
