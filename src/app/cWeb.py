#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import re
import datetime
import cgi, cgitb
import binascii
cgitb.enable()

# Extracted from: https://www.tamasoft.co.jp/en/general-info/unicode.html
WWwhitespace = "[\s                                                                                                      ฀឴   ឵᠋  ᠌   ᠍   ᠎   ᠏᠚  ᠛   ᠜   ᠝   ᠞   ᠟ᡸ  ᡹   ᡺   ᡻   ᡼   ᡽   ᡾   ᡿ᢪ  ᢫   ᢬   ᢭   ᢮   ᢯                                           ​   ‌   ‍   ‎   ‏                            ⁠  ⁡   ⁢   ⁣   ⁤   ⁥   ⁦   ⁧   ⁨   ⁩   ⁪   ⁫   ⁬   ⁭   ⁮   ⁯⠀　꒍    ꒎   ꒏꒢  ꒣꓅﬏︀    ︁   ︂   ︃   ︄   ︅   ︆   ︇   ︈   ︉   ︊   ︋   ︌   ︍   ︎   ️￰  ￱   ￲   ￳   ￴   ￵   ￶   ￷   ￸   ￹   ￺   ￻   ]"
# Extracted from: https://www.fileformat.info/info/unicode/category/Po/list.htm
# ᳀᳁᳂᳃᳄᳅᳆᳇᳓৽੶౷಄࿙࿚⸱⸲⸳⸴⸵⸶⸷⸸⸹⸼⸽⸾⸿⹁⹃⹄⹅⹆⹇⹈⹉⹊⹋⹌⹍⹎⹏꣸꣹꣺꣼𐫰𐫱𐫲𐫳𐫴𐫵𐫶𐮙𐮚𐮛𐮜𐽕𐽖𐽗𐽘𐽙𒑴𖩮𖩯𖫵𖬷𖬸𖬹𖬺𖬻𖭄𖺗𖺘𖺙𖺚𖿢𛲟𝪇𝪈𝪉𝪊𝪋𞥞𞥟𑗎𑗏𑗐𑗑𑗒𑗓𑗔𑗕𑗖𑗗𑙁𑙂𑙃𑙠𑙡𑙢𑙣𑙤𑙥𑙦𑙧𑙨𑙩𑙪𑙫𑙬𑜼𑜽𑜾𑠻𑧢𑨿𑩀𑩁𑩂𑩃𑩄𑩅𑩆𑪚𑪛𑪜𑪞𑪟𑪠𑪡𑪢𑱁𑱂𑱃𑱄𑱅𑱰𑱱𑻷𑻸𑿿𑅀𑅁𑅂𑅃𑅴𑅵𑇅𑇆𑇇𑇈𑇍𑇛𑇝𑇞𑇟𑈸𑈹𑈺𑈻𑈼𑈽𑊩𑑋𑑌𑑍𑑎𑑏𑑛𑑝𑓆𑗁𑗂𑗃𑗄𑗅𑗆𑗇𑗈𑗉𑗊𑗋𑗌𑗍
WWpunctuatio = "[\!\"\#\'\%\*\,\.\:\?\@\¡§¶·¿;·՚՛՜՝՞։׀׃׆׳״؉؊،؍؛؞؟٪٫٬٭۔܀܁܂܃܄܅܆܇܈܉܊܋܌܍߷߸߹࠰࠱࠲࠳࠴࠵࠶࠷࠸࠹࠺࠻࠼࠽࠾࡞।॥॰૰෴๏๚๛༄༅༆༇༈༉༊་༌།༎༏༐༑༒༔྅࿐࿑࿒࿓࿔၊။၌၍၎၏჻፠፡።፣፤፥፦፧፨᙮᛫᛬᛭᜵᜶។៕៖៘៙៚᠀᠁᠂᠃᠄᠅᠇᠈᠉᠊᥄᥅᨞᨟᪠᪡᪢᪣᪤᪥᪦᪨᪩᪪᪫᪬᪭᭚᭛᭜᭝᭞᭟᭠᯼᯽᯾᯿᰻᰼᰽᰾᰿᱾᱿‖‗†‡•‣․‥…‧‰‱′″‴‵‶‷‸※‼‽‾⁁⁂⁃⁇⁈⁉⁊⁋⁌⁍⁎⁏⁐⁑⁓⁕⁖⁗⁘⁙⁚⁛⁜⁝⁞⳹⳺⳻⳼⳾⳿⵰⸀⸁⸆⸇⸈⸋⸎⸏⸐⸑⸒⸓⸔⸕⸖⸘⸛⸞⸟⸪⸫⸬⸭⸮⸰、。〃〽・꓾꓿꘍꘎꘏꙳꙾꛲꛳꛴꛵꛶꛷꡴꡵꡶꡷꣎꣏꤮꤯꥟꧁꧂꧃꧄꧅꧆꧇꧈꧉꧊꧋꧌꧍꧞꧟꩜꩝꩞꩟꫞꫟꫰꫱꯫︐︑︒︓︔︕︖︙︰﹅﹆﹉﹊﹋﹌﹐﹑﹒﹔﹕﹖﹗﹟﹠﹡﹨﹪﹫！＂＃％＆＇＊，．／：；？＠＼｡､･𐄀𐄁𐄂𐎟𐏐𐡗𐤟𐤿𐩐𐩑𐩒𐩓𐩔𐩕𐩖𐩗𐩘𐩿𐬹𐬺𐬻𐬼𐬽𐬾𐬿𑁇𑁈𑁉𑁊𑁋𑁌𑁍𑂻𑂼𑂾𑂿𑃀𑃁𒑰𒑱𒑲𒑳᳀᳁᳂᳃᳄᳅᳆᳇᳓৽੶౷಄࿙࿚⸱⸲⸳⸴⸵⸶⸷⸸⸹⸼⸽⸾⸿⹁⹃⹄⹅⹆⹇⹈⹉⹊⹋⹌⹍⹎⹏꣸꣹꣺꣼𐫰𐫱𐫲𐫳𐫴𐫵𐫶𐮙𐮚𐮛𐮜𐽕𐽖𐽗𐽘𐽙𒑴𖩮𖩯𖫵𖬷𖬸𖬹𖬺𖬻𖭄𖺗𖺘𖺙𖺚𖿢𛲟𝪇𝪈𝪉𝪊𝪋𞥞𞥟𑗎𑗏𑗐𑗑𑗒𑗓𑗔𑗕𑗖𑗗𑙁𑙂𑙃𑙠𑙡𑙢𑙣𑙤𑙥𑙦𑙧𑙨𑙩𑙪𑙫𑙬𑜼𑜽𑜾𑠻𑧢𑨿𑩀𑩁𑩂𑩃𑩄𑩅𑩆𑪚𑪛𑪜𑪞𑪟𑪠𑪡𑪢𑱁𑱂𑱃𑱄𑱅𑱰𑱱𑻷𑻸𑿿𑅀𑅁𑅂𑅃𑅴𑅵𑇅𑇆𑇇𑇈𑇍𑇛𑇝𑇞𑇟𑈸𑈹𑈺𑈻𑈼𑈽𑊩𑑋𑑌𑑍𑑎𑑏𑑛𑑝𑓆𑗁𑗂𑗃𑗄𑗅𑗆𑗇𑗈𑗉𑗊𑗋𑗌𑗍]"
# for command3 and command10
BasicPunctuation = "[.,，。\-?! ]"

