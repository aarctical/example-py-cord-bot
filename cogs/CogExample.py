import discord
from discord.ext import commands
from discord import guild_only
import asyncio

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("This Cog is now online!") # When the cog comes online!

    @commands.command(name="examplecommand", help="An example prefixed command!", aliases=['ec', 'e'])
    async def examplecommand(self, ctx: discord.ApplicationContext, *args):
        Text = ' '.join(args)
        if Text == "": # If the user did not give any parameters!
            await ctx.reply(f"This is an example command that uses a prefix! You didn't give any parameters!", delete_after=5) 
        else: # If the user gave parameters!
            await ctx.reply(f"This is an example command that uses a prefix! You said: `{Text}`", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()

    @commands.slash_command(name="exampleslash", help="An example slash command!", description="This gives information to the user!")
    async def exampleslash(self, ctx: discord.ApplicationContext, field):
        await ctx.respond(f"Hi <@{ctx.author.id}>! You said: `{field}`", ephemeral=True, delete_after=5)

    @commands.Cog.listener()
    async def on_message(self, ctx):
        print(f"{ctx.author} said {ctx.content}!") # Prints a line to the console of: user said message!

def setup(bot):
    bot.add_cog(ExampleCog(bot))

#           //
#          //
#          ||   
#          ||   It is important to remember each declaration (event or function) must start with self as its a function of the cog
#          ||   
#          ||   delete_after=x (x: int) Deletes the bots response after x seconds
#          ||   ephemeral=True (true/false: bool) Slash command reply option that shows the response to only the command author
#          ||   
#          ||   help="text" (text: str) This will show on the [prefix]help description of the command
#          ||   description="text" (text: str) This will show on the command description of the slash command
#          ||
#          \\
#           \\
