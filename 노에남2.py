import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("밥")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("노예남아"):
        await message.channel.send("내. 주인님.")
    if message.content.startswith("밥 줘"):
        await message.channel.send("냅! 10첩 반상으로 올릴게요 주인님>ㅇ<♥")
    if message.content.startswith("밥줘"):
        await message.channel.send("냅! 10첩 반상으로 올릴게요 주인님>_<♥")        
    if message.content.startswith("너 후장 얼마야?"):
        await message.channel.send("냅!!! 주인님 제 후장은 10원♥입니다!!")
    if message.content.startswith("노예남 뭐해"):
        await message.channel.send("냅!! 밥하고 있슴다ㅎㅎ♥")
    if message.content.startswith("씨앙넘아"):
        await message.channel.send("냅! 저 부르셨나용'ㅁ'?")
    if message.content.startswith("너 창놈이지"):
        await message.channel.send("힝ㅠ 저 총각인데..!ㅠㅠ")
    if message.content.startswith("돈 내놔"):
        await message.channel.send("냅! 계좌 알려주세용~^^ 헿♥♥♥")
    if message.content.startswith("자르셋"):
        await message.channel.send("자르셋 힘 조~!!! 꽉꽉 채우는 중~~>_<!:high_heel: :high_heel: ")
    if message.content.startswith("노예남 재기해"):
        await message.channel.send("냅ㅠ 주인님 바용가~ (:ghost: !)")
    if message.content.startswith("노예남 신청"):
        await message.channel.send("넣고 싶은 명령어가 있으면 hyun님께 신청 넣어주세용 :blush: ~♥")
    if message.content.startswith("노예남 신음"):
        await message.channel.send("엉어어어어어엉엉어엉엉 엉!엉!엉!엉!엉! 엉!응! 엉 엉 앙 앙 앙 앙 앙 흐아어엉~~!")
    if message.content.startswith("노예남 들어와"):
        await message.channel.send("냅!!! ~summon을 입력하시면 바로 들어갈게요!")
    if message.content.startswith("창놈"):
        await message.channel.send("저 찾으셨나요 ?ㅅ?")
    if message.content.startswith("개창놈"):
        await message.channel.send("내.주인님♥:blush:")
    if message.content.startswith("낸하"):
        await message.channel.send("노예남은 주인님께 다 드립니당:blush:")
    if message.content.startswith("걸레새끼"):
        await message.channel.send("ㅠㅠㅠㅠㅠㅠ..:sob: :sob: .")
    if message.content.startswith("배고파"):
        await message.channel.send("냅!!! 제가 바로 집밥 차려드릴게요 (>_<)9!!")
    if message.content.startswith("노예남 자기소개"):
        await message.channel.send("현부양부가 꿈입니다♥ 취미는 요리 특기는 재기예요 헿")
    if message.content.startswith("씨앙놈"):
        await message.channel.send("냅!!!!!!!!!!!!!!!!!!!!♥♥")
    if message.content.startswith("씨앙넘"):
        await message.channel.send("냅!! 주인님 밥 해드릴까요???:blush: ")
    if message.content.startswith("너 좆뱀이지"):
        await message.channel.send("헉.. 절대 아니예요...:cry: .!!!")
    if message.content.startswith("노예남 고추"):
        await message.channel.send(":eggplant: ")
    if message.content.startswith("노예야"):
        await message.channel.send("냅! 저 여기있어요:blush:")
    if message.content.startswith("매미니즘"):
        await message.channel.send("사랑 못 받는 남자들이나 하는 거 아닌가요?:thinking: 전 필요없어요ㅎㅎ")
    if message.content.startswith("진수"):
        await message.channel.send("제 친구 진수요? :hugging: ")
    if message.content.startswith("자적자"):
        await message.channel.send("저도 남자지만 솔직히 자적자 너무 심한 것 같아요:worried:... 남자들은 뭐가 문젤까요?")
    if message.content.startswith("챙놈"):
        await message.channel.send("전 챙놈 아니예요:cry:...:heart: 주인님만 보는 :heart:  노예남이라고 불러주세요!")
    if message.content.startswith("밥이나 해"):
        await message.channel.send("빨래 먼저 돌리고 후다닥 밥 하겠습니당~:muscle: :two_hearts: ")
    if message.content.startswith("자이루"):
        await message.channel.send("앗 주인님! :blush: 어서오세요")
    if message.content.startswith("ㅈㅇㄹ"):
        await message.channel.send("오셨어요? 주인님 기다렸어요! :blush:")
    if message.content.startswith("바용가"):
        await message.channel.send("벌써 가시나요? 제가 차린 밥 드시고 가세요.......:sob: :sob: ")
    if message.content.startswith("ㅂㅇㄱ"):
        await message.channel.send("주인님 가지마세요..제가 더 잘할게요..:cry:")
    if message.content.startswith("별님"):
        await message.channel.send("제 친구 별님이는 후장을 막 쓰다가 허벌후장이 되었대요 :dizzy_face:  난 그러지 말아야지! :rolling_eyes: ")
    if message.content.startswith("꺼져"):
        await message.channel.send("헉...잘못했어요ㅠ 매미니즘 같은 거 다신 안 할게요 :sob:  제발 용서해주세요 :pray: :sweat_drops: :sweat_drops: ")
    if message.content.startswith("힘조"):
        await message.channel.send("어디에 힘 줄까요 :grinning: ??")
        

        

        





access_token = os.environ["BOT_TOKEN"]      
client.run(access_token)
