from .utils import StringEnum

import enum


@enum.unique
class GuildFeature(StringEnum):
    """Discord guild enabled features.

    Attributes
    ----------
    ANIMATED_BANNER
        Guild has access to set an animated guild banner image.
    ANIMATED_ICON
        Guild has access to set an animated guild icon.
    AUTO_MODERATION
        Guild has set up auto moderation rules.
    BANNER
        Guild has access to set a guild banner image.
    COMMUNITY
        Guild can enable welcome screen, Membership Screening, stage channels and discovery,
        and receives community updates.
    DISCOVERABLE
        Guild is able to be discovered in the directory.
    ENABLED_DISCOVERABLE_BEFORE
        > No information available from Discord.
    EXPOSED_TO_ACTIVITIES_WTP_EXPERIMENT
        > No information available from Discord.
    FEATURABLE
        Guild is able to be featured in the directory.
    GUILD_HOME_TEST
        > No information available from Discord.
    HAS_DIRECTORY_ENTRY
        > No information available from Discord.
    INVITE_SPLASH
        Guild has access to set an invite splash background.
    MEMBER_PROFILES
        > No information available from Discord.
    MEMBER_VERIFICATION_GATE_ENABLED
        Guild has enabled Membership Screening.
    MONETIZATION_ENABLED
        Guild has enabled monetization.
    MORE_STICKERS
        Guild has increased custom sticker slots.
    NEWS
        Guild has access to create news channels.
    NEW_THREAD_PERMISSIONS
        > No information available from Discord.
    PARTNERED
        Guild is partnered.
    PREVIEW_ENABLED
        Guild can be previewed before joining via Membership Screening or the directory.
    PRIVATE_THREADS
        Guild has access to create private threads.
    RELAY_ENABLED
        > No information available from Discord.
    ROLE_ICONS
        Guild is able to set role icons.
    SEVEN_DAY_THREAD_ARCHIVE
        > No information available from Discord.
    TEXT_IN_VOICE_ENABLED
        > No information available from Discord.
    TICKETED_EVENTS_ENABLED
        Guild has enabled ticketed events.
    THREADS_ENABLED
        Guild has enabled threads.
    THREE_DAY_THREAD_ARCHIVE
        > No information available from Discord.
    VANITY_URL
        Guild has access to set a vanity URL.
    VERIFIED
        Guild is verified.
    VIP_REGIONS
        Guild has access to set 384kbps bitrate in voice (previously VIP voice servers).
    WELCOME_SCREEN_ENABLED
        Guild has enabled the welcome screen.

    """

    ANIMATED_BANNER = "ANIMATED_BANNER"
    ANIMATED_ICON = "ANIMATED_ICON"
    APPLICATION_COMMAND_PERMISSIONS_V2 = "APPLICATION_COMMAND_PERMISSIONS_V2"
    AUTO_MODERATION = "AUTO_MODERATION"
    AUTOMOD_TRIGGER_SPAM_LINK_FILTER = "AUTOMOD_TRIGGER_SPAM_LINK_FILTER"
    AUTOMOD_TRIGGER_ML_SPAM_FILTER = "AUTOMOD_TRIGGER_ML_SPAM_FILTER"
    CREATOR_MONETIZABLE_PROVISIONAL = "CREATOR_MONETIZABLE_PROVISIONAL"
    BANNER = "BANNER"
    COMMUNITY = "COMMUNITY"
    CREATOR_MONETIZABLE = "CREATOR_MONETIZABLE"
    COMMUNITY_EXP_LARGE_GATED = "COMMUNITY_EXP_LARGE_GATED"
    COMMUNITY_EXP_LARGE_UNGATED = "COMMUNITY_EXP_LARGE_UNGATED"
    COMMUNITY_EXP_MEDIUM = "COMMUNITY_EXP_MEDIUM"
    DISCOVERABLE = "DISCOVERABLE"
    ENABLED_DISCOVERABLE_BEFORE = "ENABLED_DISCOVERABLE_BEFORE"
    EXPOSED_TO_ACTIVITIES_WTP_EXPERIMENT = "EXPOSED_TO_ACTIVITIES_WTP_EXPERIMENT"
    FEATURABLE = "FEATURABLE"
    GUILD_HOME_TEST = "GUILD_HOME_TEST"
    GUILD_COMMUNICATION_DISABLED_GUILDS = "GUILD_COMMUNICATION_DISABLED_GUILDS"
    GUILD_ONBOARDING = "GUILD_ONBOARDING"
    GUILD_ONBOARDING_HAS_PROMPTS = "GUILD_ONBOARDING_HAS_PROMPTS"
    GUILD_ONBOARDING_EVER_ENABLED = "GUILD_ONBOARDING_EVER_ENABLED"
    GUILD_WEB_PAGE_VANITY_URL = "GUILD_WEB_PAGE_VANITY_URL"
    HAS_DIRECTORY_ENTRY = "HAS_DIRECTORY_ENTRY"
    INVITE_SPLASH = "INVITE_SPLASH"
    MEMBER_PROFILES = "MEMBER_PROFILES"
    MEMBER_VERIFICATION_GATE_ENABLED = "MEMBER_VERIFICATION_GATE_ENABLED"
    MONETIZATION_ENABLED = "MONETIZATION_ENABLED"
    MORE_STICKERS = "MORE_STICKERS"
    NEWS = "NEWS"
    NEW_THREAD_PERMISSIONS = "NEW_THREAD_PERMISSIONS"
    PARTNERED = "PARTNERED"
    PREVIEW_ENABLED = "PREVIEW_ENABLED"
    PRIVATE_THREADS = "PRIVATE_THREADS"
    RAID_ALERTS_ENABLED = "RAID_ALERTS_ENABLED"
    RELAY_ENABLED = "RELAY_ENABLED"
    ROLE_ICONS = "ROLE_ICONS"
    ROLE_SUBSCRIPTIONS_ENABLED = "ROLE_SUBSCRIPTIONS_ENABLED"
    SEVEN_DAY_THREAD_ARCHIVE = "SEVEN_DAY_THREAD_ARCHIVE"
    TEXT_IN_VOICE_ENABLED = "TEXT_IN_VOICE_ENABLED"
    TICKETED_EVENTS_ENABLED = "TICKETED_EVENTS_ENABLED"
    THREADS_ENABLED = "THREADS_ENABLED"
    THREE_DAY_THREAD_ARCHIVE = "THREE_DAY_THREAD_ARCHIVE"
    VANITY_URL = "VANITY_URL"
    VERIFIED = "VERIFIED"
    VIP_REGIONS = "VIP_REGIONS"
    WELCOME_SCREEN_ENABLED = "WELCOME_SCREEN_ENABLED"
