M1 = [[1,0,0],[0,1,0],[0,0,1]]
def esEscalar(m):
    d = m[0][0]
    if len(m) == len(m[0]):
        for i in range(len(m)):
            for j in range(len(m)):
                if i != j:
                    if m[i][j] != 0:
                        print(m[i][j])
                        return False
                elif m[i][j] != d:
                    print(m[i][j])
                    return False
        return True;
    else:
        return False

print(esEscalar(M1))

# Determine si una matriz es unitaria
def esUnitaria(m):
  return m[0][0] == 1 and esEscalar(m)
print(esEscalar(M1))