def build_sync_times(filepath):
    sync_t = {}

    last_sync = ""

    with open(filepath) as f:
        ln = -1
        for line in f:
            ln = ln + 1

            line = line.rstrip("\r\n")
            if re.match("<Sync time=\"[\s\d\.]+\"/>", line):
                last_sync = line
            sync_t[ln] = last_sync
    return sync_t


def list_files(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.trs' in file:
                files.append(os.path.join(r, file))
    return files

#Disallowed characters
def command1(filepath):
    ## String: Update with new chars between the regex brackets [..] ##
    bad_chars = "[£$@}%^&*{…–—;:\"/❛❜❝❞〃״＇״‷⁗‴「」『』„”‚“”‘„”»«""‘“”«»‹›„““”‘‹›«»„（）［］｛｝｟｠⦅⦆〚〛⦃⦄「」〈〉《》【】〔〕⦗⦘『』〖〗〘〙｢｣⟦⟧⟨⟩⟪⟫⟮⟯⟬⟭⌈⌉⌊⌋⦇⦈⦉⦊❨❩❪❫❴❵❬❭❮❯❰❱❲❳﴾﴿〈〉⦑⦒⧼⧽﹙﹚﹛﹜﹝﹞⁽⁾₍₎⦋⦌⦍⦎⦏⦐⁅⁆⸢⸣⸤⸥⟅⟆⦓⦔⦕⦖⸦⸧⸨⸩⧘⧙⧚⧛᚛᚜༺༻༼༽⸜⸝⸌⸍⸂⸃⸄⸅⸉⸊⏜⏝⎴⎵⏞⏟⏠⏡﹁ ﹂﹃﹄︹︺︻︼︗︘︿﹀︽︾﹇﹈︷︸]"
    ## strip off any remaining whitespace char
    s = "".join(bad_chars.split())
    ## from utf-8 to unicode encode
    regex = unicode(s, "utf-8")

    found = {}

    with open(filepath) as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            #if line starts with < and ends in >
            if line.startswith('<') and line.endswith('>'):
                #we skip everythin between <>
                continue

            #remove all lt/gt from the line
            p1 = line.find('&lt;')
            p2 = line.find('&gt;')
            while p1 >= 0 and p2 > p1:
                if (p2 + 4) == len(line):
                    line = ''
                else:
                    line = line[0:p1] + line[p2+4]
                p1 = line.find('&lt;')
                p2 = line.find('&gt;')

            uniline = unicode(line,"utf-8")

            dissch = re.findall(regex, uniline)
            s = ''.join(dissch)

            if len(dissch) > 1:
                found[ln] = [1, 'Disallowed characters', s.encode("utf-8") + '/' + line]
            if len(dissch)==1:
                found[ln] = [1, 'Disallowed character', s.encode("utf-8") + '/' + line ]

    return found

#Bracket hunter
def command2(filepath):
    found = {}
    with open(filepath,'r') as f:

        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            #if line starts with < and ends in >
            if line.startswith('<') and line.endswith('>'):
                #we skip everythin between <>
                continue

            orig_line = line

            #exclude [*]
            for m in re.findall("(\[[^\]]*\])", line):
                line = line.replace(m, '')

            #if the word contains a bracket, after all [*] tags where removed
            if re.search('\[|\]', line):
                found[ln] = [2, 'Bracket issue [', orig_line]
    return found

#Sound tag validator
def command3(filepath):
    skip_words = ['[no-speech]', '[no—speech]', '[noise]', '[overlap]', '[music]', '[applause]', '[lipsmack]', '[breath]', '[cough]', '[laugh]', '[click]', '[ring]', '[dtmf]', '[sta]', '[cry]', '[prompt]']

    regex = re.compile("\[.*?\]")

    found = {}
    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")
            prev_tag = 'none'

            if '<Speaker' not in line:

                for w in line.split():
                    #if we have something glued to tag

                    if re.match(".*[^ \s、 。 ‧ ？ ！ ，]\[.*?\]", w):
                        found[ln] = [3, 'Missing white space left of sound tag', w]
                    elif re.match("\[.*?\][^ \s.,，。\-?! ].*", w):
                        found[ln] = [3, 'Missing white space right of sound tag', w]
                    else:
                        for m in re.findall(regex, line):
                            if not m in skip_words:
                                found[ln] = [3, 'Sound tag syntax', m + '/' + line]

                            #detect duplicate tags like - [cough][cough]
                            #if we have two of the same tags in a row
                            #and there are one after the other in the line
                            elif prev_tag == m and re.search(re.escape(m)    +"\s*"+WWwhitespace+"*"  +WWpunctuatio+"*"+   re.escape(m), line):
                                found[ln] = [3, 'Sound tag duplicate', m + '/' + line]
                            prev_tag = m
    return found

#Initial tag validator
def command4(filepath):

    punctuation = "[^'.~,!?\s:;-_\"]"
    allowed_characters_after_tag = "s"
    allowed_expressions_before_tag = ["l'"]
    regex = re.compile(r"(?P<content>(?P<before_first>(\b\w*\b)|[\S\w]+)?(?P<first_open>&lt;|\<)(?P<first_tag>[int\w\s/\\]+)(?P<first_close>&gt;|\>)(?P<inner_text>.*?)(?P<second_open>&lt;|\<)(?P<forward>[\\/\s]*)(?P<second_tag>[int\w\s]+)(?P<second_close>&gt;|\>)(?P<after_second>\b\w*\b|{}+)?)".format(punctuation), re.UNICODE)

    found = {}
    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n").decode('utf')

            for m in re.finditer(regex, line):

                # Check tag syntax
                if (
                    m.group('first_open') != '&lt;' or
                    m.group('first_close') != '&gt;' or
                    m.group('second_open') != '&lt;' or
                    m.group('second_close') != '&gt;' or
                    m.group('forward') != '/'
                ):
                    found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]
                    continue

                # Check tag spelling
                if (
                    m.group('first_tag') != 'initial' or
                    m.group('second_tag') != 'initial'
                ):
                    found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]
                    continue

                # Check for disallowed expressions before tag
                if (
                    m.group('before_first') is not None and
                    not m.group('before_first') in allowed_expressions_before_tag
                ):
                    found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]
                    continue

                # Check for disallowed expressions after tag
                if (
                    m.group('after_second') is not None and
                    not m.group('after_second') in allowed_characters_after_tag
                ):
                    found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]
                    continue

                # Check for incorrect white space
                if (
                    #m.group('before_first') is not None or
                    not m.group('inner_text').startswith(' ') or
                    not m.group('inner_text').endswith(' ')
                ):
                    found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]
                    continue

                # Check for errors in text
                inner_text = m.group('inner_text')
                inner_content = inner_text.split()
                # If no text in tag -> error
                if not inner_content:
                    found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]

                elif len(inner_content) == 1:
                    content = inner_content[0]
                    # Catch anything different from pattern `W`
                    if len(content) == 1 and re.match(r'\W', content, re.UNICODE):
                        found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]

                    # Catch anything different from pattern `WE` and `W.`
                    elif len(content) == 2 and not re.match(r'^\w+\.?$', content, re.UNICODE):
                        found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]

                    # Catch anything different from pattern `WEB`, `Ph.D.`
                    elif len(content) > 2:
                        if re.match(r'[\w.]*', content, re.UNICODE).group() != content:
                            found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]

                # If text doesn't feet pattern `W. E. B.` -> error
                elif len(inner_content) > 1:
                    for content in inner_content:
                        if not re.match(r'^\w\.$', content, re.UNICODE):
                            found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]

    return found

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
                    if re.search(r'(&lt;|\<)([int\w\s/\\]+)(&gt;|\>).*?(&lt;|\<)([\\/\s]*)([int\w\s]+)(&gt;|\>)', inner_text):
                        continue

                    # Check final punctuation
                    inner_text_end = inner_text[-1]
                    if inner_text_end in punctuation_marks:
                        found[ln] = [5, "Final punctuation marks should be outside the tag", match.group('content')]

    return found

    
    
