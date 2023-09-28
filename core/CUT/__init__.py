""" 文本預處理模組。  by 治嘉 & 程學
"""
import re
from opencc import OpenCC
from typing import List


input_data_str: str = "凡用兵之法全國篇上，破國次之。全軍篇上，破軍次之全旅篇上，破旅次之全伍篇上，破伍次之是故百藏百勝，非善之善者也不殿而屈人之兵，善之善者也谋攻篇-饰缘天法的證道者雨位一踩子世人所的一揉子一有两位：一是春秋時代吴王阖間（『史記』作膚）的將軍！丨對横張吴國國力很有貢献的齊人武；另一位是係武的俊代丨丨戳時代齊國的揉隋0保是齊國軍師，辅佐名將田忌，管雨次大破魏國軍師靡滑，名麒天下，世傅其兵法。事見『史記·踩子吴起列傅两位揉子的事亦散見『戴國策一，但其餐料未必鞍『史記』群翘。踩武的事情又見俊漢趙所著的『吴越春秋、袁康的『越韬艳書』』，些都是相當於民間傅奇的野史。『韓非子·五蠹篇』云：一境内皆言兵，藏揉丶吴之書』『漢者家有之』又難言篇』云：係子脚於魏書·藝文志』記係武兵書云：吴係子兵法八十二篇L記揉兵法云：一齊子八十九篇』。雨千年俊的西元九七二年，由山東省歸沂縣城近郊龈雀山的两座漢墓中，出土了舒多竹簡，其中包括『吴揉子兵法』和齊係隋兵法』。由二墓中同時出士的古綫推断，墓主葬於西元前一一八年以前，亦即溪武帝及司馬獲在世的時代，追些竹簡麗薇和司馬獲讀到的兵法書差不多。而事實，追雨部竹簡的『係子』和『史記』中所記迹的綫乎相同，大概是輪瓣揉武、揉的著而成琛子一的镉慕7孫子武者，膺人也。7深子』业非書名，而是揉先生一之意。武是子之刑断其雨足一故名鑽，俊以號行而名遂不傅舆踩武丶踩同列於史記·踩子哭起列傅』中的哭起，也是戳國時代有名的兵法家秉政治家。『史記』一對於吴起的事情記戴得比二揉尤篇群細，逅大概是吴起在歷史舞毫L所扮演的角色重要的緣故『史記』在琛子武者，齊人也一之俊接著説7以兵法見於哭王阖。齊國在今山東省。在此出身的係武，篇什會曾跑到江蘇省的哭國求仕於閣間呢？追一黏可馬没有交待。當黄河流域侯争霸中原之際，哭國是境的一個小國，而齊國自春秋時代霸主齊桓公以來，即一直是個强。係武離關最可以發掸才能的國，遠去哭國，追其中一定有原因，不過追些都已無法考證了。片外，俊溪時代成書的一吴越春秋』云：揉子名武，吴人一。追檬看柬，踩武或舒本柬就是吴人，吴人仕哭，是很自然的事。當然，吴越春秋』成書鞍晚，説法也舒鞍不可靠，但至少可備一韓非子既云：一境内皆三兵，藏丶吴之書者家有之一可見『揉子』在戴國時代已翘非常流行但春秋時代的』，却對揉武的事隽字不提『春秋左氏傅』重要史料丨二因此有人疑係武其人的有無。一興『吴越春秋』同檬成書於俊澳的越書』卷二有云·一巫門外大嫁篇吴王餐客齊揉武之墓，在城外十里虑。一指明武篇齊人，説法興『史記』同。吴越春秋』谓揉武篇哭人，可能是因篇躲武仕哭之故而有此阙會o檬『吴越春秋』記截，揉武乃透過伍子胥的推羯見哭王閣聞，時篇閣閣即位的第三年（西元前五一二年）○追一年阖阖正想伐楚，正好伍子胥和伯豁（太宰豁，伯豁又作白喜丶帛喜）由楚國亡命來歸，對楚國十分怨恨，立意出兵復仇，所以伍子精極地推揉武阖間係武羯見吴王阖阖時，為他一篇一篇地溝解其兵法，吴吴王閣層，聞層日·：子之十三篇，吾蛊觀之矣°』此虚所霸的十三篇一，又形成一個考證上的間題。司馬在『揉子吴起列傅』卷未所附的太史公日一7世俗所師旅，皆道揉子十三二篇。1但前面引迹的『書·藝文志』，御在兵家頭下記『哭了兵法八十二篇』。漢書』篇俊漢班固所纂，其『懿文志』是記戴当時所有古代到漢代書籍的分類目。光是兵家便戴有五十三家，共七百九十篇。司馬獲所翻的一『三二篇』和哭王閣聞所髓的7十三篇一，是不是一檬的呢？是不是叫遥的時代，除了一十三篇一本之外另有一八「篇一本的『踩子』呢？對於追個間題，有多種説法。濮·藝文志』除了吴係子八十二篇之外，又戴们一臀揉了八九篇』。粉六百年之俊成書的『隋書·翘籍志』，記戴兵法書一百三十三部，五百十二卷，其中有·係子兵法二卷，一、揉子兵法一卷一，一揉武兵翘二卷一、7钞係子兵法一卷一四頭，都是武所著至於揉嘴的兵法，没有配戴。逅四種書，前二者各為魏武帝注及姚武帝丶王凌集解；一钞踩子兵法一卷一剧為魏太尉賣朝本，可見此四者都是同一系統的東西。漢書』和隋、南北朝，各代皆有正史，但都不輪『藝文志』或一翘籍志』之類的圖書目緣。也就是，在追六世記間，揉的兵法書已翘下落不明。而踩武育·藝文志』的八十二篇，成『揉子的坛法也已由『漢書兴法一二一卷』，藍號魏武帝，他所校前注解的『揉子俊晚期的曹操一般篇『魏武注揉子』。以好知名的曹操兵法書讀得很多，他説：以揉武所書最篇可行一（踩武略解』序）豁予揉子』很高的價，且根據自己豐富的體，作『踩子略解』，篇敷興『史記』所記的十三篇同。追一本『揉子』就是今日我们所能見到的唯一版本，因此曹操的注干本，一般懿爲是曹操整理漢代所流傅的八十二篇而成的。"

