# 292. Nim Game

def canWinNim (n):
    if n%4==0:
        return True
    else:
        return False


print(canWinNim(16))