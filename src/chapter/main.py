# -*- coding: utf-8 -*-
"""Chapter: story 1
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.chapter.e1_orphanage import ep_orphanage
from src.chapter.e2_herdream import ep_herdream
from src.chapter.e3_meetagain import ep_meetagain
from src.chapter.e4_organ import ep_oldorgan

## define alias
W = Writer
_ = W.getWho()

## chapter
def ch_main(w: World):
    return w.chapter("Ch: main",
            ep_orphanage(w),
            ep_herdream(w),
            ep_meetagain(w),
            ep_oldorgan(w),
            ## NOTE
            ##  - 孤児院の幼馴染と再会した男は、彼女が歌手を目指していると知る
            ##  - 彼女の夢の為に身を引いて、自分は離れた
            ##  - 彼女と場末のバーで再会し、そっと逃げ出す
            ##  - 思い出の教会でオルガンを弾きながら、選択が正しかったのだと信じようとした
            note="男は廃墟となった思い出の教会にやってきて、オルガンを弾く。自分の人生の選択が正しかったと信じたくて")
