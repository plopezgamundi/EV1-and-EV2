#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on November 27, 2019, at 13:05
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""
# ***************** CRAZY CODE FROM PSYCHOPY *************
from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, parallel
from psychopy.visual.slider import Slider
#from psychopy.hardware import keyboard
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import random
import os  # handy system and path functions
import sys  # to get file system encoding





# Ensure that relative paths start from the same directory as this script
#_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'CogEffVal_EEGv9'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': '', 'condition':'', 'handedness':''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=True, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    #In the end you don't really need originPath to match the directory
    originPath='C:\\Users\\Brainvitge\\Desktop\\Paula\\Cognitive Task_EEG_with triggers.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

#hopefully creating a global shutdown key ctrl+q
event.globalKeys.add(key='x', modifiers=['ctrl'], func=core.quit)

#adding port for triggers
port = parallel.ParallelPort(address = u'0xC100') #address depende de si es windows o linux y del ordenador
#aqui esta puesto en Window. 
#port.setData(4) est es lo que envias. reiniciar a zero porque no se suman.
#tiene que ser integer (poner int())

# Start Code - component code to be run before the window creation

# Setup the Window
#win = visual.Window(
#    size=(1024, 768), fullscr=False, screen=0, 
#    winType='pyglet', allowGUI=False, allowStencil=False,
#    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
#    blendMode='avg', useFBO=True, 
#    units='height')

win = visual.Window(size=[1920, 1080], fullscr=True,colorSpace='rgb', color=[0,0,0], monitor='testMonitor',)


# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess





# ******************* FILES AND ARRAYS FOR DATA STORAGE ****************************#
# array to store data
#array for by trial file
loglist=[]
loglist.append("Subject, Session, Condition, Block, Trial, Cue, TaskType, Difficulty, EasyCueDecType, PotentialReward, CurrMedDecNum, CorrChoices, IncorrChoices, TrialReward, CumulReward, SuccessfulTrial, MeanDecTime")

#array for log file
loglist_all=[]
loglist_all.append("Subject, Block, Trial, EventType, TrialType, Desc, EventTime, Response, Correct, Trigger, RT\n")

#by trial file
filename2="byTrial_data\\CogEffVal_EEGv9_byTrial_" + expInfo['participant']
with open(filename2+'.txt', "a") as f:
    f.write("Subject, Handedness, Session, Condition, Block, Trial, Cue, TaskType, Difficulty, EasyCueDecType, PotentialReward, CurrDecThresh, CorrChoices, IncorrChoices, TrialReward, CumulReward, SuccessfulTrial, MeanDecTime, SDevDecTime, CatchQuestResp, CatchQuestCorr\n")


#full log file
filename3="allEvents_data\\CogEffVal_EEGv9_AllEvents_" + expInfo['participant']
with open(filename3+'.txt', "a") as f:
        f.write("Subject, Block, Trial, EventType, TrialType, Desc, EventTime, Response, Correct, Trigger, RT\n")

#by trial file back up
filename5="backup_data\\CogEffVal_EEGv9_byTrial_" + expInfo['participant']


#catch_mean and reward output so you can figure out how much reward to give them!
filename_catchmean="payout_data\\CogEffVal_EEGv9_payout_" + expInfo['participant']

#scales file
scale_file="selfreport_data\\CogEffVal_EEGv9_liking_" + expInfo['participant']
with open(scale_file + '.txt', "a") as f:
    f.write("Subject, Session, Condition, Block, Fatigue, Like_lclr_cue, Like_hclr_cue, Like_lchr_cue, Like_hchr_cue, Difficulty_Yell, Difficulty_Blue, Difficulty_Hard\n")


#####################  INITIALIZING IMPORTANT ELEMENTS FOR TASK #############################3

# create a default keyboard (e.g. to check for escape)

#initializing main clock that I will use for whole experiment
mClock = core.Clock()
#setting condition 
condition=int(expInfo['condition'])  
handedness=str(expInfo['handedness'])

your_mouse = event.Mouse(visible = False)

#variables I will use to store data
event_type=None
trial_type=None
desc=None
eventTime=None
response=None
correct=0

#instructions and training is all in Block -99.
block=-99
        
# ARRAYS FOR STIMULI
numarr=[1,2,3,4,6,7,8,9]
colarr=['yellow', 'blue']
lclr_cued_y, lclr_cued_b, lchr_cued_y, lchr_cued_b, hclr_cued, hchr_cued=  None, None, None, None, None, None
lclr_notask,hclr_notask, lchr_notask, hchr_notask=None, None, None, None
lclr_notask_quest,hclr_notask_quest, lchr_notask_quest, hchr_notask_quest=None, None, None, None


if (condition==1):
    #circles are stroop task
    lclr_cued_y=('stim/circle_5.png', 'lclr_cued', 'cued', 'easy', 5, 'yellow', 40, 1)
    lclr_cued_b=('stim/circle_5.png', 'lclr_cued', 'cued', 'easy', 5, 'blue', 40, 1)
    hclr_cued=('stim/square_5.png', 'hclr_cued', 'cued', 'hard', 5, 20, 1)
    lchr_cued_y=('stim/circle_25.png', 'lchr_cued', 'cued', 'easy', 25, 'yellow',30, 1)
    lchr_cued_b=('stim/circle_25.png', 'lchr_cued', 'cued', 'easy', 25, 'blue', 30, 1)
    hchr_cued=('stim/square_25.png', 'hchr_cued', 'cued', 'hard', 25, 10,1)
    lclr_notask=('stim/circle_5.png','lclr_notask', 'cued', 'easy', 5, 45, 2)
    hclr_notask=('stim/square_5.png', 'hclr_notask', 'cued', 'hard', 5, 25, 2)
    lchr_notask=('stim/circle_25.png', 'lchr_notask', 'cued', 'easy', 25, 35, 2)
    hchr_notask=('stim/square_25.png', 'hchr_notask', 'cued', 'hard', 25, 15, 2)
    lclr_notask_quest=('stim/circle_5.png','lclr_notask_quest', 'cued', 'easy', 5, 45, 3)
    hclr_notask_quest=('stim/square_5.png', 'hclr_notask_quest', 'cued', 'hard', 5, 25, 3)
    lchr_notask_quest=('stim/circle_25.png', 'lchr_notask_quest', 'cued', 'easy', 25, 35, 3)
    hchr_notask_quest=('stim/square_25.png', 'hchr_notask_quest', 'cued', 'hard', 25, 15, 3)
elif (condition==2):
     #circles are cued task switching task
    lclr_cued_y=('stim/square_5.png', 'lclr_cued', 'cued', 'easy', 5, 'yellow', 40, 1)
    lclr_cued_b=('stim/square_5.png', 'lclr_cued', 'cued', 'easy', 5, 'blue', 40, 1)
    hclr_cued=('stim/circle_5.png', 'hclr_cued', 'cued', 'hard', 5, 20, 1)
    lchr_cued_y=('stim/square_25.png', 'lchr_cued', 'cued', 'easy', 25, 'yellow', 30, 1)
    lchr_cued_b=('stim/square_25.png', 'lchr_cued', 'cued', 'easy', 25, 'blue', 30, 1)
    hchr_cued=('stim/circle_25.png', 'hchr_cued', 'cued', 'hard', 25, 10, 1)
    lclr_notask=('stim/square_5.png', 'lclr_notask', 'cued', 'easy', 5, 45, 2)
    hclr_notask=('stim/circle_5.png', 'hclr_notask', 'cued', 'hard', 5, 25, 2)
    lchr_notask=('stim/square_25.png', 'lchr_notask', 'cued', 'easy', 25, 35, 2)
    hchr_notask=('stim/circle_25.png', 'hchr_notask', 'cued', 'hard', 25, 15, 2)
    lclr_notask_quest=('stim/square_5.png', 'lclr_notask_quest', 'cued', 'easy', 5, 45, 3)
    hclr_notask_quest=('stim/circle_5.png', 'hclr_notask_quest', 'cued', 'hard', 5, 25, 3)
    lchr_notask_quest=('stim/square_25.png', 'lchr_notask_quest', 'cued', 'easy', 25, 35, 3)
    hchr_notask_quest=('stim/circle_25.png', 'hchr_notask_quest', 'cued', 'hard', 25, 15, 3)

else:
    print("condition not detected")
    

#blocks
cues_1=[lchr_notask, lclr_cued_y, hchr_notask, hchr_cued, hclr_notask, lchr_cued_b, hclr_cued, lclr_notask, 
        lchr_notask_quest, hclr_cued, hclr_notask, lclr_notask, lchr_cued_y, hchr_cued, hchr_notask, lclr_cued_b,
        hclr_notask, hchr_cued, lclr_notask, lclr_cued_y, hclr_cued, lchr_notask, hchr_notask, lchr_cued_b,
        lclr_notask, hchr_notask_quest, lclr_cued_b, lchr_notask, lchr_cued_y, hchr_cued, hclr_notask, hclr_cued,
        hclr_notask, lclr_notask, lclr_cued_y, hchr_notask, hchr_cued, lchr_notask, lchr_cued_b, hclr_cued,
        lchr_notask, lclr_cued_b, lchr_cued_y, hchr_cued, hchr_notask, hclr_cued, lclr_notask_quest, hclr_notask,
        hclr_cued, lclr_cued_y, hchr_notask, lclr_notask,  hchr_cued, hclr_notask,lchr_notask, lchr_cued_b,
        hchr_cued, lchr_notask, lclr_notask, lclr_cued_b, hclr_notask_quest, hchr_notask, hclr_cued, lchr_cued_y,
        hchr_cued, hclr_notask, hclr_cued, lchr_notask, lchr_cued_b, lclr_notask, hchr_notask, lclr_cued_y,
        hclr_notask, hchr_notask, lclr_cued_b, lchr_cued_y, lchr_notask, hclr_cued, lclr_notask, hchr_cued]


cues_2=[lclr_notask, hchr_notask,lclr_cued_y, hclr_notask, hchr_cued, lchr_cued_b, hclr_cued, lchr_notask,
        hclr_cued, lclr_cued_b, hchr_notask_quest, hchr_cued, hclr_notask, lclr_notask, lchr_cued_y, lchr_notask,
        hchr_notask, lchr_cued_b, hclr_cued, hclr_notask, hchr_cued, lchr_notask, lclr_cued_y, lclr_notask, 
        hclr_cued, hclr_notask_quest, lclr_notask, lclr_cued_b, lchr_notask, lchr_cued_y, hchr_cued, hchr_notask, 
        lchr_cued_b, hchr_notask, hchr_cued, hclr_notask, hclr_cued, lclr_cued_y, lclr_notask, lchr_notask,
        hchr_cued, hchr_notask, hclr_cued, hclr_notask, lclr_cued_b, lchr_cued_y, lclr_notask_quest, lchr_notask,
        hclr_cued, hchr_notask, lchr_cued_b, hclr_notask, lchr_notask, lclr_cued_y, lclr_notask, hchr_cued,
        lchr_cued_y, hclr_cued, lchr_notask_quest, hchr_notask, hchr_cued, lclr_notask, lclr_cued_b, hclr_notask,
        hchr_cued, lclr_cued_y, hclr_notask, hclr_cued, lchr_cued_b, hchr_notask, lclr_notask, lchr_notask,
        hclr_cued, lclr_notask, lclr_cued_b, hclr_notask, lchr_notask, hchr_cued, lchr_cued_y, hchr_notask]

