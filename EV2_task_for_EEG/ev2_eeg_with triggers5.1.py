#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on febrer 07, 2022, at 15:15
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import random
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import pyxid2

#pyxid2 es una librería de PsychoPy que funciona con CEDRUS c-pod, el nuevo adaptador del lab
# get a list of all attached XID devices
devices = pyxid2.get_xid_devices()
 
dev = devices[0] # get the first device to use
dev.reset_base_timer()
dev.set_pulse_duration(5) # duration of trigger
 
for bm in range(0, 16):
    mask = 2 ** bm
    print("activate_line bitmask: ", mask)
    #dev.activate_line(lines=[1,3,5,7,9,11,13,15])
    dev.activate_line(bitmask=mask)




# Ensure that relative paths start from the same directory as this script
#_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'EV2_eeg'  # from the Builder filename that created this script
expInfo = {'participant': '', 'handedness':'', 'condition':''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=True, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='v5',
    extraInfo=expInfo, runtimeInfo=None,
    #In the end you don't really need originPath to match the directory
    originPath='C:\\Users\\plope\\OneDrive - Universitat de Barcelona\\PHD\\Studies\\Effort Valuation study 2\\EV2_cond\\ev2_task.py',
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
#port = parallel.ParallelPort(address = u'0xC100') #address depende de si es windows o linux y del ordenador
#aqui esta puesto en Window. 
#port.setData(4) est es lo que envias. reiniciar a zero porque no se suman.
#tiene que ser integer (poner int())

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), 
    #size=(1200, 900),
    fullscr=False, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], #colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')

#win = visual.Window(size=[1920, 1080], fullscr=True,colorSpace='rgb', color=[0,0,0], monitor='testMonitor',)
your_mouse = event.Mouse(visible = False)

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess


SID=str(expInfo['participant'])
cond=int(expInfo['condition'])
hand=str(expInfo['handedness'])


filename=str("by_Trial_data\\EV2_byTrial_" + SID)
with open(filename+'.csv', "a") as f:
    f.write("Subject, Condition, Handedness, Trial, Block, Trial_block, Effort, Probability, CurrDecThresh,CorrChoices,IncorrChoices,MeanDecTime,SDevDecTime,SuccessfulTrial,TrialReward,CumulReward, CatchQuestResp, CatchQuestCorr\n")

filename_sr=str("self_report_data\\sr_data_" + SID)
with open(filename_sr+".csv", "a") as f:
    f.write("Subject, Block, like_hchp_cue, like_hclp_cue, like_lchp_cue, like_lclp_cue, eff_hchp, eff_hclp, eff_lchp, eff_lclp, prob_hchp, prob_hclp, prob_lchp, prob_lclp, fatigue_sr\n")

prac_filename=str("prac_data\\prac_data_" + SID)
with open(prac_filename+".csv", "a") as f:
    f.write("Subject ,Block, Practice_Count, Trial_Type, Trial, Correct, Incorrect, Success\n")

log_filename=str("log_data\\log_data_" + SID)
with open(log_filename+".csv", "a") as f:
    f.write("Subject ,Block, Trial, EventType, TrialType, Desc, EventTime, Response, Correct, Trigger, RT\n")



###################### main experimental variables

#initializing main clock that I will use for whole experiment
mClock = core.Clock()

your_mouse = event.Mouse(visible = False)

##### stimulus variables
numarr=[1,2,3,4,6,7,8,9]
colarr=[("yellow"), ("blue")]


#****** arrays and values necessary for continuous task calibration 
easy_high_thresh=0
easy_low_thresh=0
hard_high_thresh=0
easy_low_thresh=0

easy_thresh_rt=0
hard_thresh_rt=0

easy_cal_arr=[]
hard_cal_arr=[]

#****** arrays for creating stimuli values
block_stim_arr=[]

#***** tracks reward
total_rew=0

###timers just in case
num_startTime=-99
displayTime=-99
trial_startTime=-99

##### codes for log files
block_counter=-99
yes_effort=0  
choice_resp_rt=-99
succ=-99
corr_choices=-99
incorr_choices=-99
meanDecTime=-99
sdDecTime=-99
thresh=-99


easy_cue_like=-99
hard_cue_like=-99

easy_cue_diff=-99
hard_cue_diff=-99

fatigue_sr=-99

export_trial_array=[]
export_sr_array=[]


################################################
#  ~~~~~~~~~~~~ GLOBAL FUNCTIONS ~~~~~~~~~~~~  #
################################################

#******* cue_easy_stim() **********
# This function generates a random array of numbers
# and array of one color for the easy cue switching task
# note that this array is fixed to 10, but ideally 
# this will be calibrated later on
# We also may make this a fixed array later on once we decide the trial stucture
def cue_easy_stim(color):
    addnum=[0]
    randnumlist=[0]*30
    shuffle(numarr)
    newnumarr=numarr
    while len(newnumarr)<len(randnumlist):
        n=len(randnumlist)-len(newnumarr)
        if (n>=8):
            shuffle(numarr)
            addnum=numarr
        else:
            shuffle(numarr)
            addnum=numarr[0:n]
        if (addnum[0]!=newnumarr[len(newnumarr)-1]):
            newnumarr=newnumarr+addnum
        else:
            pass
    randnumlist=newnumarr
    randcollist=[color]*len(randnumlist)
    return(randnumlist,randcollist)
    
   
#******* cue_hard_stim() **********
#This function generates a random array of numbers
#And a list of alternating yellow and blue for the hard task
def cue_hard_stim():
    addnum=[0]
    randnumlist=[0]*30
    shuffle(numarr)
    newnumarr=numarr
    while len(newnumarr)<len(randnumlist):
        n=len(randnumlist)-len(newnumarr)
        if (n>=8):
            shuffle(numarr)
            addnum=numarr
        else:
            shuffle(numarr)
            addnum=numarr[0:n]
            
        if (addnum[0]!=newnumarr[len(newnumarr)-1]):
            newnumarr=newnumarr+addnum
        else:
            pass
    randnumlist=newnumarr
    
    shuffle(colarr)
    randcollist = [None]*len(randnumlist)

    evens=range(0, len(randnumlist), 2)
    odds=range(1, len(randnumlist), 2)
    for i in evens:
        randcollist[i] = colarr[0]
    for i in odds:
        randcollist[i] = colarr[1]
    return(randnumlist,randcollist)




#******* cue_task_resp(number, color,resp, trialtype, last_trial, displayTime, cutoff) **********
#This function reads the response of for a cued task switching task,
# and scores the response based on a set of rules
# For blue numbers: if even, click left; if odd, click right
# For yellow numbers: if <5, click left; if >5 click right
# if you didn't respond and the number was presented for less than your average response time, then it doesn't count as incorrect
def cue_task_resp(number, color,resp, trialtype, last_trial, displayTime, cutoff=3):
    if (resp=="right"):
        if (color=='blue') and (number%2==0): #if response was blue and number was even
            corr, incorr, noresp=1,0,0
        elif (color=='yellow') and (number>5): #if response was a right button and number greater than 5
            corr, incorr, noresp=1,0,0
        else:
            corr, incorr, noresp=0,1,0
    elif (resp=="left"):
        if (color=='blue')  and (number%2!=0): #if color was blue and number is odd
            corr, incorr, noresp=1,0,0
        elif (color=='yellow') and (number<5): #if color was yellow  and number less than 5
            corr, incorr, noresp=1,0,0
        else:
            corr, incorr, noresp=0,1,0
    else: #if no response and its the last trial, assess how long that number was displayed
        if (last_trial==1 and displayTime<cutoff):
            corr, incorr, noresp=0,0,1
        else:
            corr, incorr, noresp=0,1,1
    return(corr, incorr, noresp, displayTime)




