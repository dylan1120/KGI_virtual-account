def check_code(enterprise, serial, test):
    if len(str(enterprise)) == 4 and len(str(serial)) == 9 and len(str(test)) == 3 :
        synthetic = str(enterprise)+str(serial)
        tests = str(test)*4+str(test)[0]
        step1 =[]
        for i in range(len(synthetic)):
            step1.append(str(int(synthetic[i])*int(tests[i])))
        step2 = 0
        for i in range(len(step1)):
            step2 = step2+ int(step1[i][-1])
        step3 = int(str(step2)[-1])
        result = 10-step3
        return result
    else :
        print("input error")
        return None