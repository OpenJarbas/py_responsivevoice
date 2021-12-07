![](pyresponsive_voice.png)

Unofficial python API for [Responsive Voice](https://responsivevoice.org)

  * [Install](#install)
  * [Example](#example)
    * [Voices](#voices)
  * [Usage](#usage)
  * [Credits](#credits)
  
Last tested with [ResponsiveVoice - Version 1.8.1](https://responsivevoice.org/change-log/)


# Install
```bash
pip install ResponsiveVoice
```
# Example

```python
from responsive_voice import ResponsiveVoice

engine = ResponsiveVoice()
file_path = engine.get_mp3("hello world")
file_path = engine.get_mp3("hello world",
           gender=ResponsiveVoice.MALE,
           rate=0.45)

engine = ResponsiveVoice(lang=ResponsiveVoice.PORTUGUESE_PT)
file_path = engine.get_mp3(u"olá mundo")
```


```python
get_mp3(sentence, mp3_file=None, lang=None, pitch=None, rate=None, vol=None, gender=None)
```
- *sentence* : The text you want to speak.
- *mp3_file* : The name of the output file. If `None`, this will be generated from the text.
- *pitch* : The pitch of the speaker.
- *rate* : The rate (speed) of the speaker, value between 0 and 1.
- *vol* : The volume (loudness) of the speaker, value between 0 and 1.
- *gender* : The gender of the speaker. E.g. `ResponsiveVoice.FEMALE`


## Voices

You can use pre defined configurations, aka, voices

```python
from responsive_voice.voices import EnglishIndia, UkEnglishMale, \
    PortuguesePortugal

india = EnglishIndia()
uk = UkEnglishMale()
pt = PortuguesePortugal()
```


## Credits

[ResponsiveVoice](https://responsivevoice.org/)

[JarbasAI](https://jarbasal.github.io)