#******* trainingCal(results_array) **********
#trainingCal(totcorr, totincorr, trial_type, mean_trialTime, sd_trialTime)
#trainingCal takes results of a practice trial, decides if trial was correctly completed
# and adds the trial information to the practice array for the specific trial type
def trainingCal(tot_corr, tot_incorr, trial_type, mean_rt, sd_rt):
    global easy_cal_arr
    global hard_cal_arr
    
    if tot_corr>0:
        perc=(tot_corr/(tot_corr+tot_incorr))*100
    else:
        perc=0
    
    total_resp=tot_corr+tot_incorr

    if (tot_incorr>1 or perc<75 or total_resp<3): 
        curr_success=0
    else:
        curr_success=1

    if trial_type=="easy":
        easy_cal_arr.append((curr_success, tot_corr, mean_rt, trial_type))
        curr_arr=easy_cal_arr
    elif trial_type=="hard":
        hard_cal_arr.append((curr_success, tot_corr, mean_rt, trial_type))
        curr_arr=hard_cal_arr
    
    print("easy cal arr updated in trainingCal:     " + str(easy_cal_arr))
    print("hard cal arr updated in trainingCal:      " + str(hard_cal_arr))
    
    return(curr_success, curr_arr, trial_type)




########## FUNCTIONS FOR CREATING STIMULI  ########## 

if (cond==1):
    #circles are easy
    hchp_stim='stim\highprob_square.png'
    hclp_stim='stim\lowprob_square.png'
    lchp_stim='stim\highprob_circ.png'
    lclp_stim='stim\lowprob_circ.png'
elif (cond==2):
     #circles are hard
    lchp_stim='stim\highprob_square.png'
    lclp_stim='stim\lowprob_square.png'
    hchp_stim='stim\highprob_circ.png'
    hclp_stim='stim\lowprob_circ.png'
    
hchp=(hchp_stim, 'hard', 'high', 'effort', 'no_quest')
hclp=(hclp_stim, 'hard', 'low', 'effort', 'no_quest')
lchp=(lchp_stim, 'easy', 'high', 'effort', 'no_quest')
lclp=(lclp_stim, 'easy', 'low', 'effort', 'no_quest')

hchp_noeff=(hchp_stim, 'hard', 'high', 'no_effort', 'no_quest')
hclp_noeff=(hclp_stim, 'hard', 'low', 'no_effort', 'no_quest')
lchp_noeff=(lchp_stim, 'easy', 'high', 'no_effort', 'no_quest')
lclp_noeff=(lclp_stim, 'easy', 'low', 'no_effort', 'no_quest')

hchp_noeff_quest=(hchp_stim, 'hard', 'high', 'no_effort', 'quest')
hclp_noeff_quest=(hclp_stim, 'hard', 'low', 'no_effort', 'quest')
lchp_noeff_quest=(lchp_stim, 'easy', 'high', 'no_effort', 'quest')
lclp_noeff_quest=(lclp_stim, 'easy', 'low', 'no_effort', 'quest')

#trial_types=[hchp, hclp, lchp, lclp, hchp_noeff, hclp_noeff, lchp_noeff, lclp_noeff]
#no_eff_trials=[hchp_noeff, hclp_noeff, lchp_noeff, lclp_noeff]
#block_arr=[]
#block_counter=-99
#
#for i in range(0,9):
#    block_trials=[]
#    select=0
#    for k in range(0,4):
#        for t in trial_types: 
#            block_trials.append(trial_types)
#    while select==0:
#        x=np.random.choice(range(len(block_trials)))
#        item=block_trials[x]
#        item=list(item)
#        if item[3]=="no_effort":
#            item_quest=item
#            item_quest[4]='quest'
#            item_quest=tuple(item_quest)
#            block_trials[x]=item_quest
#            select=1
#    shuffle(block_trials)
#    block_arr.append(block_trials)
#
#print(block_arr)


#blocks
block_1=[lchp_noeff, lclp, hchp_noeff, hchp, hclp_noeff, lchp, hclp, lclp_noeff, 
        lchp_noeff_quest, hclp, hclp_noeff, lclp_noeff, lchp, hchp, hchp_noeff, lclp,
        hclp_noeff, hchp, lclp_noeff, lclp, hclp, lchp_noeff, hchp_noeff, lchp,
        lclp_noeff, hchp_noeff_quest, lclp, lchp_noeff, lchp, hchp, hclp_noeff, hclp,
        hclp_noeff, lclp_noeff, lclp, hchp_noeff, hchp, lchp_noeff, lchp, hclp]
        
block_2=[lchp_noeff, lclp, lchp, hchp, hchp_noeff, hclp, lclp_noeff_quest, hclp_noeff,
        hclp, lclp, hchp_noeff, lclp_noeff,  hchp, hclp_noeff,lchp_noeff, lchp,
        hchp, lchp_noeff, lclp_noeff, lclp, hclp_noeff_quest, hchp_noeff, hclp, lchp,
        hchp, hclp_noeff, hclp, lchp_noeff, lchp, lclp_noeff, hchp_noeff, lclp,
        hclp_noeff, hchp_noeff, lclp, lchp, lchp_noeff, hclp, lclp_noeff, hchp]


block_3=[lclp_noeff, hchp_noeff,lclp, hclp_noeff, hchp, lchp, hclp, lchp_noeff,
        hclp, lclp, hchp_noeff_quest, hchp, hclp_noeff, lclp_noeff, lchp, lchp_noeff,
        hchp_noeff, lchp, hclp, hclp_noeff, hchp, lchp_noeff, lclp, lclp_noeff, 
        hclp, hclp_noeff_quest, lclp_noeff, lclp, lchp_noeff, lchp, hchp, hchp_noeff, 
        lchp, hchp_noeff, hchp, hclp_noeff, hclp, lclp, lclp_noeff, lchp_noeff]
        
block_4=[hchp, hchp_noeff, hclp, hclp_noeff, lclp, lchp, lclp_noeff_quest, lchp_noeff,
        hclp, hchp_noeff, lchp, hclp_noeff, lchp_noeff, lclp, lclp_noeff, hchp,
        lchp, hclp, lchp_noeff_quest, hchp_noeff, hchp, lclp_noeff, lclp, hclp_noeff,
        hchp, lclp, hclp_noeff, hclp, lchp, hchp_noeff, lclp_noeff, lchp_noeff,
        hclp, lclp_noeff, lclp, hclp_noeff, lchp_noeff, hchp, lchp, hchp_noeff]

block_5=[hchp, hchp_noeff, hclp, lchp_noeff, lclp_noeff, lclp, hclp_noeff, lchp,
        lchp_noeff_quest, lclp, hchp, hclp_noeff, hclp, lchp, hchp_noeff, lclp_noeff,
        lclp, hchp, hchp_noeff, lclp_noeff, lchp, lchp_noeff, hclp, hclp_noeff,
        hclp_noeff_quest, lclp_noeff, hchp, lchp_noeff, hchp_noeff, lchp, hclp, lclp,
        hchp, hclp_noeff, lchp, lclp_noeff, lchp_noeff, hclp, lclp, hchp_noeff]
        
block_6=[lclp, hchp_noeff_quest, hchp, lchp, lchp_noeff, hclp, lclp_noeff, hclp_noeff,
        lclp, lchp_noeff, lchp, lclp_noeff, hclp, hchp_noeff, hclp_noeff, hchp, 
        lclp, lclp_noeff_quest, hclp, lchp_noeff, hchp, hchp_noeff, lchp, hclp_noeff,
        hclp, lclp, lchp_noeff, hchp, hclp_noeff, lclp_noeff, lchp, hchp_noeff, 
        hchp_noeff, hchp, lchp, hclp_noeff, lchp_noeff, hclp, lclp_noeff, lclp]

