#For Loops in EarSketch-  Jan 16, 2019_Example 2
#		python code
#		script_name: for loops-example 2_earSketch
#
#		author: Ernie Yijie
#		description:foor loop- example 2_Basic Build-up
#


#For Loops in EarSketch- Jan 16, 2019_video timelapse 3:18 

from earsketch import *
init()
setTempo(120)

#--------------------------------------------------------
EDM_Beats = [YG_EDM_PAD_3,YG_EDM_BASS_1,RD_EDM_MAINBEAT_5,HOUSE_DEEP_ARPLEAD_001,HOUSE_DEEP_MOOGLEAD_004,
             HOUSE_DEEP_MOOGLEAD_010,HOUSE_DEEP_SINELEAD_002,RD_UK_HOUSE_SOLODRUMPART_1,RD_UK_HOUSE__ACIDLINE_1,
             RD_UK_HOUSE__ACIDLINE_2,Y34_SNARE_1]
#---------------------------------------------------------

start = 1
track = 1
end = 20
beats = EDM_Beats

for beat in beats:
    # fitMedia is like insertMedia
    #except it allows you to change the length of the track
    # it has another parameter,end,which specifies where
    # the track will stop
    fitMedia(beat, track,start,end)
    start+=3
    end+=5
    track+=1



print("you there matey!")  # optional

finish()
