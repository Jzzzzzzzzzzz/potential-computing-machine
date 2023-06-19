def strcounter1(s):
    for sym in s:
        counter = 0
        for sub_sum in s:
            if sub_sum ==sym:
                counter+=1
        print(sym,counter)


strcounter1("12442")

def strcounter_2(s):
    for sum in set(s):
        counter = 0
        for sub_sum in s:
            if sub_sum == sum:
                counter=counter+1
        print(sum,counter)

#strcounter_2("sdferghgflhkrtlhketklwertokwportkwruckiocccccccccccceweweqewqwqqqqweggfgfsdfjsdifjfgohnfgojsigsdfujgsdjigipfddjgiofdjgpodfjiphjjhopiko[ik-idiof0-sdfisdo-fisd-nice")




def strcounter_3(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym,0)+1

    for sym,count in syms_counter.items():
        print(sym,count)



strcounter_3("asfsdfksdfjgedohjdfposoefw4jyoejkg")


