block_7=[lchp, lchp_noeff, hchp, hclp_noeff, lclp, lclp_noeff, hchp_noeff, hclp,
        lchp_noeff, hclp, hchp_noeff_quest, lclp, hchp, lchp, lclp_noeff, hclp_noeff, 
        lclp, hchp_noeff, lchp_noeff, hchp, lclp_noeff, lchp, hclp_noeff, hclp, 
        lchp_noeff_quest, lclp, lchp, hclp_noeff, hclp, lclp_noeff, hchp_noeff, hchp, 
        lclp_noeff, hclp, lchp_noeff, lchp, hchp_noeff, hchp, hclp_noeff, lclp]
        
block_8=[hchp, lclp_noeff_quest, lclp, hclp_noeff, hchp_noeff, hclp, lchp_noeff, lchp, 
        lclp_noeff, hchp_noeff, lchp, hclp_noeff, hclp, lchp_noeff, hchp, lclp,
        hclp_noeff_quest, lchp, hchp_noeff, hchp, lclp, lclp_noeff, hclp, lchp_noeff,
        lclp_noeff, lchp, lclp, lchp_noeff, hclp, hchp_noeff, hclp_noeff, hchp,
        hclp_noeff, hclp, hchp_noeff, lclp, lchp_noeff, lclp_noeff, lchp, hchp]

block_9=[lclp_noeff, lchp_noeff, lchp, lclp, hchp, hclp_noeff, hclp, hchp_noeff,
        hchp, hclp_noeff_quest, lclp, hchp_noeff, lchp_noeff, hclp, lclp_noeff, lchp,
        lchp, hclp_noeff, lclp, hchp, lchp_noeff, hchp_noeff, hclp, lclp_noeff, 
        lchp, lclp_noeff_quest, hclp, lchp_noeff, hchp_noeff, hclp_noeff, hchp, lclp,
        lchp_noeff, lclp, lclp_noeff, hclp, hchp_noeff, hclp_noeff, lchp, hchp]
        
block_10=[lchp, lclp, hclp_noeff, hchp, hchp_noeff_quest, lclp_noeff, lchp_noeff, hclp,
        hclp_noeff, lclp, lchp, lchp_noeff, hclp, lclp_noeff, hchp, hchp_noeff,
        lclp, lchp_noeff_quest, lclp_noeff, hchp, lchp, hclp_noeff, hchp_noeff, hclp,
        lchp_noeff, hchp, lclp_noeff, lchp, hclp, hchp_noeff, lclp, hclp_noeff, 
        lclp_noeff, hclp, lchp_noeff, hchp, lclp, hclp_noeff, lchp, hchp_noeff]
block_arr=[block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9, block_10]
shuffle(block_arr)

#******* cue_task_pres(randnumlist, randcollist) **********
#This function presents the stimuli for both hard and easy cue switching tasks,
# captures the response, and keeps track of performance.
# It returns the total number of correct, incorrect, no responses, x (total number of numbers presented),
# mean time to make a decision and sd time to make a decision for a trial.
def cue_task_pres(randnumlist, randcollist, typeoftrial, trig_base, cutoff=3.0):
    trial_log_data_arr=[]
    RT=0
    totcorr, totincorr, totnoresp, x=0,0,0,0
    kp, kp_out, corr_out=None, None, None
    lastnum=0
    time_arr=[]
    mean_trialTime, sd_trialTime =0,0
    
    maintimer=core.Clock()
    maintimer.add(8) #8 seconds for the trial
    
    secondTimer=core.Clock()
    
    key_press=event.getKeys(keyList=("left", "right"),timeStamped=mClock)
    
    while (maintimer.getTime()<0):
        for n in range(len(randnumlist)):
            if (maintimer.getTime()>0):
                break
            else:
                num_color=randcollist[n]
                num_text=randnumlist[n]
                num_pres.setText(num_text)
                num_pres.setColor(num_color)
                if num_color=="yellow":
                    num_trig=trig_base+num_text
                else:
                    num_trig=trig_base+10+num_text
                dev.activate_line(bitmask=num_trig)
                num_pres.setAutoDraw(True)
                win.flip()
                secondTimer=core.Clock()
                startTrial= secondTimer.getTime()
                win.flip()
                
                eventTime=mClock.getTime()
                event_type="pres"
                desc=str(num_color) + "_" + str(num_text)
                #add to log_data_arr
                #log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, resp, correct, trial_trig, rt]
                log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, "NaN", "NaN", num_trig, "NaN"]
                trial_log_data_arr.append(log_file_line)
                
            
                key_press=event.getKeys(keyList=("left", "right"), timeStamped=secondTimer)
                ### adding everything until next comment
                if key_press!=[]:
                    dev.activate_line(bitmask=200)
                    print('200')
                    pass
                else:
                     ### 
                    while (key_press==[]):
                        key_press=event.getKeys(keyList=("left", "right"), timeStamped=secondTimer)
                        eventTime=mClock.getTime() 
                        if (maintimer.getTime()>0):
                            lastnum=1
                            break
                        ### adding everything until next comment
                        if key_press!=[]:
                            dev.activate_line(bitmask=200)
                            break
                        ### 
            presTime=secondTimer.getTime()-startTrial
            
            num_pres.setAutoDraw(False)
            win.flip()

            #outputting response 
            event_type="resp"
            if (key_press!=[]):
                kp, kp_out=key_press[0][0],key_press[0][0]
                RT=key_press[0][1]-startTrial
            else:
                kp, kp_out=[], "No press"
                eventTime="No press"
                RT="NaN"
                
            
            corr, incorr, noresp, displayTime=cue_task_resp(num_text,num_color, kp, typeoftrial, lastnum, presTime) #determining if response was correct, 3 second cut off for practice 
            totcorr=totcorr+corr
            totincorr=totincorr+incorr
            totnoresp=totnoresp+noresp
            x=x+1
            
            event_type="resp"
            desc=kp_out
            #add to log_data_arr
            #log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, resp, correct, trial_trig, rt]
            log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, kp_out, corr, 200, RT]
            trial_log_data_arr.append(log_file_line)
            
            #correct of -1 means that they didn't have time to respond
            if (kp==[] and incorr==0):
                corr_out=-1
            elif (kp==[] and incorr==1):
                corr_out=0
            elif (kp!=[]):
                corr_out=corr
                time_arr.append(RT)
            

                
    num_pres.setAutoDraw(False)
    win.flip()
    #port.setData(0)
    
    time_arr=np.array(time_arr)
    mean_trialTime =np.mean(time_arr)
    sd_trialTime=np.std(time_arr)
    
    #write to log file for all events
    logfile = open(log_filename+'.csv', "a")
    for item in trial_log_data_arr:
        log_dataline = [str(element) for element in item]
        log_dataline_csv= ",".join(log_dataline)
        logfile.write(log_dataline_csv + "\n")

    return(totcorr, totincorr, totnoresp,x, mean_trialTime, sd_trialTime)
    


######## Calibration functions

