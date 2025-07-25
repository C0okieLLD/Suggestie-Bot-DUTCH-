import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ✅ Modal
class SuggestieModal(discord.ui.Modal, title="Suggestie Indienen"):
    suggestie = discord.ui.TextInput(
        label="Wat is je suggestie?",
        style=discord.TextStyle.paragraph,
        placeholder="Typ hier je idee...",
        required=True,
        max_length=500
    )

    async def on_submit(self, interaction: discord.Interaction):
        try:
            embed = discord.Embed(
                title="📭 Nieuwe Suggestie",
                description=self.suggestie.value,
                color=discord.Color.green()
            )
            embed.set_footer(
                text=f"Ingezonden door {interaction.user.name}",
                icon_url=interaction.user.display_avatar.url
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(
                f"❌ Er ging iets mis: `{str(e)}`",
                ephemeral=True
            )

# ✅ View met knop
class SuggestieView(discord.ui.View):
    @discord.ui.button(label="Dien een suggestie in", style=discord.ButtonStyle.primary)
    async def knop_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(SuggestieModal())

# ✅ Command die de knop toont
@bot.command()
async def suggestie(ctx):
    await ctx.send("📬 Klik op de knop hieronder om een suggestie in te dienen:", view=SuggestieView())

# ✅ Start de bot (vervang dit door je echte token – NIET in publieke code!)
bot.run("YOUR_BOT_TOKEN_HERE")
