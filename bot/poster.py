from telegram import Bot
from datetime import datetime
import pytz

from config import TELEGRAM_TOKEN


bot = Bot(token=TELEGRAM_TOKEN)


def format_message(feature):
    properties = feature["properties"]
    geometry = feature["geometry"]

    # Convert time to UTC+3
    event_time_utc = datetime.utcfromtimestamp(properties["time"] / 1000)
    ethiopia_tz = pytz.timezone("Africa/Addis_Ababa")
    event_time_ethiopia = event_time_utc.astimezone(ethiopia_tz)

    # Location and depth
    location = properties["place"]
    latitude = geometry["coordinates"][1]
    longitude = geometry["coordinates"][0]
    depth = geometry["coordinates"][2]
    magnitude = properties["mag"]

    title = f"🌍 *New Earthquake In Ethiopia Reported ({event_time_ethiopia.strftime('%I:%M %p')})*"
    description = (
        f"*Location:* {location}\n"
        f"*Magnitude:* {magnitude}\n"
        f"*Depth:* {depth} KM\n\n"
        f"*Coordinates:* {latitude:.3f}°N {longitude:.3f}°E\n"
        f"*Reported On:* {event_time_ethiopia.strftime('%Y-%m-%d %H:%M:%S')} (UTC+03:00)\n"
        f"*More Detail:* {properties['url']}"
    )

    return title, description


async def post_to_telegram(chat_id, feature):
    title, description = format_message(feature)
    message = f"{title}\n\n{description}"
    await bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")
