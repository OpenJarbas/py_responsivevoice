import requests
import tempfile
import os


class ResponsiveVoice:
    API_URL = "http://responsivevoice.org/responsivevoice/getvoice.php"

    # Genders
    FEMALE = "female"
    MALE = "male"
    UNKNOWN_GENDER = ""

    # Languages
    ENGLISH_GB = "en-GB"
    ENGLISH_AU = "en-AU"
    ENGLISH_US = "en-US"
    ENGLISH_ZA = "en-ZA"
    ENGLISH_IE = "en-IE"
    HEBREW = "he-IL"
    THAI = "th-TH"
    PORTUGUESE_BR = "pt-BR"
    PORTUGUESE_PT = "pt-PT"
    SLOVAK = "sk-SK"
    FRENCH_CA = "fr-CA"
    ROMANIAN = "ro-RO"
    NORWEGIAN = "no-NO"
    FINNISH = "fi-FI"
    POLISH = "pl-PL"
    GERMAN = "de-DE"
    DUTCH = "nl-NL"
    INDONESIAN = "id-ID"
    TURKISH = "tr-TR"
    ITALIAN = "it-IT"
    FRENCH = "fr-FR"
    RUSSIAN = "ru-RU"
    SPANISH_MX = "es-MX"
    SPANISH_ES = "es-ES"
    CHINESE_HK = "zh-HK"
    CHINESE_TW = "zh-TW"
    CHINESE_CN = "zh-CN"
    SWEDISH = "service-SE"
    HUNGARIAN = "hu-HU"
    DUTCH_BE = "nl-BE"
    ARABIC_SA = "ar-SA"
    KOREAN = "ko-KR"
    CZECH = "cs-CZ"
    DANISH = "da-DK"
    HINDI = "hi-IN"
    GREEK = "el-GR"
    JAPANESE = "ja-JP"

    def __init__(self, lang=None, gender=None,
                 pitch=0.5, rate=0.5, vol=1,
                 voice_name="", service="", key=None):
        self.pitch = pitch
        self.rate = rate
        self.vol = vol
        self.lang = lang or ResponsiveVoice.ENGLISH_US
        self.gender = gender or ResponsiveVoice.UNKNOWN_GENDER
        self.service = service
        self.voice_name = voice_name
        # key extracted from website - 0POmS5Y2
        # key extracted from wordpress plugin - FQ9r4hgY
        # alternate key from Bundler - HY7lTyiS
        self.key = key or "FQ9r4hgY"

    def get_mp3(self, sentence, mp3_file=None, pitch=None, rate=None,
                vol=None, gender=None):
        mp3_file = mp3_file or os.path.join(tempfile.gettempdir(), str(hash(sentence)))
        if not mp3_file.endswith(".mp3"):
            mp3_file += ".mp3"

        params = {
            "key": self.key,
            "t": sentence,
            "tl": self.lang,
            "pitch": pitch or self.pitch,
            "rate": rate or self.rate,
            "vol": vol or self.vol,
            "sv": self.service,
            "vn": self.voice_name,
            "gender": gender or self.gender
        }

        r = requests.get(self.API_URL, params)
        if os.path.isfile(mp3_file):
            os.unlink(mp3_file)

        with open(mp3_file, "wb") as f:
            f.write(r.content)
        return mp3_file
