# computer guessing game using binary bisection technique

#introduction
print("Hello there! clear your mind and think of a number between 1 and 100 and I'm gonna guess it in less than eight guesses.")
print('\nPress \'Y\' if my guess is correct \nPress \'N\' if my guess is wrong')
input('press enter to see my guess\n\n')

#algorithm
    
count = 0     #for icreament of loop    
lborder = 0   #lowest value of range
hborder = 100 #highest value of range

while True:   #infinte loop
    guess=round((lborder+hborder)/2) #half value of range assigned with variable 'guess'
    ans = input('Is your number  equal to '+str(guess)+'?') #this response assigned to variable 'ans'
    if ans=='y' or ans== 'Y':
        print('\nthe value you chose is '+str(guess)+'\n'+'\nHurray! I guessed your number in '+str(count)+' tries')
        break   #loop terminates
    elif ans=='n' or ans=='N':
        ans2=input('is your number greater than '+str(guess)+'?') #this response assigned to variable 'ans2'
        if ans2=='n'or ans2=='N':
            hborder = guess   #highest value reassigned to half value of range
        elif ans2 =='y'or ans2=='Y':
            lborder = guess   #lowest value reassigned to half value of range 
    count+=1 
input('\nPress Enter to Exit.')
