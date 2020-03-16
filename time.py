class Time:
    h = 0
    m = 0

    def accept(self):
        print("Enter time in hours and minutes")
        self.h = int(input())
        self.m = int(input())

    def display(self):
        print(self.h, "Hours and:", self.m, "Minutes:")


class final_time:
    h = 0
    m = 0

    def accept(self, t):
        self.h = t.h
        self.m = t.m

    def sum(self, t1, t2):
        self.m = t1.m + t2.m
        self.h = self.m / 60
        self.m = self.m % 60
        self.h = self.h + t1.h + t2.h

    def display(self):
        print(self.h, "hours and", self.m, "minutes")

t1_obj = Time()
t1_obj.accept()

t2_obj = Time()
t2_obj.accept()