#******* threshCal(curr_arr) **********
#threshCal is ONLY FOR THE INITIAL CALIBRATION
# it takes curr_arr, which is an array of tuples with
# (current_success, total number of responses, mean resp time, trial_type) and 
# calculates the new response threshold based off of that
def threshCal(curr_arr, effort_type, prac=False):
    
    if prac==True:
        print("PRAC IS TRUE!!!")
        corr_res_arr=[tot_resp for (curr_succ,tot_resp, mean_rt, trial_type) in curr_arr if curr_succ == 1]
        rt_arr=[mean_rt for (curr_succ,tot_resp, mean_rt, trial_type) in curr_arr if curr_succ == 1]
    else:
        print("NOT PRAC!!!")
        corr_res_arr=[tot_resp for (curr_succ,tot_resp, rt,trial_type) in curr_arr]
        rt_arr=[rt for (curr_succ,tot_resp, rt,trial_type) in curr_arr]
        
    last_five=corr_res_arr[-5:] 
    last_five_rt=rt_arr[-5:]
    
    sorted_last_five = [] 
    while last_five:
        minimum = last_five[0]  # arbitrary number in list 
        for x in last_five: 
            if x < minimum:
                minimum = x
        sorted_last_five.append(minimum)
        last_five.remove(minimum)    
    print("SORTED LAST 5:     " +str(sorted_last_five))
    new_low_thresh=sorted_last_five[0] #so this is the 20% percentile, so in theory you should win 80% of trials if we set it to this
    #new_high_thresh=sorted_last_five[2] #so this is the 60% percentile, so in theory you should win 40% of trials if we set it to this
    new_high_thresh=sorted_last_five[3] #I think we need to pick them on two extremes because number of responses doesn't vary that much once people get good
    print("new_low_thresh:     " +str(new_low_thresh))
    print("new_high_thresh:     " +str(new_high_thresh))
    
    if new_high_thresh==new_low_thresh:
        new_high_thresh+=1
    else:
        pass
    
    mean_rt=sum(last_five_rt)/len(last_five_rt)
    var_rt = sum((x - mean_rt) ** 2 for x in last_five_rt) / len(last_five_rt)
    std_rt= var_rt**0.5
    new_thresh_rt=mean_rt+(2*std_rt)

#    if effort_type=="easy":
#        easy_high_thresh=new_high_thresh
#        easy_low_thresh=new_low_thresh
#        easy_thresh_rt=new_thresh_rt
#        print("easy high thresh:    " + str(easy_high_thresh))
#    elif effort_type=="hard":
#        hard_high_thresh=new_high_thresh
#        hard_low_thresh=new_low_thresh
#        hard_thresh_rt=new_thresh_rt
#        print("hard high thresh:    " + str(hard_high_thresh))

    return(new_low_thresh, new_high_thresh, new_thresh_rt) #I don't think there is any need to return this yet

   
# ************** taskCal() ********************
#This function takes the follow variables:
#trial_results : array with the following information about this trial performance[totcorr, totincorr, totnoresp,x, mean_trialTime, sd_trialTime, trial_type]
#trial_info : a list that has info about the trial, regardless of choice: 0)indiff point, 1) effort type, 2) reward for HE option, 3) proximity parameter, 4) reward for no effort, 5) effort block, 6) color (if easy trial)
#ch_resp: ne vs he (don't think I actually use this in the end
#curr_thresh: threshold of the current trial type
#it updates the calibration arrays, calls the calibration function, and 
#returns success (1=trial was successful or 0=unsuccessful) and amount to be rewarded for trial.
def taskCal(trial_results, trial_info, ch_resp, curr_array, curr_thresh):
    global easy_cal_arr
    global easy_high_thresh
    global easy_low_thresh
    global easy_thresh_rt
    global hard_cal_arr
    global hard_high_thresh
    global hard_low_thresh
    global hard_thresh_rt
    
    success=0
    curr_rt_thresh=0
    task_performed= trial_info[1]

    total_corr=trial_results[0]
    total_incorr=trial_results[1]
    mean_rt=trial_results[4]

    #grading it
    print("taskCal curr_thresh:     " + str(curr_thresh))
    if total_corr>=curr_thresh and total_incorr<2:
        success=1
    else:
        success=0

    summary_of_trial=(success,  total_corr, mean_rt, task_performed)
    curr_array.append(summary_of_trial)
    #curr_thresh, curr_rt_thresh=threshCal2(curr_array) #keeping the threshold calibration for no effort just in case
    new_low_thresh, new_high_thresh, new_thresh_rt=threshCal(curr_array, task_performed) 
    
    if task_performed=="easy":
        easy_cal_arr=curr_array
        easy_high_thresh=new_high_thresh
        easy_low_thresh=new_low_thresh
        easy_thresh_rt=new_thresh_rt
        print("easy high thresh from taskCal:    " + str(easy_high_thresh))
        print("easy cal array from taskCal:  " + str(easy_cal_arr))
    elif task_performed=="hard":
        hard_cal_arr=curr_array
        hard_high_thresh=new_high_thresh
        hard_low_thresh=new_low_thresh
        hard_thresh_rt=new_thresh_rt
        print("hard high thresh from taskCal:    " + str(hard_high_thresh))
        print("hard cal array from taskCal:  " + str(hard_cal_arr))
    
    if success==1:
        reward_amount=15 #NEED TO CHANGE THIS
    else:
        reward_amount=0
    
    return(success, reward_amount)



# ************** SELF REPORT SCALE FUNCTION *************#
# only takes the block number for data storage. Everything else is built in


def selfreport(block_x):
    log_data_arr=[]
    sr_text=[]
    sr_text.append(u"¿Cuanto te gusta este imagen?")
    sr_text.append(u"¿Cuanto te gusta este imagen?")
    sr_text.append(u"¿Cuanto te gusta este imagen?")
    sr_text.append(u"¿Cuanto te gusta este imagen?")
    
    sr_text.append(u"¿Cuanto esfuerzo te requiere esta tarea?") 
    sr_text.append(u"¿Cuanto esfuerzo te requiere esta tarea?")
    sr_text.append(u"¿Cuanto esfuerzo te requiere esta tarea?")
    sr_text.append(u"¿Cuanto esfuerzo te requiere esta tarea?")
    
    sr_text.append(u"¿Que probabilidad tienes de hacer bien esta tarea?")
    sr_text.append(u"¿Que probabilidad tienes de hacer bien esta tarea?")
    sr_text.append(u"¿Que probabilidad tienes de hacer bien esta tarea?")
    sr_text.append(u"¿Que probabilidad tienes de hacer bien esta tarea?")
    
    sr_text.append(u"¿Estas cansad@?")
    scale_cues=[hchp_stim, hclp_stim, lchp_stim, lclp_stim]*3
    
    fatigue=None
    like_hchp_cue, like_hclp_cue, like_lchp_cue, like_lclp_cue=None, None, None, None
    eff_hchp, eff_hclp, eff_lchp, eff_lclp=None, None, None, None
    prob_hchp, prob_hclp, prob_lchp, prob_lclp=None, None, None, None
    resp=None
    your_mouse = event.Mouse(visible = True)
    sr_results=[SID, block_x]
    for i in range(0,len(sr_text)):
        trial_type=str(sr_text[i])+"_"+str(block_x)
        I.setSize(0.07)
        if i>11:
            I.setText(sr_text[i])
            I.setPos([0,0])
            I.setAutoDraw(True)
        else:
            I.setPos([0,.2])
            I.setText(sr_text[i])
            I.setAutoDraw(True)
            I_image.setImage(scale_cues[i])
            I_image.setSize([.15,.15])
            I_image.setPos([0,.05])
            I_image.setAutoDraw(True)

        win.flip()
        if block_counter==-99:
            trig=50
        else:
            trig=50+block_counter
        dev.activate_line(bitmask=trig)
        eventTime=mClock.getTime()
        event_type="sr_quest"
        desc=sr_text[i][0:6]
        log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, "NaN", "NaN", trig, "NaN"]
        log_data_arr.append(log_file_line)
        
        
        if i in range(0, 4):
            while cue_rating.getRating()==None:
                cue_rating.draw()
                win.flip()
            sr_results.append(cue_rating.getRating())
        elif i in range(4,8):
            while eff_rating.getRating()==None:
                eff_rating.draw()
                win.flip()
            sr_results.append(eff_rating.getRating())
        elif i in range(8,12):
            while prob_rating.getRating()==None:
                prob_rating.draw()
                win.flip()
            sr_results.append(prob_rating.getRating())
        elif i==12:
            while fat_rating.getRating()==None:
                fat_rating.draw()
                win.flip()
            sr_results.append(fat_rating.getRating())
