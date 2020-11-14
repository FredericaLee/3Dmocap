# Filtering

This folder contains filtering techniques that reduce the shaking effects on the output of the 3dssl and 3dvideo program. To filtering out the output of 3dssl, run filtering_3D_ssl.py. To filtering out the output of 3dvideo, run filtering_3D_video.py. Be sure to change the root of the input files for both program. 

# Input Format

Each program will take the first 273 frames of the output and filtering out each x,y,z cordinate of each depth locations of 273 frames. The input format for filtering_3D_ssl.py is txt files. In this .txt file, each row represent one frame. For filtering_3D_video.py the input is .npy file and the format of each input data is (number of frames, depth location, xyz cordinates). 

# Output Format

The output format is the same as input. Except only the first 273 frames will be present. 

# Filter types

1. sg filter
references: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.savgol_filter.html

2. median filter
references: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.medfilt.html

3. wiener filter
references: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.wiener.html

4. moving average filter
   Self-implemented by sliding window method with parameter of the window size. 

## Questions?

Please contact Qinghao Meng via qinghaom@usc.edu
