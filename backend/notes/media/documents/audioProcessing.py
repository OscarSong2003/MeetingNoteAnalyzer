from pyannote.audio import Pipeline
import os
def recognitionAndSegmentation(fname, actualName): 
    audioFile = fname
    pipeline = Pipeline.from_pretrained("pyannote/speaker-segmentation")
    output = pipeline(audioFile)

    # speaker segmentation
    labelling = []
    for turn, _, speaker in output.itertracks(yield_label=True):
        if (turn.end - turn.start > 1): 
            # speaker speaks between turn.start and turn.end
            label = [speaker, turn.start, turn.end]
            labelling.append(label);
        
    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
    from .processing import get_large_audio_transcription
    f = open(f'notes/media/documents/transcript/{actualName[:-4]}.txt', 'w'); 
    for el in labelling: 
        speaker = el[0]
        start = el[1]
        end = el[2]
        filename = "audioSegment.wav"
        # f = open(filename, "w");
        # extract audio segment 
        print('GOT HERE')
        ffmpeg_extract_subclip(audioFile, start, end, targetname=filename)
        print(el[0], el[1], el[2])
        text = speaker + ' ' + get_large_audio_transcription(filename) + '\n\n'
        f.write(text)
        # print("\nActual Full text:", get_large_audio_transcription(filename))


