# Stop Signal Task
# Created: February 29, 2017
# This script has been created in the free program PsychoPy and adapted with my own
# Python code in order to make the methodology consistent with the standards of cognitive
# neuroscience journals.

# You may need PsychoPy 1.82.01 in order to effectively run this code-- all Python code
# added, however, works with Python 2.7.  Any difficulties in later versions stem from
# PsychoPy's changes in that time, not necessarily Python itself.

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), April 02, 2017, at 23:56
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'StopSignal'  # from the Builder filename that created this script
expInfo = {u'gender': u'', u'participant': u'', u'letter': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "PracInst"
PracInstClock = core.Clock()
InstrText = visual.TextStim(win=win, ori=0, name='InstrText',
    text='Welcome to our study! In this task, you will see green arrows that point either left or right.  \nAs soon as you see the arrow, you should respond as QUICKLY AND ACCURATELY as possible by \npressing the LEFT arrow key if the arrow points LEFT or the RIGHT arrow key if the arrow \npoints RIGHT. On some trials, the green arrows may turn red.  If the arrow turns RED, you \nshould STOP your response immediately and NOT RESPOND to that particular arrow. Still respond \nto the other green arrows after it, unless the arrow turns red. Both going and stopping are \nequally important. Your performance on this task will be measured equally by both how fast \nand accurately you respond. \n\n\nPress the LEFT arrow key to begin the practice trials.\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
import random
Green=["left_green.jpg", "right_green.jpg"]
Red=["left_red.jpg", "right_red.jpg"]
realTask=[0, 0, 0, 1]
corrAns=""
arrow=""
arrow2=""
rewardtask=0
Overall=0


# Initialize components for Routine "ITI"
ITIClock = core.Clock()
outcome=""
total=0
corrAns=""
choice=random.choice([1.2, 1.5, 1.8])
change=random.choice([0.2, 0.3, 0.4])
thisTrial=random.choice(realTask)
if thisTrial==0:
    arrow=random.choice(Green)
    arrow2=arrow
    corrAns=arrow.partition("_")[0]
    
elif thisTrial==1:
    arrow=random.choice(Green)
    if arrow=="left_green.jpg":
        arrow2="left_red.jpg"
    elif arrow=="right_green.jpg":
        arrow2="right_red.jpg"
    corrAns=""
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Cross = visual.TextStim(win=win, ori=0, name='Cross',
    text='+',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
Arrow1 = visual.ImageStim(win=win, name='Arrow1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Arrow2 = visual.ImageStim(win=win, name='Arrow2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstrText2 = visual.TextStim(win=win, ori=0, name='InstrText2',
    text='You have completed the practice trials.  We will now begin the test trials.  \nRemember that both responding and stopping are equally important. Your \nperformance on this task will be measured equally by both how fast and \naccurately you respond. \n\n\nIf you have any questions before you begin the test phase, \nplease ask the experimenter now. \n\n\nIf not, press the RIGHT arrow key to begin the test trials.\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
outcome=""
total=0
corrAns=""
choice=random.choice([1.2, 1.5, 1.8])
change=random.choice([0.2, 0.3, 0.4])
thisTrial=random.choice(realTask)
if thisTrial==0:
    arrow=random.choice(Green)
    arrow2=arrow
    corrAns=arrow.partition("_")[0]
    
elif thisTrial==1:
    arrow=random.choice(Green)
    if arrow=="left_green.jpg":
        arrow2="left_red.jpg"
    elif arrow=="right_green.jpg":
        arrow2="right_red.jpg"
    corrAns=""
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Cross = visual.TextStim(win=win, ori=0, name='Cross',
    text='+',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
Arrow1 = visual.ImageStim(win=win, name='Arrow1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Arrow2 = visual.ImageStim(win=win, name='Arrow2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "Break"
BreakClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='BREAK\n\nGreat job!  Please take a brief break \nbefore continuing with the task. \n\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Press the spacebar to continue whenever you are ready!',    font='Arial',
    pos=[0, -.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
outcome=""
total=0
corrAns=""
choice=random.choice([1.2, 1.5, 1.8])
change=random.choice([0.2, 0.3, 0.4])
thisTrial=random.choice(realTask)
if thisTrial==0:
    arrow=random.choice(Green)
    arrow2=arrow
    corrAns=arrow.partition("_")[0]
    
elif thisTrial==1:
    arrow=random.choice(Green)
    if arrow=="left_green.jpg":
        arrow2="left_red.jpg"
    elif arrow=="right_green.jpg":
        arrow2="right_red.jpg"
    corrAns=""
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Cross = visual.TextStim(win=win, ori=0, name='Cross',
    text='+',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
Arrow1 = visual.ImageStim(win=win, name='Arrow1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Arrow2 = visual.ImageStim(win=win, name='Arrow2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "Break"
BreakClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='BREAK\n\nGreat job!  Please take a brief break \nbefore continuing with the task. \n\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Press the spacebar to continue whenever you are ready!',    font='Arial',
    pos=[0, -.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
outcome=""
total=0
corrAns=""
choice=random.choice([1.2, 1.5, 1.8])
change=random.choice([0.2, 0.3, 0.4])
thisTrial=random.choice(realTask)
if thisTrial==0:
    arrow=random.choice(Green)
    arrow2=arrow
    corrAns=arrow.partition("_")[0]
    
elif thisTrial==1:
    arrow=random.choice(Green)
    if arrow=="left_green.jpg":
        arrow2="left_red.jpg"
    elif arrow=="right_green.jpg":
        arrow2="right_red.jpg"
    corrAns=""
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Cross = visual.TextStim(win=win, ori=0, name='Cross',
    text='+',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
Arrow1 = visual.ImageStim(win=win, name='Arrow1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Arrow2 = visual.ImageStim(win=win, name='Arrow2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "Break"
BreakClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='BREAK\n\nGreat job!  Please take a brief break \nbefore continuing with the task. \n\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Press the spacebar to continue whenever you are ready!',    font='Arial',
    pos=[0, -.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
outcome=""
total=0
corrAns=""
choice=random.choice([1.2, 1.5, 1.8])
change=random.choice([0.2, 0.3, 0.4])
thisTrial=random.choice(realTask)
if thisTrial==0:
    arrow=random.choice(Green)
    arrow2=arrow
    corrAns=arrow.partition("_")[0]
    
elif thisTrial==1:
    arrow=random.choice(Green)
    if arrow=="left_green.jpg":
        arrow2="left_red.jpg"
    elif arrow=="right_green.jpg":
        arrow2="right_red.jpg"
    corrAns=""
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Cross = visual.TextStim(win=win, ori=0, name='Cross',
    text='+',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
Arrow1 = visual.ImageStim(win=win, name='Arrow1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Arrow2 = visual.ImageStim(win=win, name='Arrow2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "Break"
BreakClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='BREAK\n\nGreat job!  Please take a brief break \nbefore continuing with the task. \n\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Press the spacebar to continue whenever you are ready!',    font='Arial',
    pos=[0, -.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
outcome=""
total=0
corrAns=""
choice=random.choice([1.2, 1.5, 1.8])
change=random.choice([0.2, 0.3, 0.4])
thisTrial=random.choice(realTask)
if thisTrial==0:
    arrow=random.choice(Green)
    arrow2=arrow
    corrAns=arrow.partition("_")[0]
    
elif thisTrial==1:
    arrow=random.choice(Green)
    if arrow=="left_green.jpg":
        arrow2="left_red.jpg"
    elif arrow=="right_green.jpg":
        arrow2="right_red.jpg"
    corrAns=""
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Cross = visual.TextStim(win=win, ori=0, name='Cross',
    text='+',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
Arrow1 = visual.ImageStim(win=win, name='Arrow1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Arrow2 = visual.ImageStim(win=win, name='Arrow2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "Break"
BreakClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='BREAK\n\nGreat job!  Please take a brief break \nbefore continuing with the task. \n\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Press the spacebar to continue whenever you are ready!',    font='Arial',
    pos=[0, -.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "Instructions2"
Instructions2Clock = core.Clock()
Instr3 = visual.TextStim(win=win, ori=0, name='Instr3',
    text=BONUS INFORMATION!
You now have an opportunity to earn a 
monetary bonus of up to 10 based on your 
performance on the rest of the task.  The 
bonus will be based on BOTH how quickly 
and accurately you respond on go trials 
AND how accurately you stop your response 
on stop trials.  Bonus amounts will usually 
appear after you correctly stop your response 
on stop trials.  However, if you respond too 
slowly or make too many mistakes on go trials, 
then you may not receive a bonus even if you 
correctly stop your response on stop trials.  
So, try your best to respond as quickly and 
accurately as possible on go trials AND stop 
your response on stop trials so you can earn 
as much money as possible.

If you have any questions, 
please ask the experimenter now. 


If not, press either arrow key to continue.,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "ITI"
ITIClock = core.Clock()
outcome=""
total=0
corrAns=""
choice=random.choice([1.2, 1.5, 1.8])
change=random.choice([0.2, 0.3, 0.4])
thisTrial=random.choice(realTask)
if thisTrial==0:
    arrow=random.choice(Green)
    arrow2=arrow
    corrAns=arrow.partition("_")[0]
    
elif thisTrial==1:
    arrow=random.choice(Green)
    if arrow=="left_green.jpg":
        arrow2="left_red.jpg"
    elif arrow=="right_green.jpg":
        arrow2="right_red.jpg"
    corrAns=""
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Cross = visual.TextStim(win=win, ori=0, name='Cross',
    text='+',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
image1 = visual.ImageStim(win=win, name='image1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image2 = visual.ImageStim(win=win, name='image2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "Response"
ResponseClock = core.Clock()
Feedback = visual.TextStim(win=win, ori=0, name='Feedback',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "RewardBreak"
RewardBreakClock = core.Clock()

Banked = visual.TextStim(win=win, ori=0, name='Banked',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
BreatherStarter = visual.TextStim(win=win, ori=0, name='BreatherStarter',
    text='Feel free to take a break.\nPress space when you want to continue.',    font='Arial',
    pos=[0, -.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
outcome=""
total=0
corrAns=""
choice=random.choice([1.2, 1.5, 1.8])
change=random.choice([0.2, 0.3, 0.4])
thisTrial=random.choice(realTask)
if thisTrial==0:
    arrow=random.choice(Green)
    arrow2=arrow
    corrAns=arrow.partition("_")[0]
    
elif thisTrial==1:
    arrow=random.choice(Green)
    if arrow=="left_green.jpg":
        arrow2="left_red.jpg"
    elif arrow=="right_green.jpg":
        arrow2="right_red.jpg"
    corrAns=""
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Cross = visual.TextStim(win=win, ori=0, name='Cross',
    text='+',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
image1 = visual.ImageStim(win=win, name='image1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image2 = visual.ImageStim(win=win, name='image2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "Response"
ResponseClock = core.Clock()
Feedback = visual.TextStim(win=win, ori=0, name='Feedback',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "RewardBreak"
RewardBreakClock = core.Clock()

Banked = visual.TextStim(win=win, ori=0, name='Banked',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
BreatherStarter = visual.TextStim(win=win, ori=0, name='BreatherStarter',
    text='Feel free to take a break.\nPress space when you want to continue.',    font='Arial',
    pos=[0, -.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
outcome=""
total=0
corrAns=""
choice=random.choice([1.2, 1.5, 1.8])
change=random.choice([0.2, 0.3, 0.4])
thisTrial=random.choice(realTask)
if thisTrial==0:
    arrow=random.choice(Green)
    arrow2=arrow
    corrAns=arrow.partition("_")[0]
    
elif thisTrial==1:
    arrow=random.choice(Green)
    if arrow=="left_green.jpg":
        arrow2="left_red.jpg"
    elif arrow=="right_green.jpg":
        arrow2="right_red.jpg"
    corrAns=""
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Cross = visual.TextStim(win=win, ori=0, name='Cross',
    text='+',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
image1 = visual.ImageStim(win=win, name='image1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image2 = visual.ImageStim(win=win, name='image2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "Response"
ResponseClock = core.Clock()
Feedback = visual.TextStim(win=win, ori=0, name='Feedback',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "RewardBreak"
RewardBreakClock = core.Clock()

Banked = visual.TextStim(win=win, ori=0, name='Banked',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
BreatherStarter = visual.TextStim(win=win, ori=0, name='BreatherStarter',
    text='Feel free to take a break.\nPress space when you want to continue.',    font='Arial',
    pos=[0, -.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
outcome=""
total=0
corrAns=""
choice=random.choice([1.2, 1.5, 1.8])
change=random.choice([0.2, 0.3, 0.4])
thisTrial=random.choice(realTask)
if thisTrial==0:
    arrow=random.choice(Green)
    arrow2=arrow
    corrAns=arrow.partition("_")[0]
    
elif thisTrial==1:
    arrow=random.choice(Green)
    if arrow=="left_green.jpg":
        arrow2="left_red.jpg"
    elif arrow=="right_green.jpg":
        arrow2="right_red.jpg"
    corrAns=""
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Cross = visual.TextStim(win=win, ori=0, name='Cross',
    text='+',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
image1 = visual.ImageStim(win=win, name='image1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image2 = visual.ImageStim(win=win, name='image2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "Response"
ResponseClock = core.Clock()
Feedback = visual.TextStim(win=win, ori=0, name='Feedback',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "RewardBreak"
RewardBreakClock = core.Clock()

Banked = visual.TextStim(win=win, ori=0, name='Banked',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
BreatherStarter = visual.TextStim(win=win, ori=0, name='BreatherStarter',
    text='Feel free to take a break.\nPress space when you want to continue.',    font='Arial',
    pos=[0, -.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
outcome=""
total=0
corrAns=""
choice=random.choice([1.2, 1.5, 1.8])
change=random.choice([0.2, 0.3, 0.4])
thisTrial=random.choice(realTask)
if thisTrial==0:
    arrow=random.choice(Green)
    arrow2=arrow
    corrAns=arrow.partition("_")[0]
    
elif thisTrial==1:
    arrow=random.choice(Green)
    if arrow=="left_green.jpg":
        arrow2="left_red.jpg"
    elif arrow=="right_green.jpg":
        arrow2="right_red.jpg"
    corrAns=""
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Cross = visual.TextStim(win=win, ori=0, name='Cross',
    text='+',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
image1 = visual.ImageStim(win=win, name='image1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image2 = visual.ImageStim(win=win, name='image2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "Response"
ResponseClock = core.Clock()
Feedback = visual.TextStim(win=win, ori=0, name='Feedback',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "Earnings"
EarningsClock = core.Clock()
EarningTotal = visual.TextStim(win=win, ori=0, name='EarningTotal',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Continue = visual.TextStim(win=win, ori=0, name='Continue',
    text='Please let the experimenter know\nthat you have finished!\n\n',    font='Arial',
    pos=[0, -.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "PracInst"-------
t = 0
PracInstClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
PracInstComponents = []
PracInstComponents.append(InstrText)
PracInstComponents.append(key_resp_2)
for thisComponent in PracInstComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "PracInst"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = PracInstClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrText* updates
    if t >= 0.0 and InstrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrText.tStart = t  # underestimates by a little under one frame
        InstrText.frameNStart = frameN  # exact frame index
        InstrText.setAutoDraw(True)
    
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['left', 'right'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "PracInst"-------
for thisComponent in PracInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "PracInst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_practice = data.TrialHandler(nReps=12, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials_practice')
thisExp.addLoop(trials_practice)  # add the loop to the experiment
thisTrials_practice = trials_practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrials_practice.rgb)
if thisTrials_practice != None:
    for paramName in thisTrials_practice.keys():
        exec(paramName + '= thisTrials_practice.' + paramName)

for thisTrials_practice in trials_practice:
    currentLoop = trials_practice
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
    if thisTrials_practice != None:
        for paramName in thisTrials_practice.keys():
            exec(paramName + '= thisTrials_practice.' + paramName)
    
    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    reward=random.choice([0,1])
    choice=random.choice([1.2, 1.5, 1.8])
    change=random.choice([0.2, 0.3, 0.4])
    thisTrial=random.choice(realTask)
    if thisTrial==0:
        arrow=random.choice(Green)
        arrow2=arrow
        corrAns=arrow.partition("_")[0]
        
    elif thisTrial==1:
        arrow=random.choice(Green)
        if arrow=="left_green.jpg":
            arrow2="left_red.jpg"
        elif arrow=="right_green.jpg":
            arrow2="right_red.jpg"
        corrAns=""
    # keep track of which components have finished
    ITIComponents = []
    ITIComponents.append(ISI)
    ITIComponents.append(Cross)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Cross* updates
        if t >= 0.0 and Cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cross.tStart = t  # underestimates by a little under one frame
            Cross.frameNStart = frameN  # exact frame index
            Cross.setAutoDraw(True)
        if Cross.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(choice)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Practice"-------
    t = 0
    PracticeClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    KeyResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyResp.status = NOT_STARTED
    Arrow1.setImage(arrow)
    Arrow2.setImage(arrow2)
    
    # keep track of which components have finished
    PracticeComponents = []
    PracticeComponents.append(KeyResp)
    PracticeComponents.append(Arrow1)
    PracticeComponents.append(Arrow2)
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Practice"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = PracticeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *KeyResp* updates
        if t >= 0.0 and KeyResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyResp.tStart = t  # underestimates by a little under one frame
            KeyResp.frameNStart = frameN  # exact frame index
            KeyResp.status = STARTED
            # keyboard checking is just starting
            KeyResp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if KeyResp.status == STARTED and t >= (0.0 + (2.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyResp.status = STOPPED
        if KeyResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if KeyResp.keys == []:  # then this was the first keypress
                    KeyResp.keys = theseKeys[0]  # just the first key pressed
                    KeyResp.rt = KeyResp.clock.getTime()
                    # was this 'correct'?
                    if (KeyResp.keys == str(corrAns)) or (KeyResp.keys == corrAns):
                        KeyResp.corr = 1
                    else:
                        KeyResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *Arrow1* updates
        if t >= 0.0 and Arrow1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Arrow1.tStart = t  # underestimates by a little under one frame
            Arrow1.frameNStart = frameN  # exact frame index
            Arrow1.setAutoDraw(True)
        if Arrow1.status == STARTED and t >= (0.0 + (change + .5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Arrow1.setAutoDraw(False)
        
        # *Arrow2* updates
        if t >= change and Arrow2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Arrow2.tStart = t  # underestimates by a little under one frame
            Arrow2.frameNStart = frameN  # exact frame index
            Arrow2.setAutoDraw(True)
        if Arrow2.status == STARTED and t >= (change + (1.9-win.monitorFramePeriod*0.75)): #most of one frame period left
            Arrow2.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Practice"-------
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyResp.keys in ['', [], None]:  # No response was made
       KeyResp.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': KeyResp.corr = 1  # correct non-response
       else: KeyResp.corr = 0  # failed to respond (incorrectly)
    # store data for trials_practice (TrialHandler)
    trials_practice.addData('KeyResp.keys',KeyResp.keys)
    trials_practice.addData('KeyResp.corr', KeyResp.corr)
    if KeyResp.keys != None:  # we had a response
        trials_practice.addData('KeyResp.rt', KeyResp.rt)
    thisExp.addData("ITI", choice)
    thisExp.addData("Changes", change)
    thisExp.addData("Arrow1", arrow)
    thisExp.addData("Arrow2", arrow2)
    thisExp.addData("StopTrial", thisTrial) # is it a stop trial?
    thisExp.addData("RewardTask", rewardtask) # does this task have reward?
    thisExp.addData("RewardActive", reward) # is the reward active?
    if rewardtask==0:
        thisExp.addData("GotDollar", 0)
    elif rewardtask==1:
        if thisTrial==1 and reward==1:
            thisExp.addData("GotDollar", 1)
        else:
            thisExp.addData("GotDollar", 0)
    else:
        thisExp.addData("GotDollar", 2)
    thisExp.addData("CumulativeBlock", total)
    thisExp.addData("CumulativeOverall", Overall)
    thisExp.addData("key_resp_trial.keys", KeyResp.keys)
    thisExp.addData("key_resp_trial.corr", KeyResp.corr)
    thisExp.addData("key_resp_trial.rt", KeyResp.rt)
    
    
    # the Routine "Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 12 repeats of 'trials_practice'


#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(InstrText2)
InstructionsComponents.append(key_resp_5)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrText2* updates
    if t >= 0.0 and InstrText2.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrText2.tStart = t  # underestimates by a little under one frame
        InstrText2.frameNStart = frameN  # exact frame index
        InstrText2.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['left', 'right'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    reward=random.choice([0,1])
    choice=random.choice([1.2, 1.5, 1.8])
    change=random.choice([0.2, 0.3, 0.4])
    thisTrial=random.choice(realTask)
    if thisTrial==0:
        arrow=random.choice(Green)
        arrow2=arrow
        corrAns=arrow.partition("_")[0]
        
    elif thisTrial==1:
        arrow=random.choice(Green)
        if arrow=="left_green.jpg":
            arrow2="left_red.jpg"
        elif arrow=="right_green.jpg":
            arrow2="right_red.jpg"
        corrAns=""
    # keep track of which components have finished
    ITIComponents = []
    ITIComponents.append(ISI)
    ITIComponents.append(Cross)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Cross* updates
        if t >= 0.0 and Cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cross.tStart = t  # underestimates by a little under one frame
            Cross.frameNStart = frameN  # exact frame index
            Cross.setAutoDraw(True)
        if Cross.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(choice)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Practice"-------
    t = 0
    PracticeClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    KeyResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyResp.status = NOT_STARTED
    Arrow1.setImage(arrow)
    Arrow2.setImage(arrow2)
    
    # keep track of which components have finished
    PracticeComponents = []
    PracticeComponents.append(KeyResp)
    PracticeComponents.append(Arrow1)
    PracticeComponents.append(Arrow2)
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Practice"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = PracticeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *KeyResp* updates
        if t >= 0.0 and KeyResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyResp.tStart = t  # underestimates by a little under one frame
            KeyResp.frameNStart = frameN  # exact frame index
            KeyResp.status = STARTED
            # keyboard checking is just starting
            KeyResp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if KeyResp.status == STARTED and t >= (0.0 + (2.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyResp.status = STOPPED
        if KeyResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if KeyResp.keys == []:  # then this was the first keypress
                    KeyResp.keys = theseKeys[0]  # just the first key pressed
                    KeyResp.rt = KeyResp.clock.getTime()
                    # was this 'correct'?
                    if (KeyResp.keys == str(corrAns)) or (KeyResp.keys == corrAns):
                        KeyResp.corr = 1
                    else:
                        KeyResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *Arrow1* updates
        if t >= 0.0 and Arrow1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Arrow1.tStart = t  # underestimates by a little under one frame
            Arrow1.frameNStart = frameN  # exact frame index
            Arrow1.setAutoDraw(True)
        if Arrow1.status == STARTED and t >= (0.0 + (change + .5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Arrow1.setAutoDraw(False)
        
        # *Arrow2* updates
        if t >= change and Arrow2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Arrow2.tStart = t  # underestimates by a little under one frame
            Arrow2.frameNStart = frameN  # exact frame index
            Arrow2.setAutoDraw(True)
        if Arrow2.status == STARTED and t >= (change + (1.9-win.monitorFramePeriod*0.75)): #most of one frame period left
            Arrow2.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Practice"-------
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyResp.keys in ['', [], None]:  # No response was made
       KeyResp.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': KeyResp.corr = 1  # correct non-response
       else: KeyResp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('KeyResp.keys',KeyResp.keys)
    trials.addData('KeyResp.corr', KeyResp.corr)
    if KeyResp.keys != None:  # we had a response
        trials.addData('KeyResp.rt', KeyResp.rt)
    thisExp.addData("ITI", choice)
    thisExp.addData("Changes", change)
    thisExp.addData("Arrow1", arrow)
    thisExp.addData("Arrow2", arrow2)
    thisExp.addData("StopTrial", thisTrial) # is it a stop trial?
    thisExp.addData("RewardTask", rewardtask) # does this task have reward?
    thisExp.addData("RewardActive", reward) # is the reward active?
    if rewardtask==0:
        thisExp.addData("GotDollar", 0)
    elif rewardtask==1:
        if thisTrial==1 and reward==1:
            thisExp.addData("GotDollar", 1)
        else:
            thisExp.addData("GotDollar", 0)
    else:
        thisExp.addData("GotDollar", 2)
    thisExp.addData("CumulativeBlock", total)
    thisExp.addData("CumulativeOverall", Overall)
    thisExp.addData("key_resp_trial.keys", KeyResp.keys)
    thisExp.addData("key_resp_trial.corr", KeyResp.corr)
    thisExp.addData("key_resp_trial.rt", KeyResp.rt)
    
    
    # the Routine "Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 50 repeats of 'trials'


#------Prepare to start Routine "Break"-------
t = 0
BreakClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
BreakComponents = []
BreakComponents.append(text)
BreakComponents.append(text_2)
BreakComponents.append(key_resp_7)
for thisComponent in BreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Break"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *text_2* updates
    if t >= 5 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    reward=random.choice([0,1])
    choice=random.choice([1.2, 1.5, 1.8])
    change=random.choice([0.2, 0.3, 0.4])
    thisTrial=random.choice(realTask)
    if thisTrial==0:
        arrow=random.choice(Green)
        arrow2=arrow
        corrAns=arrow.partition("_")[0]
        
    elif thisTrial==1:
        arrow=random.choice(Green)
        if arrow=="left_green.jpg":
            arrow2="left_red.jpg"
        elif arrow=="right_green.jpg":
            arrow2="right_red.jpg"
        corrAns=""
    # keep track of which components have finished
    ITIComponents = []
    ITIComponents.append(ISI)
    ITIComponents.append(Cross)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Cross* updates
        if t >= 0.0 and Cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cross.tStart = t  # underestimates by a little under one frame
            Cross.frameNStart = frameN  # exact frame index
            Cross.setAutoDraw(True)
        if Cross.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(choice)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Practice"-------
    t = 0
    PracticeClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    KeyResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyResp.status = NOT_STARTED
    Arrow1.setImage(arrow)
    Arrow2.setImage(arrow2)
    
    # keep track of which components have finished
    PracticeComponents = []
    PracticeComponents.append(KeyResp)
    PracticeComponents.append(Arrow1)
    PracticeComponents.append(Arrow2)
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Practice"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = PracticeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *KeyResp* updates
        if t >= 0.0 and KeyResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyResp.tStart = t  # underestimates by a little under one frame
            KeyResp.frameNStart = frameN  # exact frame index
            KeyResp.status = STARTED
            # keyboard checking is just starting
            KeyResp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if KeyResp.status == STARTED and t >= (0.0 + (2.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyResp.status = STOPPED
        if KeyResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if KeyResp.keys == []:  # then this was the first keypress
                    KeyResp.keys = theseKeys[0]  # just the first key pressed
                    KeyResp.rt = KeyResp.clock.getTime()
                    # was this 'correct'?
                    if (KeyResp.keys == str(corrAns)) or (KeyResp.keys == corrAns):
                        KeyResp.corr = 1
                    else:
                        KeyResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *Arrow1* updates
        if t >= 0.0 and Arrow1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Arrow1.tStart = t  # underestimates by a little under one frame
            Arrow1.frameNStart = frameN  # exact frame index
            Arrow1.setAutoDraw(True)
        if Arrow1.status == STARTED and t >= (0.0 + (change + .5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Arrow1.setAutoDraw(False)
        
        # *Arrow2* updates
        if t >= change and Arrow2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Arrow2.tStart = t  # underestimates by a little under one frame
            Arrow2.frameNStart = frameN  # exact frame index
            Arrow2.setAutoDraw(True)
        if Arrow2.status == STARTED and t >= (change + (1.9-win.monitorFramePeriod*0.75)): #most of one frame period left
            Arrow2.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Practice"-------
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyResp.keys in ['', [], None]:  # No response was made
       KeyResp.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': KeyResp.corr = 1  # correct non-response
       else: KeyResp.corr = 0  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('KeyResp.keys',KeyResp.keys)
    trials_2.addData('KeyResp.corr', KeyResp.corr)
    if KeyResp.keys != None:  # we had a response
        trials_2.addData('KeyResp.rt', KeyResp.rt)
    thisExp.addData("ITI", choice)
    thisExp.addData("Changes", change)
    thisExp.addData("Arrow1", arrow)
    thisExp.addData("Arrow2", arrow2)
    thisExp.addData("StopTrial", thisTrial) # is it a stop trial?
    thisExp.addData("RewardTask", rewardtask) # does this task have reward?
    thisExp.addData("RewardActive", reward) # is the reward active?
    if rewardtask==0:
        thisExp.addData("GotDollar", 0)
    elif rewardtask==1:
        if thisTrial==1 and reward==1:
            thisExp.addData("GotDollar", 1)
        else:
            thisExp.addData("GotDollar", 0)
    else:
        thisExp.addData("GotDollar", 2)
    thisExp.addData("CumulativeBlock", total)
    thisExp.addData("CumulativeOverall", Overall)
    thisExp.addData("key_resp_trial.keys", KeyResp.keys)
    thisExp.addData("key_resp_trial.corr", KeyResp.corr)
    thisExp.addData("key_resp_trial.rt", KeyResp.rt)
    
    
    # the Routine "Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 50 repeats of 'trials_2'


#------Prepare to start Routine "Break"-------
t = 0
BreakClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
BreakComponents = []
BreakComponents.append(text)
BreakComponents.append(text_2)
BreakComponents.append(key_resp_7)
for thisComponent in BreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Break"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *text_2* updates
    if t >= 5 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    reward=random.choice([0,1])
    choice=random.choice([1.2, 1.5, 1.8])
    change=random.choice([0.2, 0.3, 0.4])
    thisTrial=random.choice(realTask)
    if thisTrial==0:
        arrow=random.choice(Green)
        arrow2=arrow
        corrAns=arrow.partition("_")[0]
        
    elif thisTrial==1:
        arrow=random.choice(Green)
        if arrow=="left_green.jpg":
            arrow2="left_red.jpg"
        elif arrow=="right_green.jpg":
            arrow2="right_red.jpg"
        corrAns=""
    # keep track of which components have finished
    ITIComponents = []
    ITIComponents.append(ISI)
    ITIComponents.append(Cross)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Cross* updates
        if t >= 0.0 and Cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cross.tStart = t  # underestimates by a little under one frame
            Cross.frameNStart = frameN  # exact frame index
            Cross.setAutoDraw(True)
        if Cross.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(choice)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Practice"-------
    t = 0
    PracticeClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    KeyResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyResp.status = NOT_STARTED
    Arrow1.setImage(arrow)
    Arrow2.setImage(arrow2)
    
    # keep track of which components have finished
    PracticeComponents = []
    PracticeComponents.append(KeyResp)
    PracticeComponents.append(Arrow1)
    PracticeComponents.append(Arrow2)
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Practice"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = PracticeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *KeyResp* updates
        if t >= 0.0 and KeyResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyResp.tStart = t  # underestimates by a little under one frame
            KeyResp.frameNStart = frameN  # exact frame index
            KeyResp.status = STARTED
            # keyboard checking is just starting
            KeyResp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if KeyResp.status == STARTED and t >= (0.0 + (2.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyResp.status = STOPPED
        if KeyResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if KeyResp.keys == []:  # then this was the first keypress
                    KeyResp.keys = theseKeys[0]  # just the first key pressed
                    KeyResp.rt = KeyResp.clock.getTime()
                    # was this 'correct'?
                    if (KeyResp.keys == str(corrAns)) or (KeyResp.keys == corrAns):
                        KeyResp.corr = 1
                    else:
                        KeyResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *Arrow1* updates
        if t >= 0.0 and Arrow1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Arrow1.tStart = t  # underestimates by a little under one frame
            Arrow1.frameNStart = frameN  # exact frame index
            Arrow1.setAutoDraw(True)
        if Arrow1.status == STARTED and t >= (0.0 + (change + .5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Arrow1.setAutoDraw(False)
        
        # *Arrow2* updates
        if t >= change and Arrow2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Arrow2.tStart = t  # underestimates by a little under one frame
            Arrow2.frameNStart = frameN  # exact frame index
            Arrow2.setAutoDraw(True)
        if Arrow2.status == STARTED and t >= (change + (1.9-win.monitorFramePeriod*0.75)): #most of one frame period left
            Arrow2.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Practice"-------
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyResp.keys in ['', [], None]:  # No response was made
       KeyResp.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': KeyResp.corr = 1  # correct non-response
       else: KeyResp.corr = 0  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('KeyResp.keys',KeyResp.keys)
    trials_3.addData('KeyResp.corr', KeyResp.corr)
    if KeyResp.keys != None:  # we had a response
        trials_3.addData('KeyResp.rt', KeyResp.rt)
    thisExp.addData("ITI", choice)
    thisExp.addData("Changes", change)
    thisExp.addData("Arrow1", arrow)
    thisExp.addData("Arrow2", arrow2)
    thisExp.addData("StopTrial", thisTrial) # is it a stop trial?
    thisExp.addData("RewardTask", rewardtask) # does this task have reward?
    thisExp.addData("RewardActive", reward) # is the reward active?
    if rewardtask==0:
        thisExp.addData("GotDollar", 0)
    elif rewardtask==1:
        if thisTrial==1 and reward==1:
            thisExp.addData("GotDollar", 1)
        else:
            thisExp.addData("GotDollar", 0)
    else:
        thisExp.addData("GotDollar", 2)
    thisExp.addData("CumulativeBlock", total)
    thisExp.addData("CumulativeOverall", Overall)
    thisExp.addData("key_resp_trial.keys", KeyResp.keys)
    thisExp.addData("key_resp_trial.corr", KeyResp.corr)
    thisExp.addData("key_resp_trial.rt", KeyResp.rt)
    
    
    # the Routine "Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 50 repeats of 'trials_3'


#------Prepare to start Routine "Break"-------
t = 0
BreakClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
BreakComponents = []
BreakComponents.append(text)
BreakComponents.append(text_2)
BreakComponents.append(key_resp_7)
for thisComponent in BreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Break"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *text_2* updates
    if t >= 5 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4.keys():
        exec(paramName + '= thisTrial_4.' + paramName)

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4.keys():
            exec(paramName + '= thisTrial_4.' + paramName)
    
    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    reward=random.choice([0,1])
    choice=random.choice([1.2, 1.5, 1.8])
    change=random.choice([0.2, 0.3, 0.4])
    thisTrial=random.choice(realTask)
    if thisTrial==0:
        arrow=random.choice(Green)
        arrow2=arrow
        corrAns=arrow.partition("_")[0]
        
    elif thisTrial==1:
        arrow=random.choice(Green)
        if arrow=="left_green.jpg":
            arrow2="left_red.jpg"
        elif arrow=="right_green.jpg":
            arrow2="right_red.jpg"
        corrAns=""
    # keep track of which components have finished
    ITIComponents = []
    ITIComponents.append(ISI)
    ITIComponents.append(Cross)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Cross* updates
        if t >= 0.0 and Cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cross.tStart = t  # underestimates by a little under one frame
            Cross.frameNStart = frameN  # exact frame index
            Cross.setAutoDraw(True)
        if Cross.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(choice)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Practice"-------
    t = 0
    PracticeClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    KeyResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyResp.status = NOT_STARTED
    Arrow1.setImage(arrow)
    Arrow2.setImage(arrow2)
    
    # keep track of which components have finished
    PracticeComponents = []
    PracticeComponents.append(KeyResp)
    PracticeComponents.append(Arrow1)
    PracticeComponents.append(Arrow2)
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Practice"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = PracticeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *KeyResp* updates
        if t >= 0.0 and KeyResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyResp.tStart = t  # underestimates by a little under one frame
            KeyResp.frameNStart = frameN  # exact frame index
            KeyResp.status = STARTED
            # keyboard checking is just starting
            KeyResp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if KeyResp.status == STARTED and t >= (0.0 + (2.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyResp.status = STOPPED
        if KeyResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if KeyResp.keys == []:  # then this was the first keypress
                    KeyResp.keys = theseKeys[0]  # just the first key pressed
                    KeyResp.rt = KeyResp.clock.getTime()
                    # was this 'correct'?
                    if (KeyResp.keys == str(corrAns)) or (KeyResp.keys == corrAns):
                        KeyResp.corr = 1
                    else:
                        KeyResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *Arrow1* updates
        if t >= 0.0 and Arrow1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Arrow1.tStart = t  # underestimates by a little under one frame
            Arrow1.frameNStart = frameN  # exact frame index
            Arrow1.setAutoDraw(True)
        if Arrow1.status == STARTED and t >= (0.0 + (change + .5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Arrow1.setAutoDraw(False)
        
        # *Arrow2* updates
        if t >= change and Arrow2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Arrow2.tStart = t  # underestimates by a little under one frame
            Arrow2.frameNStart = frameN  # exact frame index
            Arrow2.setAutoDraw(True)
        if Arrow2.status == STARTED and t >= (change + (1.9-win.monitorFramePeriod*0.75)): #most of one frame period left
            Arrow2.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Practice"-------
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyResp.keys in ['', [], None]:  # No response was made
       KeyResp.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': KeyResp.corr = 1  # correct non-response
       else: KeyResp.corr = 0  # failed to respond (incorrectly)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('KeyResp.keys',KeyResp.keys)
    trials_4.addData('KeyResp.corr', KeyResp.corr)
    if KeyResp.keys != None:  # we had a response
        trials_4.addData('KeyResp.rt', KeyResp.rt)
    thisExp.addData("ITI", choice)
    thisExp.addData("Changes", change)
    thisExp.addData("Arrow1", arrow)
    thisExp.addData("Arrow2", arrow2)
    thisExp.addData("StopTrial", thisTrial) # is it a stop trial?
    thisExp.addData("RewardTask", rewardtask) # does this task have reward?
    thisExp.addData("RewardActive", reward) # is the reward active?
    if rewardtask==0:
        thisExp.addData("GotDollar", 0)
    elif rewardtask==1:
        if thisTrial==1 and reward==1:
            thisExp.addData("GotDollar", 1)
        else:
            thisExp.addData("GotDollar", 0)
    else:
        thisExp.addData("GotDollar", 2)
    thisExp.addData("CumulativeBlock", total)
    thisExp.addData("CumulativeOverall", Overall)
    thisExp.addData("key_resp_trial.keys", KeyResp.keys)
    thisExp.addData("key_resp_trial.corr", KeyResp.corr)
    thisExp.addData("key_resp_trial.rt", KeyResp.rt)
    
    
    # the Routine "Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 50 repeats of 'trials_4'


#------Prepare to start Routine "Break"-------
t = 0
BreakClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
BreakComponents = []
BreakComponents.append(text)
BreakComponents.append(text_2)
BreakComponents.append(key_resp_7)
for thisComponent in BreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Break"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *text_2* updates
    if t >= 5 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5.keys():
        exec(paramName + '= thisTrial_5.' + paramName)

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5.keys():
            exec(paramName + '= thisTrial_5.' + paramName)
    
    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    reward=random.choice([0,1])
    choice=random.choice([1.2, 1.5, 1.8])
    change=random.choice([0.2, 0.3, 0.4])
    thisTrial=random.choice(realTask)
    if thisTrial==0:
        arrow=random.choice(Green)
        arrow2=arrow
        corrAns=arrow.partition("_")[0]
        
    elif thisTrial==1:
        arrow=random.choice(Green)
        if arrow=="left_green.jpg":
            arrow2="left_red.jpg"
        elif arrow=="right_green.jpg":
            arrow2="right_red.jpg"
        corrAns=""
    # keep track of which components have finished
    ITIComponents = []
    ITIComponents.append(ISI)
    ITIComponents.append(Cross)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Cross* updates
        if t >= 0.0 and Cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cross.tStart = t  # underestimates by a little under one frame
            Cross.frameNStart = frameN  # exact frame index
            Cross.setAutoDraw(True)
        if Cross.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(choice)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Practice"-------
    t = 0
    PracticeClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    KeyResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyResp.status = NOT_STARTED
    Arrow1.setImage(arrow)
    Arrow2.setImage(arrow2)
    
    # keep track of which components have finished
    PracticeComponents = []
    PracticeComponents.append(KeyResp)
    PracticeComponents.append(Arrow1)
    PracticeComponents.append(Arrow2)
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Practice"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = PracticeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *KeyResp* updates
        if t >= 0.0 and KeyResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyResp.tStart = t  # underestimates by a little under one frame
            KeyResp.frameNStart = frameN  # exact frame index
            KeyResp.status = STARTED
            # keyboard checking is just starting
            KeyResp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if KeyResp.status == STARTED and t >= (0.0 + (2.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyResp.status = STOPPED
        if KeyResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if KeyResp.keys == []:  # then this was the first keypress
                    KeyResp.keys = theseKeys[0]  # just the first key pressed
                    KeyResp.rt = KeyResp.clock.getTime()
                    # was this 'correct'?
                    if (KeyResp.keys == str(corrAns)) or (KeyResp.keys == corrAns):
                        KeyResp.corr = 1
                    else:
                        KeyResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *Arrow1* updates
        if t >= 0.0 and Arrow1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Arrow1.tStart = t  # underestimates by a little under one frame
            Arrow1.frameNStart = frameN  # exact frame index
            Arrow1.setAutoDraw(True)
        if Arrow1.status == STARTED and t >= (0.0 + (change + .5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Arrow1.setAutoDraw(False)
        
        # *Arrow2* updates
        if t >= change and Arrow2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Arrow2.tStart = t  # underestimates by a little under one frame
            Arrow2.frameNStart = frameN  # exact frame index
            Arrow2.setAutoDraw(True)
        if Arrow2.status == STARTED and t >= (change + (1.9-win.monitorFramePeriod*0.75)): #most of one frame period left
            Arrow2.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Practice"-------
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyResp.keys in ['', [], None]:  # No response was made
       KeyResp.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': KeyResp.corr = 1  # correct non-response
       else: KeyResp.corr = 0  # failed to respond (incorrectly)
    # store data for trials_5 (TrialHandler)
    trials_5.addData('KeyResp.keys',KeyResp.keys)
    trials_5.addData('KeyResp.corr', KeyResp.corr)
    if KeyResp.keys != None:  # we had a response
        trials_5.addData('KeyResp.rt', KeyResp.rt)
    thisExp.addData("ITI", choice)
    thisExp.addData("Changes", change)
    thisExp.addData("Arrow1", arrow)
    thisExp.addData("Arrow2", arrow2)
    thisExp.addData("StopTrial", thisTrial) # is it a stop trial?
    thisExp.addData("RewardTask", rewardtask) # does this task have reward?
    thisExp.addData("RewardActive", reward) # is the reward active?
    if rewardtask==0:
        thisExp.addData("GotDollar", 0)
    elif rewardtask==1:
        if thisTrial==1 and reward==1:
            thisExp.addData("GotDollar", 1)
        else:
            thisExp.addData("GotDollar", 0)
    else:
        thisExp.addData("GotDollar", 2)
    thisExp.addData("CumulativeBlock", total)
    thisExp.addData("CumulativeOverall", Overall)
    thisExp.addData("key_resp_trial.keys", KeyResp.keys)
    thisExp.addData("key_resp_trial.corr", KeyResp.corr)
    thisExp.addData("key_resp_trial.rt", KeyResp.rt)
    
    
    # the Routine "Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 50 repeats of 'trials_5'


#------Prepare to start Routine "Break"-------
t = 0
BreakClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
BreakComponents = []
BreakComponents.append(text)
BreakComponents.append(text_2)
BreakComponents.append(key_resp_7)
for thisComponent in BreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Break"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *text_2* updates
    if t >= 5 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "Instructions2"-------
t = 0
Instructions2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
rewardtask=1
# keep track of which components have finished
Instructions2Components = []
Instructions2Components.append(Instr3)
Instructions2Components.append(key_resp_6)
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr3* updates
    if t >= 0.0 and Instr3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr3.tStart = t  # underestimates by a little under one frame
        Instr3.frameNStart = frameN  # exact frame index
        Instr3.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['left', 'right'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions2"-------
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6.keys():
        exec(paramName + '= thisTrial_6.' + paramName)

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6.keys():
            exec(paramName + '= thisTrial_6.' + paramName)
    
    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    reward=random.choice([0,1])
    choice=random.choice([1.2, 1.5, 1.8])
    change=random.choice([0.2, 0.3, 0.4])
    thisTrial=random.choice(realTask)
    if thisTrial==0:
        arrow=random.choice(Green)
        arrow2=arrow
        corrAns=arrow.partition("_")[0]
        
    elif thisTrial==1:
        arrow=random.choice(Green)
        if arrow=="left_green.jpg":
            arrow2="left_red.jpg"
        elif arrow=="right_green.jpg":
            arrow2="right_red.jpg"
        corrAns=""
    # keep track of which components have finished
    ITIComponents = []
    ITIComponents.append(ISI)
    ITIComponents.append(Cross)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Cross* updates
        if t >= 0.0 and Cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cross.tStart = t  # underestimates by a little under one frame
            Cross.frameNStart = frameN  # exact frame index
            Cross.setAutoDraw(True)
        if Cross.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(choice)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_trial = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_trial.status = NOT_STARTED
    image1.setImage(arrow)
    image2.setImage(arrow2)
    
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(key_resp_trial)
    TrialComponents.append(image1)
    TrialComponents.append(image2)
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_trial* updates
        if t >= 0.0 and key_resp_trial.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_trial.tStart = t  # underestimates by a little under one frame
            key_resp_trial.frameNStart = frameN  # exact frame index
            key_resp_trial.status = STARTED
            # keyboard checking is just starting
            key_resp_trial.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_trial.status == STARTED and t >= (0.0 + (2.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            key_resp_trial.status = STOPPED
        if key_resp_trial.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_trial.keys = theseKeys[-1]  # just the last key pressed
                key_resp_trial.rt = key_resp_trial.clock.getTime()
                # was this 'correct'?
                if (key_resp_trial.keys == str(corrAns)) or (key_resp_trial.keys == corrAns):
                    key_resp_trial.corr = 1
                else:
                    key_resp_trial.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *image1* updates
        if t >= 0.0 and image1.status == NOT_STARTED:
            # keep track of start time/frame for later
            image1.tStart = t  # underestimates by a little under one frame
            image1.frameNStart = frameN  # exact frame index
            image1.setAutoDraw(True)
        if image1.status == STARTED and t >= (0.0 + (change + .5-win.monitorFramePeriod*0.75)): #most of one frame period left
            image1.setAutoDraw(False)
        
        # *image2* updates
        if t >= change and image2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image2.tStart = t  # underestimates by a little under one frame
            image2.frameNStart = frameN  # exact frame index
            image2.setAutoDraw(True)
        if image2.status == STARTED and t >= (change + (1.9-win.monitorFramePeriod*0.75)): #most of one frame period left
            image2.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_trial.keys in ['', [], None]:  # No response was made
       key_resp_trial.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': key_resp_trial.corr = 1  # correct non-response
       else: key_resp_trial.corr = 0  # failed to respond (incorrectly)
    # store data for trials_6 (TrialHandler)
    trials_6.addData('key_resp_trial.keys',key_resp_trial.keys)
    trials_6.addData('key_resp_trial.corr', key_resp_trial.corr)
    if key_resp_trial.keys != None:  # we had a response
        trials_6.addData('key_resp_trial.rt', key_resp_trial.rt)
    if reward==0:
        outcome=""
        total=total
        Overall=Overall
    elif reward==1 and arrow2.partition("_")[-1]=="red.jpg" and not key_resp_trial.keys:
        outcome="You earned $1"
        total=total+1
        Overall=Overall+1
    elif reward==1 and arrow2.partition("_")[-1]=="red.jpg" and key_resp_trial.keys:
        outcome=""
        total=total
        Overall=Overall
    elif reward==1 and arrow2.partition("_")[-1]=="green.jpg":
        outcome=""
        total=total
        Overall=Overall
    else:
        outcome="There was an error."
        total=total
        Overall=Overall
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Response"-------
    t = 0
    ResponseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    Feedback.setText(outcome)
    thisExp.addData("ITI", choice)
    thisExp.addData("Changes", change)
    thisExp.addData("Arrow1", arrow)
    thisExp.addData("Arrow2", arrow2)
    thisExp.addData("StopTrial", thisTrial) # is it a stop trial?
    thisExp.addData("RewardTask", rewardtask) # does this task have reward?
    thisExp.addData("RewardActive", reward) # is the reward active?
    if rewardtask==0:
        thisExp.addData("GotDollar", 0)
    elif rewardtask==1:
        if thisTrial==1 and reward==1:
            thisExp.addData("GotDollar", 1)
        else:
            thisExp.addData("GotDollar", 0)
    else:
        thisExp.addData("GotDollar", 2)
    thisExp.addData("CumulativeBlock", total)
    thisExp.addData("CumulativeOverall", Overall)
    # keep track of which components have finished
    ResponseComponents = []
    ResponseComponents.append(Feedback)
    for thisComponent in ResponseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Response"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ResponseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Feedback* updates
        if t >= 0.0 and Feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            Feedback.tStart = t  # underestimates by a little under one frame
            Feedback.frameNStart = frameN  # exact frame index
            Feedback.setAutoDraw(True)
        if Feedback.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Feedback.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Response"-------
    for thisComponent in ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 50 repeats of 'trials_6'


#------Prepare to start Routine "RewardBreak"-------
t = 0
RewardBreakClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

Banked.setText(u"So far, you've banked a total of\n%2.f dollar(s)." %Overall)
Breatherender = event.BuilderKeyResponse()  # create an object of type KeyResponse
Breatherender.status = NOT_STARTED
# keep track of which components have finished
RewardBreakComponents = []
RewardBreakComponents.append(Banked)
RewardBreakComponents.append(Breatherender)
RewardBreakComponents.append(BreatherStarter)
for thisComponent in RewardBreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "RewardBreak"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = RewardBreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *Banked* updates
    if t >= 0.0 and Banked.status == NOT_STARTED:
        # keep track of start time/frame for later
        Banked.tStart = t  # underestimates by a little under one frame
        Banked.frameNStart = frameN  # exact frame index
        Banked.setAutoDraw(True)
    
    # *Breatherender* updates
    if t >= .5 and Breatherender.status == NOT_STARTED:
        # keep track of start time/frame for later
        Breatherender.tStart = t  # underestimates by a little under one frame
        Breatherender.frameNStart = frameN  # exact frame index
        Breatherender.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Breatherender.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *BreatherStarter* updates
    if t >= 0.5 and BreatherStarter.status == NOT_STARTED:
        # keep track of start time/frame for later
        BreatherStarter.tStart = t  # underestimates by a little under one frame
        BreatherStarter.frameNStart = frameN  # exact frame index
        BreatherStarter.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RewardBreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "RewardBreak"-------
for thisComponent in RewardBreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
total=0
# the Routine "RewardBreak" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_7 = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials_7')
thisExp.addLoop(trials_7)  # add the loop to the experiment
thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_7.rgb)
if thisTrial_7 != None:
    for paramName in thisTrial_7.keys():
        exec(paramName + '= thisTrial_7.' + paramName)

for thisTrial_7 in trials_7:
    currentLoop = trials_7
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7.keys():
            exec(paramName + '= thisTrial_7.' + paramName)
    
    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    reward=random.choice([0,1])
    choice=random.choice([1.2, 1.5, 1.8])
    change=random.choice([0.2, 0.3, 0.4])
    thisTrial=random.choice(realTask)
    if thisTrial==0:
        arrow=random.choice(Green)
        arrow2=arrow
        corrAns=arrow.partition("_")[0]
        
    elif thisTrial==1:
        arrow=random.choice(Green)
        if arrow=="left_green.jpg":
            arrow2="left_red.jpg"
        elif arrow=="right_green.jpg":
            arrow2="right_red.jpg"
        corrAns=""
    # keep track of which components have finished
    ITIComponents = []
    ITIComponents.append(ISI)
    ITIComponents.append(Cross)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Cross* updates
        if t >= 0.0 and Cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cross.tStart = t  # underestimates by a little under one frame
            Cross.frameNStart = frameN  # exact frame index
            Cross.setAutoDraw(True)
        if Cross.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(choice)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_trial = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_trial.status = NOT_STARTED
    image1.setImage(arrow)
    image2.setImage(arrow2)
    
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(key_resp_trial)
    TrialComponents.append(image1)
    TrialComponents.append(image2)
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_trial* updates
        if t >= 0.0 and key_resp_trial.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_trial.tStart = t  # underestimates by a little under one frame
            key_resp_trial.frameNStart = frameN  # exact frame index
            key_resp_trial.status = STARTED
            # keyboard checking is just starting
            key_resp_trial.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_trial.status == STARTED and t >= (0.0 + (2.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            key_resp_trial.status = STOPPED
        if key_resp_trial.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_trial.keys = theseKeys[-1]  # just the last key pressed
                key_resp_trial.rt = key_resp_trial.clock.getTime()
                # was this 'correct'?
                if (key_resp_trial.keys == str(corrAns)) or (key_resp_trial.keys == corrAns):
                    key_resp_trial.corr = 1
                else:
                    key_resp_trial.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *image1* updates
        if t >= 0.0 and image1.status == NOT_STARTED:
            # keep track of start time/frame for later
            image1.tStart = t  # underestimates by a little under one frame
            image1.frameNStart = frameN  # exact frame index
            image1.setAutoDraw(True)
        if image1.status == STARTED and t >= (0.0 + (change + .5-win.monitorFramePeriod*0.75)): #most of one frame period left
            image1.setAutoDraw(False)
        
        # *image2* updates
        if t >= change and image2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image2.tStart = t  # underestimates by a little under one frame
            image2.frameNStart = frameN  # exact frame index
            image2.setAutoDraw(True)
        if image2.status == STARTED and t >= (change + (1.9-win.monitorFramePeriod*0.75)): #most of one frame period left
            image2.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_trial.keys in ['', [], None]:  # No response was made
       key_resp_trial.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': key_resp_trial.corr = 1  # correct non-response
       else: key_resp_trial.corr = 0  # failed to respond (incorrectly)
    # store data for trials_7 (TrialHandler)
    trials_7.addData('key_resp_trial.keys',key_resp_trial.keys)
    trials_7.addData('key_resp_trial.corr', key_resp_trial.corr)
    if key_resp_trial.keys != None:  # we had a response
        trials_7.addData('key_resp_trial.rt', key_resp_trial.rt)
    if reward==0:
        outcome=""
        total=total
        Overall=Overall
    elif reward==1 and arrow2.partition("_")[-1]=="red.jpg" and not key_resp_trial.keys:
        outcome="You earned $1"
        total=total+1
        Overall=Overall+1
    elif reward==1 and arrow2.partition("_")[-1]=="red.jpg" and key_resp_trial.keys:
        outcome=""
        total=total
        Overall=Overall
    elif reward==1 and arrow2.partition("_")[-1]=="green.jpg":
        outcome=""
        total=total
        Overall=Overall
    else:
        outcome="There was an error."
        total=total
        Overall=Overall
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Response"-------
    t = 0
    ResponseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    Feedback.setText(outcome)
    thisExp.addData("ITI", choice)
    thisExp.addData("Changes", change)
    thisExp.addData("Arrow1", arrow)
    thisExp.addData("Arrow2", arrow2)
    thisExp.addData("StopTrial", thisTrial) # is it a stop trial?
    thisExp.addData("RewardTask", rewardtask) # does this task have reward?
    thisExp.addData("RewardActive", reward) # is the reward active?
    if rewardtask==0:
        thisExp.addData("GotDollar", 0)
    elif rewardtask==1:
        if thisTrial==1 and reward==1:
            thisExp.addData("GotDollar", 1)
        else:
            thisExp.addData("GotDollar", 0)
    else:
        thisExp.addData("GotDollar", 2)
    thisExp.addData("CumulativeBlock", total)
    thisExp.addData("CumulativeOverall", Overall)
    # keep track of which components have finished
    ResponseComponents = []
    ResponseComponents.append(Feedback)
    for thisComponent in ResponseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Response"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ResponseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Feedback* updates
        if t >= 0.0 and Feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            Feedback.tStart = t  # underestimates by a little under one frame
            Feedback.frameNStart = frameN  # exact frame index
            Feedback.setAutoDraw(True)
        if Feedback.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Feedback.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Response"-------
    for thisComponent in ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 50 repeats of 'trials_7'


#------Prepare to start Routine "RewardBreak"-------
t = 0
RewardBreakClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

Banked.setText(u"So far, you've banked a total of\n%2.f dollar(s)." %Overall)
Breatherender = event.BuilderKeyResponse()  # create an object of type KeyResponse
Breatherender.status = NOT_STARTED
# keep track of which components have finished
RewardBreakComponents = []
RewardBreakComponents.append(Banked)
RewardBreakComponents.append(Breatherender)
RewardBreakComponents.append(BreatherStarter)
for thisComponent in RewardBreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "RewardBreak"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = RewardBreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *Banked* updates
    if t >= 0.0 and Banked.status == NOT_STARTED:
        # keep track of start time/frame for later
        Banked.tStart = t  # underestimates by a little under one frame
        Banked.frameNStart = frameN  # exact frame index
        Banked.setAutoDraw(True)
    
    # *Breatherender* updates
    if t >= .5 and Breatherender.status == NOT_STARTED:
        # keep track of start time/frame for later
        Breatherender.tStart = t  # underestimates by a little under one frame
        Breatherender.frameNStart = frameN  # exact frame index
        Breatherender.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Breatherender.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *BreatherStarter* updates
    if t >= 0.5 and BreatherStarter.status == NOT_STARTED:
        # keep track of start time/frame for later
        BreatherStarter.tStart = t  # underestimates by a little under one frame
        BreatherStarter.frameNStart = frameN  # exact frame index
        BreatherStarter.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RewardBreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "RewardBreak"-------
for thisComponent in RewardBreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
total=0
# the Routine "RewardBreak" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_8 = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials_8')
thisExp.addLoop(trials_8)  # add the loop to the experiment
thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_8.rgb)
if thisTrial_8 != None:
    for paramName in thisTrial_8.keys():
        exec(paramName + '= thisTrial_8.' + paramName)

for thisTrial_8 in trials_8:
    currentLoop = trials_8
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8.keys():
            exec(paramName + '= thisTrial_8.' + paramName)
    
    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    reward=random.choice([0,1])
    choice=random.choice([1.2, 1.5, 1.8])
    change=random.choice([0.2, 0.3, 0.4])
    thisTrial=random.choice(realTask)
    if thisTrial==0:
        arrow=random.choice(Green)
        arrow2=arrow
        corrAns=arrow.partition("_")[0]
        
    elif thisTrial==1:
        arrow=random.choice(Green)
        if arrow=="left_green.jpg":
            arrow2="left_red.jpg"
        elif arrow=="right_green.jpg":
            arrow2="right_red.jpg"
        corrAns=""
    # keep track of which components have finished
    ITIComponents = []
    ITIComponents.append(ISI)
    ITIComponents.append(Cross)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Cross* updates
        if t >= 0.0 and Cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cross.tStart = t  # underestimates by a little under one frame
            Cross.frameNStart = frameN  # exact frame index
            Cross.setAutoDraw(True)
        if Cross.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(choice)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_trial = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_trial.status = NOT_STARTED
    image1.setImage(arrow)
    image2.setImage(arrow2)
    
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(key_resp_trial)
    TrialComponents.append(image1)
    TrialComponents.append(image2)
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_trial* updates
        if t >= 0.0 and key_resp_trial.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_trial.tStart = t  # underestimates by a little under one frame
            key_resp_trial.frameNStart = frameN  # exact frame index
            key_resp_trial.status = STARTED
            # keyboard checking is just starting
            key_resp_trial.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_trial.status == STARTED and t >= (0.0 + (2.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            key_resp_trial.status = STOPPED
        if key_resp_trial.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_trial.keys = theseKeys[-1]  # just the last key pressed
                key_resp_trial.rt = key_resp_trial.clock.getTime()
                # was this 'correct'?
                if (key_resp_trial.keys == str(corrAns)) or (key_resp_trial.keys == corrAns):
                    key_resp_trial.corr = 1
                else:
                    key_resp_trial.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *image1* updates
        if t >= 0.0 and image1.status == NOT_STARTED:
            # keep track of start time/frame for later
            image1.tStart = t  # underestimates by a little under one frame
            image1.frameNStart = frameN  # exact frame index
            image1.setAutoDraw(True)
        if image1.status == STARTED and t >= (0.0 + (change + .5-win.monitorFramePeriod*0.75)): #most of one frame period left
            image1.setAutoDraw(False)
        
        # *image2* updates
        if t >= change and image2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image2.tStart = t  # underestimates by a little under one frame
            image2.frameNStart = frameN  # exact frame index
            image2.setAutoDraw(True)
        if image2.status == STARTED and t >= (change + (1.9-win.monitorFramePeriod*0.75)): #most of one frame period left
            image2.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_trial.keys in ['', [], None]:  # No response was made
       key_resp_trial.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': key_resp_trial.corr = 1  # correct non-response
       else: key_resp_trial.corr = 0  # failed to respond (incorrectly)
    # store data for trials_8 (TrialHandler)
    trials_8.addData('key_resp_trial.keys',key_resp_trial.keys)
    trials_8.addData('key_resp_trial.corr', key_resp_trial.corr)
    if key_resp_trial.keys != None:  # we had a response
        trials_8.addData('key_resp_trial.rt', key_resp_trial.rt)
    if reward==0:
        outcome=""
        total=total
        Overall=Overall
    elif reward==1 and arrow2.partition("_")[-1]=="red.jpg" and not key_resp_trial.keys:
        outcome="You earned $1"
        total=total+1
        Overall=Overall+1
    elif reward==1 and arrow2.partition("_")[-1]=="red.jpg" and key_resp_trial.keys:
        outcome=""
        total=total
        Overall=Overall
    elif reward==1 and arrow2.partition("_")[-1]=="green.jpg":
        outcome=""
        total=total
        Overall=Overall
    else:
        outcome="There was an error."
        total=total
        Overall=Overall
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Response"-------
    t = 0
    ResponseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    Feedback.setText(outcome)
    thisExp.addData("ITI", choice)
    thisExp.addData("Changes", change)
    thisExp.addData("Arrow1", arrow)
    thisExp.addData("Arrow2", arrow2)
    thisExp.addData("StopTrial", thisTrial) # is it a stop trial?
    thisExp.addData("RewardTask", rewardtask) # does this task have reward?
    thisExp.addData("RewardActive", reward) # is the reward active?
    if rewardtask==0:
        thisExp.addData("GotDollar", 0)
    elif rewardtask==1:
        if thisTrial==1 and reward==1:
            thisExp.addData("GotDollar", 1)
        else:
            thisExp.addData("GotDollar", 0)
    else:
        thisExp.addData("GotDollar", 2)
    thisExp.addData("CumulativeBlock", total)
    thisExp.addData("CumulativeOverall", Overall)
    # keep track of which components have finished
    ResponseComponents = []
    ResponseComponents.append(Feedback)
    for thisComponent in ResponseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Response"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ResponseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Feedback* updates
        if t >= 0.0 and Feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            Feedback.tStart = t  # underestimates by a little under one frame
            Feedback.frameNStart = frameN  # exact frame index
            Feedback.setAutoDraw(True)
        if Feedback.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Feedback.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Response"-------
    for thisComponent in ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 50 repeats of 'trials_8'


#------Prepare to start Routine "RewardBreak"-------
t = 0
RewardBreakClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

Banked.setText(u"So far, you've banked a total of\n%2.f dollar(s)." %Overall)
Breatherender = event.BuilderKeyResponse()  # create an object of type KeyResponse
Breatherender.status = NOT_STARTED
# keep track of which components have finished
RewardBreakComponents = []
RewardBreakComponents.append(Banked)
RewardBreakComponents.append(Breatherender)
RewardBreakComponents.append(BreatherStarter)
for thisComponent in RewardBreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "RewardBreak"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = RewardBreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *Banked* updates
    if t >= 0.0 and Banked.status == NOT_STARTED:
        # keep track of start time/frame for later
        Banked.tStart = t  # underestimates by a little under one frame
        Banked.frameNStart = frameN  # exact frame index
        Banked.setAutoDraw(True)
    
    # *Breatherender* updates
    if t >= .5 and Breatherender.status == NOT_STARTED:
        # keep track of start time/frame for later
        Breatherender.tStart = t  # underestimates by a little under one frame
        Breatherender.frameNStart = frameN  # exact frame index
        Breatherender.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Breatherender.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *BreatherStarter* updates
    if t >= 0.5 and BreatherStarter.status == NOT_STARTED:
        # keep track of start time/frame for later
        BreatherStarter.tStart = t  # underestimates by a little under one frame
        BreatherStarter.frameNStart = frameN  # exact frame index
        BreatherStarter.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RewardBreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "RewardBreak"-------
for thisComponent in RewardBreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
total=0
# the Routine "RewardBreak" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_9 = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials_9')
thisExp.addLoop(trials_9)  # add the loop to the experiment
thisTrial_9 = trials_9.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_9.rgb)
if thisTrial_9 != None:
    for paramName in thisTrial_9.keys():
        exec(paramName + '= thisTrial_9.' + paramName)

for thisTrial_9 in trials_9:
    currentLoop = trials_9
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
    if thisTrial_9 != None:
        for paramName in thisTrial_9.keys():
            exec(paramName + '= thisTrial_9.' + paramName)
    
    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    reward=random.choice([0,1])
    choice=random.choice([1.2, 1.5, 1.8])
    change=random.choice([0.2, 0.3, 0.4])
    thisTrial=random.choice(realTask)
    if thisTrial==0:
        arrow=random.choice(Green)
        arrow2=arrow
        corrAns=arrow.partition("_")[0]
        
    elif thisTrial==1:
        arrow=random.choice(Green)
        if arrow=="left_green.jpg":
            arrow2="left_red.jpg"
        elif arrow=="right_green.jpg":
            arrow2="right_red.jpg"
        corrAns=""
    # keep track of which components have finished
    ITIComponents = []
    ITIComponents.append(ISI)
    ITIComponents.append(Cross)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Cross* updates
        if t >= 0.0 and Cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cross.tStart = t  # underestimates by a little under one frame
            Cross.frameNStart = frameN  # exact frame index
            Cross.setAutoDraw(True)
        if Cross.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(choice)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_trial = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_trial.status = NOT_STARTED
    image1.setImage(arrow)
    image2.setImage(arrow2)
    
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(key_resp_trial)
    TrialComponents.append(image1)
    TrialComponents.append(image2)
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_trial* updates
        if t >= 0.0 and key_resp_trial.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_trial.tStart = t  # underestimates by a little under one frame
            key_resp_trial.frameNStart = frameN  # exact frame index
            key_resp_trial.status = STARTED
            # keyboard checking is just starting
            key_resp_trial.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_trial.status == STARTED and t >= (0.0 + (2.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            key_resp_trial.status = STOPPED
        if key_resp_trial.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_trial.keys = theseKeys[-1]  # just the last key pressed
                key_resp_trial.rt = key_resp_trial.clock.getTime()
                # was this 'correct'?
                if (key_resp_trial.keys == str(corrAns)) or (key_resp_trial.keys == corrAns):
                    key_resp_trial.corr = 1
                else:
                    key_resp_trial.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *image1* updates
        if t >= 0.0 and image1.status == NOT_STARTED:
            # keep track of start time/frame for later
            image1.tStart = t  # underestimates by a little under one frame
            image1.frameNStart = frameN  # exact frame index
            image1.setAutoDraw(True)
        if image1.status == STARTED and t >= (0.0 + (change + .5-win.monitorFramePeriod*0.75)): #most of one frame period left
            image1.setAutoDraw(False)
        
        # *image2* updates
        if t >= change and image2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image2.tStart = t  # underestimates by a little under one frame
            image2.frameNStart = frameN  # exact frame index
            image2.setAutoDraw(True)
        if image2.status == STARTED and t >= (change + (1.9-win.monitorFramePeriod*0.75)): #most of one frame period left
            image2.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_trial.keys in ['', [], None]:  # No response was made
       key_resp_trial.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': key_resp_trial.corr = 1  # correct non-response
       else: key_resp_trial.corr = 0  # failed to respond (incorrectly)
    # store data for trials_9 (TrialHandler)
    trials_9.addData('key_resp_trial.keys',key_resp_trial.keys)
    trials_9.addData('key_resp_trial.corr', key_resp_trial.corr)
    if key_resp_trial.keys != None:  # we had a response
        trials_9.addData('key_resp_trial.rt', key_resp_trial.rt)
    if reward==0:
        outcome=""
        total=total
        Overall=Overall
    elif reward==1 and arrow2.partition("_")[-1]=="red.jpg" and not key_resp_trial.keys:
        outcome="You earned $1"
        total=total+1
        Overall=Overall+1
    elif reward==1 and arrow2.partition("_")[-1]=="red.jpg" and key_resp_trial.keys:
        outcome=""
        total=total
        Overall=Overall
    elif reward==1 and arrow2.partition("_")[-1]=="green.jpg":
        outcome=""
        total=total
        Overall=Overall
    else:
        outcome="There was an error."
        total=total
        Overall=Overall
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Response"-------
    t = 0
    ResponseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    Feedback.setText(outcome)
    thisExp.addData("ITI", choice)
    thisExp.addData("Changes", change)
    thisExp.addData("Arrow1", arrow)
    thisExp.addData("Arrow2", arrow2)
    thisExp.addData("StopTrial", thisTrial) # is it a stop trial?
    thisExp.addData("RewardTask", rewardtask) # does this task have reward?
    thisExp.addData("RewardActive", reward) # is the reward active?
    if rewardtask==0:
        thisExp.addData("GotDollar", 0)
    elif rewardtask==1:
        if thisTrial==1 and reward==1:
            thisExp.addData("GotDollar", 1)
        else:
            thisExp.addData("GotDollar", 0)
    else:
        thisExp.addData("GotDollar", 2)
    thisExp.addData("CumulativeBlock", total)
    thisExp.addData("CumulativeOverall", Overall)
    # keep track of which components have finished
    ResponseComponents = []
    ResponseComponents.append(Feedback)
    for thisComponent in ResponseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Response"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ResponseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Feedback* updates
        if t >= 0.0 and Feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            Feedback.tStart = t  # underestimates by a little under one frame
            Feedback.frameNStart = frameN  # exact frame index
            Feedback.setAutoDraw(True)
        if Feedback.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Feedback.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Response"-------
    for thisComponent in ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 50 repeats of 'trials_9'


#------Prepare to start Routine "RewardBreak"-------
t = 0
RewardBreakClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

Banked.setText(u"So far, you've banked a total of\n%2.f dollar(s)." %Overall)
Breatherender = event.BuilderKeyResponse()  # create an object of type KeyResponse
Breatherender.status = NOT_STARTED
# keep track of which components have finished
RewardBreakComponents = []
RewardBreakComponents.append(Banked)
RewardBreakComponents.append(Breatherender)
RewardBreakComponents.append(BreatherStarter)
for thisComponent in RewardBreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "RewardBreak"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = RewardBreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *Banked* updates
    if t >= 0.0 and Banked.status == NOT_STARTED:
        # keep track of start time/frame for later
        Banked.tStart = t  # underestimates by a little under one frame
        Banked.frameNStart = frameN  # exact frame index
        Banked.setAutoDraw(True)
    
    # *Breatherender* updates
    if t >= .5 and Breatherender.status == NOT_STARTED:
        # keep track of start time/frame for later
        Breatherender.tStart = t  # underestimates by a little under one frame
        Breatherender.frameNStart = frameN  # exact frame index
        Breatherender.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Breatherender.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *BreatherStarter* updates
    if t >= 0.5 and BreatherStarter.status == NOT_STARTED:
        # keep track of start time/frame for later
        BreatherStarter.tStart = t  # underestimates by a little under one frame
        BreatherStarter.frameNStart = frameN  # exact frame index
        BreatherStarter.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RewardBreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "RewardBreak"-------
for thisComponent in RewardBreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
total=0
# the Routine "RewardBreak" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_10 = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials_10')
thisExp.addLoop(trials_10)  # add the loop to the experiment
thisTrial_10 = trials_10.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_10.rgb)
if thisTrial_10 != None:
    for paramName in thisTrial_10.keys():
        exec(paramName + '= thisTrial_10.' + paramName)

for thisTrial_10 in trials_10:
    currentLoop = trials_10
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
    if thisTrial_10 != None:
        for paramName in thisTrial_10.keys():
            exec(paramName + '= thisTrial_10.' + paramName)
    
    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    reward=random.choice([0,1])
    choice=random.choice([1.2, 1.5, 1.8])
    change=random.choice([0.2, 0.3, 0.4])
    thisTrial=random.choice(realTask)
    if thisTrial==0:
        arrow=random.choice(Green)
        arrow2=arrow
        corrAns=arrow.partition("_")[0]
        
    elif thisTrial==1:
        arrow=random.choice(Green)
        if arrow=="left_green.jpg":
            arrow2="left_red.jpg"
        elif arrow=="right_green.jpg":
            arrow2="right_red.jpg"
        corrAns=""
    # keep track of which components have finished
    ITIComponents = []
    ITIComponents.append(ISI)
    ITIComponents.append(Cross)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Cross* updates
        if t >= 0.0 and Cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cross.tStart = t  # underestimates by a little under one frame
            Cross.frameNStart = frameN  # exact frame index
            Cross.setAutoDraw(True)
        if Cross.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(choice)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_trial = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_trial.status = NOT_STARTED
    image1.setImage(arrow)
    image2.setImage(arrow2)
    
    # keep track of which components have finished
    TrialComponents = []
    TrialComponents.append(key_resp_trial)
    TrialComponents.append(image1)
    TrialComponents.append(image2)
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_trial* updates
        if t >= 0.0 and key_resp_trial.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_trial.tStart = t  # underestimates by a little under one frame
            key_resp_trial.frameNStart = frameN  # exact frame index
            key_resp_trial.status = STARTED
            # keyboard checking is just starting
            key_resp_trial.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_trial.status == STARTED and t >= (0.0 + (2.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            key_resp_trial.status = STOPPED
        if key_resp_trial.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_trial.keys = theseKeys[-1]  # just the last key pressed
                key_resp_trial.rt = key_resp_trial.clock.getTime()
                # was this 'correct'?
                if (key_resp_trial.keys == str(corrAns)) or (key_resp_trial.keys == corrAns):
                    key_resp_trial.corr = 1
                else:
                    key_resp_trial.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *image1* updates
        if t >= 0.0 and image1.status == NOT_STARTED:
            # keep track of start time/frame for later
            image1.tStart = t  # underestimates by a little under one frame
            image1.frameNStart = frameN  # exact frame index
            image1.setAutoDraw(True)
        if image1.status == STARTED and t >= (0.0 + (change + .5-win.monitorFramePeriod*0.75)): #most of one frame period left
            image1.setAutoDraw(False)
        
        # *image2* updates
        if t >= change and image2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image2.tStart = t  # underestimates by a little under one frame
            image2.frameNStart = frameN  # exact frame index
            image2.setAutoDraw(True)
        if image2.status == STARTED and t >= (change + (1.9-win.monitorFramePeriod*0.75)): #most of one frame period left
            image2.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_trial.keys in ['', [], None]:  # No response was made
       key_resp_trial.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': key_resp_trial.corr = 1  # correct non-response
       else: key_resp_trial.corr = 0  # failed to respond (incorrectly)
    # store data for trials_10 (TrialHandler)
    trials_10.addData('key_resp_trial.keys',key_resp_trial.keys)
    trials_10.addData('key_resp_trial.corr', key_resp_trial.corr)
    if key_resp_trial.keys != None:  # we had a response
        trials_10.addData('key_resp_trial.rt', key_resp_trial.rt)
    if reward==0:
        outcome=""
        total=total
        Overall=Overall
    elif reward==1 and arrow2.partition("_")[-1]=="red.jpg" and not key_resp_trial.keys:
        outcome="You earned $1"
        total=total+1
        Overall=Overall+1
    elif reward==1 and arrow2.partition("_")[-1]=="red.jpg" and key_resp_trial.keys:
        outcome=""
        total=total
        Overall=Overall
    elif reward==1 and arrow2.partition("_")[-1]=="green.jpg":
        outcome=""
        total=total
        Overall=Overall
    else:
        outcome="There was an error."
        total=total
        Overall=Overall
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Response"-------
    t = 0
    ResponseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    Feedback.setText(outcome)
    thisExp.addData("ITI", choice)
    thisExp.addData("Changes", change)
    thisExp.addData("Arrow1", arrow)
    thisExp.addData("Arrow2", arrow2)
    thisExp.addData("StopTrial", thisTrial) # is it a stop trial?
    thisExp.addData("RewardTask", rewardtask) # does this task have reward?
    thisExp.addData("RewardActive", reward) # is the reward active?
    if rewardtask==0:
        thisExp.addData("GotDollar", 0)
    elif rewardtask==1:
        if thisTrial==1 and reward==1:
            thisExp.addData("GotDollar", 1)
        else:
            thisExp.addData("GotDollar", 0)
    else:
        thisExp.addData("GotDollar", 2)
    thisExp.addData("CumulativeBlock", total)
    thisExp.addData("CumulativeOverall", Overall)
    # keep track of which components have finished
    ResponseComponents = []
    ResponseComponents.append(Feedback)
    for thisComponent in ResponseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Response"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ResponseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Feedback* updates
        if t >= 0.0 and Feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            Feedback.tStart = t  # underestimates by a little under one frame
            Feedback.frameNStart = frameN  # exact frame index
            Feedback.setAutoDraw(True)
        if Feedback.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Feedback.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Response"-------
    for thisComponent in ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 50 repeats of 'trials_10'


#------Prepare to start Routine "Earnings"-------
t = 0
EarningsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
EarningTotal.setText(u"All finished! You banked a total of\n%2.f dollar(s)." %Overall)
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
EarningsComponents = []
EarningsComponents.append(EarningTotal)
EarningsComponents.append(Continue)
EarningsComponents.append(key_resp_3)
for thisComponent in EarningsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Earnings"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = EarningsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EarningTotal* updates
    if t >= 0.0 and EarningTotal.status == NOT_STARTED:
        # keep track of start time/frame for later
        EarningTotal.tStart = t  # underestimates by a little under one frame
        EarningTotal.frameNStart = frameN  # exact frame index
        EarningTotal.setAutoDraw(True)
    
    # *Continue* updates
    if t >= 0.0 and Continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        Continue.tStart = t  # underestimates by a little under one frame
        Continue.frameNStart = frameN  # exact frame index
        Continue.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EarningsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Earnings"-------
for thisComponent in EarningsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Earnings" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


win.close()
core.quit()