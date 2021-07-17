import robloxpy,requests,random,string,datetime,multiprocessing
from robloxpy import Utils as Utils

def new_line(file_name, text_to_append):
    with open(file_name, "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(text_to_append)

def GetID(Username):
    r = requests.get(Utils.APIURL + f'users/get-by-username?username={Username}')
    try:
        return r.json()['Id']
    except:
        return r.json()['errorMessage']

def checkusername():
    while True:
        name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        function = GetID(name)
        if function == "User not found":
            new_line("valid.txt", name)
            print(name)

if __name__ == "__main__":
    q=multiprocessing.Queue()
    processes=[multiprocessing.Process(target=checkusername) for i in range(1,35)]
    for p in processes:
        p.start()
 
    for p in processes:
        p.join()
 
    result = [q.get() for p in processes]
    print(result)
