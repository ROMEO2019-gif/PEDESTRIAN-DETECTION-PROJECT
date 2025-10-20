import os
import shutil

# Path to KITTI label and image folders
LABELS_DIR = "D:/MSCS/MSCS21/Intelligent_Systems_Robotics/OD_Project/dataset/labels"  # e.g., "kitti/training/label_2"
IMAGES_DIR = "D:/MSCS/MSCS21/Intelligent_Systems_Robotics/OD_Project/dataset/images"  # e.g., "kitti/training/image_2"

# Output folder for filtered labels (optional: can overwrite original)
OUTPUT_LABELS_DIR = "D:/MSCS/MSCS21/Intelligent_Systems_Robotics/OD_Project/dataset/filtered_labels"
os.makedirs(OUTPUT_LABELS_DIR, exist_ok=True)

# Classes to keep
PEDESTRIAN_CLASSES = ["Pedestrian", "Person_sitting"]

# Process all label files
for label_file in os.listdir(LABELS_DIR):
    if not label_file.endswith(".txt"):
        continue

    input_path = os.path.join(LABELS_DIR, label_file)
    output_path = os.path.join(OUTPUT_LABELS_DIR, label_file)

    with open(input_path, "r") as f:
        lines = f.readlines()

    # Filter lines for pedestrian classes
    filtered_lines = [line for line in lines if line.split()[0] in PEDESTRIAN_CLASSES]

    # Write filtered labels (can be empty if no pedestrian)
    with open(output_path, "w") as f:
        f.writelines(filtered_lines)

print("Filtering complete! Labels now contain only pedestrian classes.")
