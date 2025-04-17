import paddle
import numpy as np
import sys
sys.path.append("./PaddleScience/")
sys.path.append('/home/aistudio/3rd_lib')

from pathlib import Path
from src.data.base_datamodule import BaseDataModule
from src.data.velocity_datamodule import read, read_obj, centoirds


class CdDataset(paddle.io.Dataset):
    def __init__(self, input_dir, obj_list, cd_list):
        self.cd_list = cd_list
        self.input_dir = input_dir
        self.obj_list = obj_list
        self.len = len(obj_list)

    def __getitem__(self, index):
        cd_label = self.cd_list[index]
        obj_name = self.obj_list[index]
        data_dict = read(self.input_dir / "Feature_File"/ f"{obj_name}.obj")
        data_dict["cd"] = cd_label
        return data_dict

    def __len__(self):
        return self.len


class CdDataModule(BaseDataModule):
    def __init__(self, train_data_dir, test_data_dir, n_train, n_test, train_obj_list, test_obj_list):
        BaseDataModule.__init__(self)
        train_csv = np.loadtxt(train_data_dir + "/Label_File/dataset2_train_label.csv", delimiter=",", dtype=str, encoding='utf-8')
        cd_label_train_list = train_csv[:,2][1:].astype(np.float32)
        train_obj_list = train_csv[:,1][1:]
        test_csv =np.loadtxt(test_data_dir + "/Label_File/dataset2_fake_test_label.csv", delimiter=",", dtype=str, encoding='utf-8')
        cd_label_test_list = test_csv[:,2][1:].astype(np.float32)
        fake_test_obj_list = test_csv[:,1][1:]
        
        cd_label_train_list = cd_label_train_list[:n_train]
        cd_label_test_list = cd_label_test_list[:n_test]
        train_obj_list = train_obj_list[:n_train]
        test_obj_list = fake_test_obj_list[:n_test]

        available_train_number = len(train_obj_list)
        available_test_number = len(test_obj_list)
        available_case_number = len(test_obj_list)

        if n_train + n_test < available_case_number:
            warnings.warn(
                f"{available_train_number} traning meshes are available, but n_train= {n_train} are requested."
            )
            warnings.warn(
                f"{available_test_number} testing meshes are available, but n_train= {n_test} are requested."
            )

        self.train_data = CdDataset(Path(train_data_dir), train_obj_list, cd_label_train_list)
        self.test_data  = CdDataset(Path(test_data_dir),  test_obj_list, cd_label_test_list)
        self.train_indices = train_obj_list
        self.test_indices = test_obj_list
    
    def decode(self, x):
        return x
