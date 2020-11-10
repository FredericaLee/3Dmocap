vin = VideoReader('SGM1.avi'); 
vout = VideoWriter('SGM_out.avi'); 
framenum = 0; 
everyNframe = 5; 
vout.open(); 
while vin.hasFrame
    frame = vin.readFrame; 
    if rem(framenum,everyNframe) == 0
     vout.writeVideo(frame); 
     % OR 
     imwrite(frame, [num2str(framenum,'%04i') '.jpg']); 
     disp(framenum) 
    end 
    framenum = framenum + 1; 
end 
vout.close(); 