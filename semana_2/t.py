class t:
    def __init__(self,v):
        self.v = v
    
    def __eq__(self,outro):
        if self.v == outro.v:
            return True
        return False

u = t(1)
z = t(2)
print(u == z)