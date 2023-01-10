## Easy
1 what is writing to this log file?
```bash
kill -9 $(lsof | grep bad.log | awk '{print $2}')
```
2 countng IPs
```bash
cat /home/admin/access.log | awk '{print $1}' | sort | uniq -c | sort | tail -1 | awk '{print $2}' > /home/admin/highestip.txt
```
3 Find the secret combination
```bash
echo -n $(cat /home/admin/*.txt | grep -c Alice) > /home/admin/solution;

for file in /home/admin/*.txt; do if [[ $(grep -c Alice $file) -eq 1 ]]; then cat $file | tr -d '\n' | awk -F Alice '{print $2}' | awk '{print $2}' >> /home/admin/solution; fi ; done
```

## Medium
4 can't write data into database

5 can't serve web file

6 Borked Nginx

7 Docker container won't start

8 Am I in a container?

9 Close an Open File

10 WSGI with Gunicorn

11 etcd SSL cert troubles

## Hard
12 it's always DNS.

13 Docker web container can't connect to db container.

14  WTFIT - What The Fun Is This?

15 Docker and Kubernetes web app not working.

16 can't write data into database.
