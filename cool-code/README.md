## Sleep Sort
https://www.reddit.com/r/ProgrammerHumor/comments/zt9oov
```bash
function f() { sleep $1; echo $1; }
for i in "$@"; do f $i & done
wait
```

I really learn a lot from this code idea, it's so cute
