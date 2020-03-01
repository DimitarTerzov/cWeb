import re


#Language tag validator
def command5(filepath):

    #load the languages to array
    languages = [
        'Foreign','Acholi','Afrikaans','Albanian','Amharic','Arabic','Ashante','Assyrian','Azerbaijani','Azeri',
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
        'Ambonese', 'Betawinese', 'Latin', 'Manadonese'
    ]

    punctuation_marks = """:,-'—_!".?;"""

    regex = re.compile(r'(?P<content>(?P<before_first>\b\w*\b)?(?P<first_open>(?:&lt;)|\<)(?P<first_tag>/*\s*\w*\s*):(?P<first_tag_lang>\s*\w*\s*)(?P<first_close>(?:&gt;)|\>)(?P<inner_text>.*?)(?P<second_open>(?:&lt;)|\<)(?P<forward>[\/]*)(?P<second_tag>\s*\w*\s*):(?P<second_tag_lang>\s*\w*\s*)(?P<second_close>(?:&gt;)|\>)(?P<after_second>\b\w*\b)?)')

    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            matches = re.finditer(regex, line)
            for match in matches:
                if match:

                    # Check for stucked words
                    if (
                        match.group('before_first') is not None or
                        not match.group('inner_text').startswith(" ") or
                        not match.group('inner_text').endswith(" ") or
                        match.group('after_second') is not None
                    ):
                        found[ln] = [5, "Tag syntax error", match.group('content')]
                        continue

                    # Check spelling
                    if (
                        match.group('first_tag') != 'lang' or
                        match.group('second_tag') != 'lang' or
                        match.group('first_tag_lang') not in languages or
                        match.group('second_tag_lang') not in languages
                    ):
                        found[ln] = [5, "Tag syntax error", match.group('content')]
                        continue

                    # Check for wrong syntax `<lang:*>`
                    if (
                        match.group('first_open') != '&lt;' or
                        match.group('first_close') != '&gt;' or
                        match.group('second_open') != '&lt;' or
                        match.group('second_close') != '&gt;' or
                        match.group('forward') != '/'
                    ):
                        found[ln] = [5, "Tag syntax error", match.group('content')]
                        continue


                    inner_text = match.group('inner_text').strip()
                    if not inner_text:
                        found[ln] = [5, 'Language tag is empty', match.group('content')]
                        continue

                    # Check for initial tag inside lang tag
                    if re.match(r'^&lt;initial&gt;\s[\w.\s]*\s&lt;/initial&gt;$', inner_text):
                        continue

                    # Check final punctuation
                    inner_text_end = inner_text[-1]
                    if inner_text_end in punctuation_marks:
                        found[ln] = [5, "Final punctuation marks should be outside the tag", match.group('content')]

    return found


if __name__ == "__main__":
    found = command5('../files/test_5.trs')
    keys = found.keys()
    sorted_keys = sorted(keys)
    print "Errors:", len(sorted_keys)
    for key in sorted_keys:
        print key, " <=> ", found[key]
