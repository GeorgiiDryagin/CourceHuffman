
class Node:
    def __init__(self, val):
        self.chars = val[0]
        self.frequency = val[1]
        self.right = None
        self.left = None

def parent(Right, Left):
        node = Node([Right.chars + Left.chars, Right.frequency + Left.frequency])
        node.right = Right
        node.left = Left
        return node



def getAlphabetFrequency(text):
    alphabet = []   # [char, frequency]
    for char in text:
        charFound = False
        for i in alphabet:
            if char == i[0]:
                i[1] += 1
                charFound = True
                break
        if not charFound:
            alphabet.append([char, 1])
    return alphabet

def getFreq(row):
    return row[1]

def getChar(row):
    return row[0]

def decode(codedMessage, codes):
    decoded = ''
    current = ''
    for c in codedMessage:
        current += c
        for code in codes:
            if current == code[1]:
                decoded += code[0]
                current = ''
                break
    return decoded

def unfoldTree(node, code, result):
    if node.right == None and node.left == None:
        result.append([node.chars, code])
        return
    if node.left != None:
        unfoldTree(node.left, code + '0', result);
    if node.right != None:
        unfoldTree(node.right, code + '1', result);

def HuffmanCodes(text):
    alphabetFrequency = getAlphabetFrequency(text)
    alphabetFrequency.sort(key = getFreq)

    for item in alphabetFrequency:
        item.append(Node(item))

    while len(alphabetFrequency) > 1:
        least1 = alphabetFrequency.pop(0)
        least2 = alphabetFrequency.pop(0)
        newItem = [least1[0] + least2[0], least1[1] + least2[1], parent(least1[2], least2[2])]
        
        place = 0
        for item in alphabetFrequency:
            if newItem[1] > item[1]:
                place += 1
            else:
                break
        alphabetFrequency.insert(place, newItem)

    result = []
    unfoldTree(alphabetFrequency[0][2], '', result)
    result.sort(key = getChar)

    codedMessage = ''
    for c in text:
        for r in result:
            if c == r[0]:
                codedMessage += r[1]
                break


    print("Given message: \n" + text, end = "\n\n")
    print("Coded message: \n" + codedMessage, end = "\n\n")
    print("Decoded message: \n" + decode(codedMessage, result))


HuffmanCodes("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris id ultricies tortor. Aenean tristique odio sed dignissim dapibus. Duis gravida urna egestas ligula tincidunt gravida. Vivamus dictum, nunc eu venenatis consequat, diam ipsum viverra sapien, congue tristique ante ante ut dolor. Nullam at velit et tellus venenatis rhoncus. Quisque volutpat est eget libero porta hendrerit. Sed gravida felis metus, non bibendum erat tempor non.")

