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

    #correct_spelling_re = re.compile(r'(&lt;(\s*\w*\s*):(\s*\w*\s*)&gt;\s*)')
    no_separation_re = re.compile(r'((?P<before_first>\b\w*\b)?&lt;(\s*\w*\s*):(\s*\w*\s*)&gt;(?P<after_first>\b\w*\b)?(.*?)(?P<before_second>\b\w*\b)?&lt;/(\s*\w*\s*):(\s*\w*\s*)&gt;(?P<after_second>\b\w*\b)?)')

    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            matches = re.finditer(no_separation_re, line)
            for match in matches:
                if match:
                    if (
                        match.group('before_first') is not None or
                        match.group('after_first') is not None or
                        match.group('before_second') is not None or
                        match.group('after_second') is not None
                    ):
                        print ln, match.groups()

    return found


if __name__ == "__main__":
    found = command5('../files/RNZ_Insight_002.trs')
    #for item in found:
        #print item, " <=> ", found[item]
