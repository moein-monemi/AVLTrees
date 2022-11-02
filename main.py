class Node:
    def __init__(self, rootNode):
        self.leftChild = None
        self.rightChild = None
        self.rootNode = rootNode


def searchNode(key, node):
    if not node:
        print('No Value in Tree')
        return None
    if node.rootNode == key:
        print(f'Your key is {key}')
    if node.rootNode < key:
        searchNode(key, node.rightChild)
    if node.rootNode > key:
        searchNode(key, node.leftChild)


def createAVL(array):
    if len(array) == 0:
        return None
    middle = (len(array)) // 2
    root = Node(array[middle])
    root.leftChild = createAVL(array[:middle])
    root.rightChild = createAVL(array[middle + 1:])
    return root


def PrintTreeInOrder(node):
    if not node:
        return None
    PrintTreeInOrder(node.leftChild)
    print(node.rootNode)
    PrintTreeInOrder(node.rightChild)


array = [1, 2, 3, 4, 5, 200, 1000]
avlTree = createAVL(array)
PrintTreeInOrder(avlTree)
searchNode(200, avlTree)
