class Automaton:
    def __init__(self):
        self.old = ''
        self.res_desc = ''
        self.c_desc = 0
        self.state = 'init'
        self.table = {
            'init':['start', 'start'],
            'start':['start', 'count'],
            'count':['start', 'count']
        }
    def get(self, c):
        '''
        if self.state == 'init':
            self.state = 'start'
            self.old = c
        '''
          

        if self.state == 'start':
            if self.old != c:
                self.state = 'start'
            else:
                self.state = 'count'

        if self.state == 'count':
            if self.old != c:
                self.state = 'start'
            else:
                self.state = 'count'


        if self.state == 'start':
            self.res_desc += (str(self.c_desc) + self.old)
            self.old = c
            self.c_desc = 1
        
        elif self.state == 'count':
            self.c_desc += 1

        else: #self.state == 'init':
            self.state = 'start'
            self.old = c
            self.c_desc = 1

    def get_result(self):
        print(self.res_desc)
        self.res_desc += (str(self.c_desc) + self.old)
        print(self.res_desc)
        return self.res_desc


class Solution:
    def countAndSay(self, n: int) -> str:
        # str description(str)
        # str recursive_desc(n)
        return self.recursive_desc(n)
    
    def recursive_desc(self, n):
        if n == 1:
            return '1'
        else:
            return self.description(self.recursive_desc(n-1))

    def description(self, s):
        automaton = Automaton()
        for c in s:
            automaton.get(c)
        return automaton.get_result()

