from collections import defaultdict, deque


class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(deque)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        users = [userId] + list(self.following[userId])
        for user in users:
            if user in self.tweets:
                all_tweets.extend(self.tweets[user])

        all_tweets.sort(reverse=True, key=lambda x: x[0])
        return [tweet_id for _, tweet_id in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
