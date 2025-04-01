import discord
from gtts import gTTS
import os

bot=discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is ready")
    bot.loop.create_task(sync_commands())

async def sync_commands():
    await bot.wait_until_ready()  # 機器人準備
    try:
        await bot.sync_commands()
        print("斜線指令已同步！")
    except Exception as e:
        print(f"同步指令時發生錯誤: {e}")
#斜線指令
@bot.slash_command(guild_ids=[ord("you_shouldn\'t_know_this")],name="send_code")
async def send_code(ctx,num:int,code:str):
    #符合人類念法(?)
    code=code.replace(")","").replace("}","").replace("]","")
    spelled_out = " ".join(code.upper())
    #是的,沒有念空白,不然會炸掉
    spelled_out=spelled_out.replace(".","dot").replace("\"","quotes").replace("\'","apostrophe").replace("\\","Back Slash").replace("/","Slash")
    spelled_out=spelled_out.replace(":","colon").replace(";","semicolon").replace("~","tilde").replace("@","at")
    spelled_out=spelled_out.replace("(","parentheses").replace("{","braces").replace("[","brackets")
    
    tts = gTTS(text=spelled_out, lang="en")  # 轉換文字為語音 (英文)
    tts.save(f"code{num}.mp3")  # 存成 MP3 檔案
    spelled_out=""
    code=""
    # 發送音檔
    try:
        await ctx.respond(file=discord.File(f"code{num}.mp3"))
    except Exception as e:
        await ctx.respond(f"發生錯誤: {e}")
    finally:
        # 刪除音檔（確保不佔空間）
        if os.path.exists(f"code{num}.mp3"):
            os.remove(f"code{num}.mp3")

# 啟動機器人
token="I_WON'T_TELL_U_THIS!_BRO"
bot.run(token)
