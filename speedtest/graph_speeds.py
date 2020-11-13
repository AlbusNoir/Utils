import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv
import datetime

times = []
download = []
upload = []

cur_date = datetime.datetime.now().strftime("%Y%m%d")
cur_date_str = str(cur_date)
ext = ".csv"
ext2 = ".png"
speedtest_file = cur_date_str + ext
speedtest_image = cur_date_str + ext2

with open(speedtest_file, 'r') as csv_file:
    plots = csv.reader(csv_file, delimiter=',')
    next(csv_file)
    for row in plots:
        if row:
            time.append(str(row[0]))
            download.append(float(row[1]))
            upload.append(float(row[2]))

#print(time, '\n', download, '\n', upload)

plt.figure()
plt.plot(time, download, label='Download', color='r')
plt.plot(time, upload, label='Upload', color='b')
plt.xlabel('Time')
plt.ylabel('Speed in Mb/s')
plt.title("Internet Speed")
plt.legend()
plt.savefig(speedtest_image, bbox_inches='tight')
plt.show()
