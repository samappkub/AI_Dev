# def lovely(ingledient, inerible):
#     ingle = ingledient.split()
#     ineri = inerible.split()
#     count = 0
#     for equitliment in ingle:
#         if equitliment not in ineri:
#             count += 1
#     return count

def decrypt(library, message):
    calem = dict()
    for i in library:
        vals = i.split()
        calem[vals[1]] = vals[0]
    result = ''
    m = message.split()
    for n in m:
        if n not in calem.keys():
            result += '?'
        else:
            result += calem[n]
    return result

library = [
 "H -.-.-.-.-.-.-.-.-.-.",
 "I .-.-.-.-.-.-.-.-.-.-",
 "K -.-.-.-.-.",
 "E .-.-.-.-.-"]
message = "-.-.-.-.-.-.-.-.-.-. .-.-.-.-.-.-.-.-.-.-"
print(decrypt(library, message))

# frank = {'togo': 'jeans', 'galiba': 'ghana2pak', 22: 'Ghana dey bee'}
# print(frank[22])
# print()
# men = 'hhhhhhhhh'
# rand = {}
# for let in men:
#     print(rand.keys())
#     if let in rand.keys():
#         rand[let] = rand[let] + 1
#     else:
#         rand[let] = 1
#     print(rand)
