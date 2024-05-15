import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

genai.configure(api_key=os.getenv["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-latest",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

@bot.command()
async def chat(ctx, *, prompt=None):
  """Starts a conversation with the Gemini Therapist!"""
  await ctx.author.send("Hi! I'm ready to chat. Ask me anything!")

  chat_session = model.start_chat()
  if prompt:
    response = chat_session.send_message(prompt)
    await ctx.author.send(response.text)

  def check(m):
    return m.author == ctx.author and m.channel == ctx.author.dm_channel

  while True:
    message = await bot.wait_for("message", check=check)

    response = chat_session.send_message(message.content)
    await ctx.author.send(response.text)

# Run the bot
bot.run(os.getenv["DISCORD_TOKEN"])
