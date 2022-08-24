# function check neu 1 so la2 so nguyen to
# Tra ve True neu la so nguyen to, False neu ko phai
def isPrimeNumber(n):
    # So nguyen to khong the la so 0 hay so 1
    if (n == 1 or n == 0):
        return False
    # cho i chay tu 2 den so can check
    for i in range(2,n):
        # neu so can check chia het cho i thi
        # ko phai la so nguyen to
        if (n%i == 0):
            return False
    # nhung truong hop con lai ko bi loai
    # se la so nguyen to
    return True

# theo de bai chi tim so nguyen to tu 0 toi 250
n=250
resultString = ""
# cho i chay tu 1 toi 250
for i in range(1,n+1):
    # neu i la so nguyen to thi add i vao string ket qua
    if (isPrimeNumber(i)):
        resultString += str(i) + " "
print(resultString)

# in string ket qua vao file results.txt theo de bai
f = open("results.txt", "w")
f.write(resultString)
f.close()