#Numeral hunter
def command6(filepath):

    found = {}

    with open(filepath) as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            #if line starts with < and ends in >
            if line.startswith('<') and line.endswith('>'):
                #we skip everythin between <>
                continue

            for word in line.split():
                if re.match('\S*\d+\S*', word) and not (word.startswith('<') and word.endswith('>')):
                    found[ln] = [6, 'Numerals not allowed', word]
    return found

import string


#Filler word validator
def command7(filepath):

    # Allowed punctuation after tag
    punctuation = "[:',!—_\".?\-;]"
    #default english skip tags
    skip_tags = "(#uh|#um|#ah|#eh|#hm)"
    possible_missing_tag = "(uh|um|ah|eh|hm)"
    filler_re = re.compile(r'[\W\w]?#\w*\W?', re.UNICODE)

    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n").decode('utf')

            for match in re.finditer(filler_re, line):

                target = match.group().strip()
                # Pass filler tag with tilde.
                # They are reported in command 15.
                if "~" in target:
                    continue

                if not re.match(r'^{0}{1}?$'.format(skip_tags, punctuation), target, re.UNICODE):
                    found[ln] = [7, 'Invalid filler tag', match.group().encode('ascii', 'replace')]
                    continue


            for match in re.finditer(r'\s{0}\W'.format(possible_missing_tag), line, re.UNICODE):
                if ln not in found:
                    found[ln] = [7, 'Possible filler tag missing #', match.group().encode('ascii', 'replace')]

    return found



