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
        min_heap = []
        
        # for t_id, time in self.tweets[userId]:
        #     heapq.heappush_max(max_heap, (time, t_id))
        
        # Should have 10 most recent tweets by the end if 10 available or less
        for tweet, t in self.tweets[userId]:
            if len(min_heap) == 10:
                if t > min_heap[0][0]:
                    heapq.heapreplace(min_heap, (t, tweet))
            else:
                heapq.heappush(min_heap, (t, tweet))

        for following in self.following[userId]:
            for tweet, t in self.tweets[following]:
                if len(min_heap) == 10:
                    if t > min_heap[0][0]:
                        heapq.heapreplace(min_heap, (t, tweet))
                else:
                    heapq.heappush(min_heap, (t, tweet))
        out = []
        while min_heap:
            _, tweet = heapq.heappop(min_heap)
            out.append(tweet)
        return out[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId) # no error if doesnt exist
