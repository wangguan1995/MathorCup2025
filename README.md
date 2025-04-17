# MathorCup2025

报名链接：
https://www.saikr.com/vse/mathorcup/2025


# 实验方法1：在线运行
## AIStudio项目链接：
https://aistudio.baidu.com/projectdetail/9021898


# 实验方法2：本地部署
## 数据下载(AIStudio跳过)：
```
wget https://dataset.bj.bcebos.com/PaddleScience/DNNFluid-Car/mathor_cup_2025.tar
tar -xvf mathor_cup_2025.tar
apt install zip
mkdir data
mv data258885/ data281827/ data/
git clone -b develop https://gitee.com/paddlepaddle/PaddleScience.git
``` 

## 环境准备
bash prepare_env.sh

## 训练+推理+结果文件打包
python main.py



![512x512px](https://github.com/user-attachments/assets/12e981b2-3d24-413f-832f-c14008c17343)


![image](https://github.com/user-attachments/assets/e01e1756-bb74-4fa2-b973-baa21df1091d)

