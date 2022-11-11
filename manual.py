
text= "aa aa bb bb ab ab cc cc dd dd da da"
codes=['$001', '$002', '$003', '$004', '$005', '$006', '$007', '$008', '$009', '$010', '$011', '$012', '$013', '$014', '$015', '$016', '$017', '$018', '$019', '$020', '$021', '$022', '$023', '$024', '$025', '$026', '$027', '$028', 
'$029', '$030', '$031', '$032', '$033', '$034', '$035', '0$36', '$037', '$038', '$039', '$040', '$041', '$042', '$043', '$044', '$045', '$046', '$047', '$048', '$049', '$050', '$051', '$052', '$053', '$054', '$055', '$056', 
'$057', '$058', '$059', '$060', '$061', '$062', '$063', '$064', '$065', '$066', '$067', '$068', '$069', '$070', '$071', '$072', '$073', '$074', '$075', '$076', '$077', '$078', '$079', '$080', '$081', '$082', '$083', '$084', 
'$085', '$086', '$087', '$088', '$089', '$090', '$091', '$092', '$093', '$094', '$095', '$096', '$097', '$098', '$099', '$100', '$101', '$102', '$103', '$104', '$105', '$106', '$107', '$108', '$109', '$110',
 '$111', '$112', '$113', '$114', '$115', '$116', '$117', '$118', '$119', '$120', '$121', '$122', '$123', '$124', '$125', '$126', '$127', '$128']
lens = 0
cntdwn = 0
decryptbl = {}
cont = True
decomp = [] 
temp = []
while True:
    #prompt the user
    
    replacetxt = input("What text do you want to replace \n")
    #do the replacement 
    text = text.replace(replacetxt,codes[lens])
    #add to the lookup list
    decryptbl.update({codes[lens]:replacetxt})
    print(text)
    lens = lens + 1
    continu = input("would you like to continue? y/n, to print everything p \n")
    if continu == "n":
        break
    elif continu == "p":
        print(text)
        print(decryptbl)
        print(lens)
    else:
        continue

print(text)
for element in text:
    print("current element is " + element)
    
    if element == "$":
        #use replace() to replace the element + the next 3 elements with the corespointing value in the dictionary, could make it skip the next 3 elements when $ is detected
        temp = list(temp)
        temp.append(element)
        cntdwn = 3 
        print("temp" + str(temp))
    elif cntdwn > 0:
        temp.append(element)
        print("temp" + str(temp))
        cntdwn = cntdwn - 1
    if len(temp) == 4:
        temp = "".join(temp)
        print(decryptbl)
        print("this is str temp" + temp)
        decomp.append(decryptbl.get(temp))
        print("this is the coresponding value" + decryptbl.get("".join(temp)))
        temp = []
    else:
        print("doing this")
        decomp.append(element)
print("".join(decomp))

'''
#code generator
a = 0
for i in range (128):

    a = a + 1
    a = str(a)
    var = "$" + a  
    a = int(a)
    codes.append(var)
print(codes)
'''