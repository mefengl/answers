#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#

# @lc code=start
import queue
from typing import List


class Twitter:
    time_stamp = 0

    def __init__(self):
        self._user_map = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self._user_map:
            self._user_map[userId] = Twitter.User(userId)
        user = self._user_map[userId]
        user.post(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        if userId not in self._user_map:
            return res
        pq = queue.PriorityQueue()
        followed_ids = self._user_map[userId].followed
        # 先压入各个被关注者的最新推文
        for followed_id in followed_ids:
            tweet = self._user_map[followed_id].head
            if tweet is None:
                continue
            # 最新时间，是逆序的，所以加负号
            pq.put([-tweet.time, tweet.id, tweet.next])
        # 然后不断获取最新推文的下一条（贪婪算法，是剩余最新的）
        while not pq.empty():  # loop while not empty
            if len(res) == 10:
                break
            _, tweet_id, next_tweet = pq.get()
            res.append(tweet_id)
            if next_tweet is not None:
                # 最新时间，是逆序的，所以加负号
                pq.put([-next_tweet.time, next_tweet.id, next_tweet.next])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        for user_id in [followerId, followeeId]:
            if user_id not in self._user_map:
                self._user_map[user_id] = Twitter.User(user_id)
        self._user_map[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 不存在则什么也不做，因为新建用户的unfollow也不会成功
        if followerId not in self._user_map:
            return
        self._user_map[followerId].unfollow(followeeId)

    class Tweet:
        def __init__(self, id: int, time: int):
            self.id = id
            self.time = time
            self.next: Tweet = None

    class User:
        def __init__(self, id: int):
            self.id = id
            self.followed = {id}  # init set with id
            self.head: Tweet = None

        def follow(self, user_id: int):
            self.followed.add(user_id)

        def unfollow(self, user_id: int):
            # 不可取关自己
            if user_id == self.id:
                return
            # 没必要取关没有关注的人
            if user_id not in self.followed:
                return
            self.followed.remove(user_id)

        def post(self, tweetId: int):
            tweet = Twitter.Tweet(tweetId, Twitter.time_stamp)
            Twitter.time_stamp += 1
            # 插入表头，类似 新推文插入页首
            tweet.next = self.head
            self.head = tweet


# Your Twitter object will be instantiated and called as such:
# obj = twitter()
# obj.posttweet(111,222)
# param_2 = obj.getnewsfeed(111)
# obj.follow(111,112)
# obj.unfollow(111,112)
# @lc code=end