cues_3=[hchr_cued, hchr_notask, hclr_cued, lchr_notask, lclr_notask, lclr_cued_y, hclr_notask, lchr_cued_b,
        lchr_notask_quest, lclr_cued_b, hchr_cued, hclr_notask, hclr_cued, lchr_cued_y, hchr_notask, lclr_notask,
        lclr_cued_y, hchr_cued, hchr_notask, lclr_notask, lchr_cued_b, lchr_notask, hclr_cued, hclr_notask,
        hclr_notask_quest, lclr_notask, hchr_cued, lchr_notask, hchr_notask, lchr_cued_y, hclr_cued, lclr_cued_b,
        hchr_cued, hclr_notask, lchr_cued_b, lclr_notask, lchr_notask, hclr_cued, lclr_cued_y, hchr_notask, 
        lclr_cued_b, hchr_notask_quest, hchr_cued, lchr_cued_y, lchr_notask, hclr_cued, lclr_notask, hclr_notask,
        lclr_cued_y, lchr_notask, lchr_cued_b, lclr_notask, hclr_cued, hchr_notask, hclr_notask, hchr_cued, 
        lclr_cued_b, lclr_notask_quest, hclr_cued, lchr_notask, hchr_cued, hchr_notask, lchr_cued_y, hclr_notask,
        hclr_cued, lclr_cued_y, lchr_notask, hchr_cued, hclr_notask, lclr_notask, lchr_cued_b, hchr_notask, 
        hchr_notask, hchr_cued, lchr_cued_y, hclr_notask, lchr_notask, hclr_cued, lclr_notask, lclr_cued_b]

cues_4=[lchr_cued_b, lchr_notask, hchr_cued, hclr_notask, lclr_cued_y, lclr_notask, hchr_notask, hclr_cued,
        lchr_notask, hclr_cued, hchr_notask_quest, lclr_cued_b, hchr_cued, lchr_cued_y, lclr_notask, hclr_notask, 
        lclr_cued_y, hchr_notask, lchr_notask, hchr_cued, lclr_notask, lchr_cued_b, hclr_notask, hclr_cued, 
        lchr_notask_quest, lclr_cued_b, lchr_cued_y, hclr_notask, hclr_cued, lclr_notask, hchr_notask, hchr_cued, 
        lclr_notask, hclr_cued, lchr_notask, lchr_cued_b, hchr_notask, hchr_cued, hclr_notask, lclr_cued_y,
        hchr_cued, lclr_notask_quest, lclr_cued_b, hclr_notask, hchr_notask, hclr_cued, lchr_notask, lchr_cued_y, 
        lclr_notask, hchr_notask, lchr_cued_b, hclr_notask, hclr_cued, lchr_notask, hchr_cued, lclr_cued_y,
        hclr_notask_quest, lchr_cued_y, hchr_notask, hchr_cued, lclr_cued_b, lclr_notask, hclr_cued, lchr_notask,
        lclr_notask, lchr_cued_b, lclr_cued_y, lchr_notask, hclr_cued, hchr_notask, hclr_notask, hchr_cued,
        hclr_notask, hclr_cued, hchr_notask, lclr_cued_b, lchr_notask, lclr_notask, lchr_cued_y, hchr_cued]

cues_5=[lclr_notask, lchr_notask, lchr_cued_b, lclr_cued_y, hchr_cued, hclr_notask, hclr_cued, hchr_notask,
        hchr_cued, hclr_notask_quest, lclr_cued_b, hchr_notask, lchr_notask, hclr_cued, lclr_notask, lchr_cued_y,
        lchr_cued_b, hclr_notask, lclr_cued_y, hchr_cued, lchr_notask, hchr_notask, hclr_cued, lclr_notask, 
        lchr_cued_y, lclr_notask_quest, hclr_cued, lchr_notask, hchr_notask, hclr_notask, hchr_cued, lclr_cued_b,
        lchr_notask, lclr_cued_y, lclr_notask, hclr_cued, hchr_notask, hclr_notask, lchr_cued_b, hchr_cued, 
        lchr_cued_y, lclr_cued_b, hclr_notask, hchr_cued, hchr_notask_quest, lclr_notask, lchr_notask, hclr_cued,
        hclr_notask, lclr_cued_y, lchr_cued_b, lchr_notask, hclr_cued, lclr_notask, hchr_cued, hchr_notask,
        lclr_cued_b, lchr_notask_quest, lclr_notask, hchr_cued, lchr_cued_y, hclr_notask, hchr_notask, hclr_cued,
        lchr_notask, hchr_cued, lclr_notask, lchr_cued_b, hclr_cued, hchr_notask, lclr_cued_y, hclr_notask, 
        lclr_notask, hclr_cued, lchr_notask, hchr_cued, lclr_cued_b, hclr_notask, lchr_cued_y, hchr_notask]


block_arr=[cues_1, cues_2, cues_3, cues_4, cues_5] 

fb_cues=["stim/x_mark.png"]

fc_isi1=[1.2, 1.3, 1.4, 1.5] #used after cue and before effort

fc_isi2=[2, 2.1, 2.2, 2.3, 2.4, 2.5] #used after effort and before feedback --used to be [.3, .4, .5, .6, .7, .8] and then [.8, .9, 1.0, 1.1, 1.2, 1.3] in 9.2

fc_iti=[2, 2.2, 2.4, 2.6, 2.8, 3] #used after feedback and before a new trial -- used to be [.5, .6, .7, .8, .9, 1]




# ******************** INITIALIZE VISUAL ELEMENTS FOR INSTRUCTIONS/ PRACTICE/ TRIALS **********************************

#************* SCALES ************

cue_rating= visual.Slider(win,
             ticks=(0,1,2,3,4,5,6,7,8,9,10),
             labels=('No me gusta','Indiferente', 'Me gusta mucho'),
             granularity=1, size=(1,.1), pos=(0,-.2),
             color='white', labelHeight = .05)

fat_rating= visual.Slider(win,
             ticks=(0,1,2,3,4,5,6,7,8,9,10),
             labels=('No cansado/a', 'Muy cansado/a'),
             granularity=1, size=(1,.1), pos=(0,-.2),
             color='white', labelHeight = .05)

dif_rating= visual.Slider(win,
             ticks=(0,1,2,3,4,5,6,7,8,9,10),
             labels=(u'Nada de difícil', u'Extremadamente difícil'),
             granularity=1, size=(1,.1), pos=(0,-.2),
             color='white', labelHeight = .05)

