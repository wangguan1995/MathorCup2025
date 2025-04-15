# 74 s
unzip -o /home/aistudio/3rd_lib.zip -d /home/aistudio/

# DataSet 1
# Pressure
unzip -o data/data258885/train_data.zip -d /home/aistudio/data
unzip -o /home/aistudio/data/data258885/track_A.zip -d /home/aistudio/data/
mv /home/aistudio/data/track_A /home/aistudio/data/test_data_1
mkdir /home/aistudio/data/validate_data_1/
cp /home/aistudio/data/data/press_001.npy  /home/aistudio/data/test_data_1/press_658.npy
unzip /home/aistudio/data/data281827/train_velocity.zip -d /home/aistudio/data
mv /home/aistudio/data/train /home/aistudio/data/train_data_1_velocity
mkdir -p /home/aistudio/data/Test/Dataset_1/
unzip /home/aistudio/data/data281827/test_dataset1_velocity.zip -d /home/aistudio/data/Test/Dataset_1/
mv /home/aistudio/data/Test/Dataset_1/test_dataset1_velocity /home/aistudio/data/Test/Dataset_1/Feature_File

# Dataset 2 (Building)
# geometry input: https://www.dropbox.com/scl/fo/h7q1msrlq6jdkyxxwki1s/h?dl=0&e=2
mkdir -p /home/aistudio/data/Training/Dataset_2/
mkdir -p /home/aistudio/data/Training/Dataset_2/Label_File/
cp /home/aistudio/data/data281827/dataset2_train_label.csv /home/aistudio/data/Training/Dataset_2/Label_File/
unzip /home/aistudio/data/data281827/Dataset_2_Feature.zip -d /home/aistudio/data/Training/Dataset_2/

mkdir -p /home/aistudio/data/Test/Dataset_2/Feature_File/
unzip /home/aistudio/data/data281827/test_data2_cd.zip -d /home/aistudio/data/Test/Dataset_2/Feature_File/
