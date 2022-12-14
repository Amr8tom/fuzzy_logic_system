#20198060
#amr alaa ali

#20198107
import pandas
import  matplotlib.pyplot as plt
##exp_level
l1=["beginner","TRI",[1,15,30]]
l2=["intermediate","TRI",[1,15,30]]
l3=["expert","TRI",[1,15,30]]
## proj_funding
s1=["very_low","TRAP",[0,0,10,30]]
s2=["low","TRAP",[10,30,40,60]]
s3=["medium","TRAP",[40,60,70,90]]
s4=["high","TRAP",[70,90,100,100]]
class fuzzy_var:
    var_name=""
    var_type=""
    var_range=[]
    def __init__(self,name,type,range):
        self.var_name=name
        self.var_type=str(type).upper()
        self.var_range=range

class fuzzy_set(fuzzy_var):
    name=""
    Type=""
    set=[]
    y=[]
    def __init__(self,name,type,set,vn,vt,vr):
#        super.__init__(vn,vt,vr)
        self.name=name
        self.Type=str(type).upper()
        self.set=set
        if (self.Type=="TRAP"):
            self.y=[0,1,1,0]
        elif(self.Type=="TRI"):
            self.y=[0,1,0]
        else: print("error type")
var1=fuzzy_var("fabric","IN",[0,100])
#begginer=fuzzy_set("begginer","TRI",[0.,0,20,40])
#intermediate=fuzzy_set("intermediate","TRI",[0.,0,20,40])
#expert=fuzzy_set("expert","TRI",[0.,0,20,40])
#print(begginer.name)
#print(begginer.Type)
#print(begginer.set)
degreemember=[]
def fuzzification(degree_of_variable,l):
    # fabric
    len_var=len(l[0])
    stamp=[0,1,1,0]
    if(len_var==3):
        stamp=[0,1,0]
    if(len_var==4):
        stamp=[0,1,1,0]
    #fabric=[soft,ordinary,stiff]
    tot=l
    for set in tot:
        if(degree_of_variable in set):
            for i in range(len(set)):
                if(degree_of_variable==set[i]):
                    degreemember.append(stamp[i])
        elif(degree_of_variable):
            for i in range(len(set)-1):
                if(set[i]<degree_of_variable and degree_of_variable<set[i+1]):
                    x_axis=[set[i],set[i+1]]
                    y_axis=[stamp[i],stamp[i+1]]
                    slop=(y_axis[1]-y_axis[0])/(x_axis[1]-x_axis[0])
                    # y= slop * x + c
                    # c=y- slop * x
                    Intercept=y_axis[0]-slop * x_axis[0]
                    degreemember.append(slop*degree_of_variable+Intercept)
        else:
            degreemember.append(0)
            #degreemember.append(100)
    print(degreemember)
soft=[0,0,20,40]
ordinary=[20,40,60,100]
stiff=[60,80,100,100]
soft
def rules():
    stop_condition=False
    membership1=0
    membership2=0
    out_list=[]
    while(stop_condition==False):
        l=[]
        in1=input("enter IN var")
        operator=input(" set opertator")
        in2=input("enter IN var")
        out=input("enter out var")
        l.append(in1,operator,in2,out)
        for i in l:
            if (l == "x"):
                stop_condition=True
            else:
                stop_condition=False
        for i in range(len(fuzzzy)):
            if(fuzzzy[i].var_name==in1):
                membership1=degreemember[i]
                if("not" in in1):
                    membership1=1-membership1
            if(fuzzzy[i].var_name==in2):
                membership2=degreemember[i]
                if("not" in in2):
                    membership2=1-membership2
        if(operator=="and"):
            temp=min(membership1,membership2)
            out_list.append(temp)
        if(operator=="or"):
            temp=max(membership1,membership2)
            out_list.append((temp))
        for i in range(len(variables)):
            if(variables[i].var_type=="OUT"):
                print(out_list[i])


variables=[]
variablessets=[]
fuzzzy=[]
def Top_mian():
    x=int(input("Fuzzy Logic Toolbox\n===================\n1- Create a new fuzzy system\n2- Quit\n"))
    if(x==1):
        mian_menu()
    elif(x==2):
        print("the program is closed")
    else:
        print("Please enter correct number")
        Top_mian()
def mian_menu():
   x= int(input(" Fuzzy Logic Toolbox \n =================== \n 1- Add variables \n 2- Add fuzzy sets to an existing variable \n 3- Add rules \n 4- Run the simulation on crisp values\n"))
   if (x==1):
       num1=int(input("enter number of variables"))
       for i in range(num1):
           n=str(input("Enter the variable’s name"))
           t=str(input( "type (IN/OUT)"))
           r=list(input( "range ([lower, upper]):"))
           variable=fuzzy_var(name=n,range=r,type=t)
           variables.append(variable)
       mian_menu()
   elif (x==2):
       varname=str(input("Enter the variable’s name:"))
       numsetsinvar=int(input("enter number of sets"))
       tot=[]
       if(len(variables)==0):
           print("Please Inter variables first")
       else:
           for i in range(numsetsinvar):
               fuzzyname=input("Enter the fuzzy set name")
               fuzzytype=input("Enter the  type (TRI/TRAP)")
               value=int(input("Enter the fuzzy set  values"))
               n = int(input("Enter number of elements : "))
               for i in range(0, n):
                   ele = int(input())
                   value.append(ele)
               fuzzySet=[]
               fuzzySet.append(fuzzyname)
               fuzzySet.append(fuzzytype)
               fuzzySet.append(value)
               obj=fuzzy_set(name=fuzzySet[0],type=fuzzySet[1],set=fuzzySet[2],vn=varname)
               fuzzzy.append(obj)
               tot.append(obj.set)
       variablessets.append(tot)
       mian_menu()
   elif (x==3):
       print("Add rules")
       rules()
       mian_menu()
   elif (x==4):
       temp=int(input("Enter the crisp values:\n-----------------------\n"))
       fuzzification(temp,variables[0])
       mian_menu()
   else:
       mian_menu()
Top_mian()
f1=fuzzy_set(name="small",type="TRAP",set=[0,0,20,40],vn="dirt",vt="in",vr=[0,100])
f2=fuzzy_set(name="med",type="TRAP",set=[20,40,60,80],vn="dirt",vt="in",vr=[0,100])
f3=fuzzy_set(name="large",type="TRAP",set=[60,80,100,100],vn="dirt",vt="in",vr=[0,100])
fuzzification(25,[f1.set,f2.set,f3.set])


#begginer=fuzzy_set("begginer","TRI",[0.,0,20,40])
#intermediate=fuzzy_set("intermediate","TRI",[0.,0,20,40])
#expert=fuzzy_set("expert","TRI",[0.,0,20,40])
