from collections import defaultdict
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
        
        for t_id, time in self.tweets[userId]:
            heapq.heappush_max(max_heap, (time, t_id))
        
        # find all tweets
        all_tweets = []
        for following in self.following[userId]:
            for t_id, time in self.tweets[following]:
                heapq.heappush_max(max_heap, (time, t_id))
        
        most_recents = []
        num_tweets = 0
        while max_heap and num_tweets < 10:
            _, tweet = heapq.heappop_max(max_heap)
            num_tweets += 1
            most_recents.append(tweet)
        return most_recents

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId) # no error if doesnt exist
