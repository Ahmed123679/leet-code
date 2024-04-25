class DFS:
    def __init__(self,graph:dict) -> None:
        self.graph:dict = graph
    def getPath(self,rootNode:str,targetNode:str) -> None:
        stack = []
        visited = []
        stack.append(rootNode)
        
        while len(stack) != 0:
        
            # check if the node is visited
            if stack[-1] in visited:
                stack.remove(stack[-1])
                continue
            
            # visit node
            visited.append(stack[-1])

            if stack[-1] == targetNode:
                
                print('path:',stack)
                return
            
            
            # explore node
            connectedNodes = self.graph[stack[-1]]
            connectedNodes.sort()     
            connectedNodes.reverse()
            if(len(connectedNodes) == 0):
                stack.remove(stack[-1])
                continue
            else:
                for x in connectedNodes:
                    stack.append(x)


search = DFS({
    'A':['B','C'],
    'B':['D','E'],
    'C':['G','F'],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
})
print()
search.getPath('A','F')
