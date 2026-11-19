from collections import defaultdict, deque
import heapq
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        
        # for t_id, time in self.tweets[userId]:
        #     heapq.heappush_max(max_heap, (time, t_id))
        
        # Should have 10 most recent tweets by the end if 10 available or less
        feeds = self.following[userId] | {userId}

        # add latest tweet from each user
        for following in feeds:
            # since sorted by least recent to most recent by default
            if self.tweets[following]:
                index = len(self.tweets[following]) - 1 
                most_recent_user_tweet, t = self.tweets[following][index]
                heapq.heappush_max(max_heap, (t, index, following, most_recent_user_tweet))
        
        feed = []
        while max_heap and len(feed) < 10:
            _, i, usr, twt = heapq.heappop_max(max_heap)
            feed.append(twt)
            if i > 0:
                i -= 1
                next_recent_user_tweet, t = self.tweets[usr][i]
                heapq.heappush_max(max_heap, (t, i, usr, next_recent_user_tweet))

        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId) # no error if doesnt exist
