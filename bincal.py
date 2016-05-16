__author__ = 'yaseen'

import calendar


class BinCalendar(object):
    """
    out put calendar in binary to a txt file
    """
    day_name = 'MON     TUE     WED     THR     FRI     SAT     SUN\n'
    day_bin = '1       10      11      100     101     110     111\n\n'
    mon_name = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

    def choice_input(self):
        yr = raw_input("Enter year: ")
        while not yr or isinstance(yr, str):
            try:
                yr = int(yr)
            except:
                yr = raw_input("Enter year: ")
        mn = raw_input("Enter month: (leave blank for whole year) ")

        try:
            mn = int(mn)
            if mn > 12:
                print "month number greater than  12  getting  calendar for whole year"
                disp_cal = self.whole_year(year=int(yr))
            else:
                disp_cal = self.month_binary(year=int(yr), mnum=mn)
        except:
            print "printing calendar for whole year"
            disp_cal = self.whole_year(year=int(yr))

        f = open('bincal.txt', 'w') #write it to file
        f.write(disp_cal)
        f.close()
        return

    def month_binary(self, year, mnum):
        """
        takes care of spacing as well so as to properly write it in file
        :param year: year number
        :param mnum: month number
        :return: binary calendar of month of year
        """
        month_data = calendar.TextCalendar(calendar.MONDAY).monthdays2calendar(year, mnum)
        bin_cal = bin(year)[2:] + '  (' + str(year) + ')\n'
        bin_cal += '\n\n\n' + bin(mnum)[2:] + ' (' + self.mon_name[mnum - 1] + ')\n\n'
        bin_cal += self.day_name + self.day_bin
        for weekdata in month_data:
            for day in weekdata:
                if int(day[0]) != 0:
                    m = bin(day[0])
                    bin_cal += m[2:]
                    spaces = 8 - len(m[2:])
                    bin_cal += ' ' * spaces
                else:
                    bin_cal += ' ' * 8
            bin_cal += '\n'
        return bin_cal

    def whole_year(self, year):
        """
        takes care of spacing as well so as to properly write it in file
        :param year: year
        :return: binary calendar of year
        """
        year_cal = calendar.TextCalendar(calendar.MONDAY).yeardays2calendar(year)
        bin_cal = bin(year)[2:] + '  (' + str(year) + ')\n'
        numbr = 0
        for months in year_cal:
            for month_data in months:
                bin_cal += '\n\n\n' + bin(numbr + 1)[2:] + ' (' + self.mon_name[numbr] + ')\n\n'
                bin_cal += self.day_name + self.day_bin
                for weekdata in month_data:
                    for day in weekdata:
                        if int(day[0]) != 0:
                            m = bin(day[0])
                            bin_cal += m[2:]
                            spaces = 8 - len(m[2:])
                            bin_cal += ' ' * spaces
                        else:
                            bin_cal += ' ' * 8
                    bin_cal += '\n'
                numbr += 1
        return bin_cal


if __name__ == '__main__':
    BinCalendar().choice_input()
