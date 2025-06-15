import re

def parse_chat(file_path):
    # WhatsApp message pattern (dd/mm/yy, hh:mm - sender: message)
    pattern = r"^\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}\s?(AM|PM|am|pm)?\s?-\s([^:]+): (.+)"
    messages = []

    with open(file_path, encoding="utf-8") as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                sender = match.group(2).strip()
                message = match.group(3).strip()

                # Skip system messages and non-text content
                if not message.startswith("<Media omitted>") and \
                   not message.lower().startswith("missed") and \
                   "location:" not in message.lower() and \
                   "end-to-end encrypted" not in message.lower():
                    messages.append((sender, message))  # return as tuple for consistency

    print(f"✅ Parsed {len(messages)} valid messages.")
    return messages