#White space validator
def command8(filepath):
    rv = {}
    patterns = ['\[[^\]*]\]', '&lt;[^;&]*&gt;', '#[^ #\.,，。\s?!~‘s-]*', '\(\(\)\)', '\(\([^\)]*\)\)']

    for pat in patterns:
        found = command8_real(f, pat)
        rv.update(found)
    return rv

def command8_real(filepath, pattern):

    reg_allowed = '[\.,，。\s?!~‘s-]'
    regex_pat = '(.)' + pattern + '(.)'

    regex = re.compile('.' + pattern + '.')

    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            #if line starts with < and ends in >
            if line.startswith('<') and line.endswith('>'):
                #we skip everythin between <>
                continue

            #put spaces in front/end of line, to avoid checking for startswith/endswith for each token
            line = ' ' + line + ' '

            for m in re.findall(regex, line):
                matchObj = re.match(regex_pat, m)
                if not matchObj:
                    found[ln] =  [8, 'Missing white space (syntax)', m]
                else:
                    lC = matchObj.group(1)
                    rC = matchObj.group(2)

                    #if language is not in the list
                    if not re.match('[\s　。，]', lC):
                        found[ln] =  [8, 'Missing white space (invalid left char)', lC + '/' + m]
                    elif not re.match(reg_allowed, rC):
                        found[ln] =  [8, 'Missing white space (invalid right char)', rC + '/' + m]
    return found

#UTF-8 validator
def command9(filepath):
    found = {}
    with open(filepath, 'r') as f:
        line = f.readline()
        if line.strip("\r\n") != '<?xml version="1.0" encoding="UTF-8"?>':
            found[1] = [9, 'Invalid encoding, must be UTF-8', line]
    return found

#Inaudible tag validator
def command10(filepath):

    trailing_ok = '.,，。-?! '

    found = {}

    with open(filepath) as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            #if line starts with < and ends in >
            if line.startswith('<') and line.endswith('>'):
                #we skip everythin between <>
                continue

            #detect repeating tags
            if re.search("\(\(\)\)\s?\(\(\)\)", line):
                found[ln] = [10, 'Cannot have more than on (()) in a row', line]
                continue

            #detect invalid tags
            if re.search("\(\(\s+\)\)", line):
                found[ln] = [10, 'Invalid tag', line]
                continue

            #detect single (a-z) tags
            if re.search("[^\(]\([a-zA-Z0-9]+\)[^\)]", line):
                found[ln] = [10, '(()) tag incorrectly written', line]
                continue

            counter = 0
            last = 'x'

            for c in list(line):

                #check for space after ))
                if last == ')' and counter == 0 and c != line[-1] and not c in trailing_ok:
                    found[ln] = [10, 'Missing training white space', line]
                    counter = 0
                    break

                if c == '(':
                    counter = counter + 1

                    #if we don't have a space before (
                    if c != line[0] and counter == 1 and not re.match('[\s\t　。，]', last):
                        found[ln] = [10, 'Missing leading white space', line]
                        counter = 0
                        break

                elif c == ')':
                    counter = counter - 1

                    #if we have a space before )
                    if (last == ' ' or last == '\t'):
                        found[ln] = [10, 'Space before closing', line]
                        counter = 0
                        break

                last = c

                if counter > 2 or counter < 0:           #more than 2 ( or )
                    found[ln] = [10, 'Space inside', line]
                    counter = 0
                    break

            #check1) if line has invalid number of open/close brackets
            if counter != 0:
                found[ln] = [10, 'Missing parenthesis', line]

    return found

