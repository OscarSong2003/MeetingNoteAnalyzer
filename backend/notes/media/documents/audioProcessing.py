from pyannote.audio import Pipeline
import os
import wave
# from google.cloud import speech_v1 as speech
from google.cloud import speech_v1 as speech
from .convertChannel import save_wav_channel
import io

def getTranscript(path, actualName):
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/oscarsong/Desktop/meetingnotesanalyzer-5a8a64e88aca.json"
    # Creates google client
    client = speech.SpeechClient()

    # convert file to single channel 
    wav = wave.open(path)
    # save_wav_channel(f'{actualName}.wav', wav, 0)
    save_wav_channel(path, wav, 0)
    # Full path of the audio file, Replace with your file name
    file_name = path

    #Loads the audio file into memory
    with io.open(file_name, "rb") as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

    diarization_config = speech.SpeakerDiarizationConfig(
        enable_speaker_diarization=True,
        max_speaker_count=4,
        min_speaker_count=1
    )
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        audio_channel_count=1,
        language_code="en-US",
        diarization_config=diarization_config,
    )

    # Sends the request to google to transcribe the audio
    response = client.recognize(config=config, audio=audio)
    result = response.results[-1]

    convoInfo = result.alternatives[0].words
    prevSpeakerText = ""
    prevSpeakerTag = convoInfo[0].speaker_tag

    # open file for writing
    f = open(f'notes/media/documents/transcript/{actualName[:-4]}.txt', 'w'); 
    print('CONVO INFO', convoInfo)
    # go through each words object in alternatives
    for convo in convoInfo:
        print('CONVO:', convo)
        # check if speaker is equal to previous speaker -> if so continue to append 
        if (convo.speaker_tag == prevSpeakerTag):
            print('SPEAKER TAG SAME\n')
            print(type(convo.speaker_tag))
            print('SpEAKER TAG:', convo.speaker_tag, prevSpeakerTag, "\n\n")
            print('CONVO.WORD: ', convo.word, "\n\n")
            # append text to sentence
            prevSpeakerText = prevSpeakerText + " " + convo.word
        else: 
            print('SPEAKER TAG DIFFERENT!')
            # speaker is different, so write prevSpeaker text into file
            f.write("Speaker " + str(prevSpeakerTag) + ": " + prevSpeakerText + ".\n\n")
            # set prevspeaker text to current word
            prevSpeakerText = convo.word
            # update prev speaker tag
            prevSpeakerTag = convo.speaker_tag

    # at the end write prevSpeakerTag to file 
    f.write("Speaker " + str(prevSpeakerTag) + ": " + prevSpeakerText + ".\n\n")
    
#     words_info = result.alternatives[0].words

# # Printing out the output:
#     for word_info in words_info:
#         print(
#             u"word: '{}', speaker_tag: {}".format(word_info.word, word_info.speaker_tag)
#         )
#     # Reads the response
    
#-----------------------------------------------------------------------------------------
# getTranscript('/Users/oscarsong/Desktop/notes/backend/notes/media/documents/df940d72-ddbf-4792-b956-766118c546b9-1.wav', 'df940d72-ddbf-4792-b956-766118c546b9-1' )

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
    for i, el in enumerate(labelling): 
        print("i:", i)
        speaker = el[0]
        start = el[1]
        end = el[2]
        filename = f"notes/media/documents/audioSegment{i}.wav"
        print("i2:", i)
        # f = open(filename, "w");
        # extract audio segment 
        ffmpeg_extract_subclip(audioFile, start, end, targetname=filename)
        print(el[0], el[1], el[2], filename)
        # transcr = get_large_audio_transcription(filename)
        transcr = getPartialTranscript(filename)
        # # print('transcript:', transcr);
        # if (transcr): 
        #     print('SUCCESS')
        #     text = speaker + ' ' + transcr + '\n\n'
        #     print(text);
        #     f.write(text)
        # print("\nActual Full text:", get_large_audio_transcription(filename))



def getPartialTranscript(path):
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/oscarsong/Desktop/meetingnotesanalyzer-5a8a64e88aca.json"
    # Creates google client
    client = speech.SpeechClient()

    # convert file to single channel 
    wav = wave.open(path)
    # save_wav_channel(f'{actualName}.wav', wav, 0)
    save_wav_channel(path, wav, 0)
    # Full path of the audio file, Replace with your file name
    file_name = path

    #Loads the audio file into memory
    with io.open(file_name, "rb") as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

    diarization_config = speech.SpeakerDiarizationConfig(
        min_speaker_count=1,
        max_speaker_count=10,
    )
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        audio_channel_count=1,
        language_code="en-US",
    )

    # Sends the request to google to transcribe the audio
    response = client.recognize(config=config, audio=audio)
    print('PARTIAL RESPONSE: ', response.results)
    result = response.results[-1]

    
    # convoInfo = result.alternatives[0].words
    # prevSpeakerText = ""
    # prevSpeakerTag = convoInfo[0].speaker_tag

    # # open file for writing
    # f = open(f'notes/media/documents/transcript/{actualName[:-4]}.txt', 'w'); 
    # print('CONVO INFO', convoInfo)
    # # go through each words object in alternatives
    # for convo in convoInfo:
    #     print('CONVO:', convo)
    #     # check if speaker is equal to previous speaker -> if so continue to append 
    #     if (convo.speaker_tag == prevSpeakerTag):
    #         print('SPEAKER TAG SAME\n')
    #         print(type(convo.speaker_tag))
    #         print('SpEAKER TAG:', convo.speaker_tag, prevSpeakerTag, "\n\n")
    #         print('CONVO.WORD: ', convo.word, "\n\n")
    #         # append text to sentence
    #         prevSpeakerText = prevSpeakerText + " " + convo.word
    #     else: 
    #         print('SPEAKER TAG DIFFERENT!')
    #         # speaker is different, so write prevSpeaker text into file
    #         f.write("Speaker " + str(prevSpeakerTag) + ": " + prevSpeakerText + ".\n\n")
    #         # set prevspeaker text to current word
    #         prevSpeakerText = convo.word
    #         # update prev speaker tag
    #         prevSpeakerTag = convo.speaker_tag

    # # at the end write prevSpeakerTag to file 
    # f.write("Speaker " + str(prevSpeakerTag) + ": " + prevSpeakerText + ".\n\n")