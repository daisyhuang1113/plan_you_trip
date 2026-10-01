from shortest_path import turn_id, find
from trip_revise import add_station, display_f, delete_station, modify_station
from list_map import makeMap, find_line
import sys

def main():
    while True:
        print('功能選擇')
        print('1. 捷運路線圖查詢')
        print('2. 建議路線查詢')
        print('3. 查看我的旅程')
        print('4. 新增旅行計劃')
        print('5. 離開系統')
        ans = eval(input('請選擇: '))
        if ans==1:
            show_map()
        elif ans==2:
            search_road()
        elif ans==3:
            display_f()
        elif ans==4:
            add_()
        elif ans==5:
            sys.exit()
        print()
        print('------------------------')

def show_map():
    print()
    while True:
        print('1. 顯示所有地圖')
        print('2. 單一路線查詢')
        print('3. 回上一頁')
        ans = eval(input('請選擇: '))
        if ans==1:
            makeMap()
        elif ans==2:
            line = input('欲查詢路線： ')
            find_line(line)
        elif ans==3:
            break
        print()
        

def search_road():
    print()
    start = input("請輸入出發地: ")
    end = input("請輸入目的地: ")
    start, end = turn_id(start, end)
    print('以下為建議路線：')
    find(start, end)

def add_():
    print()
    while True:
        print('1.新增旅行計劃')
        print('2.刪除旅行計劃')
        print('3.更改旅行計劃')
        print('4.回上一頁')
        ans = eval(input('請選擇: '))
        if ans==1:
            station = input('加入新地點：')
            add_station(station)
        elif ans==2:
            station = input('欲刪除地點：')
            delete_station(station)         
        elif ans==3:
            station = input('與更改地點：')
            modify_station(station)
        elif ans==4:
            break        
        display_f()
        print()

if __name__ == "__main__":
    main()