#Punctuation space validator
def command11(filepath):

    exlusion_list = ['-nya', '-exclusion2', '-exclusion3']

    #match a symbol with one space
    regex = re.compile('(\s\-\s)|(\s[\.,，。!?-])|([\.,，。!?-]\s{3,})')

    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            #if line starts with < and ends in >
            if line.startswith('<') and line.endswith('>'):
                #we skip everythin between <>
                continue

            for m in re.findall(regex, line):

                label = ''
                val = exlusion_list[0]

                #allow ' - '
                if m[0]:
                    val = exlusion_list[0]
                elif m[1]:
                    val = m[0]
                elif m[2]:
                    val = m[1]

                if not val in exlusion_list:
                    found[ln] = [11, 'Punctuation spacing issue', line]
    return found


#Disallowed strings
def command12(filepath):
    bad_regex = ['\sok\s', 'Dr\.', 'Dra\.', 'www\.', '[a-zA-Z]- ']
    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            #if line starts with < and ends in >
            if line.startswith('<') and line.endswith('>'):
                #we skip everythin between <>
                continue

            matchObj = re.search('([,!?:\.]{2,})', line)
            if matchObj:
                found[ln] = [12, 'Invalid sequence', matchObj.group(1) + ') -> '+ line]
            else:
                for bad in bad_regex:

                    if bad == 'Dr\.' or bad == 'Dra\.':
                        if re.match('.*' + bad + '.*', line):
                            found[ln] = [12, 'Disallowed string found (' + bad.replace('\\', '').strip('s') + ')', line]
                            break
                    else:
                        if re.match('.*' + bad + '.*', line , re.IGNORECASE):
                            found[ln] = [12, 'Disallowed string found (' + bad.replace('\\', '').strip('s') + ')', line]
                            break

    return found

#Speaker validator
def command13(filepath):

    regex = re.compile('<Turn (?:speaker="(spk[0-9]+)")?(?:.*)startTime="([0-9.]+)"(?:.*) (?:speaker="(spk[0-9]+)")?')

    found = {}

    prev_spk='none'
    sync = False
    sync_count = 0
    end_time = 0

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            # Catch empty turns and empty segments.
            if line == '':
                pass
            elif '<Turn' in line:
                start_time = re.search(r'(?P<content>startTime="(?P<value>\d+\.?\d*)")', line)
                start_value = float(start_time.group('value'))
                start_time = start_time.group('content')

                # Catch turns out of order
                if start_value != end_time:
                    found[ln] = [13, "Turn out of sync", start_time]

                end_time = re.search(r'endTime="(?P<value>\d+\.?\d*)"', line)
                end_time = float(end_time.group('value'))
                sync_count = 0

            elif 'Sync' in line and not sync:
                sync = True
                sync_count += 1
                new_sync = re.search(r'(?P<content>Sync time="(?P<value>\d+\.?\d*)")', line)
                new_sync_time = new_sync.group('content')
                sync_time_value = float(new_sync.group('value'))

                if sync_count == 1:
                    # compare sync_time with start_value
                    if sync_time_value != start_value:
                        found[ln] = [13, "Segment out of sync", new_sync_time]

                elif sync_count > 1:
                    # compare new sync_time with old sync_time
                    old_sync_value = re.search(r'(\d+\.?\d*)', sync_time)
                    if sync_time_value <= float(old_sync_value.group()):
                        found[ln] = [13, "Segment out of sync", new_sync_time]

                sync_time = new_sync_time

            elif "</Turn>" == line and sync and sync_count == 1:
                found[ln] = [13, "Empty turns are not allowed", start_time]
                sync = False
                sync_count = 0

            elif 'Sync' in line and sync:
                found[ln] = [13, "Empty segments are not allowed", sync_time]
                sync_count += 1
                new_sync = re.search(r'(?P<content>Sync time="(?P<value>\d+\.?\d*)")', line)
                new_sync_time = new_sync.group('content')
                sync_time_value = float(new_sync.group('value'))

                # Compare new sync_time with old sync_time
                old_sync_value = re.search(r'(\d+\.?\d*)', sync_time)
                if sync_time_value <= float(old_sync_value.group()):
                    found[ln] = [13, "Segment out of sync", new_sync_time]

                sync_time = new_sync_time

            elif 'Sync' not in line and line != "</Turn>":
                sync = False

            elif "</Turn>" == line and sync and sync_count > 1:
                found[ln] = [13, "Empty segments are not allowed", sync_time]
                sync = False
                sync_count = 0

            elif "</Turn>" == line and not sync:
                sync = False
                sync_count = 0

            for m in re.findall(regex, line):
                # If turn is speakerless -> set speaker to 'none'.
                if m[0] == '' and m[2] == '':
                    speaker = 'none'
                else:
                    # If turn has speaker -> take it.
                    speaker = m[0] if m[0] != '' else m[2]

                    if speaker == prev_spk:
                        found[ln] = [13, 'Sequential turns by the same speaker', speaker + " at " + m[1]]

                #save speaker
                prev_spk = speaker

    return found
