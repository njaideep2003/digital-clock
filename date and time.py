from datetime import datetime
import pytz

# Specify the timezone (e.g., UTC)
timezone = pytz.timezone('America/Chicago')  # Change 'America/Chicago' to other timezones as needed

# Get the current date and time for the specified timezone
current_time = datetime.now(timezone)

# Print date, time with AM/PM, and day on separate lines
print("Current Date:", current_time.strftime("%Y-%m-%d"))
print("Current Day:", current_time.strftime("%A"))
print("Current Time:", current_time.strftime("%I:%M:%S %p"))
