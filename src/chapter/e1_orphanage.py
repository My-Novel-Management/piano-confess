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
            outside.look("雨粒がひび割れたアスファルトの上を流れていった"),
            josef.come("そこを、右足を引き摺るようにして端の縮れたコートを着た男が歩いている", "傘もない",
                "男の先には十年も前に捨てられて廃墟となったままの教会がまだ建っていたが、",
                "突風に煽られ、入り口のドアの片方が外れて飛んでいった"),
            _.do("男は気にせず、湿気混じりの空気が流れ込むその建物へと入る"),
            _.think("まだ半分の身長だった頃、毎日のように神父から説教されていたのが昨日のことのようだ、と男は思い出す","ただその懐かしさは半壊していた",
                "並べられた木椅子は倒れ、瓦礫まみれだ",
                "天井の一部が破れ、薄日が差し込む",
                "宣誓台も横倒しになり、聖書が数冊散らばっている",
                "それでも正面の壁にはマリア像が張り付き、男を迎えてくれていた"),
            josef.talk("ああ、神よ……$meに、もう一度、弾かせてくれ",
                "最期の、ピアノを"),
            _.do("ポケットから取り出した黒いロザリオを握り締めて祈る", "&"),
            _.do("それから砂埃を被ったオルガンの前まで進むと、",
                "椅子を引き、その蓋を開けた",
                "右の人差し指をＡの白鍵に乗せると、乾いた音が響いた",
                "あれだけ震えていた指が不思議なほど静まり返り、懐かしのメロディを奏で始める"),
            _.do("男はマリア像を見上げながら後悔の日々を思い起こしていた"),
            camera=w.josef,
            stage=w.on_church_int,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_meetagain(w: World):
    josef, an = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    jean = W(w.jean)
    return w.scene("幼馴染",
            w.symbol("　　　　◆"),
            w.comment("ずっと一緒にいた、方がよいのでそっちに"),
            josef.be("#仕事先のカフェ。働いている"),
            josef.look("まだ髭もなく、目もよく見え、足も軽々と地面を蹴ることができた三十一年前、",
                "男は東海岸のカフェで働いていた"),
            an.come("#入ってきて"),
            an.talk("ねえ$josef、ピアノ弾いてよ"),
            an.do("客のいない店内に急いで入ってきた金髪のショートボブの娘は、ジュニアスクールのような白いワンピースを見せつけるようにひらりとさせ、",
                "モップを掛けていた$josefに笑いかける"),
            josef.talk("$annaはもうピザ屋の手伝いは終わったのか？"),
            an.talk("うん、終わったよー", "出来損ないのピザ貰ったから後で持ってってあげる",
                "それより今暇でしょ？", "ピアノ、お願い"),
            josef.talk("だから店長に怒られるって"),
            josef.do("カウンターの奥で気難しい顔をしている入れ墨の大男は新聞を広げていたが、彼女に気づいたようでこちらを見ると親指を立てて、奥のピアノを差した"),
            an.talk("店長大好き！"),
            josef.talk("じゃあ、一曲だけな"),
            an.talk("うん！"),
            josef.do("モップを置いて、先に駆けていった$annaの後に続く",
                "カウンターの右側に黒のグランドピアノが置かれている",
                "毎日$Sが手入れをしていて頼まれれば曲を弾いた",
                "蓋を開け、十本の指を乗せる"),
            _.do("彼女を見れば準備完了とばかりに両手を胸の前で組んでいる", "目配せを待ってから、鍵盤を押し下げた"),
            josef.do("曲は決まっている",
                "『$w_wonderful』",
                "天才サッチモの名曲だ",
                "静かなアルペジオに彼女の澄んだ声が乗っていく", "&"),
            an.do("小さな体で思い切り息を吸い込み、伸びやかに歌い上げるそれは外を歩く人間の足をよく止めた"),
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
            ).omit()

def sc_happydays(w: World):
    josef, an = W(w.josef), W(w.anna)
    inside, outside = W(w.inside), W(w.outside)
    jean = W(w.jean)
    return w.scene("楽しかった日々",
            an.talk("いらっしゃいませ"),
            josef.do("働いている彼女を見て、こんな日々が続けばいいなと"),
            ).omit()

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