#slide for question trials
quest_slide = visual.TextStim(win=win, name='quest',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

                              
#instruction slides
I = visual.TextStim(win=win, name='I',
    #text='El objetivo de esta tarea es ayudar Paula',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
                    
    
I_image= visual.ImageStim(
    win=win, name='I_image',
    image='stim/circle_cues_inst.png', mask=None,
    pos=(0.4, -.2), size=(.9,.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0);
   
        
#for cue and number presentation
cues_pres = visual.ImageStim(
    win=win, name='cues',
    image='stim/circle_25.png', mask=None,
    pos=(0, 0), size=(.2,.33),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

fix_pres = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
                          
star_pres = visual.TextStim(win=win, name='fix',
    text='*',
    font='Arial',
    pos=(0, -.14), height=0.4, wrapWidth=None, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
                           
num_pres = visual.TextStim(win=win, name='singleNum',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

corr_fb = visual.TextStim(win=win, name='singleNum',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
#corr_fb = visual.ImageStim(
#    win=win, name='corr_fb',
#    image='stim/large_fb.png', mask=None,
#    pos=(0, 0), size=(0.5 , 0.5),
#    color=[1,1,1], colorSpace='rgb', opacity=1,
#    flipHoriz=False, flipVert=False,
#    texRes=128, interpolate=True, depth=0.0);

incorr_fb = visual.ImageStim(win=win,  
    image='stim/x_mark.png', mask=None,
    pos=(0, 0), size=(0.1, 0.13),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0);

break_pres = visual.TextStim(win=win, name='break',
    text='Great Job!\nSo far you have earned___',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
    








# ********************* CUE TASK FUNCTIONS *****************************

#******* cue_hard_stim() **********
#This function generates a random array of numbers
# and array of alternating colors for the hard task
# in the cue switching task
#note that this array is fixed to 10, but ideally 
# this will be calibrated later on
def cue_hard_stim():
#    randnumlist=np.random.choice(numarr, 10, replace="TRUE")
    #creating random numbers list
    randnumlist=np.empty(30, dtype=object)
    np.random.shuffle(numarr)
    newnumarr=numarr
    while len(newnumarr)<len(randnumlist):
        n=len(randnumlist)-len(newnumarr)
        if (n>=8):
            addnum=random.sample(numarr,8)
        else:
            addnum=random.sample(numarr,n)
        newnumarr=newnumarr+addnum
    randnumlist=newnumarr
    
    np.random.shuffle(colarr)
    a = np.empty(len(randnumlist), dtype=object)
    a[::2] = colarr[0]
    a[1::2] = colarr[1]
    randcollist=a
    return(randnumlist,randcollist)
    
    
#******* cue_easy_stim() **********
#This function generates a random array of numbers
# and array of one color for the easy cue switching task
#note that this array is fixed to 10, but ideally 
# this will be calibrated later on
# We also may make this a fixed array later on once we decide the trial stucture
def cue_easy_stim(color):
#    randnumlist=np.random.choice(numarr, 10, replace="TRUE") 
    randnumlist=np.empty(30, dtype=object)
    np.random.shuffle(numarr)
    newnumarr=numarr
    while len(newnumarr)<len(randnumlist):
        n=len(randnumlist)-len(newnumarr)
        if (n>=8):
            addnum=random.sample(numarr,8)
        else:
            addnum=random.sample(numarr,n)
        if (addnum[0]!=newnumarr[len(newnumarr)-1]):
            newnumarr=newnumarr+addnum
        else:
            pass
    randnumlist=newnumarr
    
    #np.random.shuffle(colarr)
    randcollist=np.repeat(color, len(randnumlist))
    return(randnumlist,randcollist)
    

#******* cue_task_resp(j,resp) **********
#This function reads the response of for a cued task switching task,
# and scores the response based on a set of rules
# For blue numbers: if even, click left; if odd, click right
# For yellow numbers: if <5, click left; if >5 click right
# if you didn't respond and the number was presented for less than your average response time, then it doesn't count as incorrect

def cue_task_resp(j,resp, lasttrial,displayTime, cutoff):       
    if (resp=="left"): #if response was a left button
        if (j[1]=='blue'):
            if (j[0]%2==0): #if blue and even
                corr, incorr, noresp=1, 0,0
            else: #if blue and odd
                corr, incorr, noresp=0, 1,0
        else: #if yellow
            if (j[0]<5): #if yellow and less than 5
                corr, incorr, noresp=1, 0,0
            else:
                corr, incorr, noresp=0, 1,0

    elif (resp=="right"): # if response was a right button
        if (j[1]=='blue'):
            if (j[0]%2==0): #if blue and even
                corr, incorr, noresp=0, 1,0
            else: #if blue and odd
                corr, incorr, noresp=1, 0,0
        else: #if yelloW
            if (j[0]<5): #if yellow and less than 5
                corr, incorr, noresp=0, 1,0
            else:
                corr, incorr, noresp=1, 0,0

    else: #if no response and its the last trial, assess how long that number was displayed
        if (lasttrial==1 and displayTime<cutoff):
            corr, incorr, noresp=0,0,1
        else:
            corr, incorr, noresp=0,1,1
    return(corr, incorr, noresp)




#******* cue_task_pres(randnumlist, randcollist) **********
#This function presents the stimuli for both hard and easy cue switching tasks,
# captures the response, and keeps track of performance.
# It returns the total number of correct, incorrect, no responses, x (total number of numbers presented),
# mean time to make a decision and sd time to make a decision for a trial.


def cue_task_pres(randnumlist, randcollist, typeoftrial, t,cutoff=3.0):
    port.setData(0)
    trial_type=typeoftrial
    trig=0
    RT=0
    event_type=None
    desc=None
    totcorr, totincorr, totnoresp, x=0,0,0,0
    kp, kp_out, corr_out=None, None, None
    lastnum=0
    time_arr=[]
    mean_trialTime, sd_trialTime =0,0
    
    maintimer=core.Clock()
    maintimer.add(8) #changed to 8 seconds (from 10 seconds) for trial
    
    secondTimer=core.Clock()
    
    key_press=event.getKeys(keyList=("left", "right"),timeStamped=mClock)
    
    while (maintimer.getTime()<0):
        for n in range(len(randnumlist)):
            if (trial_type=="lclr_cued"):
                if (randcollist[n]=="yellow"):
                    trig=100+randnumlist[n]
                else:
                    trig=110+randnumlist[n]
            elif (trial_type=="lchr_cued"):
                if (randcollist[n]=="yellow"):
                    trig=120+randnumlist[n]
                else:
                    trig=130+randnumlist[n]
            elif (trial_type=="hclr_cued"):
                if (randcollist[n]=="yellow"):
                    trig=200+randnumlist[n]
                else:
                    trig=210+randnumlist[n]
            elif (trial_type=="hchr_cued"):
                if (randcollist[n]=="yellow"):
                    trig=220+randnumlist[n]
                else:
                    trig=230+randnumlist[n]
            else:
                trig=80+randnumlist[n]
            
            if (maintimer.getTime()>0):
                break
            else:
                j=[randnumlist[n],randcollist[n]] #j specific number and its associated color
                num_pres.setText(randnumlist[n])
                num_pres.setColor(randcollist[n])
                desc=str(randnumlist[n])+"_"+(randcollist[n])
                event_type="pres"
                

                if (maintimer.getTime()<0):
                    num_pres.setAutoDraw(True)

                    win.flip()
                    port.setData(trig)
                    eventTime=mClock.getTime()
                    secondTimer=core.Clock()
                    startTrial= secondTimer.getTime()
                    win.flip()
                    port.setData(0)
                    
                    #recording data
                    #"EventType, TrialType, Desc, EventTime, Response, Correct"
                    dataline=(str(expInfo['participant']) + "," + str(block+1) +  "," + str(t) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(trig) + "," + "NaN")
                    loglist_all.append(dataline)
                    with open(filename3+'.txt', "a") as myfile:
                        myfile.write(dataline+"\n")
                
                    key_press=event.getKeys(keyList=("left", "right"), timeStamped=secondTimer)

                    
                    if (key_press!=[]):
                        port.setData(99)
                        pass

                    else:
                        while (key_press==[]):
                            key_press=event.getKeys(keyList=("left", "right"), timeStamped=secondTimer)
                            eventTime=mClock.getTime() 
                            if (maintimer.getTime()>0):
                                lastnum=1
                                break
                            
                            if key_press!=[]:
                                port.setData(99)
                                break

                elif (maintimer.getTime()>0):
                    lastnum=1
                    win.flip()
                    break

            
            trialTime=secondTimer.getTime()-startTrial
            
            num_pres.setAutoDraw(False)
            win.flip()
            port.setData(0)
            
            #outputting response 
            event_type="resp"
            if (key_press!=[]):
                kp, kp_out=key_press[0][0],key_press[0][0]
                RT=key_press[0][1]-startTrial
            else:
                kp, kp_out=[], "No press"
                eventTime="No press"
                RT="NaN"
            
            
            corr, incorr, noresp=cue_task_resp(j,kp,lastnum, trialTime, cutoff) #determining if response was correct    
            totcorr=totcorr+corr
            totincorr=totincorr+incorr
            totnoresp=totnoresp+noresp
            x=x+1
            
            #correct of -1 means that they didn't have time to respond
            if (kp==[] and incorr==0):
                corr_out=-1
            elif (kp==[] and incorr==1):
                corr_out=0
            elif (kp!=[]):
                corr_out=corr
                time_arr.append(RT)
                
                    
            
            #"EventType, TrialType, Desc, EventTime, Response, Correct"
            dataline=(str(expInfo['participant']) + "," + str(block+1) + "," + str(t) + "," + event_type+ "," + trial_type  + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(kp_out)+ "," +str(corr_out) + "," + str(99) + "," + str(RT))
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
            
    num_pres.setAutoDraw(False)
    win.flip()
    port.setData(0)
    
    time_arr=np.array(time_arr)
    mean_trialTime =np.mean(time_arr)
    sd_trialTime=np.std(time_arr)
    
    return(totcorr, totincorr, totnoresp,x, mean_trialTime, sd_trialTime)
    




#******* INITIAL CALIBRATION FUNCTION*********


def trainingCal(cues_array, color=None):
    trainarr=[]
    done=0
    goodtrial, curr_success=0,0
    mean, sd=0,0
    mean_trialTime, sd_trialTime, initial_cutoff=0,0,0
    t,block=1,-99
    traincorr, trainincorr, trainnoresp, x, mean_trialTime, sd_trialTime= 0,0,0,0,0,0
    trial_type, desc=None, None
    dectype="-"
    I.setPos([0,-0.4])
    if (color=="yellow"):
        dectype="gtlt"
    elif (color=="blue"):
        dectype="evenodd"
    taskinfo=(str(expInfo['participant']) +','+ str(expInfo['handedness']) + ','+  str(expInfo['session']) +','+ str(expInfo['condition']) +','+str(block))
    while (done==0):
        np.random.shuffle(cues_array)
        for n in range(0,len(cues_array)):
            #I'm so annoyed I have to write this this way but I'm adding this too late now.
            if (cues_array[n][1]=="lclr_cued"):
                trial_type="easy_cue_train"
                desc="Cue_lclr_cued"
                curr_rew=5
            elif (cues_array[n][1]=="lchr_cued"):
                trial_type="easy_cue_train"
                desc="Cue_lchr_cued"
                curr_rew=25
            elif (cues_array[n][1]=="hclr_cued"):
                trial_type="hard_cue_train"
                desc="Cue_hclr_cued"
                curr_rew=5
            elif (cues_array[n][1]=="hchr_cued"):
                trial_type="hard_cue_train"
                desc="Cue_hchr_cued"
                curr_rew=25
            
            cues_pres.setImage(cues_array[n][0])
            cues_pres.setAutoDraw(True)
            I.setText(u"(Trate de recordar el significado de la imagen antes de presionar la barra espaciadora)")
            I.setAutoDraw(True)
            win.flip()

            eventTime=mClock.getTime()
            event_type="pres"
            #"EventType, TrialType, Desc, EventTime, Response, Correct"
            dataline=(str(expInfo['participant']) + "," + str(block) + "," + str(t) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0)+ "," + "NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
            
            response=event.waitKeys(keyList='space', timeStamped=mClock)
            event_type="resp"
            eventTime= str(response[0][1])
            cues_pres.setAutoDraw(False)
            I.setAutoDraw(False) 
            #"EventType, TrialType, Desc, EventTime, Response, Correct"
            dataline=(str(expInfo['participant']) + "," + str(block) + "," + str(t) + "," + event_type+ "," + trial_type  + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(response[0][0])+ "," + "NaN" + "," + str(99) + "," + "NaN" )
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
            
            event_type="pres"
            desc="fix"
            fix_pres.setText("+")
            fix_pres.setAutoDraw(True)
            I.setText(u"(Prepárate para la tarea)")
            I.setAutoDraw(True)
            win.flip()
            eventTime=mClock.getTime()
            #"EventType, TrialType, Desc, EventTime, Response, Correct"
            dataline=(str(expInfo['participant']) + "," + str(block) + "," + str(t) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0) + "," + "NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
            
            core.wait(random.choice(fc_isi1))
            fix_pres.setAutoDraw(False)
            I.setAutoDraw(False)
            win.flip()
            
            
            if (cues_array[n][1]=="lclr_cued" or cues_array[n][1]=="lchr_cued"):
                randnumlist,randcollist=cue_easy_stim(color)
                traincorr, trainincorr, trainnoresp, x, mean_trialTime, sd_trialTime= cue_task_pres(randnumlist, randcollist, trial_type, t)
                curr_cue=cues_array[n][1]
                curr_task=cues_array[n][2]
                curr_diff=cues_array[n][3]
                
            elif (cues_array[n][1]=="hclr_cued" or cues_array[n][1]=="hchr_cued"):
                randnumlist,randcollist=cue_hard_stim()
                traincorr, trainincorr, trainnoresp, x, mean_trialTime, sd_trialTime= cue_task_pres(randnumlist, randcollist, trial_type, t)
                curr_cue=cues_array[n][1]
                curr_task=cues_array[n][2]
                curr_diff=cues_array[n][3]
            else:
                pass
                
                
            if (traincorr !=0):
                perc=(traincorr/(x-trainnoresp))*100
            else:
                perc=0
            curr_cue=cues_array[n][1]
            
            #feedback stage
            event_type="pres"
            desc="fix"
            fix_pres.setText("+")
            fix_pres.setAutoDraw(True)
            win.flip()
            eventTime=mClock.getTime()
            #"EventType, TrialType, Desc, EventTime, Response, Correct"
            dataline=(str(expInfo['participant']) + "," + str(block) + "," + str(t) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN"+"," + str(0)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
            
            core.wait(random.choice(fc_isi2))
            fix_pres.setAutoDraw(False)
            I.setAutoDraw(False)
            win.flip()
            
            
            #Feedback loop - since we need the trails to be at least 85% correct in the training, we won't reward them if
            #its not a "good" trial. In the real task, we have other metrics to decide if a trial is good, but I didn't want
            # to reward them if a trial wasn't good enough
            if (trainincorr>2 or perc<85):
                curr_success=0
                trialReward=0
              
                incorr_fb.setImage("stim/x_mark.png")
                incorr_fb.setAutoDraw(True)
                I.setText(u"(No hiciste la tarea suficientamente bien para ganar puntos. Pulse la barra espaciadora para pasar a la próxima prueba)")
                I.setAutoDraw(True)
                win.flip()
                
                eventTime=mClock.getTime()
                desc="fb_0"


            else: #now reward you for successful trials
                if (cues_array[n][1]=="lclr_cued" or cues_array[n][1]=="hclr_cued"): #will need to change this
                    trialReward=5
                    curr_success=1
                    
                    corr_fb.setText("5")
                    #corr_fb.setSize([.09,.17])
                    corr_fb.setAutoDraw(True)
                    I.setText(u"(Lo hiciste bien y ganaste puntos. Pulse la barra espaciadora para pasar a la próxima prueba)")
                    I.setAutoDraw(True)
                    win.flip()
                    eventTime=mClock.getTime()
                    desc="fb_5"
                        
                    
                else:
                    trialReward=25
                    curr_success=1
                    
                    corr_fb.setText("25")
                    #corr_fb.setSize([.16,.35])
                    corr_fb.setAutoDraw(True)
                    I.setText(u"(Lo hiciste bien y ganaste puntos. Pulse la barra espaciadora para pasar a la próxima prueba)")
                    I.setAutoDraw(True)
                    win.flip()
                    eventTime=mClock.getTime()
                    desc="fb_25"
                    
            dataline=(str(expInfo['participant']) + "," + str(block) + "," + str(t) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
                
            response=event.waitKeys(keyList='space', timeStamped=mClock)
            eventTime=response[0][1]
            dataline=(str(expInfo['participant']) + "," + str(block) + "," + str(t) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + response[0][0]+ "," +"NaN" + "," + str(0)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")

            corr_fb.setAutoDraw(False)
            incorr_fb.setAutoDraw(False)
            I.setAutoDraw(False)
            win.flip()
            

            #fixation cross
            desc="fix"
            fix_pres.setText("+")
            fix_pres.setAutoDraw(True)
            win.flip()
           
            eventTime=mClock.getTime()
            dataline=(str(expInfo['participant']) + "," + str(block) + "," + str(t) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN"+ "," + str(0)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
                
            core.wait(random.choice(fc_iti))
            fix_pres.setAutoDraw(False)
            win.flip()
            
            
            if (perc>=85 and trainincorr<=2):
                goodtrial=goodtrial+1
                curr_success=1
                trainarr.append((n,trainincorr, traincorr, x, mean_trialTime))

                if (len(trainarr)<5): # set this to 6 later
                    done=0
                else:
                    correct_dec=[i[2] for i in trainarr] #storing correct answers in this array. Need to change it to np.array to get the mean
                    #no longer using the mean. Now we need to select and sort. 20% percentile = 1 of 5
                    correct_dec=np.array(correct_dec)
                    sorted_correct_dec=np.sort(correct_dec)
                    thresh=sorted_correct_dec[1]
                    
                    sd=np.std(correct_dec) #not using SD for number of correct decisions
                    correct_time=[i[4] for i in trainarr]
                    correct_time=np.array(correct_time)
                    mean_time=np.mean(correct_time)
                    sd_time=np.std(correct_time)
                    initial_cutoff=mean_time+(1.5*sd_time)
                   
                    #writing last calibration trial.
                    #Subject, Handedness, Session, Condition, Block, Trial, Cue, TaskType, Difficulty, EasyCueDecType, PotentialReward, CurrDecThresh, CorrChoices, IncorrChoices, TrialReward, CumulReward, SuccessfulTrial, MeanDecTime, SDevDecTime, CatchQuestResp, CatchQuestCorr
                    loglist.append(str(taskinfo) +','+ str(t) +','+ curr_cue +','+ curr_task +','+ curr_diff + ','+  dectype + ',' +str(curr_rew)+ ','+ str(-99) +','+ str(traincorr) +','+ str(trainincorr) +','+ str(trialReward) +','+ str(-99) + ',' + str(curr_success) + "," +str(mean_trialTime) +"," +str(sd_trialTime)+','+ str(-99) +','+ str(-99))
                    trial_data=(str(taskinfo) +','+ str(t) +','+ curr_cue  +','+ curr_task +','+ curr_diff + ','+  dectype + ',' +str(curr_rew)+ ','+ str(-99) +','+ str(traincorr) +','+ str(trainincorr) +','+ str(trialReward) +','+ str(-99)+','+str(curr_success) + "," +str(mean_trialTime) +"," +str(sd_trialTime)+','+ str(-99) +','+ str(-99)) 
                    with open(filename2+'.txt', "a") as f:
                        f.write(trial_data+"\n")
                    
                    done=1
                    break
            else:
                curr_success=0
                pass

            
            loglist.append(str(taskinfo) +','+ str(t) +','+ curr_cue +','+ curr_task +','+curr_diff+','+ dectype + ',' +str(curr_rew)+ ','+ str(-99) +','+ str(traincorr) +','+ str(trainincorr) +','+ str(trialReward) +','+ str(-99) + ',' + str(curr_success) +"," +str(mean_trialTime) +"," +str(sd_trialTime)+','+ str(-99) +','+ str(-99)) 
            trial_data=(str(taskinfo) +','+ str(t) +','+ curr_cue  +','+ curr_task +','+curr_diff+','+ dectype + ',' +str(curr_rew)+ ','+ str(-99) +','+ str(traincorr) +','+ str(trainincorr) +','+ str(trialReward) +','+ str(-99)+','+str(curr_success) + "," +str(mean_trialTime) +"," +str(sd_trialTime) +','+ str(-99) +','+ str(-99)) 
            with open(filename2+'.txt', "a") as f:
                f.write(trial_data+"\n")
            
            t=t+1
    I.setPos([0,0])
    return(thresh, sd, initial_cutoff, correct_dec, correct_time) #now also returnign arrays with correct decisions. Going to make this the original startign array for my trials
        




# ************** TASK CALIBRATION FUNCTION *****************#
def taskCal(tc, ttime, corr_arr, time_arr, task_diff):
    corr_arr=np.append(corr_arr, tc)
    time_arr=np.append(time_arr, ttime)
            
    #now recalculate the 80% percentile using the number of correct decisions in the last 5 trials
    n=len(corr_arr)-1
    cal_dec_arr=corr_arr[(n-4):n+1]
    sort_cal_dec_arr=np.sort(cal_dec_arr)
    thresh=sort_cal_dec_arr[1]
        
    meantime = np.mean(time_arr[(n-4):n+1])
    sdtime = np.std(time_arr[(n-4):n+1])
    cutoff = meantime + (1.5*sdtime)
    
    return(thresh, cutoff, corr_arr, time_arr)



# ************** SELF REPORT SCALE FUNCTION *************#
    

def selfreport(block):

    sur_text=[]
    sur_text.append(u"¿Estas cansada/o?")
    sur_text.append(u"¿Cuanto te gusta este imagen?")
    sur_text.append(u"¿Cuanto te gusta este imagen?")
    sur_text.append(u"¿Cuanto te gusta este imagen?")
    sur_text.append(u"¿Cuanto te gusta este imagen?")
    sur_text.append(u"¿Que difícil es la tarea de sólo números amarillos?\n(Use el ratón para indicar tu respuesta)")
    sur_text.append(u"¿Que difícil es la tarea de sólo números azules?\n(Use el ratón para indicar tu respuesta)")
    sur_text.append(u"¿Que difícil es la tarea de números de ambos colores?\n(Use el ratón para indicar tu respuesta)")
    scale_cues=[lclr_cued_y, hclr_cued, lchr_cued_y, hchr_cued]
    fatigue,like_lclr_cue, like_hclr_cue, like_lchr_cue, like_hchr_cue=None, None, None, None, None
    dif_yellow, dif_blue, dif_hard=None, None, None
    resp=None
    trig=None
    if (block==-99):
        trig=9
    else:
        trig=block

    for i in range(0,len(sur_text)):
        if (i==0):
            trial_type="fatigue_rate_"+str(block)
        elif (i==1):
            trial_type="lclr_cue_rate_"+str(block)
        elif (i==2):
            trial_type="hclr_cue_rate_"+str(block)
        elif (i==3):
            trial_type="lchr_cue_rate_"+str(block)
        elif (i==4):
            trial_type="hchr_cue_rate_"+str(block)
        elif (i==5):
            trial_type="diff_yellow_rate"+str(block)
        elif (i==6):
            trial_type="diff_blue_rate_"+str(block)
        elif (i==7):
            trial_type="diff_rate_"+str(block)
        
        if (i==0 or i>4):
            I.setText(sur_text[i])
            I.setPos([0,.3])
            I.setAutoDraw(True)
        elif (i>0 and i<=4):
            I.setPos([0,.4])
            I.setText(sur_text[i])
            I.setAutoDraw(True)
            I_image.setImage(scale_cues[i-1][0])
            I_image.setSize([.2,.3])
            I_image.setPos([0,.1])
            I_image.setAutoDraw(True)
        win.flip()
        port.setData(trig)
        #data log
        event_type= "pres"
        desc=sur_text[i][0:6]
            
        eventTime=mClock.getTime()  
        dataline=(str(expInfo['participant']) + "," + str(block) +"," + "SR_"+str(block) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(trig)+ "," +"NaN")
        loglist_all.append(dataline)
        with open(filename3+'.txt', "a") as myfile:
            myfile.write(dataline+"\n")        
        event_type="resp"
        if (i==0):
            while fat_rating.getRating()==None:
                fat_rating.draw()
                win.flip()
            eventTime=mClock.getTime()  
            fatigue, resp=fat_rating.getRating(), fat_rating.getRating()                  

        elif (i==1):
            while cue_rating.getRating()==None:
                cue_rating.draw()
                win.flip()
            eventTime=mClock.getTime() 
            like_lclr_cue, resp=cue_rating.getRating(),cue_rating.getRating()

        elif (i==2):
            while cue_rating.getRating()==None:
                cue_rating.draw()
                win.flip()
            eventTime=mClock.getTime()  
            like_hclr_cue, resp=cue_rating.getRating(), cue_rating.getRating()
            
        elif (i==3):
            while cue_rating.getRating()==None:
                cue_rating.draw()
                win.flip()
            eventTime=mClock.getTime()  
            like_lchr_cue, resp=cue_rating.getRating(), cue_rating.getRating()
           
        elif (i==4):
            while cue_rating.getRating()==None:
                cue_rating.draw()
                win.flip()
            eventTime=mClock.getTime()  
            like_hchr_cue, resp=cue_rating.getRating(), cue_rating.getRating()
            
        elif (i==5):
            while dif_rating.getRating()==None:
                dif_rating.draw()
                win.flip()
            eventTime=mClock.getTime()  
            dif_yellow, resp=dif_rating.getRating(), dif_rating.getRating()
            
        elif (i==6):
            while dif_rating.getRating()==None:
                dif_rating.draw()
                win.flip()
            eventTime=mClock.getTime() 
            dif_blue, resp=dif_rating.getRating(), dif_rating.getRating()
           
        elif (i==7):
            while dif_rating.getRating()==None:
                dif_rating.draw()
                win.flip()
            eventTime=mClock.getTime() 
            dif_hard, resp=dif_rating.getRating(), dif_rating.getRating()
        
        dataline=(str(expInfo['participant']) + "," + str(block) +"," + "SR_"+str(block) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(trig)+ "," +"NaN")
        loglist_all.append(dataline)
        with open(filename3+'.txt', "a") as myfile:
            myfile.write(dataline+"\n")

        fat_rating.reset()
        cue_rating.reset()
        dif_rating.reset()
        I.setAutoDraw(False)
        I_image.setAutoDraw(False)
        win.flip()
        port.setData(0)

    rating_data=(str(expInfo['participant']) +"," + str(expInfo['session'])+ ","+str(expInfo['condition']) + "," + str(block) + "," + str(fatigue)+ "," + str(like_lclr_cue) + "," + str(like_hclr_cue) +"," + str(like_lchr_cue) +","+ str(like_hchr_cue)+","+ str(dif_yellow) +","+ str(dif_blue) +","+ str(dif_hard))
    with open(scale_file + '.txt', "a") as f:
        f.write(rating_data+"\n")



#******* Initialize components for Routine "Instrucciones" *****************


curr_trigger=7 #initializing trigger value
port.setData(curr_trigger)

your_mouse = event.Mouse(visible = False)

#basic instructions
inst_text=[]
inst_text.append(u'El objetivo de esta tarea es conseguir tantos puntos como sea posible. Para conseguir puntos, tienes que completar tres tipos de tareas, que requieren que tomes una serie de decisiones sobre números. \n\nA veces las tareas serán difíciles y a veces serán fácil. Cada tarea viene con una recompensa de 5 puntos o 25 puntos. \n\nSolo ganarás puntos si completas con éxito la tarea. \n\nSu recompensa depende de cuántos puntos tenga.\n\n(Presiona la barra espaciadora para continuar)')
inst_text.append(u'Antes de comenzar la tarea, una imagen aparecerá que indica el nivel de dificultad de la tarea y la cantidad de recompensa posible. \nPrimero, repasaremos las imágenes y sus significados.\n\n(Presiona la barra espaciadora para continuar)')
#instruction loop for presentation of instructions
for i in range(0,len(inst_text)):
    event_type="pres"
    trial_type="instruction"
    desc=inst_text[i][0:6]

    I.setText(inst_text[i])
    I.setAutoDraw(True)
    eventTime=mClock.getTime()
    port.setData(0)
    win.flip()
    
    #"EventType, TrialType, Desc, EventTime, Response, Correct, Trigger"
    dataline=(str(expInfo['participant']) + "," + str(block) +"," + "-99" + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0)+ "," +"NaN")
    loglist_all.append(dataline)
    with open(filename3+'.txt', "a") as myfile:
        myfile.write(dataline+"\n")
    
    response=event.waitKeys(keyList='space', timeStamped=mClock)
    event_type="resp"
    eventTime= str(response[0][1])
    
    I.setAutoDraw(False)
    win.flip()
    
    #"EventType, TrialType, Desc, EventTime, Response, Correct, Trigger"
    dataline=(str(expInfo['participant']) + ","  + str(block) + "," + "-99" + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(response[0][0])+ "," +"NaN"+ "," + str(0)+ "," +"NaN")
    loglist_all.append(dataline)
    with open(filename3+'.txt', "a") as myfile:
        myfile.write(dataline+"\n")
    

inst_text=[]
inst_text.append(u'Al comienzo de cada ensayo, verás un círculo o cuadrado con líneas por adentro.\n\n(Presiona la barra espaciadora para continuar)')

if (condition==1):
    cue1_text=u"El círculo indica que la tarea será fácil.\n\n(Presiona la barra espaciadora para continuar)"
    cue2_text=u"El cuadrado indica que la tarea será difícil.\n\n(Presiona la barra espaciadora para continuar)"
elif(condition==2):
    cue1_text=u"El cuadrado indica que la tarea será fácil.\n\n(Presiona la barra espaciadora para continuar)"
    cue2_text=u"El círculo indica que la tarea será difícil.\n\n(Presiona la barra espaciadora para continuar)"
else:
    print("condition not detected")
inst_text.append(cue1_text)
inst_text.append(cue2_text)
inst_text.append(u'Las líneas horizontales indican cuántos puntos ganarás si completas la tarea con éxito. Una línea indica que podrías ganar 5 puntos, mientras cinco líneas indica que podrías ganar 25 puntos. En definitiva: más líneas, más puntos.\n\n(Presiona la barra espaciadora para continuar)')


#instructions to introduce tasks
for i in range(0,len(inst_text)):
    I.setText(inst_text[i])
    event_type="pres"
    trial_type="instruction"
    desc=inst_text[i][0:6]
    if (i==1): 
        I.setPos([0,.2])
        if (condition==1):
            I_image.setPos([0,-.2])
            I_image.size=([.43,.36])   #(.76,.35)
            I_image.setImage('stim/circle_cues_inst.png')
        elif (condition==2):
            I_image.setPos([0,-.2])
            I_image.size=([.45,.36])  #(.76,.35)
            I_image.setImage('stim/square_cues_inst.png')    
        I_image.setAutoDraw(True)
    elif (i==2):
        I.setPos([0,.2])
        if (condition==1):
            I_image.setPos([0,-.2])
            I_image.size=([.45,.36]) #(.8,.35)
            I_image.setImage('stim/square_cues_inst.png') 
        elif (condition==2):
            I_image.setPos([0,-.2])
            I_image.size=([.43,.36]) 
            I_image.setImage('stim/circle_cues_inst.png')
        I_image.setAutoDraw(True)
    elif (i==3):
        I.setPos([0,.4])
        I_image.setPos([0,-.2])
        I_image.size=([.39,.5])
        I_image.setImage('stim/recompensa_inst.png')
        I_image.setAutoDraw(True)
   
    I.setAutoDraw(True)
    win.flip()
    eventTime=mClock.getTime()
    
    #"EventType, TrialType, Desc, EventTime, Response, Correct"
    dataline=(str(expInfo['participant']) + ","  + str(block) + "," + "-99" + ","+ event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN"+ "," + str(0)+ "," +"NaN")
    loglist_all.append(dataline)
    with open(filename3+'.txt', "a") as myfile:
        myfile.write(dataline+"\n")
    
    
    response=event.waitKeys(keyList='space', timeStamped=mClock)
    event_type="resp"
    eventTime= str(response[0][1])
    
    I.setAutoDraw(False)
    I_image.setAutoDraw(False)
    win.flip()
    
    
    #"EventType, TrialType, Desc, EventTime, Response, Correct, Trigger"
    dataline=(str(expInfo['participant']) + ","  + str(block) + "," + "-99" + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(response[0][0])+ "," +"NaN" + "," + str(0)+ "," +"NaN")
    loglist_all.append(dataline)
    with open(filename3+'.txt', "a") as myfile:
        myfile.write(dataline+"\n")
    

inst_text=[]
inst_text.append(u'Los círculos y cuadrados se mostrarán muy brevemente. Después, la mitad de las veces aparecerá una cruz (+), y en la otra mitad, un asterisco (*).\n\nLa cruz (+) significa que te toca hacer la tarea, el asterisco (*) significa que no tienes que hacer nada.\n\n(Presiona la barra espaciadora para continuar)')
inst_text.append(u'Además, en algunos ensayos, vas a tener que identificar cual imagen fue presentado al inicio del ensayo. Tu recompensa esta basado, en parte, de que bien identificas estas imágenes, así que es muy importante que prestes atención a las imagenes.\n\n(Presiona la barra espaciadora para ver un ejemplo)')
inst_text.append(u'¿Pero cual es la tarea? La tarea consiste en un pequeño juego en el que durante 8 segundos se presentarán una serie de números que pueden ser de dos colores.\n\n(Presiona la barra espaciadora para continuar)')

for i in range(0,len(inst_text)):
    event_type="pres"
    trial_type="instruction"
    desc=inst_text[i][0:6]
    
    I.setText(inst_text[i])
    I.setPos([0,0])
    I.setAutoDraw(True)
    win.flip()
    eventTime=mClock.getTime()
    
    #"EventType, TrialType, Desc, EventTime, Response, Correct"
    dataline=(str(expInfo['participant']) + ","  + str(block) + "," + "-99" + ","+event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0)+ "," +"NaN")
    loglist_all.append(dataline)
    with open(filename3+'.txt', "a") as myfile:
        myfile.write(dataline+"\n")
    
    response=event.waitKeys(keyList='space', timeStamped=mClock)
    event_type="resp"
    eventTime= str(response[0][1])
    I.setAutoDraw(True)
    win.flip()
    
    #"EventType, TrialType, Desc, EventTime, Response, Correct"
    dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + ","+ event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(response[0][0])+ "," +"NaN" + "," + str(0)+ "," +"NaN")
    loglist_all.append(dataline)
    with open(filename3+'.txt', "a") as myfile:
        myfile.write(dataline+"\n")
    
    I.setAutoDraw(False)
    win.flip()
    
    if (i==1):
        cues_pres.setImage('stim/circle_5.png')
        cues_pres.setAutoDraw(True)
        win.flip()
        #port.setData(curr_trigger)
        
        eventTime=mClock.getTime()
        event_type="pres"
        trial_type='lclr_notask_quest' #type of trial
        desc= "cue_ex"
        dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0)+ "," +"NaN")
        loglist_all.append(dataline)
        with open(filename3+'.txt', "a") as myfile:
            myfile.write(dataline+"\n")
        
        core.wait(1.5) #1500 ms cue 
        cues_pres.setAutoDraw(False)
        win.flip()
        
        star_pres.setPos([0,-.05])
        star_pres.setAutoDraw(True)
        win.flip()
           
        eventTime=mClock.getTime()
        event_type="pres"
        desc= "noWork_ex"
        dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN"+ "," + str(0)+ "," +"NaN")
        loglist_all.append(dataline)
        with open(filename3+'.txt', "a") as myfile:
            myfile.write(dataline+"\n")
            
        core.wait(random.choice(fc_isi1))
        star_pres.setAutoDraw(False)
        win.flip()
        #filling in -99 for these values in the data file because there was no work or reward in these trials
        curr_thresh, totcorr, totincorr, trialReward, curr_success, mean_trialTime, sd_trialTime=-99, -99, -99, -99, -99, -99,-99

        quest_slide.setText(u"Pulse la tecla que corresponde al imagen presentado en este ensayo.\n\n\n(1) Tarea fácil de 5 puntos\n(2) Tarea fácil de 25 puntos\n(3) Tarea difícil de 5 puntos\n(4) Tarea difícil de 25 puntos")
        quest_slide.setAutoDraw(True)
        #data for question slide
        event_type="pres"
        trial_type="catch_question_ex"
        desc=u"Presiona el núm"
        eventTime=mClock.getTime()
        win.flip()
        #"EventType, TrialType, Desc, EventTime, Response, Correct"
        dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0)+ "," +"NaN")
        loglist_all.append(dataline)
        with open(filename3+'.txt', "a") as myfile:
            myfile.write(dataline+"\n")

        response=event.waitKeys(keyList=['1','2','3','4'],timeStamped=mClock)
        catch_response=response[0][0]
        event_type="catch_resp_ex"
        rt=response[0][1]-eventTime
        eventTime= str(response[0][1])
        quest_slide.setAutoDraw(False)
        win.flip()
        catch_response,catch_corr=-99,-99
        #Subject, Handedness, Trial, EventType, TrialType, Desc, EventTime, Response, Correct, Trigger, RT
        dataline=(str(expInfo['participant'])+ "," + str(block) + "," + "-99" + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(catch_response)+ "," +str(catch_corr) + "," + str(0)+ "," +str(rt))
        loglist_all.append(dataline)
        with open(filename3+'.txt', "a") as myfile:
            myfile.write(dataline+"\n") 





#now start the examples

cue_ex_arr=[("7","blue"), ("3","blue"), ("2", "blue"), ("6", "blue"), ("1","blue"), ("8","yellow"), ("3","yellow"), ("9", "yellow"), ("4", "yellow"), ("6","yellow"),
            ("3","yellow"), ("4","blue"), ("9", "yellow"), ("7", "blue"), ("4","yellow")]
cue_ex_corr_resp=["right", "right", "left", "left", "right", "right", "left","right", "left", "right", "left", "left","right", "right", "left"]

inst_text=[]
inst_text.append(u'Cuando el número es azul, tienes que decidir si el número es impar o par. Presiona la flecha izquierda del teclado si el número es PAR y la flecha derecha si el número es IMPAR.\n\n(Presiona la barra espaciadora para practicar)')
inst_text.append(u'Cuando el número es amarillo, tienes que decidir si el número es mayor o menor que 5. Presiona la flecha izquierda del teclado si el número es MENOR DE 5 y la flecha derecha si el número es MAYOR QUE 5. \n \n(Presiona la barra espaciadora para practicar)')
if (condition==1):
    inst_text.append(u'En tareas fáciles (círculo), los números siempre serán del mismo color, pero en las tareas difíciles (cuadrado), los colores de los números se alternarán. \n \n(Presiona la barra espaciadora para practicar)')
elif (condition==2):
    inst_text.append(u'En tareas fáciles (cuadrado), los números siempre serán del mismo color, pero en las tareas difíciles (círculo), los colores de los números se alternarán. \n \n(Presiona la barra espaciadora para practicar)')


for i in range(0,len(inst_text)):
    event_type="pres"
    trial_type="instruction"
    desc=inst_text[i][0:6]
    
    I.setText(inst_text[i])
    I.setPos([0,0])
    I.setAutoDraw(True)
    win.flip()
    eventTime=mClock.getTime()
    
    #"EventType, TrialType, Desc, EventTime, Response, Correct"
    dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + ","+event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0)+ "," +"NaN")
    loglist_all.append(dataline)
    with open(filename3+'.txt', "a") as myfile:
        myfile.write(dataline+"\n")
    
    response=event.waitKeys(keyList='space', timeStamped=mClock)
    event_type="resp"
    eventTime= str(response[0][1])
    I.setAutoDraw(True)
    win.flip()
    
    #"EventType, TrialType, Desc, EventTime, Response, Correct"
    dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + ","+ event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(response[0][0])+ "," +"NaN" + "," + str(0)+ "," +"NaN")
    loglist_all.append(dataline)
    with open(filename3+'.txt', "a") as myfile:
        myfile.write(dataline+"\n")
    
    if (i==0):
        for k in range(0,5):
            I.setPos([0,.2])
            I.setText("Izquierda si PAR            Derecha si IMPAR")
            I.setAutoDraw(True)

            num_pres.setColor(cue_ex_arr[k][1])
            num_pres.setText(cue_ex_arr[k][0])
            num_pres.setAutoDraw(True)
            win.flip()
            eventTime=mClock.getTime()
            event_type="pres"
            trial_type="easyBlueCueInst"
            desc=str(cue_ex_arr[k][0])+"_"+(cue_ex_arr[k][1])
            
            #"EventType, TrialType, Desc, EventTime, Response, Correct"
            dataline=(str(expInfo['participant']) + "," + "-99" + ","+event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
                            
                    
            response=event.waitKeys(keyList=['left', 'right'], timeStamped=mClock)
            event_type="resp"
            eventTime= str(response[0][1])

            num_pres.setAutoDraw(False)
            win.flip()
            
            if (cue_ex_corr_resp[k]==response[0][0]):
                correct=1
            else:
                correct=0
            #"EventType, TrialType, Desc, EventTime, Response, Correct"
            dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + ","+ event_type+ "," + trial_type  + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(response[0][0])+ "," +str(correct) + "," + str(0)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
                    
    elif (i==1):
        for k in range(5,10):
            I.setPos([0,.2])
            I.setText("Izquierda si <5                      Derecha si >5")
            I.setAutoDraw(True)
            
            num_pres.setColor(cue_ex_arr[k][1])
            num_pres.setText(cue_ex_arr[k][0])
            num_pres.setAutoDraw(True)
            win.flip()
            
            eventTime=mClock.getTime()
            event_type="pres"
            trial_type= "easyYellowCueInst"
            desc=str(cue_ex_arr[k][0])+"_"+(cue_ex_arr[k][1])

            #"EventType, TrialType, Desc, EventTime, Response, Correct"
            dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + ","+event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
            
            response=event.waitKeys(keyList=['left', 'right'], timeStamped=mClock)
            event_type="resp"
            eventTime= str(response[0][1])
            
            num_pres.setAutoDraw(False)
            win.flip()
            
            if (cue_ex_corr_resp[k]==response[0][0]):
                correct=1
            else:
                correct=0
            
            #"EventType, TrialType, Desc, EventTime, Response, Correct"
            dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + "," + event_type+ "," + trial_type  + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(response[0][0])+ "," +str(correct) + "," + str(0)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
                
                
    elif (i==2):
        for k in range(10,len(cue_ex_arr)):
            I.setPos([0,.2])
            I.setHeight(.05)
            I.setText("Izquierda si PAR o <5                  Derecha si IMPAR o >5")
            I.setAutoDraw(True)
            
            desc=str(cue_ex_arr[k][0])+"_"+(cue_ex_arr[k][1])
            num_pres.setColor(cue_ex_arr[k][1])
            num_pres.setText(cue_ex_arr[k][0])
            num_pres.setAutoDraw(True)
            win.flip()
            
            eventTime=mClock.getTime()
            event_type="pres"
            trial_type= "hardCueInst"
            desc=str(cue_ex_arr[k][0])+"_"+(cue_ex_arr[k][1])

            #"EventType, TrialType, Desc, EventTime, Response, Correct"
            dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
            
            response=event.waitKeys(keyList=['left', 'right'], timeStamped=mClock)
            event_type="resp"
            eventTime= str(response[0][1])
            
            num_pres.setAutoDraw(False)
            win.flip()

            if (cue_ex_corr_resp[k]==response[0][0]):
                correct=1
            else:
                correct=0

            #"EventType, TrialType, Desc, EventTime, Response, Correct"
            dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + "," + event_type+ "," + trial_type  + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(response[0][0])+ "," +str(correct) + "," + str(0)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
                
    else:
        pass

    I.setAutoDraw(False)
    win.flip()

I.setPos([0,0])
I.setHeight(.07)




# ************* Training/Calibration trials ************* #

#block=-99
traincorr, trainincorr, trainnoresp=0,0,0

goodtrial=0

# arrays to hold calibration-related values
hardcue_arr, beasycue_arr, yeasycue_arr= [], [], []
hardcue_times_arr, beasycue_times_arr, yeasycue_times_arr=[], [], []


#important global variables for calibration
med_beasycue,sd_beasycue, cutoff_beasycue, med_yeasycue,sd_yeasycue, cutoff_yeasycue =0,0,0,0,0,0
med_hardcue,sd_hardcue, cutoff_hardcue = 0,0,0


#
# ************ PRACTICE TRIALS BEGIN *************
#
#
#


inst_text=[]
inst_text.append(u'Si no tomas una cantidad razonable de decisiones o si cometes demasiados errores dentro del límite de tiempo de 8 segundos, no ganarás ningún punto. Si, por lo contrario, lo haces bien, ganarás la cantidad indicada.\n\nTen en cuenta que, en general, puedes contestar menos veces en la tarea fácil que la tarea difícil y todavía ganar puntos.\n\n(Presiona la barra espaciadora para continuar)')
inst_text.append(u'Ahora vamos a practicar las tareas. Durante la práctica, repasaremos las imágenes juntos, y luego decidirás cuándo comenzar la tarea presionando la barra espaciadora. Si tiene alguna pregunta durante la práctica, por favor pregúntame. \n\nAntes de pasar a la tarea real, tendrás que completar correctamente al menos 5 ensayos de cada tipo de tarea.\n\n(Presiona la barra espaciadora para continuar)')
inst_text.append(u'Primero comenzaremos con una de las tareas fáciles. Esta vez, los números siempre serán azul, así que tendrás que decidir si el número es par (flecha izquierda) o impar (flecha derecha). \n\n(Presiona la barra espaciadora para practicar la tarea fácil)')
inst_text.append(u'¡Bien hecho! Ahora practicaremos la otra tarea fácil. Esta vez todos los números serán amarillos, así que tendrás que decidir si el número es mayor (flecha derecha) o menor (flecha izquierda) que 5. Recuerda, necesitamos que completes con éxito al menos 5 ensayos antes de que podamos comenzar la tarea real. \n\n(Presiona la barra espaciadora para practicar la tarea fácil)')
inst_text.append(u'¡Bien hecho! Ahora practicaremos la tarea difícil. Recuerda, necesitamos que completes con éxito al menos 5 ensayos antes de que podamos comenzar la tarea real. \n\n(Presiona la barra espaciadora para practicar la tarea difícil)')


#this is in a fixed order. You are intended to walk through the practice with the participant and explain the meaning of 
# each of the cues and feedbacks. For this reason, you can only move on from the cue and feedback by pressing the space bar.
# in the real task, the cue and feedback will only be presented briefly and will move on automatically
for i in range(0,len(inst_text)):
    I.setText(inst_text[i])
    I.setPos([0,0])
    I.setAutoDraw(True)
    win.flip()
    eventTime=mClock.getTime()
    event_type="pres"
    trial_type="instruction"
    desc=inst_text[i][0:6]
    
    dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0)+ "," +"NaN")
    loglist_all.append(dataline)
    with open(filename3+'.txt', "a") as myfile:
        myfile.write(dataline+"\n")

    
    response=event.waitKeys(keyList='space', timeStamped=mClock)
    eventTime=response[0][1]
    event_type="resp"
    dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(response[0][0])+ "," +"NaN"+ "," + str(0)+ "," +"NaN")
    loglist_all.append(dataline)
    with open(filename3+'.txt', "a") as myfile:
        myfile.write(dataline+"\n")
    
    I.setAutoDraw(False)
    win.flip()

    if (i==2):
        port.setData(8) #practice test
        win.flip()
        port.setData(0)
        win.flip()
        med_beasycue,sd_beasycue, cutoff_beasycue, beasycue_arr, beasycue_times_arr=trainingCal([lclr_cued_b, lchr_cued_b], "blue")
        port.setData(0)
        win.flip()
    elif (i==3):
        port.setData(0)
        med_yeasycue,sd_yeasycue, cutoff_yeasycue, yeasycue_arr, yeasycue_times_arr=trainingCal([lclr_cued_y, lchr_cued_y], "yellow")
       port.setData(0)
        win.flip()
    elif (i==4):
        port.setData(0)
        med_hardcue,sd_hardcue, cutoff_hardcue, hardcue_arr, hardcue_times_arr=trainingCal([hclr_cued, hchr_cued])
        port.setData(0)
        win.flip()

port.setData(7)

#starting task. Reminder of the instructions and first self-report
inst_text=[]
inst_text.append(u'Terminaste el entrenamiento y estas listo para la tarea real.\n\nTenemos unas preguntas antes que empieces la tarea real. Presiona la barra espaciadora para contestar las preguntas.')
inst_text.append(u'¡Gracias! Ahora vamos a empezar la tarea real. \n \nRecuerde que durante esta parte, no vas a utilizar la barra espaciadora. Una vez que finalices una ensayo, pasará **automáticamente** al siguiente ensayo. \n\nLa imagen que indica el nivel de recompensa y el nivel de dificultad solo estará presentada brevemente, y luego comenzará el ensayo.')
inst_text.append(u'Como comentamos antes, es MUY importante que durante la tarea estés atento/a a las señales del inicio (círculos/cuadrados) para anticipar que tarea te va a tocar (fácil/difícil) y cuantos puntos vas a ganar (5 o 25). De esta manera, estarás bien preparado/a y podras contestar mejor y maximizar tus puntos.\n\n')
inst_text.append(u'Recuerde también que solo serás recompensado por los ensayos que completaste correctamente, así que trate de responder con la mayor precisión posible.\n\nTambién, como explicamos antes, de vez en cuando vamos a pedirte que identifiques el significado (nivel de dificultad y recompensa) del imagen que fue presentado al inicio del ensayo. Porque tu recompensa depende en parte de que bien contestas estas preguntas recomendamos que, trates de parpadear durante la presentación de los números o entre los ensayos, pero no durante la presentación de la imagen.')
inst_text.append(u'De vez en cuando tendrás un descanso entre los ensayos. Durante algunos de estos decansos, te vamos a preguntar la mismas preguntas que antes. \n\nSi tiene alguna pregunta, coméntalo al asistente ahora. \n\n\nPresiona la barra espaciadora para comenzar. ')
for i in range(0,len(inst_text)):
    I.setPos([0, 0])
    I.setText(inst_text[i])
    I.setAutoDraw(True)
    port.setData(0)
    win.flip()
    eventTime=mClock.getTime()
    event_type="pres"
    trial_type="instruction"
    desc=inst_text[i][0:5]
    
    dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0)+ "," +"NaN")
    loglist_all.append(dataline)
    with open(filename3+'.txt', "a") as myfile:
        myfile.write(dataline+"\n")

    response=event.waitKeys(keyList='space', timeStamped=mClock)
    eventTime=response[0][1]
    event_type="resp"
    dataline=(str(expInfo['participant']) + "," + str(block) + "," + "-99" + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(response[0][0])+ "," +"NaN" + "," + str(0) + "," +"NaN")
    loglist_all.append(dataline)
    with open(filename3+'.txt', "a") as myfile:
        myfile.write(dataline+"\n")
    
    
    I.setAutoDraw(False)
    win.flip()

    if (i==0):
        your_mouse = event.Mouse(visible = True)
        selfreport(block)
        your_mouse = event.Mouse(visible = False)

    else:
        pass



