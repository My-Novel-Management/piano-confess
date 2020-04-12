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
            w.symbol("　　　　◆"),
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
            ).omit()

def sc_ruins(w: World):
    josef, anna = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("廃墟でオルガンを弾く男",
            w.symbol("　　　　◆"),
            w.comment("オルガンを弾いている途中からここに戻ってくる"),
            josef.be("指は淀みなく鍵盤を押さえていた"),
            inside.look("自分を見下ろすマリアは何も言わない",
                "そのひび割れた顔でただ自愛の眼差しを向けているだけだ",
                "風が破れた壁から吹き込み、雨は瓦礫に打ち付ける", "&"),
            josef.think("呼吸の為に開けた口は目に見えない砂利を吸い込み、ひりつく喉を傷つけた",
                "それでも歯を食い縛り、$Sは指を動かす",
                "オルガンのやや籠もった音が誰もいない教会の壁で跳ね返り、開いた天井から空へと上がっていく"),
            josef.think("――どうして$meは！"),
            josef.do("激しい鍵盤のうねりはハーモニィではなくただのぶつかり合う音波だ",
                "感情の揺さぶりを表現する細かいトレモロも、綺麗に跳ねるアルペジオも、",
                "もう彼女は何も応えてはくれない"),
            josef.do("天を見上げ、微かに覗く青空に$Sは後悔を叫ぶ"),
            josef.think("――あいつの手を掴んでやれなかった！"),
            josef.do("不協和音が侵食する"),
            josef.think("――なぜ自分が幸せにしてやると言えなかった！"),
            josef.do("黒鍵で転調させ、エレジーに突き落とす"),
            josef.think("――どうして一緒に夢を叶える選択をしてやれなかった！"),
            josef.do("涙が頬の汚れを落としていく",
                "視界は霞み、鼻水は滲み、口を開けば後悔の念が呪詛のようにばらまかれた"),
            josef.talk("$meは！"),
            josef.do("こんなピアノの、どこが”素晴らしい世界”なんだ",
                "無茶苦茶なメロディにあの世で彼女が笑っているだろう",
                "その笑顔すら、もう想像できない",
                "思い出せるのはいつだって三十一年前のまだ鼻を赤くしていた彼女の笑顔だけだ"),
            inside.look("倒れた宣誓台の脇に落ちていた聖書が、風で捲れていく",
                "&"),
            josef.think("$Sは当時世話になっていた牧師がよく口にしていた一節を思い出した",
                "『$w_seisho1』というものだ"),
            _.think("――$meは愚か者だ"),
            _.do("指は冒頭のメロディへと戻り、テンポを落として彼女の歌声を待つ",
                "何度もぐるぐると同じメロディを奏でながら、目を閉じ、あの聖女のような歌声を待つ",
                "けれどももう何も聞こえない"),
            _.do("彼女がいないから？"),
            _.do("違う"),
            _.think("――違うんだ！"),
            _.do("思い切り叩きつけた鍵盤は、何も鳴らさなかった", "最初から音など一つも鳴っていなかったのだ"),
            camera=w.josef,
            stage=w.on_church_int,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_truth(w: World):
    josef, anna = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("真実の演奏",
            josef.be("$Sは立ち上がり、壊れたオルガンの蓋を閉じる",
                "けれど蓋はうまく閉まらずに止め金が外れ、床に転がって落ちた"),
            _.do("それを見て、思わず嗚咽が漏れる", "自分がただ、何もかもを駄目にするだけの存在な気がして、情けなくなるのだ",
                "膝を折り、地面に拳を叩きつける",
                "彼女を守る為に使わなかった拳を、ピアニストとして一番大事な指を、思い切り傷つける",
                "でもそんなことをしても、もうあの頃には戻れない"),
            _.do("コートの懐に手を入れ、黒いロザリオを取り出した", "彼女が身につけていたものだ"),
            anna.voice("もう一度、あなたのピアノで歌いたかった"),
            josef.do("ロザリオを握りしめ、拳を叩きつける", "&"),
            josef.do("紐が千切れ、玉が転がる",
                "散らばって、見えなくなって、全部どこかに行ってしまった",
                "それは$Sの前から消えてしまった彼女のように"),
            josef.do("男は声を上げる",
                "愛していたと、心の鍵盤を殴りつけた"),
            w.symbol("（了）"),
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
