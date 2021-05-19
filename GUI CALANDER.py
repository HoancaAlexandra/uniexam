import calendar
import datetime
import tkinter as tk
import csv
from collections import deque

class Calendar:
    def __init__(self, parent, values):
        self.values = values
        self.parent = parent
        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        self.wid = []
        self.day_selected = 1
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = ''

        self.setup(self.year, self.month)

    def clear(self):
        for w in self.wid[:]:
            w.grid_forget()
            self.wid.remove(w)

    def go_prev(self):
        if self.month > 1:
            self.month -= 1
        else:
            self.month = 12
            self.year -= 1

        self.clear()
        self.setup(self.year, self.month)

    def go_next(self):
        if self.month < 12:
            self.month += 1
        else:
            self.month = 1
            self.year += 1


        self.clear()
        self.setup(self.year, self.month)

    def findexam(self,a,b):

        if (a < 10):
            a = '0' + str(a)
        a = str(a) + str(b)

        for i in result.keys():
            if (i == a):
                w = tk.Label(self.parent,text=result[i])
                w.grid(row=13, column=0, columnspan=7)
                count = 0
                for j in result[i]:
                    count += 1
                count = str(count)+'persoana/persoane'
                w = tk.Label(self.parent, text=count)
                w.grid(row=13, column=2, columnspan=7)
                break
            else:
                w=tk.Label(self.parent,text='\t\t\t\t\t')
                w.grid(row=13,column=0,columnspan=7)


    def selection(self, day, name):
        self.day_selected = day
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = name

        self.values['day_selected'] = day
        self.values['month_selected'] = self.month
        self.values['year_selected'] = self.year
        self.values['day_name'] = name
        self.values['month_name'] = calendar.month_name[self.month_selected]

        self.clear()
        self.setup(self.year, self.month)

    def setup(self, y, m):

        left = tk.Button(self.parent, text='<', command=self.go_prev)
        self.wid.append(left)
        left.grid(row=1, column=1)

        header = tk.Label(self.parent, height=2, text='{}{}   {}'.format("Anul  ", str(y),calendar.month_abbr[m]))
        self.wid.append(header)
        header.grid(row=1, column=2, columnspan=3)

        right = tk.Button(self.parent, text='>', command=self.go_next)
        self.wid.append(right)
        right.grid(row=1, column=5)

        days = ('duminica', 'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata')
        for num, name in enumerate(days):
            t = tk.Label(self.parent, text=name[:3])
            self.wid.append(t)
            t.grid(row=2, column=num)

        for w, week in enumerate(self.cal.monthdayscalendar(y, m), 3):
            for d, day in enumerate(week):
                if day:
                    b = tk.Button(self.parent, width=4, text=day,
                                  command=lambda day=day: self.selection(day, calendar.day_name[(day - 1) % 7]))
                    self.wid.append(b)
                    b.grid(row=w, column=d)

        sel = tk.Label(self.parent, height=2, text='{} {} {}'.format(
            self.month_selected, '/', self.day_selected,self.findexam(self.month_selected,
                                                                        self.day_selected)))
        self.wid.append(sel)
        sel.grid(row=8, column=0, columnspan=7)

class printbirth:
    def __init__(self):
        window = tk.Tk()
        deque_list = deque(birth_list)
        for i in birth_list:
            w2 = tk.Label(window,padx=10,text=i).pack()
            print(w2)

if __name__ == '__main__':
    birth_list = []

    with open('Lista participanților și informații despre ziua de naștere.csv', 'r') as birth:
        csv_reader = csv.reader(birth, delimiter=',', quotechar='"')
        for row in csv_reader:
            if row[1] == '' or row[1] == 'Nume' or row[3] == '':
                continue
            birth_info = {row[1]: row[3]}  # 딕셔너리 사용
            birth_list.append(birth_info)

    result = {}
    check = False

    for person in birth_list:
        for name in person:
            birth = person[name][-4:]
            dayList = result.keys()
            for day in dayList:
                if day == birth:
                    check = True
                    break
            if check == True:
                result[birth].append(name)
                check = False
            else:
                result[birth] = [name]


    class Control:
        def __init__(self, parent):
            self.parent = parent
            self.choose_btn = tk.Button(self.parent, text='Iesirea calendarului', command=self.popup)
            self.show_btn = tk.Button(self.parent, text='Lista tuturor zilelor de naștere ale studenților', command=self.print_selected_date)
            self.choose_btn.grid()
            self.show_btn.grid()
            self.data = {}

        def popup(self):
            child = tk.Toplevel()
            cal = Calendar(child, self.data)

        def print_selected_date(self):
            b = printbirth()


    root = tk.Tk()
    root.title("성신여자대학교 융합보안공학과 20171934 백혜민")
    app = Control(root)
    root.mainloop()
