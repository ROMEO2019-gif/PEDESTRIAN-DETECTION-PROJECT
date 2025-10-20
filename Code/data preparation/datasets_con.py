from pathlib import Path
from labelformat.formats import KittiObjectDetectionInput, YOLOv8ObjectDetectionOutput

# Load KITTI labels
label_input = KittiObjectDetectionInput(
    input_folder=Path("D:/MSCS/MSCS21/Intelligent_Systems_Robotics/OD_Project/dataset/filtered_labels"),
    category_names="Pedestrian,Person_sitting",
    images_rel_path="../images"
)

# Convert to YOLOv8 and save
YOLOv8ObjectDetectionOutput(
    output_file=Path("D:/MSCS/MSCS21/Intelligent_Systems_Robotics/OD_Project/dataset/data.yaml"),
    output_split="train"
).save(label_input=label_input)