class stack:
    def __init__(self):
        self.stack=[]
    def append(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    def pop(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            print("popped elemet is",self.stack.pop())
    def printlist(self):
        print(self.stack)
st=stack()
st.append('mon')
st.append('tue')
st.append('wed')
st.append('thurs')
st.printlist()
st.pop()
st.pop()
st.printlist()
