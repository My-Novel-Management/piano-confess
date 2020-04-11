# -*- coding: utf-8 -*-
"""Episode: 1.孤児院
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## define alias
W = Writer
_ = W.getWho()


## scenes
def sc_memory(w: World):
    josef, an = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("振り返りの",
            w.comment("オルガンを弾いているところから開始に"),
            josef.come("壊れた教会に入ってくる"),
            _.do("埃ののったオルガンを開け、弾き始める"),
            _.do("後悔の日々を思い出す"),
            camera=w.josef,
            stage=w.on_church_int,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_meetagain(w: World):
    josef, an = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    jean = W(w.jean)
    return w.scene("幼馴染",
            w.comment("ずっと一緒にいた、方がよいのでそっちに"),
            josef.be("仕事先のカフェ。働いている"),
            an.come("入ってきて"),
            an.talk("ねえ$josef、ピアノ弾いてよ"),
            josef.talk("店長に怒られる"),
            an.talk("ちょっとくらい平気よ", "ね？"),
            josef.talk("分かった"),
            josef.do("店のピアノの蓋をあけて、指を乗せる",
                "弾き始める"),
            josef.do("曲は『$w_wonderful』だ",
                "静かな旋律のメロディから流れ出す"),
            an.do("歌い始める"),
            camera=w.josef,
            stage=w.on_cafe_int,
            day=w.in_meet1, time=w.at_afternoon,
            )

def sc_herdream(w: World):
    josef, an = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    jean = W(w.jean)
    return w.scene("彼女の夢",
            josef.do("二人で飲んでいる"),
            _.do("彼女の誕生日"),
            josef.talk("歌手は目指さないのか？"),
            an.talk("歌ってるのが楽しいだけだから",
                "それにただ歌がいいんじゃなくて、あなたのピアノがあるから楽しいんだよ"),
            an.talk("$josefはピアニストにはならないの？"),
            josef.talk("店で弾かせてもらえればいいよ",
                "学もない、金もない、知識もない",
                "特別な才能もない", "そんな自分がプロにはなれないよ"),
            an.talk("素敵なピアノなのに"),
            josef.do("活躍中の$samuelのレコードを取り出してかける"),
            josef.talk("こんな風には弾けない"),
            josef.hear("ジャズ特有の遊び",
                "音楽はうねり、感情を揺さぶる",
                "到底到達できない領域だ"),
            )

def sc_happydays(w: World):
    josef, an = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    jean = W(w.jean)
    return w.scene("楽しかった日々",
            an.talk("いらっしゃいませ"),
            josef.do("働いている彼女を見て、こんな日々が続けばいいなと"),
            )

## episode
def ep_orphanage(w: World):
    return w.episode("１．孤児院の幼馴染",
            sc_memory(w),
            sc_meetagain(w),
            sc_herdream(w),
            sc_happydays(w),
            ## NOTE
            ##  - ピアニストを目指して喫茶店でピアノを弾いていた男は、同じ孤児院で育った彼女と再会する
            ##  - 彼女は歌手を目指して働きながら勉強していた
            ##  - 男は彼女の為にピアノを弾き、彼女は歌った。楽しい日々だった
            note="孤児院出身の男は同じようにそこで育った彼女と再会する。彼女は歌手を目指し、男はピアニストを目指していた")
