import discord
import random
 
def run_discord_bot():
  TOKEN = 'MTQ3Njc2MDM1OTI5NjU2NTQ2OQ.GH9DfU.ofKx5Ot3nsogvZtnDkbVCTDv8qqynds3e2vF54' #enter token
  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)
 
  @client.event
  async def on_ready():
     print(f'{client.user} is now running!')
 
  @client.event
  async def on_message(message):
    if message.author == client.user:
      return
 
    # IN THE FOLLOWING CODE, CHOOSE WHAT MATH FUNCTION YOUR CODE WILL DO
    if message.content.startswith('!exponent'):
        nums = message.content.split()[1:]
        if len(nums) != 2:
            await message.channel.send('Please provide 2 numbers.')
            return
 
        try:
            num1 = float(nums[0])
            num2 = float(nums[1])
        except ValueError:
            await message.channel.send('Please provide valid numbers.')
            return
 
        result = num1 ** num2
        await message.channel.send(f'{num1} to the {num2} power is {result}.')
 
      #RANDOM FUNCTION, CHOOSE THE PARAMATERS OF THE RANDOM NUMBER YOU WANT TO GENERATE
      if message.content.startswith('!random'):
        await message.channel.send(random.randint(1,10))
 
      #DEFINE FUNCTION BELOW IS A SAMPLE, CREATE AN ADDITIONAL 5-10 MATH WORDS THAT YOU WILL RESEARCH AND DEFINE
      if message.content.startswith('!define function'):
        await message.channel.send("A function in mathematics is an expression, rule, or law that defines a relationship between one variable (the independent variable) and another variable (the dependent variable).")
 
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f'{username} said: "{user_message}" ({channel})')
 
 
  client.run(TOKEN)
