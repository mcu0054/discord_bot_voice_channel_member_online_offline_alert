from typing import List
import discord
from discord.ext import commands
from discord.ext import tasks

onlineM=[]

#Get difference between two lists
def Diff(li1, li2):
    print('Li1:', li1, 'Li2:', li2)
    c=[x for x in li1 if x in li2]
    d=[y for y in (li1+li2) if y not in c]
    print(d)
    return d


#Check member changes
async def getOnlineMember():
    channel = client.get_channel('Voice Channel ID')
    members = channel.members  # finds members connected to the channel
    tempList=[]
    for member in members:
        tempList.append(member.name)
        print(member.name)
    print("--------")
    re=Diff(onlineM,tempList)

    channelMSG = client.get_channel('Text Channel ID')
   

    for rows in re:
        if rows in onlineM:
            to_send = f'{rows}Enter voice channel' #rows:member's name
            print(to_send)
            await channelMSG.send(to_send, tts=True)
            
        if rows in tempList:
            to_send = f'{rows}Leave voice channel'
            print(to_send)
            await channelMSG.send(to_send, tts=True)
            
    for i in range (len(onlineM)):
        onlineM.pop(0)
    for j in tempList:
        onlineM.append(j)


@tasks.loop(seconds=1)  # 每幾秒執行#Execute every one second
async def printer():
    await client.wait_until_ready()
    await getOnlineMember()

class MyClient(discord.Client):

    async def on_ready(self):#bot start
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        channel = client.get_channel('Voice Channel ID')
        members = channel.members  # finds members connected to the channel
        for member in members:
            onlineM.append(member.name)
        printer.start()#loop start
        # gets the channel you want to get the list from

        


    


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('bot token ')



