
export LD_LIBRARY_PATH=/home/keze/anaconda3/lib:/usr/local/cuda-8.0/cudnn_v51/lib64:/usr/local/cuda-8.0/lib64:/home/keze/anaconda2/lib:$LD_LIBRARY_PATH
python pred_v2.py --trained_model ../models/model_extension_mask3d/mask3d-400000.pkl --protocol 1 --data_dir /home/keze/Codes/3Dpose_ssl/data/h36m --coarse_3d ../test/mask3d --save srr_results --pose2d hourglass
