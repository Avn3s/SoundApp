from os import listdir
from os import remove
from pygame import mixer
from time import sleep
mixer.init()
print("\nWelcome to Sappy!\n")
print("Here are your saved songs... To add more, move the required audio files to the 'songs' folder.\n")
v=1.0
for i in range(len(listdir('songs'))):
        if listdir('songs')[i]!='ZZZ.txt':
            print(i+1,'.','\t',listdir('songs')[i])
print('\n')
while True:
    n=input("\nChoose function (Enter h for help): ")
    if n.lower()=='p':
        sn=int(input("Specify the song ID from the list: "))
        if sn in range(len(listdir('songs'))):
            s=str(listdir('songs')[sn-1])
            if mixer.music.get_busy()==False:
                print("Now playing:",s)
                mixer.music.load("./songs/"+s)
                mixer.music.set_volume(v)
                mixer.music.play()
            else:
                mixer.music.queue("./songs/"+s)
                print("Queued:",s)
        else:
            print('Invalid function... try again.')
    elif n.lower()=='l':
        print("\nShowing song list.\n")
        for i in range(len(listdir('songs'))):
            if listdir('songs')[i]!='ZZZ.txt':
                print(i+1,'.','\t',listdir('songs')[i])
    elif n.lower()=='v':
        print("Current volume:",mixer.music.get_volume()*100,'%')
        v=(float(input("Enter Volume: ")))/100
        if mixer.music.get_busy()==True:
            mixer.music.set_volume(v)
        print("New volume:",v*100,'%')
    elif n.lower()=='h':
        print("\nKindly ignore the quotes and enter the characters only\n1. Enter 'P' to play a song\n2. Enter 'L' to view the list of songs in the songs folder\n3. Enter 'PP' to pause the current song\n4. Enter 'r' to resume\n5. Enter 'S' to stop playing the current song\n6. Enter 'V' to change the Volume\n7. Enter 'Q' to exit the app")
    elif n.lower()=="pp":
        mixer.music.pause()
    elif n.lower()=="r":
        mixer.music.unpause()
    elif n.lower()=="s":
        mixer.music.stop()
        mixer.music.unload()
    elif n.lower()=="d":
        d=input("Song number to be deleted (enter 'esc' to skip): ")
        if d=='esc':
            continue
        elif int(d)-1 in range(len(listdir('songs'))):
            remove('songs/'+str(listdir('songs')[int(d)-1]))
    elif n.lower()=='q':
        if mixer.music.get_busy()==True:
            mixer.music.stop()
        print("Thank you for using Sappy.\nMade with <3 by Avnes.")
        sleep(6)
        exit()