class particle:
    x = 0
    
    def __init__(self, a, b, c, d, e, f, g):
        self.massa = a
        self.v = b
        self.d = c
        self.x = d
        self.y = e
        self.z = f
        self.nama = g
        
    def pindah_ke(self, a,b,c):
        self.x = a
        self.y = b
        self.z = c

a = particle(2.6, 3, 5, 4, 5, 1, "boron")

a.pindah_ke(1,2,3)

print(str(a.x) + "\n")
print(str(a.y) + "\n")
print(str(a.z) + "\n")
