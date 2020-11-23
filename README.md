# 3Dmocap

" 3Dmocap" is a mocap project that takes a video with one character as input, and outputs corresponding 3d skeleton stored in .fbx file, which is a directed research project supervised by Prof. Scott Easley.

This repo is an refine version of our previous work. see [3DMoCap](https://github.com/ReWr1te/3DMoCap)
In the new version, we add the world movement for hip position by using depth info got by [OpenMMD](https://github.com/peterljq/OpenMMD) .

Also, this repo contains a tutorial to run [3Dpose_ssl](https://github.com/chanyn/3Dpose_ssl) on the custom data. Details please refer to README.md in 3Dpose_ssl folder. All the instruction below is for our 3Dmocap project.




## Requirements
This repo is tested on:

1. GPU:  NVIDIA® GeForce® RTX 2060 SUPER™ 
2. OS: Ubuntu 18.04
3. Cuda 10.1, cuDnn 7.6.1
4. Python 3.6.10
6. Pytorch 1.6.0



## Quick Start

#### 1. Install the previous repo
 Please refer [here](https://github.com/ReWr1te/3DMoCap) to install



#### 2. Get Depth Information by OpenMMD

[OpenMMD](https://github.com/peterljq/OpenMMD) is a vedio analyzing and processing tool that can convert an input vedio to VMD file which can be read by Blender or MikuMikuDance(MMD). It has [FCRN](https://github.com/iro-cp/FCRN-DepthPrediction) as an intermediate step to get the depth information of the vedio. We will apply it here as it is convenient and has relativaly good performance.

For the installation guide and dependencies, please refer to [OpenMMD](https://github.com/peterljq/OpenMMD). You can also find a Chinese tutorial here.

**Instruction:**

* Download package and a activate environment in anaconda as required.
* Run OpenposeVideo.bat. Then you'll have a \_json folder in the same dirictory of input video.
* Run 3d-pose-baseline-vmd\OpenposeTo3D.bat. Then you'll have one more folder named like \_json\_3d\_\*\*\*\*\*\*\*\*\_\*\*\*\*\*\*\_idx01.
* Run FCRN-DepthPrediction-vmd\VideoToDepth.bat. Please note you should enter 1 when it ask the interval (defult is 10), if you'd like to get depth of each frame of the video. Then you can find depth.txt in the folder generated in the last step.
* You are all set for getting depth. You can complete the remaining steps to generate VMD file for fun!



#### 3. Replace
Replace the demo.ipynb using file provided in this repo.



#### 4. Run
According to the instruction in demo get the final .bvh file.
**Note:** you need replace the **Choose data folder** part in order to run the code. 
Then you could use [blender](https://www.blender.org/) to transfer the .bvh file to .fbx file or other format you want.



#### 5. Smooth

Our repo also provides different way to smooth the final result to get less jitter. Please refer to the instruciton in **filtering** folder. After it, you could just replace the 3d coordinate in demo in part **Visualization: Step 7**. Read the result into a numpy array and use it as the  keypoints_sequence.



## Others

An detailed description of this project is uploaded as Description.md for anyone who intended to continue this project

If you have and concerns, feel free to contact us.
