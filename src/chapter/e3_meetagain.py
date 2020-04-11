# -*- coding: utf-8 -*-
"""Episode: 3.再会
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
def sc_slumbar(w: World):
    josef, anna = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("場末のバーで",
            josef.come(),
            _.do("やってくる"),
            inside.look("薄暗いバー",
                "店内にはくだをまくゴロツキばかり"),
            josef.do("カウンターに座り、酒を頼む"),
            anna.be("スポットライトが当たる"),
            inside.look("客から歓声が上がる"),
            anna.do("アカペラで歌い始める"),
            josef.do("酒を飲みながら、その歌声に聞き惚れる"),
            anna.do("＜ジャズの名盤＞"),
            josef.do("よく彼女が弾いてくれと頼んだ曲だ",
                "それに歌声、随分とかすれてハスキィになっていたが思い出す"),
            josef.do("立ち上がり、彼女を見る"),
            anna.look("太っていて、化粧も濃い。胸も大きくなり、だらしなく開けている",
                "昔からは考えられない扇情的な衣装だったが、それはまぎれもなく$annaだった"),
            camera=w.josef,
            stage=w.on_bar,
            day=w.in_meet2, time=w.at_night,
            )

def sc_meetagain(w: World):
    josef, anna = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("彼女との再会",
            josef.be(),
            anna.be(),
            josef.do("一緒に酒を飲んでいる"),
            anna.talk("ほんと、久しぶり", "今もピアノ弾いてるの？"),
            josef.talk("趣味程度だけどな"),
            _.do("つい彼女をじろじろと見てしまう",
                "あの頃の面影はあるものの、完全に摂生をかいた肉の塊になり果てている"),
            josef.talk("そっちこそ、歌、続けてたんだな"),
            anna.talk("聞いてくれた？", "なんとかね、ここで歌わせてもらってるの",
                "でもまだ夢を諦めた訳じゃない", "なんたって一度はあの$samuelに見込まれた歌声なんだから"),
            josef.think("酒で潰れた声",
                "それでもまだ彼女は目指しているという",
                "でも雑誌に散々書かれていたことを知っている",
                "ただのロリコンにもてあそばれただけだ、と", "つい先月、あいつの裁判が始まったところだ"),
            anna.do("徐々に$josefに近づいて、もたれかかってくる"),
            josef.talk("飲みすぎたのか？"),
            anna.talk("なんであの時、行くなって言ってくれなかったの？"),
            josef.talk("え"),
            anna.talk("なんで……"),
            anna.do("寝てしまう"),
            )

def sc_runaway(w: World):
    josef, anna = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("逃亡",
            josef.be(),
            anna.be(),
            josef.do("彼女をこんな風にしてしまったのは自分だったと知り、激しく後悔して、そっと逃げ出した"),
            josef.do("外を走る"),
            stage=w.on_street,
            )

def sc_regret(w: World):
    josef, anna = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("後悔を叫ぶ",
            josef.come("走り出てくる"),
            _.do("薄暗い路地に"),
            _.do("物取りにからまれて、殴られる"),
            _.do("ゴミのようにゴミ山に捨てられ、情けない思いで空を見上げる"),
            _.think("$meが悪かったんだ",
                "あの時、彼女の手を離さなければ"),
            stage=w.on_street,
            )

## episode
def ep_meetagain(w: World):
    return w.episode("３．再会",
            sc_slumbar(w),
            sc_meetagain(w),
            sc_runaway(w),
            sc_regret(w),
            ## NOTE
            ##  - 場末のバーに辿り着いた男は、そこで歌う女の歌声に聞き覚えがあった
            ##  - 女は彼女だった。歌手になった、はずなのに、落ちぶれて今、小汚いバーで歌っている
            ##  - 彼女と少し話して、男は逃げ出すようにバーを出た
            note="場末のバーに入った男は、そこで歌う女性の歌声に聞き覚えがあった")
