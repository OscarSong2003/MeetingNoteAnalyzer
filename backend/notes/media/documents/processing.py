import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pyannote.audio import Pipeline

#credit: https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):

#     r = sr.Recognizer();

#     pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")


# # print the result
#     # for turn, _, speaker in diarization.itertracks(yield_label=True):
#     #     print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
#     """
#     Splitting the large audio file into chunks
#     and apply speech recognition on each of these chunks
#     """
#     # open the audio file using pydub
#     sound = AudioSegment.from_wav(path)  
#     # split audio sound where silence is 700 miliseconds or more and get chunks
#     chunks = split_on_silence(sound,
#         # experiment with this value for your target audio file
#         min_silence_len = 300,
#         # adjust this per requirement
#         silence_thresh = sound.dBFS-20,
#         # keep the silence for 1 second, adjustable as well
#         keep_silence=600,
#     )
#     folder_name = "audio-chunks"
#     # create a directory to store the audio chunks
#     if not os.path.isdir(folder_name):
#         os.mkdir(folder_name)
#     whole_text = ""
#     # process each chunk 
#     for i, audio_chunk in enumerate(chunks, start=1):
#         # export audio chunk and save it in
#         # the `folder_name` directory.
#         chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
#         audio_chunk.export(chunk_filename, format="wav")
#         # recognize the chunk
#         with sr.AudioFile(chunk_filename) as source:
#             audio_listened = r.record(source)
#             # try converting it to text
#             try:
#                 text = yield r.recognize_google(audio_listened)
#             except sr.UnknownValueError as e:
#                 print("Error:", str(e))
#             else:
#                 text = f"{text.capitalize()}. "
#                 # print(chunk_filename, ":", text)
#                 whole_text += text
#     # return the text for all chunks detected
#     return whole_text

    #import library
    import speech_recognition as sr

    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Audio file as source
    # listening the audio file and store in audio_text variable

    with sr.AudioFile(path) as source:
        audio_text = r.record(source)
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        return text
     
    except:
         print('Sorry.. run again...')
# path = "ch2.wav";
# print("\nFull text:", get_large_audio_transcription(path))