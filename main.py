
import robloxpy,requests,random,string,datetime,multiprocessing
from robloxpy import Utils as Utils

f = open('codes.txt', "a+")

def gencode():
    while True:
        code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        f.write(f'{code}\n')
        print(code)

if __name__ == "__main__":
    q=multiprocessing.Queue() # Instance of queue class created
    processes=[multiprocessing.Process(target=gencode) for i in range(1,35)]
    for p in processes:
        p.start()
 
    for p in processes:
        p.join()
 
    result = [q.get() for p in processes]
    print(result)

# name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))