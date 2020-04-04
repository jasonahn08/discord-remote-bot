import discord
import random
import os


client = discord.Client()
@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("made in jason (REMOTE BOT)")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.author == client.user:
        return



    if message.content.startswith("신입이에요"):
        await message.channel.send("신입인가요?")


    if message.content.startswith("무슨서버 인가요?"):
        await message.channel.send("코코 발게로 입니다 제이슨한테 연락 가겠습니다 #rule을 확인해 주세요")
        jason = message.guild.get_member(int("492704346333773834"))
        await jason.send("새로운 부족원이 와써")

    if message.content.startswith("무슨서버인가요?"):
        await message.channel.send("코코 발게로 입니다 제이슨한테 연락 가겠습니다 #rule을 확인해 주세요")
        jason = message.guild.get_member(int("492704346333773834"))
        await jason.send("새로운 부족원이 와써")

    if message.content.startswith("무슨 서버인가요?"):
        await message.channel.send("코코 발게로 입니다 제이슨한테 연락 가겠습니다 #rule을 확인해 주세요")
        jason = message.guild.get_member(int("492704346333773834"))
        await jason.send("새로운 부족원이 와써")


    if message.content.startswith("님"):
        MESSAGES = ["왜요??", "왜 불름니까?", "뭡니까?" , "."]
        rand = random.randint(0, 3)
        await message.channel.send(MESSAGES[rand])
        #jason = message.guild.get_member(int("492704346333773834"))
        #await jason.send("님을 썼쒀쒀")

    if message.content.startswith("삼슨아"):
        sam = ["왜요??", "왜 불름니까?", "뭡니까?", "." , "?" , "!?" , "아크하셈" , "괴롭힐려고 나 불렀음?" , "읭?" , ".ww." , "공격 갈 집을 찾은거야?" , "흠냐" , "부르지마@!@" , "@@" , "ㅇㅅㅇ" , "ㅇㅇ?" , "ㅇ?" , "뭐?"]
        rand = random.randint (0, 18)
        await message.channel.send(sam[rand])





    if message.content.startswith("규칙"):
        await message.channel.send("@everyone 패드립 금지 , 건의.문의 사항 있으면 족장 Dm으로 하기 , 서로 싸우지 않기 혹시라도 싸우면 빨리 화해하기 , 인사이딩 하지 않기 , 도배하지 않기 , 원하는것 있으면 role에다가 적기")

    if message.content.startswith("노래"):
         await message.channel.send("노래를 듣고 싶으시다면은 zerotwo 또는 ferdboat을 이용하세요 참 mee6도 사용 가능하답니다")

    if message.content.startswith("애너미"):
         await message.channel.send("애너미? 어디? @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미@everyone애너미@everyone애너미@everyone애너미")

    if message.content.startswith("simple키블 재료"):
        await message.channel.send("smallegg,cooked fish meat(요리된 생선)1개 , Rockarrot(당근)2개 , mejoberry(매조베리)5개 , fiber(섬유)5개 water(물)")

    if message.content.startswith("basic키블 재료"):
        await message.channel.send("extra small egg , cooked meat(요리된 고기)1개 , amarberry(아마르베리리)10개 , mejoberry(매조베리)5개 , tintoberry(틴토베리)10개 , fber(섬유)5개 , water(물)")

    if message.content.startswith("superior키블 재료"):
        await message.channel.send("large egg , prime meat jerky(고품질 육포)1개 , citronal(시트론)2개 , sap(수액) , rare mushroom(희귀 버섯)2개 , fiber(섬유)5개 , water(물)")

    if message.content.startswith("exceptioanl키블 재료"):
        await message.channel.send("Extra Large Egg , Focal Chili(포칼칠리)1개 , Rare Flower(희귀 꽃) , Mejoberry(매조베리)10개 , fiber(섬유)5개 water(물)")

    if message.content.startswith("extraordinary키블 재료"):
        await message.channel.send("Special Egg , Giant Bee Honey(벌꿀)1개 , Lazarus Chowder(라자르 차우더)1개 , Mejoberry(매조베리)10개 , fiber(섬유)5개 water(물)")

    if message.content.startswith("regular키블 재료"):
        await message.channel.send("medium egg , Cooked Meat Jerky(요리된 육포) , Longrass(옥수수)2개 , Savoroot(감자)2개 , fiber(섬유)5개 water(물)")


    if message.content.startswith("!아크키블재료"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("!DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("!mtue"):
        author = message.guild.get_member(int(message.content[6:24]))
        role = discord.utils.get(message.guild.roles, name= "mute")
        await author.add_roles(role)
        role = discord.utils.get(message.guild.roles, name="NEW MEMBER")
        await author.remove_roles(role)
        role = discord.utils.get(message.guild.roles, name="MEMBER")
        await author.remove_roles(role)
        role = discord.utils.get(message.guild.roles, name="ADMIN")
        await author.remove_roles(role)

    if message.content.startswith("!unmtue"):
        author = message.guild.get_member(int(message.content[8:26]))
        role = discord.utils.get(message.guild.roles, name= "mute")
        await author.remove_roles(role)
        role = discord.utils.get(message.guild.roles, name="NEW MEMBER")
        await author.add_roles(role)
        role = discord.utils.get(message.guild.roles, name="MEMBER")
        await author.add_roles(role)

    if message.content.startswith("!역할부여NEWMEMBER"):
        author = message.guild.get_member(int(message.content[15:33]))
        role = discord.utils.get(message.guild.roles, name= "NEW MEMBER")
        await author.add_roles(role)

    if message.content.startswith("!역할부여MEMBER"):
        author = message.guild.get_member(int(message.content[12:30]))
        role = discord.utils.get(message.guild.roles, name="MEMBER")
        await author.add_roles(role)

    if message.content.startswith("!역할부여ADMIN"):
        author = message.guild.get_member(int(message.content[11:29]))
        role = discord.utils.get(message.guild.roles, name="ADMIN")
        await author.add_roles(role)

    if message.content.startswith("!역할해제NEWMEMBER"):
        author = message.guild.get_member(int(message.content[15:33]))
        role = discord.utils.get(message.guild.roles, name="NEW MEMBER")
        await author.remove_roles(role)

    if message.content.startswith("!역할해체MEMBER"):
        author = message.guild.get_member(int(message.content[12:30]))
        role = discord.utils.get(message.guild.roles, name="MEMBER")
        await author.remove_roles(role)

    if message.content.startswith("!역할해체ADMIN"):
        author = message.guild.get_member(int(message.content[11:29]))
        role = discord.utils.get(message.guild.roles, name="ADMIN")
        await author.remove_roles(role)

    if message.content.startswith("!밴"):
        author = message.guild.get_member(int(message.content[3:21]))
        await message.guild.ban(author)
        await message.channel.send("당신은 바로 밴 되었습니다")

    if message.content.startswith("!밴접속"):
        author = message.guild.get_member(int(message.content[5:23]))
        author2 = message.guild.get_member(int(message.content[5:20]))
        await message.guild.ban(author)
        await message.channel.send(author2 + "는 하루동안 접속을 하지 않았기 때문에 밴 되었습니다")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