#Segment length validator
def command14(filepath):

    regex = re.compile('<Sync time="\s*([0-9\.]+)\s*"/>')
    regez = re.compile("<Sync time=\"" + WWwhitespace +"+[0-9\.]+\"/>|<Sync time=\"[0-9\.]+"+ WWwhitespace+"\"/>|<Sync time=\""+ WWwhitespace +"+[0-9\.]+"+ WWwhitespace+"\"/>")

    found = {}
    cur_time = 0.0

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")
            for m in re.findall(regex, line):

                seg_time = float(m)
                seg_len = seg_time - cur_time

                if seg_len > 15.0:
                    found[ln] = [14, 'Segment exceeds limit', 'Sync time="' + str(cur_time) + '" length: ' + str(seg_len) + ' seconds']

                #update current time
                cur_time = seg_time
            for m in re.findall(regez, line):
               
                found[ln] = [14, 'Unexpected white space in sync time tag', line]


    return found


#Tilde checker
def command15(filepath):

    punctuation = "[:',!—_\".?\-;\]\[]"

    match_no_white_space = re.compile(r'(\b\w+~\w*\b)', re.UNICODE)
    match_double_white_space = re.compile(r'\w* ~ \w*', re.UNICODE)
    match_double_tilde = re.compile(r'\w*\s*~~\s*\w*', re.UNICODE)
    match_punctuation_before = re.compile(r"(?<=\w|\W){0}~{0}?".format(punctuation), re.UNICODE)
    match_punctuation_after = re.compile(r"(?<=\s)~{0}".format(punctuation), re.UNICODE)
    match_filler = re.compile(r"#\w*~", re.UNICODE)


    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1

            no_white_space = re.findall(match_no_white_space, line)
            for match in no_white_space:
                found[ln] = [15, 'Incorrect white space', match]

            double_white_space = re.findall(match_double_white_space, line)
            for match in double_white_space:
                found[ln] = [15, 'Incorrect white space', match]

            double_tilde = re.findall(match_double_tilde, line)
            for match in double_tilde:
                found[ln] = [15, 'Double tilde', match]

            touching_punctuation_before = re.finditer(match_punctuation_before, line)
            for match in touching_punctuation_before:
                found[ln] = [15, 'Punctuation touch tilde', match.group()]

            touching_punctuation_after = re.finditer(match_punctuation_after, line)
            for match in touching_punctuation_after:
                found[ln] = [15, 'Punctuation touch tilde', match.group()]

            fillers = re.finditer(match_filler, line)
            for match in fillers:
                found[ln] = [15, 'Filler word with tilde', match.group()]

    return found



#Speaker labels
def command16(filepath):

    regex = re.compile('([a-z]+)="([^"]*)"')

    needed_keys = ['type', 'dialect', 'accent']

    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            if line == '</Speakers>':
                break

            if line.startswith('<Speaker id='):
                attrs = {'id': 'unknown', 'name':'unknown'}
                for kv in re.findall(regex, line):
                    attrs[kv[0]] = kv[1]

                missing_keys = []
                for k in needed_keys:
                    if not k in attrs:
                        missing_keys.append(k)

                if missing_keys:
                    found[ln] = [16, 'missing label', 'Speaker id=' + attrs['id'] + '|' + attrs['name']  + ' -> '+ ','.join(missing_keys)]

                elif attrs['type'] != 'male' and attrs['type'] != 'female' and attrs['type'] != 'unknown':
                    found[ln] = [16,  'type invalid', attrs['type'] ]

                elif attrs['dialect'] == '':
                    found[ln] = [16, 'dialect empty', attrs['dialect'] ]

                elif attrs['dialect'] == 'non-native' and attrs['accent'] == '':
                    found[ln] = [16, 'null accent', '']
    return found

#Short turns
def command17(filepath):

    regex = re.compile('<Sync time="\s*([0-9\.]+)\s*"/>')
    regez = re.compile("<Sync time=\"" + WWwhitespace +"+[0-9\.]+\"/>|<Sync time=\"[0-9\.]+"+ WWwhitespace+"\"/>|<Sync time=\""+ WWwhitespace +"+[0-9\.]+"+ WWwhitespace+"\"/>")

    found = {}
    cur_time = 0.0

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")
            for m in re.findall(regex, line):

                seg_time = float(m)
                seg_len = seg_time - cur_time

                if seg_len < 3.0:
                    found[ln] = [17, 'Segment is less than 3 seconds, possible use of [overlap] or combine with other segment', 'Sync time="' + str(cur_time) + '" length: ' + str(seg_len) + ' seconds']

                #update current time
                cur_time = seg_time
            for m in re.findall(regez, line):

                found[ln] = [17, 'Unexpected white space in sync time tag', line]


    return found


