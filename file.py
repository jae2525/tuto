f = open("C:/car_txt/a.csv")
lines = f.readlines()
cur_date = "20200319"
cur_line=""
for line in lines:
    line = line[1:-2]
    a=line.split("^")
    date = a[1][:8]
    if cur_line !=line:
        if cur_date != date:
            f_w = open("C:/car_txt/"+date+".csv",'w')
            f_w.write(line+"\n")
        else :
            f_w.write(line+"\n")
    cur_line=line
    cur_date = date

f.close()

