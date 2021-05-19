def KGI(serial):
    if len(str(serial)) == 10 :
        enterprise = "362"
        tests = "3713713713713"
        synthetic = enterprise+str(serial)
        step1 =[]
        for i in range(len(synthetic)):
            step1.append(str(int(synthetic[i])*int(tests[i])))
        step2 = 0
        for i in range(len(step1)):
            step2 = step2+ int(step1[i][-1])
        step3 = int(str(step2)[-1])
        result = str(10-step3)[-1]
        return enterprise+str(serial)+result
    else :
        print("input error")
        return None