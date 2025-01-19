import os
import csv

def create_labels_csv(data_dir, output_csv):
    """
    Generates a CSV file mapping images to their labels.

    Args:
        data_dir (str): Path to the dataset directory (organized by folders for each class).
        output_csv (str): Path to save the generated CSV file.
    """
    # Open the CSV file for writing
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        # Write the header
        writer.writerow(['image_path', 'label'])
        
        # Walk through each folder in the dataset directory
        for label in os.listdir(data_dir):
            label_path = os.path.join(data_dir, label)
            
            # Ensure it's a directory
            if os.path.isdir(label_path):
                # Iterate over all files in the label folder
                for image_file in os.listdir(label_path):
                    if image_file.endswith(('.png', '.jpg', '.jpeg')):  # Adjust extensions as needed
                        image_path = os.path.join(label_path, image_file)
                        # Write the image path and label to the CSV
                        writer.writerow([image_path, label])
    
    print(f"CSV file created: {output_csv}")

# Example usage
data_directory = "data"  # Path to your dataset
output_csv_path = "labels.csv"
create_labels_csv(data_directory, output_csv_path)
