# -*- coding: utf-8 -*-
"""Story config.
"""
################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
# 2) AREAS
#       エリア設定
# 3) STAGES
#       舞台基本設定
# 4) DAYS
#       年月日設定
# 5) TIMES
#       時間帯基本設定
# 6) ITEMS
#       小道具設定
# 7) WORDS
#       辞書設定
# 8) RUBIS
#       ルビ設定
# 9) LAYERS
#       レイヤ設定
#
################################################################


PERSONS = (
        # Tag / 氏,名 / 歳 / 誕生日 / 性別 / 職業 / 呼称 / 紹介
        ("josef", "ヨーゼフ", "", 40,(1,1), "male", "無職", "me:僕"),
        ("anna", "アンナ", "", 40,(1,1), "female", "歌手", "me:私"),
        ##
        ("samuel", "サミュエル", "サミュエル,ジェイ", 60,(1,1), "male", "ミュージシャン", "me:ワタシ"),
        ("jean", "ジェーン", "", 50,(1,1), "female", "店長", "me:あたい"),
        ("armstrong", "アームストロング", "アームストロング,ルイ", 70,(1,1), "male", "ジャズ"),
        ##
        ("man", "ごろつき", "", 30,(1,1), "male", "ごろつき"),
        )

AREAS = (
        # Tag / 名前 / x,y / 備考
        ("NewYork", "ニューヨーク", 13675,3541),
        ("Portland", "ポートランド", 12240,4531),# メイン州
        )

STAGES = (
        # Tag / 名前 / Area / 紹介
        ("bar", "バー", "NewYork"),
        ("cafe", "カフェ", "Portland"),
        ("slum", "スラム街", "Portland"),
        ("church", "教会", "Portland"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("afterwar", "戦後のある日", 10,10, 1950),
        ("meet1", "再会した日", 10,10, 1960),
        ("meet2", "三十年後の再会", 10,10, 1990),
        ("current", "現在", 1,1,2020),
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        )

WORDS = (
        # Tag / 名前 / 紹介
        ("wonderful", "ワット・ア・ワンダフル・ワールド", "サッチモことアームストロングが歌った名曲"),
        ("seisho1", "賢い者は災いを見て自ら避け、思慮のない者は進んでいって、罰を受ける"),
        )

RUBIS = (
        # Base / Rubi / Exclusion / Type
        ("引き摺る", "引き｜摺《ず》る"),
        ("煽られ", "｜煽《あお》られ"),
        ("瓦礫", "｜瓦礫《がれき》"),
        ("蓋", "｜蓋《ふた》"),
        ("貰った", "｜貰《もら》った"),
        ("喋る", "｜喋《しゃべ》る"),
        ("覆って", "｜覆《おお》って"),
        ("溢れる", "｜溢《あふ》れる"),
        ("笑窪", "｜笑窪《えくぼ》"),
        ("痺れて", "｜痺《しび》れて"),
        ("躓いた", "｜躓《つまず》いた"),
        ("憂えて", "｜憂《うれ》えて"),
        ("皺", "｜皺《しわ》"),
        ("鬱憤", "｜鬱憤《うっぷん》"),
        ("霞み", "｜霞《かす》み"),
        ("呪詛", "｜呪詛《じゅそ》"),
        ("捲れて", "捲《めく》れて"),
        )

LAYERS = (
        # Key / Title / Words
        )

