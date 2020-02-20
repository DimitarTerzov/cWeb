import re

from app.cWeb import BasicPunctuation


#Language tag validator
def command5(filepath):

    #load the languages to array
    languages = [   'Foreign','Acholi','Afrikaans','Albanian','Amharic','Arabic','Ashante','Assyrian','Azerbaijani','Azeri',
'Bajuni','Basque','Batak','Behdini','Belorussian','Bengali','Berber','Betawi','Bosnian','Bravanese','Bulgarian','Burmese',
'Cakchiquel','Cambodian','Cantonese','Catalan','Chaldean','Chamorro','Chao-chow','Chavacano','Chinese','Chuukese','Croatian',
'Czech','Danish','Dari','Dinka','Diula','Dutch','English','Estonian','Espanol','Fante',
'Farsi','Finnish','Flemish','French','Fukienese','Fula','Fulani','Fuzhou','Gaddang',
'Gaelic','Gayo','Georgian','German','Gorani','Greek','Gujarati','Haitian','Creole','Hakka',
'Hausa','Hebrew','Hindi','Hmong','Hungarian','Ibanag','Icelandic','Igbo','Ilocano',
'Indonesian','Inuktitut','Italian','Jakartanese','Japanese','Javanese','Kanjobal','Karen','Karenni','Kashmiri',
'Kazakh','Khmer','Kikuyu','Kinyarwanda','Kirundi','Korean','Kosovan','Kotokoli','Krio','Kurdish','Kurmanji',
'Kyrgyz','Lakota','Laotian','Latvian','Lingala','Lithuanian','Luganda','Maay','Macedonian','Malay',
'Malayalam','Maltese','Mandarin','Mandingo','Mandinka','Marathi','Marshallese','Mirpuri','Mixteco','Moldavan',
'Mongolian','Montenegrin','Navajo','Neapolitan','Nepali','Nigerian','Pidgin','Norwegian','Oromo','Pahari',
'Papago','Papiamento','Pashto','Patois','Persian','Pidgin','English','Polish','Portug.creole','Portuguese','Pothwari',
'Pulaar','Punjabi','Putian','Quichua','Romanian','Russian','Samoan','Serbian','Shanghainese','Shona',
'Sichuan','Sicilian','Sinhalese','Slovak','Somali','Sorani','Spanish','Sudanese','Arabic','Sundanese',
'Susu','Swahili','Swedish','Sylhetti','Tagalog','Taiwanese','Tajik','Tamil','Telugu','Thai',
'Tibetan','Tigre','Tigrinya','Toishanese','Tongan','Toucouleur','Trique','Tshiluba','Turkish','Ukrainian',
'Urdu','Uyghur','Uzbek','Vietnamese','Visayan','Welsh','Wolof','Yiddish','Yoruba','Yupik',
'Ambonese', 'Betawinese', 'Latin', 'Manadonese']

    x1 = "&lt;lang:" + BasicPunctuation + "*[a-zA-Z]+" + BasicPunctuation + "*&gt;[^;&]*&lt;\/?lang:" + BasicPunctuation + "*[a-zA-Z]+" + BasicPunctuation + "*&gt;"
    x2 = "|&lt;lang:" + BasicPunctuation + "*[a-zA-Z]+" + BasicPunctuation + "*&gt;[^;&]*&lt;\/?lang:" + BasicPunctuation + "*[a-zA-Z]+" + BasicPunctuation + "*"
    regex = re.compile(x1+x2)

    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            for m in re.findall(regex, line):
                matchObj = re.match('&lt;lang:(.+)&gt; .* &lt;\/lang:(.+)&gt;', m)
                if not matchObj:
                    found[ln]  = [5, 'Syntax error,', m]
                else:
                    lang1 = matchObj.group(1)
                    lang2 = matchObj.group(2)

                    #if language is not in the list
                    if (lang1 != lang2) or not lang1 in languages:
                        found[ln] = [5, 'Language error', m]
    return found