#
#
#
# *************** REAL TASK TRIALS BEGIN ******************* #
#
#


# initializing elements needed for the real task
port.setData(6) #SIGNALS THAT REAL TRIALS ARE STARTING NOW
trial, block_count=0,0
trialReward, runningTotal, curr_rew, curr_thresh=0,0,0,0
curr_task, curr_cue, curr_diff, curr_taskType=None, None, None, None
curr_success=0
catch_response, catch_corr=0,0
dectype="-"
ptrig=0
rt=0
catch_corr_arr=[]

#creating simple variable to help with if else loops
# if no work

win.flip()
port.setData(0)

np.random.shuffle(block_arr)
for block in range(0,len(block_arr)):   
    block_count=block_count+1
    cues=block_arr[block]
   
    for cue in range(0,len(cues)):
        trial=trial+1
        ptrig=0 #just to make sure
        dectype="-"
        curr_cue=cues[cue][1]
        curr_task=cues[cue][2]
        curr_diff=cues[cue][3]
        curr_rew=cues[cue][4]
        if (curr_cue=="lclr_cued" or curr_cue=="lchr_cued"):
            curr_trigger=int(cues[cue][6])
            curr_taskType=int(cues[cue][7])
        else:
            curr_trigger=int(cues[cue][5])
            curr_taskType=int(cues[cue][6])

        cues_pres.setImage(cues[cue][0])
        cues_pres.setAutoDraw(True)
        win.flip()
        port.setData(curr_trigger)
        
        eventTime=mClock.getTime()
        event_type="pres"
        trial_type=curr_cue #type of trial
        desc= "cue"
        dataline=(str(expInfo['participant']) + "," + str(block_count) + "," + str(trial) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(curr_trigger)+ "," +"NaN")
        loglist_all.append(dataline)
        with open(filename3+'.txt', "a") as myfile:
            myfile.write(dataline+"\n")

        
        core.wait(1.5) #1500 ms cue presentation - fixed --> used to be 800, but was too short for anyone to even understand the cue
        cues_pres.setAutoDraw(False)
        win.flip()
        port.setData(0)
        #if no work required, show star and move on to next trial
        if (curr_taskType==2 or curr_taskType==3):
            #directly present star
            star_pres.setPos([0,-.05])
            star_pres.setAutoDraw(True)
            win.flip()
            ptrig=curr_trigger+1
            port.setData(ptrig)
            
            eventTime=mClock.getTime()
            event_type="pres"
            desc= "noWork"
            dataline=(str(expInfo['participant']) + "," + str(block_count) + "," + str(trial) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN"+ "," + str(ptrig)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
            
            core.wait(random.choice(fc_isi1))
            star_pres.setAutoDraw(False)
            win.flip()
            port.setData(0)
            #filling in -99 for these values in the data file because there was no work or reward in these trials
            curr_thresh, totcorr, totincorr, trialReward, curr_success, mean_trialTime, sd_trialTime=-99, -99, -99, -99, -99, -99,-99
            if (curr_taskType==3):
                #####test questions
                quest_slide.setText(u"Presiona el número que indica el significado correcto de la imagen que recién viste.\n\n\n(1) Tarea fácil de 5 puntos\n(2) Tarea fácil de 25 puntos\n(3) Tarea difícil de 5 puntos\n(4) Tarea difícil de 25 puntos")
                quest_slide.setAutoDraw(True)
                #data for question slide
                event_type="pres"
                trial_type=curr_cue
                desc="catch_quest"
                eventTime=mClock.getTime()
                ptrig=curr_trigger+2
                win.flip()
                port.setData(ptrig)

                #"EventType, TrialType, Desc, EventTime, Response, Correct"
                dataline=(str(expInfo['participant']) + "," + str(block_count) + "," + str(trial) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(ptrig)+ "," +"NaN")
                loglist_all.append(dataline)
                with open(filename3+'.txt', "a") as myfile:
                    myfile.write(dataline+"\n")

                response=event.waitKeys(keyList=['1','2','3','4'],timeStamped=mClock)
                catch_response=response[0][0]
                event_type="resp"
                rt=response[0][1]-eventTime
                eventTime= str(response[0][1])
                quest_slide.setAutoDraw(False)
                port.setData(99) #response to question
                win.flip()
                if (curr_cue=="lclr_notask_quest"):
                    if (catch_response=="1"):
                        catch_corr=1
                    else: 
                        catch_corr=0
                elif (curr_cue=="lchr_notask_quest"):
                    if (catch_response=="2"):
                        catch_corr=1
                    else: 
                        catch_corr=0
                elif (curr_cue=="hclr_notask_quest"):
                    if (catch_response=="3"):
                        catch_corr=1
                    else: 
                        catch_corr=0
                elif (curr_cue=="hchr_notask_quest"):
                    if (catch_response=="4"):
                        catch_corr=1
                    else: 
                        catch_corr=0
                catch_corr_arr.append(catch_corr)
            else: 
                catch_response,catch_corr=-99,-99
                #Subject, Handedness, Trial, EventType, TrialType, Desc, EventTime, Response, Correct, Trigger, RT
                dataline=(str(expInfo['participant']) + "," + str(block_count) + "," + str(trial)  + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(catch_response)+ "," +str(catch_corr) + "," + str(ptrig)+ "," +str(rt))
                loglist_all.append(dataline)
                with open(filename3+'.txt', "a") as myfile:
                    myfile.write(dataline+"\n")
                win.flip()
                port.setData(0)
        else: #else work is required
            fix_pres.setText("+")
            fix_pres.setAutoDraw(True)
            win.flip()
            
            eventTime=mClock.getTime()
            event_type="pres"
            desc= "fix"
            dataline=(str(expInfo['participant']) + "," + str(block_count) + ","  + str(trial) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN"+ "," + str(0)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
                
            core.wait(random.choice(fc_isi1))
            fix_pres.setAutoDraw(False)
            win.flip()
            ptrig=curr_trigger+1 
            port.setData(ptrig) #EFFORT ONSET
            win.flip()
            port.setData(0)
            
            if (curr_cue== "hclr_cued" or curr_cue=="hchr_cued"):
                #generate a hard task number and color array
                randnumlist,randcollist=cue_hard_stim()
                curr_thresh, curr_cutoff=med_hardcue, cutoff_hardcue
                #cue_task_pres presents the task, calls another function to calculate the responses, and passes back totcorr, totincorr, and totnoresp         
                totcorr, totincorr, totnoresp,x, mean_trialTime, sd_trialTime= cue_task_pres(randnumlist, randcollist,trial_type, trial,curr_cutoff)
                med_hardcue, cutoff_hardcue, hardcue_arr, hardcue_times_arr =taskCal(totcorr, mean_trialTime, hardcue_arr, hardcue_times_arr, curr_diff)
    
    
            elif (curr_cue == "lclr_cued" or curr_cue== "lchr_cued"):
                #generate easy cue switching array
                randnumlist,randcollist=cue_easy_stim(cues[cue][5])
                if (cues[cue][5]=='yellow'):
                    curr_thresh, curr_cutoff=med_yeasycue, cutoff_yeasycue
                    dectype="evenodd"
                else:
                    curr_thresh, curr_cutoff=med_beasycue, cutoff_beasycue
                    dectype="gtlt"
                totcorr, totincorr, totnoresp,x, mean_trialTime, sd_trialTime= cue_task_pres(randnumlist, randcollist,trial_type, trial,curr_cutoff)
                #storing totals and average response time
                if (cues[cue][5]=='yellow'):
                    med_yeasycue, cutoff_yeasycue, yeasycue_arr, yeasycue_times_arr=taskCal(totcorr, mean_trialTime, yeasycue_arr, yeasycue_times_arr, curr_diff)
                else:
                    med_beasycue, cutoff_beasycue, beasycue_arr, beasycue_times_arr= taskCal(totcorr, mean_trialTime, beasycue_arr, beasycue_times_arr, curr_diff)

            #fixation cross before feedback 
            win.flip()
            port.setData(0)
            fix_pres.setText("+")
            fix_pres.setAutoDraw(True)
            win.flip()
            eventTime=mClock.getTime()
            event_type="pres"
            desc= "fix"
            dataline=(str(expInfo['participant']) +  "," + str(block_count) + "," + str(trial) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN" + "," + str(0)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
                
            
            core.wait(random.choice(fc_isi2))
            fix_pres.setAutoDraw(False)
            win.flip()
    
            
    
            #Feedback - first looking at success and not sucessful
            if (totcorr<curr_thresh):
                curr_success=0
                trialReward=0
                incorr_fb.setImage("stim/x_mark.png")
                incorr_fb.setAutoDraw(True)
                win.flip()
                ptrig=curr_trigger+2
                port.setData(ptrig)
                
                eventTime=mClock.getTime()
                desc= "fb_0"
                
                core.wait(1)
                incorr_fb.setAutoDraw(False)
                win.flip()
                port.setData(0)
            elif (curr_diff=="easy" and totincorr>3): #no more than 1 error also allowed for easy-- used to be 3 errors allowed for easy
                curr_success=0
                trialReward=0
                incorr_fb.setImage("stim/x_mark.png")
                incorr_fb.setAutoDraw(True)
                win.flip()
                ptrig=curr_trigger+2
                port.setData(ptrig)
                
                eventTime=mClock.getTime()
                desc= "fb_0"
                
                core.wait(1)
                incorr_fb.setAutoDraw(False)
                win.flip()
                port.setData(0)
            elif (curr_diff=="hard" and totincorr>1): #added restriction - no more that 1 error allowed for hard
                curr_success=0
                trialReward=0
                incorr_fb.setImage("stim/x_mark.png")
                incorr_fb.setAutoDraw(True)
                win.flip()
                ptrig=curr_trigger+2
                port.setData(ptrig)
                
                eventTime=mClock.getTime()
                desc= "fb_0"
                
                core.wait(1)
                incorr_fb.setAutoDraw(False)
                win.flip()
                port.setData(0)
            elif (totcorr>=curr_thresh):    #now reward you for successful trials
                if (curr_cue=="hclr_cued" or curr_cue=="lclr_cued"):
                    curr_success=1
                    trialReward=5
                    runningTotal=runningTotal+trialReward
                    
                    corr_fb.setText("5")
                    #corr_fb.setSize([.09,.17])
                    corr_fb.setAutoDraw(True)
                    win.flip()
                    ptrig=curr_trigger+3
                    port.setData(ptrig)
                    
                    eventTime=mClock.getTime()
                    desc= "fb_5"
                        
                    
                    core.wait(1)
                    corr_fb.setAutoDraw(False)
                    win.flip()
                    port.setData(0)
                else:
                    curr_success=1
                    trialReward=25
                    runningTotal=runningTotal+trialReward
                    
                    corr_fb.setText("25")
                    #corr_fb.setSize([.16,.35])
                    corr_fb.setAutoDraw(True)
                    win.flip()
                    ptrig=curr_trigger+4
                    port.setData(ptrig)
                    
                    eventTime=mClock.getTime()
                    desc= "fb_25"
                    
                    core.wait(1)
                    corr_fb.setAutoDraw(False)
                    win.flip()
                    port.setData(0)
                    
            #recodring feedback
            dataline=(str(expInfo['participant'])  +  "," + str(block_count) + "," + str(trial) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN"+ "," + str(ptrig)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
            

        
        #fixation cross
        fix_pres.setText("+")
        fix_pres.setAutoDraw(True)
        win.flip()
        
        eventTime=mClock.getTime()
        event_type="pres"
        desc="fix"
        dataline=(str(expInfo['participant']) +  "," + str(block_count) + "," + str(trial) + "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN"+ "," + str(0) + "," +"NaN")
        loglist_all.append(dataline)
        with open(filename3+'.txt', "a") as myfile:
            myfile.write(dataline+"\n")
        
        core.wait(random.choice(fc_iti))
        fix_pres.setAutoDraw(False)
        win.flip()

        
        #storing data for every trial
        taskinfo=(str(expInfo['participant']) +','+ str(expInfo['handedness']) + ','+str(expInfo['session']) +','+ str(condition) +','+str(block_count))
        loglist.append(str(taskinfo) +','+ str(trial) +','+ curr_cue +','+ curr_task +','+curr_diff+',' + dectype +"," +str(curr_rew)+ ','+ str(curr_thresh) +','+ str(totcorr) +','+ str(totincorr) +','+ str(trialReward) +','+ str(runningTotal)+","+str(curr_success)+ "," +str(mean_trialTime) +"," +str(sd_trialTime)+ ',' + str(catch_response) + ',' + str(catch_corr))
        trial_data=(str(taskinfo) +','+ str(trial) +','+ curr_cue +','+ curr_task +','+curr_diff+','+ dectype + "," +str(curr_rew)+ ','+ str(curr_thresh) +','+ str(totcorr) +','+ str(totincorr) +','+ str(trialReward) +','+ str(runningTotal)+","+str(curr_success)+ "," +str(mean_trialTime) +"," +str(sd_trialTime)+ ',' + str(catch_response) + ',' + str(catch_corr))
        with open(filename2+'.txt', "a") as f:
            f.write(trial_data+"\n")

 
       
    #break screen with self report
        if (trial==40 or trial==80 or trial==120 or trial==160 or trial==200 or trial==240 or trial==280 or trial==320 or trial==360):
            your_mouse = event.Mouse(visible = True)
            selfreport(block_count)
            your_mouse = event.Mouse(visible = False)
            corr_id = None
            corr_id = np.sum(catch_corr_arr)

            break_pres.setText("Puedes tomar un descanso. \n\nHasta ahora has ganado "+ str (runningTotal) + u" puntos y has identificado "+ str(corr_id) + u" de los "+ str(len(catch_corr_arr))+u"imagenes. "+u" \n\nPresiona la barra espaciadora cuando estés listo para continuar.")
            break_pres.setAutoDraw(True)
            eventTime=mClock.getTime()
            win.flip()
            port.setData(block_count)
            core.wait(.05)
            win.flip()
            port.setData(0)
            
            trial_type="break"
            desc="blockbreak"
            dataline=(str(expInfo['participant'])  +  "," + str(block_count) + "," + str(block_count)+ "," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN"+ "," + str(block_count)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
    
            event_type="resp"
            response=event.waitKeys(keyList='space', timeStamped=mClock)
            eventTime=response[0][1]
            desc="breakText_" + str(runningTotal)
            dataline=(str(expInfo['participant']) + "," + str(block_count)+ "," +event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(response[0][0])+ "," +"NaN" + "," + str(99)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
            
            break_pres.setAutoDraw(False)
            win.flip()
            port.setData(99) #pressed space bar to keep going

        elif(trial==400):#final screen
            your_mouse = event.Mouse(visible = True)
            selfreport(block_count)
            your_mouse = event.Mouse(visible = False)
            corr_id = None
            corr_id = np.sum(catch_corr_arr)
            
            break_pres.setText(u"¡Bien hecho! Has terminado la tarea.\n\n\nAl final ganaste "+ str (runningTotal) + u" puntos y has identificado "+ str(corr_id) + u" de los "+ str(len(catch_corr_arr))+u" imagenes. "+u" \n\nPresiona la barra espaciadora cuando estés listo para continuar.")
            break_pres.setAutoDraw(True)
            eventTime=mClock.getTime()
            win.flip()
            port.setData(block_count)
            core.wait(.05)
            win.flip()
            port.setData(0)
            
            
            trial_type="break"
            desc="blockbreak"
            dataline=(str(expInfo['participant']) + "," + str(block_count)+"," + event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + "NaN"+ "," +"NaN"+ "," + str(block_count)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
    
            event_type="resp"
            response=event.waitKeys(keyList='space', timeStamped=mClock)
            eventTime=response[0][1]
            desc="breakText_" + str(runningTotal)
            dataline=(str(expInfo['participant']) + "," + str(block_count)+ "," +event_type+ "," + trial_type + "," + str(desc.encode('utf8')) + "," +str(eventTime) + "," + str(response[0][0])+ "," +"NaN" + "," + str(99)+ "," +"NaN")
            loglist_all.append(dataline)
            with open(filename3+'.txt', "a") as myfile:
                myfile.write(dataline+"\n")
            
            break_pres.setAutoDraw(False)
            win.flip()
            port.setData(99)
        win.flip()
        port.setData(0)  
    
catch_mean=None    
catch_mean=np.mean(np.array(catch_corr_arr))
final_reward=None
final_reward=runningTotal*catch_mean
thefile = open(filename_catchmean+'.txt', 'w')
thefile.write("rate of correct identification:   " + str(catch_mean) + "\n")
thefile.write("Points earned:   " + str(runningTotal) + "\n")
thefile.write("Final points given:   " + str(final_reward))


    
        
#writing by trial file
thefile = open(filename5+'.txt', 'w')
for item in loglist:
  thefile.write("%s\n" % item)


logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()


