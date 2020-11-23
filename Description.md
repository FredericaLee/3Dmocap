### Target
This project in intended to create a quick pipeline for USC Game to transfer a video to a Maya editable file that contains corresponding 3d skeleton sequence.



### Pipeline
The current pipeline works like this:
Input: A video

1. Using [Detectron2](https://github.com/facebookresearch/detectron2) to get 2d joints

2. Using [VidePose3D](https://github.com/facebookresearch/VideoPose3D) to get 3d joints with fix hip position(always 0,0,0)

3. Replacing the hip position using scaled 2d position as x, y and scaled depth info got by [OpenMMD](https://github.com/peterljq/OpenMMD) as z.  

4. Using [video2bvh](https://github.com/KevinLTT/video2bvh) get .bvh file from 3d joints

5. Using [blender](https://www.blender.org/) to get .fbx file from .bvh file.

Output: .fbx  file



### Problems
1. Most of the 3d estimation use hip as coordinate origin, which makes the hip position is almost fixed as [0,0,0]

2. The jitter still exists in spite of we have tried different filter.

3. Need more user friendly interface.




### Others
We have tried buch of repo in the related areas in order to get better result.
Our initial pipeline is built based on [Openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) (Used in Step 1 in pipeline) and [HMR](https://github.com/akanazawa/hmr)(Used in Step 2 in pipeline). This pipeline surprisingly solves the fixed hip position problem. But the accuracy is unsatisfactory. The angle between knee and foot is weired and it also encounters tremendous jitter.