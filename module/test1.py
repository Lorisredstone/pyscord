import pyscord
import random
import discord

bot = pyscord.Client(token="ODc3NTY4Njc0NjY2NTI0Njgy.YR0hhA.qahcocZ66Ic7dQk8mgXLvwt4kK8", api_version=9)
guild = bot.getguild(804096311975477279)
print(guild.id)
print(guild.name)
print(guild.icon)
print(guild.description)
print(guild.splash)
print(guild.discovery_splash)
print(guild.features)
print(guild.emojis)
print(guild.stickers)
print(guild.banner)
print(guild.owner_id)
print(guild.application_id)
print(guild.region)
print(guild.afk_channel_id)
print(guild.afk_timeout)
print(guild.system_channel_id)
print(guild.widget_enabled)
print(guild.widget_channel_id)
print(guild.verification_level)
print(guild.roles)
print(guild.default_message_notifications)
print(guild.mfa_level)
print(guild.explicit_content_filter)
print(guild.max_presences)
print(guild.max_members)
print(guild.max_video_channel_users)
print(guild.vanity_url_code)
print(guild.premium_tier)
print(guild.premium_subscription_count)
print(guild.system_channel_flags)
print(guild.preferred_locale)
print(guild.rules_channel_id)
print(guild.public_updates_channel_id)
print(guild.nsfw)
print(guild.nsfw_level)