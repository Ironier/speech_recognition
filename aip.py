
# -*- coding: utf-8 -*-
import speech_recognition as sr
import os

import utils
from config import Config
from model import BiRNN

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

conf = Config()

wav_files, text_labels = utils.get_wavs_labels()

words_size, words, word_num_map = utils.create_dict(text_labels)

bi_rnn = BiRNN(wav_files, text_labels, words_size, words, word_num_map)

r = sr.Recognizer()
mic = sr.Microphone()
bi_rnn.load_params()

while True:
    print("请说话...")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    audio.get_wav_data(convert_rate=16000)
    with open("temp.wav", "wb") as f:
            f.write(audio.get_wav_data(convert_rate=16000))
    bi_rnn.test_target_wav_file(['./temp.wav'],['None'])
    print("等待下一句指令...")