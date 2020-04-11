# -*- coding: utf-8 -*-
"""Episode: 4.古いオルガン
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
def sc_slum(w: World):
    josef, anna = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("スラム街",
            josef.come("歩いていた"),
            outside.look("スラム街",
                "誰もが精気のない目で彼を見る",
                "テントやバラック"),
            _.look("物乞いが彼を見て、諦めたように去っていく"),
            josef.do("足を引き摺って歩く"),
            _.do("コートをまとい、歩いていく"),
            _.do("女の姿を探すも、人違いばかり"),
            _.do("そのバラック街を抜けた先に、土煙を抜けて、丘の上に建つ教会が見えてくる"),
            camera=w.josef,
            stage=w.on_slum,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_ruins(w: World):
    josef, anna = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("廃墟でオルガンを弾く男",
            josef.come("教会にやってくる"),
            inside.look("教会の中の描写。壊れて廃墟となった懐かしの場所"),
            josef.do("半開きのドアを開けて、中に入る"),
            inside.look("足元には瓦礫が転がる",
                "椅子には崩れた天井の欠片や埃が積もっていて、その上をトカゲが走り抜けていく"),
            _.look("宣誓台には本が置かれている"),
            _.look("教師はいない"),
            josef.do("オルガンを見つけ、歩いていく"),
            inside.look("埃が積もったオルガンの蓋をあけ、指を置く"),
            josef.do("音が鳴ることを確認して、弾き始める"),
            _.think("思い出していた",
                "彼女の為にここで弾いていた日々を",
                "一番上手かった彼女",
                "アイドルを、歌手を目指した彼女"),
            _.think("何故、あんなことになってしまったのか"),
            _.think("何故、選ばなかったのか"),
            stage=w.on_church_int,
            )

def sc_truth(w: World):
    josef, anna = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("真実の演奏",
            josef.be(),
            _.do("男がオルガンを弾いている",
                "だがぱすぱすと、音が鳴っていない"),
            _.do("男の服装はボロボロで、鳴らないオルガンを必死に弾いている",
                "男の目には涙が滲み、ただマリア像を見上げて、口を開けて、必死に弾き続けている"),
            outside.look("足元には彼女が身につけていたネックレスが千切れて落ちている"),
            )

## episode
def ep_oldorgan(w: World):
    return w.episode("４．古いオルガン",
            sc_ruins(w),
            sc_truth(w),
            ## NOTE
            ##  - 男は後悔と共に廃墟となった孤児院でオルガンを弾く
            ##  - ずっと思い出していた。音楽のように何度も何度も人生の練習をして、一番良い人生を演奏できたならと
            ##  - だが男が弾いていたオルガンは、一切音が出ていなかった
            note="既に廃墟となったよく通った孤児院に戻ってきた男は、そこでオルガンを弾きながら、自分の決断を後悔した")
