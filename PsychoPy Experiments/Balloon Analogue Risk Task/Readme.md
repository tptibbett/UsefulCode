# The Balloon Analogue Risk Task
## An impulsivity measure in Python
Created (February 22, 2017) by Tom Tibbett in PsychoPy2

PsychoPy2 created by Jonathan Pearce

## Frequently Asked Questions

### Introduction
Hello there!  Though the Balloon Analogue Risk Task (BART; Lejuez et al., 2002) has been very important to the Risk-taking literature, it is potentially difficult to program for researchers unfamiliar with arrays. As such, I decided to edit a demo on Jonathan Pearce's PsychoPy2 to make it easier and more accessible.  

### What were the limitations of the demo the first place?  Why not use it for science?  
Pearce's demo, while very useful for demonstrating the (awesome) ability of PsychoPy2, does not utilize dynamic probabilities for risk.  Basically, the pumps necessary to pop a balloon is hardcoded in the demo ahead of the experiment; altering this requires manually changing a conditions file in Excel; even then, it will not change how risky each progressive pump of the balloon is in the overall task. I'm sure this is possible with the current demo, but likely difficult for those unfamiliar with the moving parts. Similarly, the demo does not have a practice phase or an assessment that the pop is at least pseudo-random in the output as-is.  I created an edited program which addresses these shortcomings, so they can be used in more valid experiments. 

### What do you mean dynamic risk?
Put simply, every time a person puts a pump of air into the balloon, the riskier it becomes to put another pump in. Like a real balloon, it's not particularly risky to put 1 breath of air into a balloon when it is fully deflated.  But as the balloon becomes bigger, the same 1 breath is at greater risk of bursting it. In essence, I call it dynamic risk because the risk *changes* during the task in accordance with the participant's actions.

### How does this BART task operationalize dynamic risk?
The original BART task had multiple balloons with different arrays, essentially making some balloons more risky to fill than others.  For the purposes of simplicity, I have created this task with only one kind of balloon.  How I do it here is that I create Python array from 0 to 126-- this results in 128 possible integers to choose.  During the course of the experiment, every time that a participant pumps the balloon, a random number is selected from the array.  Out of 128 numbers, if the number 0 comes up, the balloon will pop. This means that on the first pump, the participant will have 1/128 odds (or about .781%) of the balloon bursting. However, if the number generator does not give a 0, the array will be trimmed by its last value.  So, 126 gets deleted.  The balloon gets bigger, and now the array is from 0 to 125, resulting in a 1/127 chance of bursting (or about .787%) when the participant next pumps.  After 28 pumps, the next pump has a 1% chance of bursting.  After 64 pumps (by the point where about 50% of balloons should have popped), there is a 1.5% chance of popping.  And that probability begins increasing dramatically as more numbers are trimmed from the array.  At 96 pumps, there's a 3.1% chance.  At 112 pumps, risk increases to 6.25%.  At 124 pumps, there is a 25% chance of the balloon bursting.  Finally, no balloon will survive 128 pumps-- the last number in the array will always be 0.

### How do I change the risk?
I chose 1/128 because it was in the original paper, but in testing different reward structures, you may want to alter the task.  If you open the program in PsychoPy, you need to change the variable Samp.  Samp resides in checkKeys (for Begin Routine) and looks like this: Samp = Samp=list(range(128)). So, if you wanted a balloon that would originally have 1/100 odds of popping, replace 128 with 100.

### What if it doesn't work as-is?
There may be an issue of permissions.  If you're working at an academic institution, make sure you have write access to install things.  If PYO appears to be an issue, that may be a problem unique to your computer, not the program.  PsychoPy has had issues with audio drivers in the past, but they look to be shoring that up for future versions.  You may have to have the relevant libraries that PsychoPy has in order for this script to work-- fortunately, PsychoPy is free, so it's very easy to set up.

### Questions, comments, complaints?
Please email me at tptibbett@gmail.com.  Thanks!