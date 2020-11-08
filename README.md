# 3Dmocap

## Get Depth Information by OpenMMD

[OpenMMD](https://github.com/peterljq/OpenMMD) is a vedio analyzing and processing tool that can convert an input vedio to VMD file which can be read by Blender or MikuMikuDance(MMD). It has [FCRN](https://github.com/iro-cp/FCRN-DepthPrediction) as an intermediate step to get the depth information of the vedio. We will apply it here as it is convenient and has relativaly good performance.

For the installation guide and dependencies, please refer to [OpenMMD](https://github.com/peterljq/OpenMMD). You can also find a Chinese tutorial here.

**Instruction:**

* Download package and a activate environment in anaconda as required.
* Run OpenposeVideo.bat. Then you'll have a \_json folder in the same dirictory of input video.
* Run 3d-pose-baseline-vmd\OpenposeTo3D.bat. Then you'll have one more folder named like \_json\_3d\_\*\*\*\*\*\*\*\*\_\*\*\*\*\*\*\_idx01.
* Run FCRN-DepthPrediction-vmd\VideoToDepth.bat. Please note you should enter 1 when it ask the interval (defult is 10), if you'd like to get depth of each frame of the video. Then you can find depth.txt in the folder generated in the last step.
* You are all set for getting depth. You can complete the remaining steps to generate VMD file for fun!
