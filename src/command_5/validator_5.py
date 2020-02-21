import re


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

    spelling_re = re.compile(r'(?P<content>&lt;(?P<first>(?P<first_tag>\s*\w*\s*):(?P<first_tag_lang>\s*\w*\s*))&gt;(?:.*?)&lt;/(?P<second>(?P<second_tag>\s*\w*\s*):(?P<second_tag_lang>\s*\w*\s*))&gt;)')
    stucked_words_re = re.compile(r'(?P<content>(?P<before_first>\b\w*\b)?&lt;(\s*\w*\s*):(\s*\w*\s*)&gt;(?P<after_first>\b\w*\b)?(?:.*?)(?P<before_second>\b\w*\b)?&lt;/(\s*\w*\s*):(\s*\w*\s*)&gt;(?P<after_second>\b\w*\b)?)')
    wrong_syntax_re = re.compile(r'(?P<content><\s*\w*\s*:\s*\w*\s*>.*?</\s*\w*\s*:\s*\w*\s*>)')

    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            # Check for wrong syntax `<lang:*>`
            wrong_syntax = re.finditer(wrong_syntax_re, line)
            for match in wrong_syntax:
                if match:
                    print ln, match.group('content')

            stucked_words_matches = re.finditer(stucked_words_re, line)
            for match in stucked_words_matches:
                if match:
                    # Check for stucked words
                    if (
                        match.group('before_first') is not None or
                        match.group('after_first') is not None or
                        match.group('before_second') is not None or
                        match.group('after_second') is not None
                    ):
                        print ln, match.group('content')

            spelling_matches = re.finditer(spelling_re, line)
            for match in spelling_matches:
                if match:
                    # Check tag spelling
                    if (
                        match.group('first_tag').strip() != 'lang' or
                        match.group('second_tag').strip() != 'lang' or
                        match.group('first_tag_lang').strip() not in languages or
                        match.group('second_tag_lang').strip() not in languages
                    ):
                        print ln, match.group('content')

                    # Check for white space in tag
                    if (
                        " " in match.group('first') or
                        " " in match.group('second')
                    ):
                        print ln, match.group('content')

    return found


if __name__ == "__main__":
    found = command5('../files/RNZ_Insight_002.trs')
    #for item in found:
        #print item, " <=> ", found[item]