####################### UTILITIES ##############################
def __removeURL(text):
    # 刪除URL網址
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)
def __simplifiedToTraditionalChineseOpenCC(text):
    # 將簡體中文轉成繁體中文
    converter = OpenCC('s2twp')
    return converter.convert(text)
def __removeCustomCharactersRE(text):
    # 刪除英文字母與全形英文字母
    text = re.sub('[\u0040-\u007E\uFF20-\uFF60]', r'', text) 
    # 刪除符號與全形符號
    text = re.sub('[\uFF5E\uFF03-\uFF06\uFF08\uFF09\uFF1C-\uFF1E]', r'', text) 
    # 刪除數字與全形數字
    text = re.sub('[\u0030-\u0039\uFF10-\uFF19]', r'', text) 
    # 刪除特定符號
    text = re.sub('[~#$%&()<=>\"]', r'', text)
    return text
def __cutSentenceRE(text: str) -> list:
    # 為了中文全形的分句，根據句號驚嘆號問號做換行
    text = re.sub('([.。！？\?])([^’”\"\'])',r'\1\n\2', text) 
    # 為了中文全形的分句，根據全形刪節號做換行
    text = re.sub('(\.{6})([^’”\"\'])',r'\1\n\2', text) 
    # 為了中文半形的分句，根據半形刪節號做換行
    text = re.sub('(\…{2})([^’”\"\'])',r'\1\n\2', text) 
    # 删除 string 字串末尾的指定符號並做分句
    text = text.rstrip()
    return text.split("\n")
####################### END UTILITIES ##############################


##################### EXPORT #####################
def cut(input_str: str) -> List[str]:
    """ 
    輸入一段文字，輸出字串陣列。 \n
    本模組會進行前處理將不必要文本移除，並正規畫後進行斷句。
    """
    result = []

    text = __simplifiedToTraditionalChineseOpenCC(input_str)
    text = __removeURL(text)
    text = __removeCustomCharactersRE(text)
    result = __cutSentenceRE(text)
    
    return result
##################### END EXPORT #####################



if __name__ == '__main__':
    print(cut(input_data_str))