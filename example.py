from responsive_voice import ResponsiveVoice

engine = ResponsiveVoice()
file_path = engine.get_mp3("hello world")
file_path = engine.get_mp3("hello world",
           gender=ResponsiveVoice.MALE,
           rate=0.45)

engine = ResponsiveVoice(lang=ResponsiveVoice.PORTUGUESE_BR)
file_path = engine.get_mp3("olá mundo")


from responsive_voice.voices import EnglishIndia, UkEnglishMale, \
    PortuguesePortugal

india = EnglishIndia()
uk = UkEnglishMale()
pt = PortuguesePortugal()
india.get_mp3("hello world")
uk.get_mp3("hello world")
pt.get_mp3("olá mundo")
