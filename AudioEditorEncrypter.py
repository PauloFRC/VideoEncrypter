from moviepy.editor import *


def create_audio_files(video_link, audio_duration, folder_name='audios'):
    audio_clip = AudioFileClip(video_link)
    video_clip = ColorClip((100, 50), color=(0, 0, 0), duration=audio_duration)
    counter = 0
    maxed_audios = int(audio_clip.duration/audio_duration)

    for i in range(maxed_audios+1):
        counter += 1
        audio = audio_clip.subclip(t_start=(counter - 1) * audio_duration, t_end=counter * audio_duration)
        if counter > maxed_audios:
            print('HEEEREEE')
            audio = audio_clip.subclip(t_start=(counter - 1) * audio_duration)
            video_clip = ColorClip((100, 50), color=(0, 0, 0),
                                   duration=round((audio_clip.duration % audio_duration), 2))
        video_clip = video_clip.set_audio(audio)
        video_clip.write_videofile(folder_name+'/output' + str(counter) + '.mp4', fps=24)
    print(counter)


if __name__ == '__main__':
    link_do_filme = ''
    duracao_de_cada_audio = 3
    create_audio_files(link_do_filme, duracao_de_cada_audio)
