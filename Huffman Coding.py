import time
import random

class Node(object):
    # Initializes the Huffman tree
    def __init__(self, name=None, value=None):
        self._name = name
        self._value = value
        self._left = None
        self._right = None

class HuffmanTree(object):
    # Build the Huffman tree based on leaf nodes
    def __init__(self, char_weights):
        self.a = [Node(part[0], part[1])
                    for part in char_weights]  # Generate leaf nodes based on input characters and their frequencies
        while len(self.a) != 1:
            self.a.sort(key=lambda node: node._value, reverse=True)
            c = Node(value=(self.a[-1]._value+self.a[-2]._value))
            c._left = self.a.pop(-1)
            c._right = self.a.pop(-1)
            self.a.append(c)
        self.root = self.a[0]
        # self.b is used to store the Huffman code for each leaf node, and the range value only needs to be greater than or equal to the depth of the tree
        self.b = list(range(50))
    
    # Generate codes using a recursive approach
    def pre(self, tree, length):
        node = tree
        if (not node):
            return
        elif node._name:
            # x = str(node._name) + ' is encoded as: '
            # for i in range(length):
            #     x += str(self.b[i])
            # print(x)
            return
        self.b[length] = 0
        self.pre(node._left, length+1)
        self.b[length] = 1
        self.pre(node._right, length+1)
    
    # Generate Huffman codes
    def get_code(self):
        self.pre(self.root, 0)

def generate_weights(n):
    freqList = random.sample(range(1, n * 20 + 1), n)
    #charList = random.sample(range(1, n * 20 + 1), n)
    char_weights = []
    for i in range(n):
        char_weights.append((freqList[i], freqList[i]))
    return char_weights

if __name__ == '__main__':
    # Input consists of characters and their frequencies
    # char_weights = [('a',5),('b',9),('c',12),('d',13),('e',16),('f',45)]
    array = [100,500,1000,1500,2000,2500,3000,3500,4000,4500]  # values of "n"
    for arr in array:
        char_weights = generate_weights(arr)
        start = time.time()
        tree=HuffmanTree(char_weights)
        tree.get_code()
        end = time.time()
        timeElapse = end - start
        print('n = ' + str(arr) + ' ,the running time is: ' + str(timeElapse))
    
