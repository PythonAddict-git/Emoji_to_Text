import emoji

# Sample text containing emojis
text_with_emojis = "I love Python! 🐍❤️😊"

# Convert emojis to text
text_with_textual_emojis = emoji.demojize(text_with_emojis)

print(text_with_textual_emojis)
