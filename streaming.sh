#! /bin/bash

# originaly from http://tinyurl.com/twitch-linux from taladan
# www.youtube.com/user/taladan

# gist created by brodul

INRES="320x240"                                            # input resolution
#OUTRES="1024x640"                                           # Output resolution
OUTRES="320x240"                                           # Output resolution
FPS="10"                                                    # target FPS
QUAL="fast"                                               # one of the many FFMPEG preset on (k)ubuntu found in /usr/share/ffmpeg
# If you have low bandwidth, put the qual preset on 'fast' (upload bandwidth)
# If you have medium bandwitch put it on normal to medium

# Write your key in a file named .twitch_key in your home directory
STREAM_KEY=$(cat ~/.twitch_key)   # This is your streamkey generated by jtv/twitch found at: http://www.justin.tv/broadcast/adv_other

echo "streaming to rtmp://live.justin.tv/app/$STREAM_KEY"

sudo avconv \
    -f video4linux2 -s $INRES  -r "$FPS" -i /dev/video0 \
    -vcodec libx264 -s $OUTRES -preset $QUAL \
    -threads 1 -qscale 3 -b 71200  -bufsize 512k \
    -f flv "rtmp://live.justin.tv/app/$STREAM_KEY"

#avconv -v verbose -r 20 -s 320x240 -f video4linux2 -i /dev/video0 http://localhost/webcam.ffm
