import os
import shutil
from sklearn.model_selection import train_test_split

# 定义数据集路径
img_dir = "./train/images/"
labels_dir = "./train/labels/"
out_dir = "validation"

# 创建验证集目录结构
os.makedirs(os.path.join(out_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(out_dir, "labels"), exist_ok=True)

# 获取文件列表并验证配对
images = [f for f in os.listdir(img_dir) if f.endswith('.jpg')]
labels = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]

valid_images = []
valid_labels = []
for img in images:
    base_name = os.path.splitext(img)[0]
    label_file = base_name + ".txt"
    if label_file in labels:
        valid_images.append(img)
        valid_labels.append(label_file)
    else:
        print(f"警告：图像 {img} 无对应标签")

# 执行数据集划分（保持图片和标签的对应关系）
train_images, val_images, train_labels, val_labels = train_test_split(
    valid_images,
    valid_labels,
    test_size=200,          # 直接指定验证集数量
    random_state=42,        # 随机种子保证可重复性
    shuffle=True            # 打乱数据
)

# 移动验证集文件到新位置
for img in val_images:
    src_img = os.path.join(img_dir, img)
    dst_img = os.path.join(out_dir, "images", img)
    shutil.move(src_img, dst_img)

for label in val_labels:
    src_label = os.path.join(labels_dir, label)
    dst_label = os.path.join(out_dir, "labels", label)
    shutil.move(src_label, dst_label)

print(f"成功创建验证集：{len(val_images)} 张图片和 {len(val_labels)} 个标签")
print(f"剩余训练集：{len(train_images)} 张图片和 {len(train_labels)} 个标签")