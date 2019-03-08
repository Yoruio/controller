import os
import tempfile
import uuid
import logging

log = logging.getLogger('LR.tts.espeak')

tempDir = None
male = None
voice_number = None
hw_num = None

def setup(robot_config):
    global tempDir
    global male
    global voice_number
    global hw_num
    global devNum

    male = robot_config.getboolean('espeak', 'male')
    voice_number = robot_config.getint('espeak', 'voice_number')
    
    try:
        hw_num = robot_config.getint('tts', 'speaker_num')
    except:
        hw_num = robot_config.getint('tts', 'hw_num')

    if robot_config.has_option('tts', 'device_number'):
        devNum = robot_config.getint('tts', 'device_number')
    else:
        devNum = 0

    #set the location to write the temp file to
    tempDir = tempfile.gettempdir()
    log.info("TTS temporary directory : %s", tempDir)

def say(*args):
    message = args[0]
    tempFilePath = os.path.join(tempDir, "text_" + str(uuid.uuid4()))
    f = open(tempFilePath, "w")
    f.write(message)
    f.close()

    if male:
        os.system('cat ' + tempFilePath + ' | espeak -v en-us+m{} -s 170 --stdout | aplay -D plughw:{},{}'.format(voice_number, hw_num, devNum) )
    else:
        os.system('cat ' + tempFilePath + ' | espeak -v en-us+f{} -s 170 --stdout | aplay -D plughw:{},{}'.format(voice_number, hw_num, devNum) )
    os.remove(tempFilePath)    