#        dev.activate_line(bitmask=200)
        eventTime=mClock.getTime()
        event_type="sr_resp"
        desc=sr_text[i][0:6]
        log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, "NaN", "NaN", 200, "NaN"]
        log_data_arr.append(log_file_line)
        
        fat_rating.reset()
        cue_rating.reset()
        eff_rating.reset()
        prob_rating.reset()
        I.setAutoDraw(False)
        I_image.setAutoDraw(False)
        win.flip()  
        
        print('SR DATA:     ' + str(sr_results))
    your_mouse = event.Mouse(visible = False)
    sr_dataline = [str(element) for element in sr_results]
    sr_dataline_csv= ",".join(sr_dataline)
    print('SR DATA line:     ' + str(sr_dataline_csv))
    with open(filename_sr+'.csv', "a") as myfile:
        myfile.write(sr_dataline_csv+"\n")



# ******************** INITIALIZE VISUAL ELEMENTS FOR INSTRUCTIONS/ PRACTICE/ TRIALS **********************************

#************* SCALES ************

cue_rating= visual.Slider(win,
             ticks=(0,1,2,3,4,5,6,7,8,9,10),
             labels=('No me gusta','Indiferente', 'Me gusta mucho'),
             granularity=1, size=(.75,.05), pos=(0,-.2),
             color='white', labelHeight = .03)

fat_rating= visual.Slider(win,
             ticks=(0,1,2,3,4,5,6,7,8,9,10),
             labels=('No cansado/a', 'Muy cansado/a'),
             granularity=1, size=(.75,.05), pos=(0,-.2),
             color='white', labelHeight = .03)
             
eff_rating= visual.Slider(win,
             ticks=(0,1,2,3,4,5,6,7,8,9,10),
             labels=(u'Nada de esfuerzo', u'Esfuerzo extremo'),
             granularity=1, size=(.75,.05), pos=(0,-.2),
             color='white', labelHeight = .03)
                
prob_rating= visual.Slider(win,
             ticks=(0,1,2,3,4,5,6,7,8,9,10),
             labels=('0%', '20%', '40%', '60%', '80%', '100%'),
             granularity=1, size=(.75,.05), pos=(0,-.2),
             color='white', labelHeight = .03)
             
             
