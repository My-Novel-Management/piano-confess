# -*- coding: utf-8 -*-
"""Episode: 2.彼女の夢
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
def sc_famouspianist(w: World):
    josef, an = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    samuel = W(w.samuel)
    return w.scene("有名なピアニスト",
            josef.be("カフェで働いている"),
            an.come("連れ立って入ってくる"),
            samuel.come(),
            samuel.look("黒人で長身", "紫のベストを着て、サングラス", "よくテレビで見た姿"),
            josef.do("ホール係が注文を取りに行くのを見ている"),
            an.do("座ってから、ちらちらと$josefを見て"),
            _.look("緊張気味"),
            samuel.talk("歌は小さい頃から？"),
            an.talk("そうです"),
            samuel.talk("誰にも習わず？"),
            an.talk("はい。独学です"),
            camera=w.josef,
            area=w.Portland,
            stage=w.on_cafe_int,
            )

def sc_herdesicion(w: World):
    josef, an = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("彼女の決断",
            josef.be(),
            an.be(),
            josef.do("彼女が部屋にきて、話している"),
            inside.look("ボロアパートの内装。風呂もなく、ベッド代わりの拾ってきたソファ",
                "それでも電子ピアノだけは置いてある"),
            josef.talk("すごいじゃないか！", "あの$samuelだろ？",
                "ブラックミュージックシーンで神扱いを受けている人だ",
                "本当に君は才能があったんだよ！"),
            an.talk("そうなのかしら",
                "でも一緒にニューヨークに来て欲しいって"),
            josef.talk("チャンスだろ？", "選ばないなんてことは絶対にできない",
                "歌手になりたいなら、行くべきだよ"),
            an.talk("そう、よね。やっぱりそうだよね"),
            josef.think("だが表情が優れない彼女を見て、どうしたんだと"),
            an.talk("$meはね、歌が好き",
                "でもそれと同じくらい今の生活も好きなの",
                "大切な仲間たちと日々の、大変だけど楽しい暮らしの中で、",
                "それをあなたが曲にして、$meが歌う",
                "でもニューヨークに行ったら、彼についていったら、それは消えてなくなってしまう"),
            josef.talk("歌手になるって、そういうことなんじゃないのか？"),
            an.talk("分かってる"),
            josef.talk("それじゃあ決まりだ"),
            an.do("寂しそうな顔"),
            josef.talk("これ、開けるか"),
            an.talk("デビュー記念まで取っておこうって言ってたのに"),
            josef.talk("いいんだよ", "デビューしたようなもんだ"),
            josef.do("高級ワインを開け、注ぐ"),
            josef.talk("乾杯だ"),
            an.talk("うん"),
            stage=w.on_apart,
            )

def sc_goodbye(w: World):
    josef, anna = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    samuel = W(w.samuel)
    return w.scene("さよなら",
            josef.be(),
            josef.do("彼女がタクシーで$samuelと一緒に行くのを見送る"),
            josef.think("これでお別れだった"),
            stage=w.on_street,
            )

## episode
def ep_herdream(w: World):
    return w.episode("２．彼女の夢",
            sc_famouspianist(w),
            sc_herdesicion(w),
            sc_goodbye(w),
            ## NOTE
            ##  - 彼女は有名なピアニストに誘われ、歌手デビューする為にニューヨークに行く
            ##  - 彼女を応援する為に男は身を引いた
            note="彼女の夢を叶える為、男は身を引いて姿を消した")
