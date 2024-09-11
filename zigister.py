import discord
import requests
import os
TOKEN = os.environ['TOKEN']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await tree.sync(guild=discord.Object(id=1212790548302405662))  # Syncing the command tree
        print("Command tree synced and ready!")

# Define intents and initialize the client
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

# Command Tree for slash commands
tree = discord.app_commands.CommandTree(client)

# Define a slash command to get repo info from Zigistry
@tree.command(
    name="tell",
    description="Tell me your GitHub repo's full name",
    guild=discord.Object(id=1212790548302405662)  # Replace with your guild ID
)
async def first_command(interaction: discord.Interaction, github_user_name: str, github_repo_name: str, need_readme:bool=False):
    # Zigistry API URL
    zigistry_url = f'https://zigistry.dev/api/packages/{github_user_name}/{github_repo_name}'
    github_url = f'https://github.com/{github_user_name}/{github_repo_name}'
    
    # Make an API request to Zigistry
    response = requests.get(zigistry_url)
    response = requests.get(zigistry_url)
    
    if response.status_code == 200:
        data = response.json()
        result = f"""## {github_repo_name.capitalize()}
_{data.get("description", "No description available.")}_
[Zigistry URL]({zigistry_url}) | [GitHub URL]({github_url})
        """
        await interaction.response.send_message(result)
    else:
        await interaction.response.send_message(f"Sorry, the repo {github_repo_name} is not registered on Zigistry yet.")

client.run(TOKEN)
