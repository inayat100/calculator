def two_no(fn,sn,op):
    if op=='+':
        return   fn+sn
    elif op=='-':
        return fn - sn
    elif op=='*':
        return fn * sn
    elif op=='/':
        return fn / sn
    else:
        print("invalid input")
def old_no(old,new,opt):
    if opt=='+':
        return  old + new
    elif opt=='-':
        return old - new
    elif opt=='*':
        return old * new
    elif opt=='/':
        return old/ new
    else:
        print("invalid input")
while True:
    while True:
        print("enter first no")
        fn = int(input())
        print("enter second no")
        sn = int(input())
        print("enter operator")
        op = input()
        old_ans=two_no(fn,sn,op)
        print("----------------    current value= ",old_ans,"      -------------------------")
        print("Do you want to take old Ans... preass Y/N\n")
        ag=input()
        if ag=='y' or ag=='Y':
            break
    while (ag=='y' or ag=='Y'):
        print("------------------     old_value= ", old_ans, " ---------------------")
        print("enter the valuye ")
        new=int(input())
        print("enter the operator")
        opt=input()
        ol=old_no(old_ans,new,opt)
        print(">>>>>>>>>>>>>>>>>>   current value= ", ol, "<<<<<<<<<<<<<<<<<<<<<<")
        # print(ol)
        old_ans=ol
        print("Do you want to take old Ans... preass Y/N\n")
        agn=input()
        if agn=='y' or agn=='Y':
            continue
        else:
            break



# this is my PAT
# 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

