import discord
import openpyxl
import os

client = discord.Client()
@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("REMOTE BOT")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("안녕"):
        await message.channel.send("ㅎㅇ")

    if message.content.startswith("규칙"):
        await message.channel.send("@everyone 패드립 금지 , 건의.문의 사항 있으면 족장 Dm으로 하기 , 서로 싸우지 않기 혹시라도 싸우면 빨리 화해하기 , 인사이딩 하지 않기 , 도배하지 않기 , 원하는것 있으면 role에다가 적기")

    if message.content.startswith("노래"):
         await message.channel.send("노래를 듣고 싶으시다면은 zerotwo 또는 ferdboat을 이용하세요 참 mee6도 사용 가능하답니다")

    if message.content.startswith("애너미"):
         await message.channel.send("애너미? 어디? @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미 @everyone애너미@everyone애너미@everyone애너미@everyone애너미")


    if message.content.startswith("!사진"):
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

    if message.content.startswith("!경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(author.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 3:
                    await message.guild.ban(author)
                    await message.channel.send("경고3회 부족에서 밴")
                elif sheet["B" + str(i)].value == 2:
                    await message.guild.ban(author)
                    await message.channel.send("경고2회 3회시 벤")
                else:
                    await message.channel.send("경고1회 3회시 밴")
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(author.id)
                sheet["B" + str(i)].value = 1
                file.save("경고.xlsx")
                await message.channel.send("경고1회 3회시 밴")
                break
            i += 1
    if message.content.startswith("!밴"):
        author = message.guild.get_member(int(message.content[3:21]))
        await message.guild.ban(author)
        await message.channel.send("당신은 바로 밴 되었습니다")










            # if message.content.startswith("/채널메시지"):
    #    channel = message.content[7:25]
     #   msg = message.comtnet[26:]
      #  await client.get_channel(int(channel)).send(msg)



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
