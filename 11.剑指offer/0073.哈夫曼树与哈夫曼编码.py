# I：实现节点类

class Node:
    def __init__(self,freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq
 
    def is_left(self):
        return self.father.left == self

# II：为每一个节点赋权值

def create_nodes(frequencies):
    return [Node(freq) for freq in frequencies]

# III：创建哈夫曼树
def create_huffman_tree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]

III：遍历叶节点
def huffman_encoding(nodes, root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.is_left():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes

