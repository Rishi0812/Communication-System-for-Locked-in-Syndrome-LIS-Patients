# Communication System for Locked-in Syndrome (LIS) Patients 

## Introduction
Locked-in syndrome is a rare neurological disorder characterized by complete paralysis of voluntary muscles except for those that control the movement of the eyes. A person with locked-in syndrome is conscious and can think and reason but cannot speak or move unless he/she was able to develop one reliable form of communication such as blinking or moving their eyelids to communicate with people around him/her. People with the locked-in syndrome have a reduced quality of life because they are totally dependent on their family members, friends, or a professional caregiver for all their basic needs. No known cure exists for locked-in syndrome and medical practitioners focus on helping the patient find novel ways to communicate.

LIS patients are, in some ways, neither alive nor dead. They are simply locked inside their own minds - unable to communicate with the outside world. It's important to find a way for patients with locked-in syndrome to communicate. Research shows that a key to successful treatment for locked-in syndrome patients is communication. However, it created a unique challenge for doctors and scientists around the world as this form of communication was essential to many patients.

## Proposed Solution
This project focuses on developing an effective communication system for Locked-In Syndrome Patients where they can do essential communications by just blinking their eyes.

The project implements a program that detects and counts the number of blinks. Open CV library is used to measure the euclidian distance of the eyes, then further count the number of blinks. There are three essential commands as of now for the prototype which can be increased according to patient need and comfort, The gTTS library has also been used to generate speech from text and later use that for the commands.

## Interface

This is a demo of the overall interface,

![](https://github.com/Rishi0812/Communication-System-for-Locked-in-Syndrome-LIS-Patients/blob/main/readme_files/demo_gif.gif)


On the count of,
- 3 Blinks - "Help Me" is Triggered
- 4 Blinks - "Sanitary Discomfort" is Triggered
- 5 Blinks - "Contact Family" is Triggered 

If the user does not blink for more than 4 sec at the 3rd blink, i.e if the 3rd Command 'Help Me' stays on the screen unchanged for more than 4 sec, It'll trigger an emergency voice alarm which keeps on saying 'Help Me' untill it's turned off. All the commands are easily and quickly customisable based on user specific needs and behaviour.

The final aim is to improve and observe the patterns of the preferred mode of communications of the patients in order to improve the overall recovery speed.

