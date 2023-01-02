1
kill -9 $(lsof | grep bad.log | awk '{print $2}')
2
cat /home/admin/access.log | awk '{print $1}' | sort | uniq -c | sort | tail -1 | awk '{print $2}' > /home/admin/highestip.txt
3


4

5

6

7

8

9

10

11


12

13

14

15

16
