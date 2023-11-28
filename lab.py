print("Welcome to Melanie Dental Clinic")
a=str(input("Patient's name: "))
b=str(input("Have you ever been here before(y/n): "))
c=float(input("Patient's Height (in cm): "))
d=float(input("Patient's Weight (in kg): "))
e=str(input("When was the patient last weighed in (1/1/2000 if never weighed)?: "))
f=float(input("What was the patient’s weight (in kg, -1 if never weighed)? : "))
g=int(input("Practitioner’s overall assessment of the patient’s health (-5=very poor to +5=excellent, 0 for neutral) : "))

print("Height: ",c)
print("Weight: ",d)
h=f-d
print("Change from previous weigh in kg :",h)

i=(d/(c*2))*100


print("Your BMI: ",round(i,1))

if i>30:
    print("You are Obese!")
    j=0
elif 29.9>i>25:
    print("You are Overweight!")
    j=3
elif 24.9>i>18.5:
    print("You are Healthy!")
    j=5
elif 18.4>i>17:
    print("You are Underweight!")
    j=3
else:
    print("You are too Thin!")
    j=0
    
print("Your Intermediate Health score is: ",j)

if f==-1:
    k=j+1
    print("New intermeidate health score: ",k)
else:
    if h==0 or h==-1 or h==1:
        k=j-1
        print("New intermeidate health score: ",k)
    else:
        if 18.4>i>17:
            if h<0:
                k=j-3
                print("New intermeidate health score: ",k)
            else:
                k=j+2
                print("New intermeidate health score: ",k)
        elif i<17:
            if h<0:
                k=j-5
                print("New intermeidate health score: ",k)
            else:
                k=j+5
                print("New intermeidate health score: ",k)
        elif 29.9>i>25:
            if h>0:
                k=j-3
                print("New intermeidate health score: ",k)
            elif h<-1:
                k=j+2
                print("New intermeidate health score: ",k)
            else:
                k=j
                print("New intermeidate health score: ",k)
        elif i>30:
            if h>0:
                k=j-5
                print("New intermeidate health score: ",k)
            elif h<-1:
                k=j+5
                print("New intermeidate health score: ",k)
            else:
                k=j
                print("New intermeidate health score: ",k)
        else:
            k=j
            print("New initermediate health score: ",k)

l=k+g

if l>=5:
    print("Great Condition")
elif 5>l>=3:
    print("Need a little Work")
elif 3>l>=1:
    print("Neet a lot of work")
else:
    print("At risk!")
    
print("Melanie Diet Clinic")
print("*-------------------------*")
print("Reciept for Patient name: ",a)
print("Patient weight: ",d)
if e==1/1/2000 or f==-1:
    print("Patient Weight LOSS: NEW")
else:
    print("Patient Weight LOSS: ",h)

if e==1/1/2000 or f==-1:
    print("Days since last visit: First visit")
else:
    print("Days Since last visit: ",e)
print("---------------------------------")
print("BMI: ",i)
print("Health: ",g)
print("---------------------------------")
print("Overall: ",l)
