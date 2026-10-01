from name import station_names, stations, lines_to_stations

class mytrip():
    def __init__(self):
        self.station = None
        self.next = None

head = None
        
def add_station(name):
    global head
    sid = get_id(name)
    ptr = mytrip()
    ptr.station = sid
    if head==None:
        head = ptr
    else:
        if find_f(name)==True:
            current = head
            while current.next!=None:
                current = current.next
            current.next = ptr
            print(name, '已加入')
        else:
            print(name, '已在行程內')

def delete_station(name):
    global head     
    sid = get_id(name)
    if head == None:
        print('沒有已儲存的地點')
    else:
        prev = head
        current = head.next
        if head.station==sid:
            head = head.next
            print(name, '已刪除')
            return
        while current!=None and current.station!=sid:
            prev = current
            current = current.next
        if current != None: 
            prev.next = current.next
            current = None
            print(name, '已刪除')
        else:
            print(f"{name}不在您的行程內")    
     
def modify_station(name):
    global head
    sid = get_id(name)
    if head == None:
        print('沒有已儲存的地點')
    else:
        current = head
        while current!=None:
            if current.station == sid:
                new_name = input('想改成的地點: ')
                nid = get_id(new_name)
                current.station = nid
                print(f'{name} 已更改為 {new_name}')
                return
            current = current.next
    
        print(f"{name} 不在您的行程內")
     
def display_f():
    global head
    if head == None:
        print('沒有已儲存的地點')
    else:
        current = head
        while current!=None:
            station = get_name(current.station)
            print(f'{station}', end='')
            if current.next!=None:
                print(' -- ', end='')
            current = current.next   
    
def find_f(name):
    global head
    current = head
    while current!=None:
        if current.station == name:
            return False
        current = current.next
    return True

def get_id(name):
    for sid, sname in station_names.items():
        if sname == name:
            return sid
    return None
def get_name(sid):
    return station_names.get(sid, None)