from tabulate import tabulate

class table:
    
    def __init__(self,source,headers=()):

        self.source = source
        self.headers = headers
        self.raw = tabulate(source,headers=headers,tablefmt='grid')
        self.computeHeightWidth()
        

    def computeHeightWidth(self):
       
        self.height = 0
        self.width = 0

        for line in self.raw.split('\n'):
            if self.width < len(line): 
                self.width = len(line)
        
        self.height = len(self.raw.split('\n')) + 2
        self.width += 1

    def returnTable(self):

        return self.raw

    def returnHeightWidth(self):

        return self.height,self.width