#instruction slides
I = visual.TextStim(win=win, name='I',
    #text='El objetivo de esta tarea es ayudar Paula',
    font='Arial',
    alignHoriz='center',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

I_image= visual.ImageStim(
    win=win, name='I_image',
    image='stim/circle_cues_inst.png', mask=None,
    pos=(0, -.12), size=(.78,.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0);
    

        
#for cue and number presentation
cue_pres = visual.ImageStim(
    win=win, name='cues',
    image='stim/lowprob_square.png', mask=None,
    pos=(0, 0), size=(.17, .17),
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
    pos=(0, -.12), height=0.25, wrapWidth=None, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
                           
num_pres = visual.TextStim(win=win, name='singleNum',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


fb_pres = visual.ImageStim(win=win,  
    image='stim/white_x.png', mask=None,
    pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0);
    
corrfb_pres = visual.ImageStim(win=win,  
    image='stim/white_check.png', mask=None,
    pos=(0, 0), size=(0.2, 0.2),
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
    
#slide for question trials
quest_slide = visual.TextStim(win=win, name='quest',
    font='Arial',
    pos=(0,0), height=0.03, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


quest_image= visual.ImageStim(
    win=win, name='I_image',
    image='stim/circle_cues_inst.png', mask=None,
    pos=(0, -.12), size=(.78,.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0);





#######################################################################
# STARTING EXPERIMENT
inst_text=[]
#0
inst_text.append(u'¡Bienvenido al experimento!\n\nEste experimento tiene dos fases:\n\nEn la primera fase, aprenderás y practicarás unos juegos de números. \n\nEn la segunda fase harás los jueguitos de números para conseguir puntos. El objetivo de la segunda fase es conseguir tantos puntos como sea posible porque al final te pagamos a base de cuantos puntos acumulaste en esta fase.\n\nPulse la barra espaciadora para pasar a las indicaciones de la primera tarea.')
#1
inst_text.append(u'Nuestro primer objetivo será practicar el juego de números. \n\nLa tarea consiste en un pequeño juego en el que durante 8 segundos se presentarán una serie de números que pueden ser de dos colores. \n\nPulse la barra espaciadora para pasar al próximo paso.')
#Instruct 2 - task specific
inst_text.append(u'Cuando el número es amarillo, tienes que decidir si el número es mayor o menor que 5. Presiona la flecha izquierda del teclado si el número es MENOR DE 5 y la flecha derecha si el número es MAYOR QUE 5. \n\nEn la tarea real, solo tendrás 8 segundos para contestar, pero en esta práctica, no hay límite de tiempo. \n\nPulse la barra espaciadora para practicar el juego  de un solo color sin la restricción de tiempo de ocho segundos.')
#Instruct 3 – hard task
inst_text.append(u'En el otro juego, el color de los números se alternará.\n\nEn el juego de dos colores, también habrá números de color azul. Si el número es azul, tendrás que decidir si el número es impar o par. Presiona la flecha izquierda del teclado si el número es IMPAR y la flecha derecha si el número es PAR. Las reglas para los números amarillos siguen igual que antes.\n\nPulse la barra espaciadora para ver un ejemplo del juego de dos colores sin la restricción de tiempo de 8 segundos.')
#Instruct 4
inst_text.append(u'En la segunda fase, solo ganarás los 15 puntos si completas con éxito el juego de números, así que es muy importante que practiquemos como hacer el juego antes de empezar el resto del experimento.\n\nSi no tomas una cantidad razonable de decisiones o si cometes demasiados errores dentro del límite de tiempo de 8 segundos, no ganarás los 15 puntos. Si, por lo contrario, lo haces bien, ganarás la cantidad indicada.\n\nPulsa la barra espaciadora para continuar.')
#Instruct 5
if cond==1:
    inst_text.append(u'Ahora comenzarémos con la primera fase.\n\nAntes de empezar cada ensayo, verás un imagen que indica que juego te tocará hacer. Un círculo indicará que harás el jueguito de un color y un cuadrado indicará que te toca el juego de dos colores.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPulsa la barra espaciadora para continuar.')
else:
    inst_text.append(u'Ahora comenzarémos con la primera fase.\n\nAntes de empezar cada ensayo, verás un imagen que indica que juego te tocará hacer. Un cuadrado indicará que harás el jueguito de un color y un círculo indicará que te toca el juego de dos colores.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPulsa la barra espaciadora para continuar.')
#Instruct 6
inst_text.append(u'Tendrás 8 segundos para completar cada tipo de juego con éxito. \n\nTendrás que completar con éxito al menos 15 ensayos antes de que podamos comenzar la segunda fase.\n\nPulsa la barra espaciadora para practicar los juegos.')
#begin calibration/practice

#first round of instructions, up until the first task
for i in range(0,len(inst_text)):
    dev.activate_line(bitmask=7) #for every instruction
    num_array,color_array=None, None
    
    I.setText(inst_text[i])
    I.setPos([0,0])
    if i==5:
        if cond==1:
            I_image.setImage("stim\inst_cond1.png") #NEED TO CHANGE THIS
        else:
            I_image.setImage("stim\inst_cond2.png")
        I.setAutoDraw(True)
        I_image.setAutoDraw(True)
        win.flip()
    else: 
        I.setAutoDraw(True)
        win.flip()
    response=event.waitKeys(keyList='space', timeStamped=mClock)
    dev.activate_line(bitmask=200)
    #get the number and colors for each practice type
    if (i==2):
        I.setText("Izquierda si <5                      Derecha si >5")
        cue_ex_arr=cue_easy_stim("yellow")
        I.setPos([0,.2])
        num_array=cue_ex_arr[0]
        color_array=cue_ex_arr[1]
                          
    elif (i==3):
        I.setPos([0,.2])
        I.setHeight(.03)
        I.setText("Izquierda si IMPAR o <5                     Derecha si PAR o >5")
        
        cue_ex_arr=cue_hard_stim()
        num_array=cue_ex_arr[0]
        color_array=cue_ex_arr[1]
    else:
        pass
    
    #now actually draw
    if (i==2 or  i==3 ):
        for k in range(0,8):
            num_pres.setColor(color_array[k])
            num_pres.setText(num_array[k])
            num_pres.setAutoDraw(True)
            I.setAutoDraw(True)
            win.flip()
            response=event.waitKeys(keyList=['left', 'right'], timeStamped=mClock)
            dev.activate_line(bitmask=200)
    
    I.setHeight(.03)
    num_pres.setAutoDraw(False)
    I_image.setAutoDraw(False)
    I.setAutoDraw(False)
    win.flip()

I.setPos([0,0])
I.setHeight(.03)



###########################################
# PRACTICE / INITIAL CALIBRATION LOOP


cal_done=0
prac_count=0 #overall counter
practice_effort_list=[]
practice_effort_list=["easy", "hard"]
easy_prac_i=0
hard_prac_i=0
practice_trial_count=0
trial_result_arr=[(0,0,0,"none")]

trial_counter=1
block_counter=-99

#fc_isi1=[2, 2.1, 2.2, 2.3, 2.4, 2.5] #used after cue and before effort
#fc_isi1=[1.8, 1.9, 2.0, 2.1, 2.2] #used after cue and before effort -- have now decided to get rid of cross before effort and just change to a 2 second continuous cue
#fc_isi2=[2, 2.1, 2.2, 2.3, 2.4, 2.5] #used after effort and before feedback --used to be [.3, .4, .5, .6, .7, .8] and then [.8, .9, 1.0, 1.1, 1.2, 1.3] in 9.2
fc_isi2=[1, 1.1, 1.2, 1.3, 1.4, 1.5] #used after effort and before feedback -
fc_iti=[2, 2.1, 2.2, 2.3, 2.4, 2.5] #used after feedback and before a new trial -- used to be [.5, .6, .7, .8, .9, 1]

easy_stim=[lchp_stim, lclp_stim]
hard_stim=[hchp_stim,hclp_stim]

while cal_done==0:
    log_data_arr=[]
    prac_count+=1
    shuffle(practice_effort_list)
    trial_type=practice_effort_list[0]
    num_count=0
    
    
    if trial_type=="easy":
        stim=cue_easy_stim("yellow")
        num_array=stim[0]
        color_array=stim[1]
        shuffle(easy_stim)
        cue_image=easy_stim[0]
        num=num_array[num_count]
        easy_prac_i+=1
        practice_trial_count=easy_prac_i    
    elif trial_type=="hard":
        stim=cue_hard_stim()
        num_array=stim[0]
        color_array=stim[1]
        shuffle(hard_stim)
        cue_image=hard_stim[0]
        num=num_array[num_count]
        hard_prac_i+=1
        practice_trial_count=hard_prac_i
     
     
    #ok now starting trial - fixation cross
    fix_pres.setAutoDraw(True)
    win.flip()
    core.wait(1)
    eventTime=mClock.getTime()
    event_type="pres"
    desc= "iti_fix_prac"
    core.wait(fc_iti[0])
    fix_pres.setAutoDraw(False)
    win.flip()
    dev.activate_line(bitmask=8)

    log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, "NaN", "NaN", 8, "NaN"]
    log_data_arr.append(log_file_line)
        
    fix_pres.setAutoDraw(False)
    win.flip()
    
    # add effort cue
    cue_pres.setImage(cue_image)
    cue_pres.setAutoDraw(True)
    win.flip()
    #core.wait(1)
    core.wait(2)
    cue_pres.setAutoDraw(False)
    win.flip()

    totcorr, totincorr, totnoresp,x, mean_trialTime, sd_trialTime= cue_task_pres(num_array, color_array, trial_type,80)
    success,curr_cal_arr,trial_type=trainingCal(totcorr, totincorr, trial_type, mean_trialTime, sd_trialTime)
    
    #send to initial calibration if have at least 15 correct
    so_far_list=[a_tuple[0] for a_tuple in curr_cal_arr]
    so_far=sum(so_far_list) 
    if so_far>=15: #change to 15 later
        prac=True
        new_low_thresh, new_high_thresh, new_thresh_rt=threshCal(curr_cal_arr, trial_type, prac) 
        if trial_type=="easy":
            easy_high_thresh=new_high_thresh
            easy_low_thresh=new_low_thresh
            easy_thresh_rt=new_thresh_rt
            print("easy high thresh from taskCal:    " + str(easy_high_thresh))
            print("easy cal array from taskCal:  " + str(easy_cal_arr))
        elif trial_type=="hard":
            hard_high_thresh=new_high_thresh
            hard_low_thresh=new_low_thresh
            hard_thresh_rt=new_thresh_rt
            print("hard high thresh from taskCal:    " + str(hard_high_thresh))
            print("hard cal array from taskCal:  " + str(hard_cal_arr))
        
        practice_effort_list.remove(trial_type)
    
    
    if success==1:
        curr_success_text="¡Bien hecho!\n\nPulsa la barra espaciadora para ir al siguiente ensayo."
    else:
        if trial_type=="easy":
            curr_success_text="No hiciste bien la tarea esta vez.\n\nRecuerdate que pulsas la flecha izquierda si en número es menor que 5, y la flecha derecha si el número es mayor que 5."
        elif trial_type=="hard":
            curr_success_text="No hiciste bien la tarea esta vez.\n\nRecuerdate que pulsas la flecha izquierda si el número es azúl y impar O  amarillo y menor que 5. \n\nPulsas la flecha derecha si el número es azúl y par O amarillo y mayor que 5."

    ########## logging practice trial 
    #SID, block, overall practice counter, trial type, trial_type counter, number correct, number incorrect, success or not
    prac_trial_results=[SID, -99, prac_count, trial_type, practice_trial_count, totcorr, totincorr, success]
    prac_dataline = [str(element) for element in prac_trial_results]
    prac_dataline_csv= ",".join(prac_dataline)

    with open(prac_filename+'.csv', "a") as myfile:
        myfile.write(prac_dataline_csv+"\n")

    
    I.setText(curr_success_text)
    I.setPos([0,0])
    I.setAutoDraw(True)
    win.flip()
    
    eventTime=mClock.getTime()
    event_type="pres"
    desc= curr_success_text[0:5]
    log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, "NaN", "NaN", 8, "NaN"]
    log_data_arr.append(log_file_line)
    
    response=event.waitKeys(keyList='space', timeStamped=mClock)
    eventTime=mClock.getTime()
    event_type="resp"
    desc= curr_success_text[0:5]
    log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, "NaN", "NaN", 8, "NaN"]
    log_data_arr.append(log_file_line)
    
    I.setAutoDraw(False)
    win.flip()
    
    if  practice_effort_list==[]:
        cal_done=1
        
    logfile = open(log_filename+'.csv', 'a')
    for item in log_data_arr:
        log_dataline = [str(element) for element in item]
        log_dataline_csv= ",".join(log_dataline)
        logfile.write(log_dataline_csv + "\n")

    trial_counter+=1


#################################
# INSTRUCTIONS AND SELF REPORT BEFORE TASK
#starting task. Reminder of the instructions and first self-report
inst_text=[]
inst_text.append(u'Terminaste el entrenamiento y estás listo para la segunda fase.\n\nAntes de explicar como funciona la segunda fase, tenemos un par de preguntas para preguntarte. Puedes usar el raton para contestar.\n\n\n\n\nPresiona la barra espaciadora para continuar. ')
inst_text.append(u'En la segunda fase verás los mismos imágenes antes de empezar el jueguito, pero ahora las líneas por adentro significan si el juego requiere más o menos respuestas para que conste como un acierto. Si el circulo o cuadrado tiene una línea, tendrás que hacer menos respuestas, lo cual significa que tendrás mayor probabilidad de hacer la tarea bien y recibir los puntos. Si el circulo o cuadrado tiene 5 líneas por adentro, necesitaras responder más para hacer bien la tarea, lo cual significa que tendrás menos probabilidad de recibir los puntos.\n\n\n\n\nPresiona la barra espaciadora para continuar.')
inst_text.append(u'Durante la tarea, la mitad de ensayos no requerirán que hagas el juego. Es decir, verás la imagen (círculo o cuadrado) y luego un asterisco. El asterisco indica que no tendrás que hacer el jueguito de números y pasaras directo al siguiente ensayo. Claro, por no tener que jugar el juego, tampoco te darán los puntos en esos ensayos.\n\n\n\n\nPresiona la barra para ver un ejemplo de un ensayo sin el jueguito.')
inst_text.append(u'También recuerde que durante esta parte, no vas a utilizar la barra espaciadora. Una vez que finalices una ensayo, pasarás **automáticamente** al siguiente ensayo. \n\nLa imagen que indica el nivel de recompensa y el nivel de dificultad solo estará presentada brevemente, y luego comenzará el ensayo. \n\n\n\n\nPresiona la barra espaciadora para continuar.')
inst_text.append(u'Recuerde también que solo serás recompensad@ por los ensayos que completaste correctamente, así que trate de responder con la mayor precisión posible.\n\nDe vez en cuando vamos a pedirte que identifiques la imagen que fue presentada al inicio del ensayo. Tu recompensa depende en parte de que bien contestas estas preguntes de identificación así que es importante que prestes atención a la imagen cuando lo presentan en la pantalla. Finalmente, recomendamos que trates de parpadear durante la presentación de los números o entre los ensayos, pero no durante la presentación de la imagen o cuando recibes los puntos. \n\n\n\n\nPresiona la barra espaciadora para continuar.')
inst_text.append(u'Tendrás diez descansos a lo largo de la tarea. Durante estos decansos, te vamos a pedir que contestes las mismas preguntas de antes. \n\nSi tiene alguna pregunta, coméntalo al asistente ahora. \n\n\n\n\nPresiona la barra espaciadora para comenzar. ')

for i in range(0,len(inst_text)):
    I.setPos([0, 0])
    I.setText(inst_text[i])
    I.setAutoDraw(True)
    #port.setData(0)
    win.flip()
    eventTime=mClock.getTime()
    event_type="pres"
    trial_type="instruction"
    desc=inst_text[i][0:5]
    response=event.waitKeys(keyList='space', timeStamped=mClock)
    
    I.setAutoDraw(False)
    win.flip()

    if (i==0):
        your_mouse = event.Mouse(visible = True)
        selfreport(block_counter)
        your_mouse = event.Mouse(visible = False)
    elif (i==2):
        cue_pres.setImage(hclp_stim)
        cue_pres.setAutoDraw(True)
        win.flip()
        core.wait(1.5) 
        cue_pres.setAutoDraw(False)
        win.flip()
        '''
        #PRE-EFFORT FIX
        fix_pres.setAutoDraw(True)
        win.flip()
        eventTime=mClock.getTime()
        shuffle(fc_isi1)
        core.wait(fc_isi1[0])
        fix_pres.setAutoDraw(False)
        win.flip()
        '''
        star_pres.setPos([0,-.05])
        star_pres.setAutoDraw(True)
        win.flip()
        core.wait(1)
        star_pres.setAutoDraw(False)
        win.flip()
    else:
        pass


        
block_counter=1
trial_counter=1


fb_cues=["stim/x_mark.png"]
catch_corr_arr=[]

for b in block_arr:
    trial_block_counter=1
    ch_resp="blank"
    choice_resp_rt=-99
    for trial in b:
        
        #initialize important trial vars
        totcorr, totincorr, totnoresp,x, mean_trialTime, sd_trialTime=0,0,0,0,0,0
        trial_results_arr=[]
        thresh=0
        trial_type="blank"
        corr=-99
        catch_response,catch_corr=-99,-99
        log_data_arr=[]
        
        #getting necessary trial information
        trial_trig=0
        #set trigger value based on trial type
        if trial[1]=="hard":
            trial_trig=10
            trial_type="hc"
        else: 
            trial_trig=30
            trial_type="lc"
            
        if trial[2]=='low':
                trial_trig=trial_trig+10
                trial_type=trial_type+ "lp"
        else:
            trial_type=trial_type+ "hp"
            
        if trial[3]=='no_effort':
            trial_trig=trial_trig+5
            trial_type=trial_type+ "_noeffort"
            if trial[4]=='quest':
                trial_type=trial_type+"_quest"
        else:
            pass
            
        #ok now starting trial - FIRST FIXATION CROSS
        fix_pres.setAutoDraw(True)
        win.flip()
        eventTime=mClock.getTime()
        event_type="pres"
        desc= "iti_fix"
        core.wait(fc_iti[0])
        fix_pres.setAutoDraw(False)
        win.flip()

        log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, "NaN", "NaN", trial_trig, "NaN"]
        log_data_arr.append(log_file_line)
        
                
        #CUE    
        dev.activate_line(bitmask=trial_trig)
        cue_pres.setImage(trial[0])
        cue_pres.setAutoDraw(True)
        win.flip()
        
        eventTime=mClock.getTime()
        event_type="pres"
        desc= "cue"
        
        #log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, resp, correct, trial_trig, rt]
        log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, "NaN", "NaN", trial_trig, "NaN"]
        log_data_arr.append(log_file_line)
            
        #core.wait(1.5) #1500 ms cue presentation - fixed --> used to be 800, but was too short for anyone to even understand the cue
        #core.wait(1)
        core.wait(2)
        cue_pres.setAutoDraw(False)
        win.flip()
        
        '''
        #PRE-EFFORT FIX
        fix_pres.setAutoDraw(True)
        win.flip()
        eventTime=mClock.getTime()
        event_type="pres"
        desc= "pre_effort_fix"
        shuffle(fc_isi1)
        core.wait(fc_isi1[0])
        fix_pres.setAutoDraw(False)
        win.flip()
        '''
        log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, "NaN", "NaN", "NaN", "NaN"]
        log_data_arr.append(log_file_line)
            
        logfile = open(log_filename+'.csv', 'a')
        for item in log_data_arr:
            log_dataline = [str(element) for element in item]
            log_dataline_csv= ",".join(log_dataline)
            logfile.write(log_dataline_csv + "\n")

        dev.activate_line(bitmask=trial_trig+1) #either star or effort onset
        
        if (trial[3]=="no_effort"):
            #directly present star
            star_pres.setPos([0,-.05])
            star_pres.setAutoDraw(True)
            win.flip()
            eventTime=mClock.getTime()
            event_type="pres"
            desc= "star"
            #shuffle(fc_isi1)
            #core.wait(fc_isi1[0])
            core.wait(1)
            star_pres.setAutoDraw(False)
            win.flip()
            log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, "NaN", "NaN", "NaN", "NaN"]
            log_data_arr.append(log_file_line)
            
            if trial[4]=='quest':
                quest_slide.setText(u"Pulse la tecla que corresponde a la imagen presentada en este ensayo.\n\n\n\n")
                if cond==1:
                    quest_image.setImage("stim/catch_question_cond1.png")
                else:
                    quest_image.setImage("stim/catch_question_cond2.png")
                quest_slide.setAutoDraw(True)
                quest_image.setAutoDraw(True)
                dev.activate_line(bitmask=trial_trig+2)
                win.flip()
                
                #data for question slide
                event_type="pres"
                desc=u"Presiona el núm"
                eventTime=mClock.getTime()

                #log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, resp, correct, trial_trig, rt]
                log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, "NaN", "NaN", trial_trig, "NaN"]
                log_data_arr.append(log_file_line)
            
                response=event.waitKeys(keyList=['1','2','3','4'],timeStamped=mClock)
                catch_response=response[0][0]
                event_type="catch_resp_ex"
                rt=response[0][1]-eventTime
                eventTime= str(response[0][1])
                quest_slide.setAutoDraw(False)
                quest_image.setAutoDraw(False)
                win.flip()
                
                print('REGISTERED CATCH RESPONSE:   ' + str(catch_response))
                print('TRIAL TYPE:    ' + str(trial_type))
                

                if (trial_type=="lchp_noeffort_quest"):
                    if (catch_response=="1"):
                        catch_corr=1
                    else: 
                        catch_corr=0
                elif (trial_type=="lclp_noeffort_quest"):
                    if (catch_response=="2"):
                        catch_corr=1
                    else: 
                        catch_corr=0
                elif (trial_type=="hchp_noeffort_quest"):
                    if (catch_response=="3"):
                        catch_corr=1
                    else: 
                        catch_corr=0
                elif (trial_type=="hclp_noeffort_quest"):
                    if (catch_response=="4"):
                        catch_corr=1
                    else: 
                        catch_corr=0
                print('CATCH CORR:    ' + str(catch_corr))
                catch_corr_arr.append(catch_corr)
                print('CATCH CORR ARR:    ' + str(catch_corr_arr))
                #log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, resp, correct, trial_trig, rt]
                log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, catch_response, catch_corr, "NaN", rt]
                log_data_arr.append(log_file_line)


        else:
            if trial[1]=="easy":
                stim=cue_easy_stim("yellow")
                if trial[2]=="low": # low probability of success so a high threshold
                    str_trial_type="easy_high" #lclp
                    trig_base=200
                else: 
                    str_trial_type="easy_low" #lchp
                    trig_base=210
            else:
                stim=cue_hard_stim()
                if trial[2]=="low":
                    str_trial_type="hard_high" #hclp
                    trig_base=100
                else:
                    str_trial_type="hard_low" #hchp
                    trig_base=120
            num_array=stim[0]
            color_array=stim[1]   

            thresh_str=str_trial_type+"_thresh"
            thresh_rt_str=str_trial_type[0:4]+"_thresh_rt"
            cal_array_str=str_trial_type[0:4]+"_cal_arr"
            thresh=eval(thresh_str)
            thresh_rt=eval(thresh_rt_str)
            cal_array=eval(cal_array_str)
            print("MAKING SURE THIS ALL WORKS:")
            print(str(trial_type))
            print(cal_array_str)
            print(str(cal_array))

            totcorr, totincorr, totnoresp,x, mean_trialTime, sd_trialTime= cue_task_pres(num_array, color_array, trial_type, trig_base,thresh_rt)
            trial_result_arr=[totcorr, totincorr, totnoresp,x, mean_trialTime, sd_trialTime, trial_type]
            succ, rew=taskCal(trial_result_arr, trial, ch_resp, cal_array, thresh)

            fix_pres.setAutoDraw(True)
            win.flip()
            eventTime=mClock.getTime()
            event_type="pres"
            desc= "aftereff_fix"
            log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, "NaN", "NaN", "NaN", "NaN"]
            log_data_arr.append(log_file_line)
            shuffle(fc_isi2)
            core.wait(fc_isi2[0])
            fix_pres.setAutoDraw(False)
            win.flip()
            
            if succ==1:
                total_rew= total_rew+rew
                corrfb_pres.setImage('stim/white_check.png')
                trial_trig=trial_trig+3
                desc= "corr_fb"
                corrfb_pres.setAutoDraw(True)
            else:
                fb_pres.setImage('stim/white_x.png')
                trial_trig=trial_trig+2
                desc= "incorr_fb"
                fb_pres.setAutoDraw(True)
            dev.activate_line(bitmask=trial_trig)
            win.flip()
            
            eventTime=mClock.getTime()
            event_type="pres"
            log_file_line=[SID, block_counter, trial_counter, event_type, trial_type, str(desc.encode('utf8')), eventTime, "NaN", "NaN", trial_trig, "NaN"]
            log_data_arr.append(log_file_line)
            core.wait(1)
            corrfb_pres.setAutoDraw(False)
            fb_pres.setAutoDraw(False)
            win.flip()

        #data storage
        #f.write("Subject,Trial, Block, Trial_block, Effort, Probability, CurrDecThresh,CorrChoices,IncorrChoices,MeanDecTime,SDevDecTime,SuccessfulTrial,TrialReward,CumulReward\n")
        #easy color = trial_info[6],
        if trial[3]=="no_effort":
            final_trial_results=[SID, cond, hand, trial_counter, block_counter, trial_block_counter, trial[1], trial[2], -99, -99, -99, -99, -99, -99, -99,-99,catch_response,catch_corr]
        else:    
            final_trial_results=[SID, cond, hand, trial_counter, block_counter, trial_block_counter, trial[1], trial[2],thresh, trial_result_arr[0], trial_result_arr[1], trial_result_arr[4], trial_result_arr[5], succ, rew, total_rew, -99, -99]

        dataline = [str(element) for element in final_trial_results]
        dataline_csv= ",".join(dataline)
        export_trial_array.append(final_trial_results)
        with open(filename+'.csv', "a") as myfile:
            myfile.write(dataline_csv+"\n")
        
        logfile = open(log_filename+'.csv', 'a')
        for item in log_data_arr:
            log_dataline = [str(element) for element in item]
            log_dataline_csv= ",".join(log_dataline)
            logfile.write(log_dataline_csv+"\n")
            
        trial_counter+=1
        trial_block_counter+=1

    
    ##back in block
    break_text=u'Genial! Ha llegado tiempo para un descanso.\n\n\nPulsa la barra espaciadora para contestar algunas preguntas.'
    I.setText(break_text)
    I.setAutoDraw(True)
    win.flip()
    
    response=event.waitKeys(keyList='space', timeStamped=mClock)
    I.setAutoDraw(False)
    win.flip()
    
    dev.activate_line(bitmask=50+block_counter)
    selfreport(block_counter)
    mean_catch_corr=sum(catch_corr_arr)/len(catch_corr_arr)
    perc_catch_corr=round(mean_catch_corr*100,2)
    if block_counter<10:
        break_text=u'Puedes tomar un descanso. \n\nHasta ahora has acumulado\n\n'+ str(round(total_rew,2)) + ' puntos y has identificado bien ' + str(perc_catch_corr) + '% de las imagenes. \n\nPresiona la barra espaciadora cuando estés list@ para continuar.'
    else:
        break_text=u'Terminaste la tarea! \n\nHas acumulado '+ str(round(total_rew,2)) + ' puntos en total y has identificado bien ' + str(perc_catch_corr) + '% de las imagenes.\n\n\n\nPresiona la barra espaciadora para salir del experimento.'
    
    I.setText(break_text)
    I.setAutoDraw(True)
    win.flip()
    
    response=event.waitKeys(keyList='space', timeStamped=mClock)
    I.setAutoDraw(False)
    win.flip()
  
    block_counter+=1

#catch_mean and reward output so you can figure out how much reward to give them!
filename_catchmean="payout_data\\EV2_payout_" + expInfo['participant']
catch_mean=None    
catch_mean=np.mean(np.array(catch_corr_arr))
final_reward=None
final_reward=total_rew*catch_mean
thefile = open(filename_catchmean+'.txt', 'a')
thefile.write("rate of correct identification:   " + str(catch_mean) + "\n")
thefile.write("Points earned:   " + str(total_rew) + "\n")
thefile.write("Final points given:   " + str(final_reward))




###########################

logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

