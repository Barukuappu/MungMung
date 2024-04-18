import random
import discord

from mytoken import token
from songs import songs
from links import links

client = discord.Client(intents = discord.Intents.all())

@client.event
async def on_ready():
    print('봇이 로그인되었습니다.')

@client.event
async def on_message(message):
    if message.content == '!!봇':
        embed = discord.Embed(title='멍멍! 귀여운 멍멍이랑 놀아주세요!',description='**!!봇** | 방금 전에 당신이 친 명령어예요.\n**!!안녕** | 멍멍이가 인사해줘요!\n**!!가위바위보 (가위/바위/보)** | 멍멍이랑 가위바위보를 해요!\n\n**!!곡** | 멍멍이가 목록에 있는 YouTube의 퍼리 커버 곡들 중 한 곡을 랜덤으로 골라줘요!\n**!!스트리머** | 멍멍이가 목록에 있는 치지직의 퍼리 스트리머들 중 한 명을 랜덤으로 골라줘요!', color=0xefe2d2)
        embed.set_author(name='MADE BY SKYDOG ( SKYDOG.DEV )', url='https://skydog.dev')
        embed.set_footer(text='취소선은 현재 개발 중이거나 계획 중에 있는 것입니다.')
        await message.channel.send(embed=embed)

    if message.content == '!!안녕':
        greetings = [
            '🐶 **안녕! 멍멍이가 인사해요!**',
            '🐶 **멍멍이랑 놀고 싶어서 왔나요?**',
            '🐶 **놀러와요! 멍멍이는 여러분이랑 놀고 싶어요!**',
            '🐶 **배고파요... 멍멍이에게 맛있는 간식을 주세요!**',
            '🐶 **오늘도 멍멍! 여러분에게 행복을 드리기 위해 멍멍이가 왔어요.**'
        ]

        random_greeting = random.choice(greetings)
        await message.channel.send(f'{random_greeting}  |  TO {message.author.display_name}')

    if message.content.startswith('!!가위바위보'):
        player_choice = message.content.split(' ')[1].lower()

        if player_choice not in ['가위', '바위', '보']:
            await message.channel.send('**잘못된 입력이야!** 가위, 바위, 보 중 하나를 입력해줘.')
            return

        bot_choice = random.choice(['가위', '바위', '보'])

        result = ''
        if player_choice == bot_choice:
            result = '**비겼어!**'
        elif (player_choice == '가위' and bot_choice == '바위') or \
             (player_choice == '바위' and bot_choice == '보') or \
             (player_choice == '보' and bot_choice == '가위'):
            result = '**네가 이겼네!**'
        else:
            result = '**멍멍이가 이겼어!**'

        await message.channel.send(f'**{message.author.display_name}**(은/는) **{player_choice}**(을/를) 선택했고, 멍멍이는 **{bot_choice}**(을/를) 선택했어.\n{result}')

    if message.content == '!!곡':
        song = random.choice(songs)
        embed = discord.Embed(title=song['title'], color=0xff0000)
        embed.add_field(name="아티스트", value=song['artist'], inline=False)
        embed.add_field(name="링크", value=song['url'], inline=False)
        embed.add_field(name="언어", value=song['language'], inline=False)
        embed.set_author(name='🐶 멍멍! 이 곡은 어떠신가요?')
        embed.set_footer(text='언어는 원곡이 아닌 커버곡 기준입니다. 영상은 YouTube의 것만 가져옵니다.')
        await message.channel.send(embed=embed)

    if message.content == '!!스트리머':
        link = random.choice(links)
        embed = discord.Embed(title=link['info'], color=0x00CC82)
        embed.add_field(name="치지직 링크는 여기로!", value=link['url'], inline=False)
        embed.set_author(name='🐶 멍멍! 이 스트리머는 어떠신가요?')
        embed.set_footer(text='스트리머 목록은 치지직의 것만 가져옵니다.')
        await message.channel.send(embed=embed)

client.run(token)