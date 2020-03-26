import numpy as np
import cv2


def codificar(link_video_principal, link_video_distrator, tempo_de_video=False):
    video_principal = cv2.VideoCapture(link_video_principal)
    video_distrator = cv2.VideoCapture(link_video_distrator)


    width = int(video_principal.get(3))
    height = int(video_principal.get(4))

    frame_rate = 24.0
    if tempo_de_video:
        frame_length = int(video_principal.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_rate = round(frame_length/tempo_de_video, 0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out1 = cv2.VideoWriter('video1.avi', fourcc, frame_rate, (width, height))
    out2 = cv2.VideoWriter('video2.avi', fourcc, frame_rate, (width, height))

    while video_principal.isOpened():
        try:
            ret1, frame_vid_principal = video_principal.read()
            ret2, frame_vid_distrator = video_distrator.read()

            frame_vid_distrator = cv2.resize(frame_vid_distrator, (width, height), interpolation=cv2.INTER_AREA)

            top_left = frame_vid_principal[0:int(height/2), 0:int(width/2)]
            bottom_left = frame_vid_principal[int(height/2):height, 0:int(width/2)]
            top_right = frame_vid_principal[0:int(height/2), int(width/2):width]
            bottom_right = frame_vid_principal[int(height/2):height, int(width/2):width]
            video1 = np.concatenate((bottom_left, top_left), axis=0)
            video2 = np.concatenate((bottom_right, top_right), axis=0)
            metade_do_distrator = frame_vid_distrator[0:int(height), 0:int(width/2)]
            video1 = np.concatenate((metade_do_distrator, video1), axis=1)
            video2 = np.concatenate((video2, metade_do_distrator), axis=1)

            out1.write(video1)
            out2.write(video2)
            cv2.imshow('sum', video1)
            cv2.imshow('sum2', video2)

            if cv2.waitKey(1) and 0xFF == ord('q'):
                break
        except TypeError:
            break
        except cv2.error:
            video_distrator.set(cv2.CAP_PROP_POS_FRAMES, 0)

    video_distrator.release()
    video_principal.release()
    out1.release()
    out2.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    link_video_principal = 'haikyuu.mp4'
    link_video_distrator = 'codegeass.mp4'
    tempo_video_principal = 100  #segundos
    codificar(link_video_principal, link_video_distrator)