#Dissalowed tag combinations
def command18(filepath):

    regex = re.compile("^\s*\[no-speech\]"+WWpunctuatio+"*" +WWwhitespace+"*\[overlap\]\s*$|^\s*\[overlap\]"+WWpunctuatio+"*" +WWwhitespace+"*\[no-speech\]\s*$|^\s*\[overlap\]"+WWpunctuatio+"*" +WWwhitespace+"*\[music\]\s*$|^\s*\[music\]"+WWpunctuatio+"*" +WWwhitespace+"*\[overlap\]\s*$|^\s*\[no-speech\]"+WWpunctuatio+"*" +WWwhitespace+"*\[music\]\s*$|^\s*\[music\]"+WWpunctuatio+"*" +WWwhitespace+"*\[no-speech\]\s*$")

    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            for m in re.findall(regex, line):
                found[ln] = [18, 'Dissallowed tag combinations!', m]

    return found


def command19(filepath):
    #  WWwhitespacelist found in this file at: line 10 
    regex = re.compile("&lt;initial&gt;\s*[a-zA-Z]+" + WWwhitespace + "+[a-zA-Z]+\s*&lt;\/initial&gt;")

    found = {}

    with open (filepath, 'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            for m in re.findall(regex, line):

                found[ln] = [19, 'Multiple initialisms in single tag', m]

    return found


def command20(filepath):
    # WWpunctuatio found in this file at: line 13
    regex = re.compile("&lt;initial&gt;[a-zA-z\s]*" + WWpunctuatio + "+[a-zA-z\s]*&lt;\/initial&gt;|&lt;lang:\s?[a-zA-Z]*&gt;.*" + WWpunctuatio + "+\s+&lt;\/lang:\s?[a-zA-z]*&gt;")

    found = {}

    with open (filepath, 'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            for m in re.findall(regex, line):

                if re.match("&lt;initial&gt;", m):


                    if not re.search("&lt;initial&gt;\s?[A-Za-zÀ-ÖØ-öø-ÿ]{1}\.\s?&lt;\/initial&gt;", line):
                        found[ln] = [20, 'Disallowed punctuation inside initial tag', m]
                    else:
                        if re.search("&lt;initial&gt;\s?[A-Za-zÀ-ÖØ-öø-ÿ]{1}\.\s?&lt;\/initial&gt;\s*$", line) != None:
                            found[ln] = [20, 'Disallowed punctuation inside initial tag', m]

    return found

#Unused speakers
def command21(filepath):
    regex = re.compile("\"spk(\d*)\"")
    speakerlist = []
    sectionspeakers = []
    found =  {}

    with open (filepath, 'r') as f:

        for line in f:
            if "speaker=" in line:
                #print line
                if re.match(".*speaker=(\"spk\d+\").*", line):
                    if re.match(".*speaker=(\"spk\d+\").*", line).group(1) not in sectionspeakers: 
                        sectionspeakers.append(re.match(".*speaker=(\"spk\d+\").*", line).group(1))

    with open (filepath, 'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            if "<Speaker " in line:
                #print line
                nameoccurences = re.findall("name=", line)
                sp = re.match(".*(\"spk\d+\").*", line).group(1)
                if sp not in sectionspeakers:
                    found[ln] = [21, 'Unused speaker', 'Speaker id=' + sp + ' | name=' + re.match(".*name=(\".*\").*check", line).group(1) + ' not found in content.  Try Edit > Speakers > Remove unused speakers']
            elif "<Section" in line:
                break

    return found

def command22(filepath):
    found = {}
    spknames = []

    with open (filepath, 'r') as f:
        for line in f:

            if "<Speaker " in line:
                spknames.append(re.match(".*name=(\".*\").*check", line).group(1))
            elif "<Section" in line:
                break

    with open (filepath, 'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            if "<Speaker " in line:
                nameregx = re.match(".*name=(\".*\").*check", line).group(1)
                if spknames.count(nameregx) > 1:
                    found[ln] = [22, 'Multiple occurences of name=' + nameregx, 'Speaker id=' + re.match(".*(\"spk\d+\").*", line).group(1) + ' | name=' + nameregx]

    return found

def command23(filepath):
    bad_strings = ['Who nb=', 'Topic id=', 'Event' 'mode=', 'channel=', 'fidelity=']
    found = {}
    regex = re.compile(".*<(.*)>.*")

    with open (filepath, 'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            inner = re.findall(regex, line)
            # < inner >
            for txt in inner:
                for bad in bad_strings:

                    if bad in txt:
                        if bad == 'Who nb=':
                            found[ln] = [23, 'Do not create turns with multiple speakers.', '(' + bad + ') | ' + line]
                            break   #print only one bad string per line
                        elif bad == 'Topic id=':
                            found[ln] = [23, 'Do not create topics', '(' + bad + ') | ' + line]
                            break
                        elif bad == 'Event':
                            found[ln] = [23, 'Do not create events', '(' + bad + ') | ' + line]
                            break
                        elif bad == 'mode=':
                            found[ln] = [23, 'Do not change the mode setting', '(' + bad + ') | ' + line]
                            break
                        elif bad == 'channel=':
                            found[ln] = [23, 'Do not change the channel setting', '(' + bad + ') | ' + line]
                            break
                        elif bad == 'fidelity=':
                            found[ln] = [23, 'Do not change the fidelity setting', '(' + bad + ') | ' + line]
                            break                            
    return found

print "Content-type:text/html; charset=UTF-8\r\n\r\n"

cmd_ids = range(1,24)

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
lang = form.getvalue('lang')
json_files = []

if not form.has_key('upload_files'):
    print '<h1>No key parameter: upload_files</h1>'
    sys.exit(0)



# strip leading path from file name to avoid
# directory traversal attacks
uploaded_files = []

try:
    for fileitem in form['upload_files']:
        fn = '/tmp/' + os.path.basename(fileitem.filename)
        open( fn, 'wb').write(fileitem.file.read())
        json_files.append(fn)
except:
    fileitem = form['upload_files']
    fn = '/tmp/' + os.path.basename(fileitem.filename)
    open( fn, 'wb').write(fileitem.file.read())
    json_files.append(fn)


lst = []
x = form.getvalue('excl_cmds')

if type(x) != list and x != None:
    lst.append(x)
    for i in lst:
        cmd_ids.remove(int(i))
elif x == None:
    pass
else:
    for i in x:
        cmd_ids.remove(int(i))

#call all commands on each file found
all_stats = {'checked_files':0, 'valid_files': 0, 'total_errors':0}
file_divs = {}

for f in json_files:
    all_stats['checked_files'] = all_stats['checked_files'] + 1

    res = []
    total_errors = 0
    for i in cmd_ids:
        rv = eval("command" + str(i))(f)
        if rv:
            total_errors = total_errors + len(rv.keys())
            res.append(rv)

    file_div = ''
    if len(res) == 0:
        all_stats['valid_files'] = all_stats['valid_files'] + 1
    else:
        sync_times = build_sync_times(f)

        file_div = '<table border="1">' \
                 + '<tr><th>#</th><th>Line no.</th><th>Sync time</th><th>Error Code</th><th>Error Type</th><th>Content</th></tr>';

        item_no = 0
        for found in res:
            for ln in sorted(found.keys()):
                res = found[ln]
                file_div += '<tr><td>' + str(item_no)       + '</td>' + \
                        '<td>' + str(ln).ljust(5)           + '</td>' + \
                        '<td>' + cgi.escape(sync_times[ln]) + '</td>' + \
                        '<td>' + str(res[0])                + '</td>' + \
                        '<td>' + res[1]                     + '</td>' + \
                        '<td>' + cgi.escape(res[2])         + '</td></tr>'
                item_no = item_no + 1
        file_div += '</table>'
    file_divs[f] = [file_div, total_errors]

    all_stats['total_errors'] = all_stats['total_errors'] + total_errors


print "<html>"
print "<head>"
print "<title>Title of Report</title>"
print '<link rel="stylesheet" type="text/css" href="../style.css">'
print '<meta charset="utf-8">'
print '<meta name="viewport" content="width=device-width, initial-scale=1">'
print '<meta name="robots" content="noindex,nofollow">'
print '<meta http-equiv="Expires" content="-1">'
print "</head>"
print "<body>"

print '<div>'
print '<table border="1">'
print '<caption>Statistics</caption>'
print '<tr><td>Language</td><td>English</td></tr>'
print '<tr><td>Date</td><td>' + datetime.datetime.now().strftime("%B %d, %Y %H:%M%p %Z") + '</td></tr>'
print '<tr><td>Number of files checked</td><td>' + str(all_stats['checked_files']) + '</td></tr>'
print '<tr><td>Total number of errors found</td><td>' + str(all_stats['total_errors']) + ' (in the whole report)' + '</td></tr>'
print '<tr><td>Number of valid files</td><td>' + str(all_stats['valid_files']) + '</td></tr>'
print '<tr><td>Commands Enabled</td><td>' + ','.join(str(x) for x in cmd_ids) + '</td></tr>'
print '</table>'
print '</div>'


print '<div name="file_bookmarks">'
print '<table border="1">'
print '<caption>File Links</caption>'
print '<tr><th>#</th><th>Name</th><th>Total Errors</th></tr>'
fe = 0
for f in sorted(file_divs.keys()):
    total_errors = str(file_divs[f][1])
    print '<tr><td>' + str(fe) +'</td><td><a href="#f' + str(fe)+ '">' + f +'</a></td><td>' + total_errors + '</tr>'
    fe = fe + 1
print '</table>'
print '</div>'

print '<p>Read about how to interpret this error report by referencing our <b><a href="https://www.greencrescent.com/cWeb/validator-output-guide.html">validator output guide</a></b>.</p> '

fe = 0
for f in sorted(file_divs.keys()):
    if file_divs[f][1] > 0:
        print '<div id="f' + str(fe) + '">'
        print '<h2>' + str(fe) + '. ' + f + '</h2>'
        print file_divs[f][0]
        print '</div>'
    fe = fe + 1
    os.remove(f)

print '</body>'
print '</html>'
