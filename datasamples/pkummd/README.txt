PKU-MMD is our new large-scale dataset focusing on long continuous sequences action detection and multi-modality action analysis. The dataset is captured via the Kinect v2 sensor. We release 364x3(view) long action sequences, each of which lasts about 3∼4 minutes (recording ratio set to 30FPS) and contains approximately 20 action instances. The total scale of our dataset is 5,312,580 frames of 3,000 minutes with 21,545 temporally localized actions.


1. Data
RGB_VIDEO:  RGB frames compressed to .avi fomat in 30 FPS.
IR_VIDEO: infrared frames compressed to .avi fomat in 30 FPS.
DEPTH_VIDEO:  depth frames compressed to .avi fomat in 30 FPS.
Skeleton.7z: contains corresponding skeleton data for each sequence. 
i)  Each sequence corresponds to a single skeleton file.
ii) The skeleton file contains many rows ordered by time and each row corresponds to a time frame. Each row is composed of two human skeleton with 50 3D skeleton points. Each human has 25 points with format x1,y1,z1,x2,y2,z2,....,x25,y25,z25. Note that there may be only one human, then the last 25 points will be filled with zero.

2. Split
cross-view.txt: cross view split list.
cross-subject.txt: cross subject split list.
These are the split settings in our own experiments. We split the training data into two parts for training and validation to tune our model for cross-view and cross-subject settings, respectively. Please note that you can use all the training data to train your model for the final testing evaluation.
Actions.xlsx: contains the 51 defined actions and corresponding IDs.

3. Label
Label_PKUMMD.7z: contains corresponding labels for each sequence. Each file contains the occurring actions and their time intervals. Each row in the label file comply with the following format: action_id, start_frame, end_frame, confidence. The confidence is the labeled value to judge the quality of the performed action. You can ignore this confidence when using this dataset. 

Notes: 
For more codes like evaluation and visualization, please refer to https://github.com/ECHO960/PKU-MMD.
 For more details, please refer to http://www.icst.pku.edu.cn/struct/Projects/PKUMMD.html.
For any questions, please contact pkustruct@gmail.com

