import json
import csv

# Load the emoji data from the JSON file
with open('dataset/emoji.json', 'r', encoding='utf-8') as json_file:
    emoji_data = json.load(json_file)

# Open CSV file for writing with two columns: 'image' and 'caption'
with open('emoji_captions.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['image', 'caption'])
    writer.writeheader()

    # Loop through each emoji entry in the JSON
    for emoji in emoji_data:
        unified = emoji.get('unified', 'Unknown')
        short_name = emoji.get('short_name', 'Unknown')

        # If the emoji has an Apple image, generate the Apple caption and write the row
        if emoji.get('has_img_apple'):
            image_path = emoji.get('img_apple')
            caption = (f"Apple Emoji: {unified} ({short_name}). "
                       "Features a glossy, 3D-like design with smooth gradients and detailed shading, "
                       "reflecting the refined aesthetics of iOS emojis.")
            writer.writerow({'image': image_path, 'caption': caption})

        # If the emoji has a Google image, generate the Google caption and write the row
        if emoji.get('has_img_google'):
            image_path = emoji.get('img_google')
            caption = (f"Google Emoji: {unified} ({short_name}). "
                       "Exhibits a flat, cartoonish style with bold outlines and minimal shading, "
                       "capturing the playful design typical of Android emojis.")
            writer.writerow({'image': image_path, 'caption': caption})
