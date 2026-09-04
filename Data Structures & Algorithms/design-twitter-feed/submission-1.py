from heapq import heappush , heappop
class Twitter:

    def __init__(self):
        self.timer_counter=0
        self.follow_map={}
        self.tweet_map={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer_counter+=1
        if userId not in self.tweet_map:
            self.tweet_map[userId]=[]
        self.tweet_map[userId].append((self.timer_counter,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        followees=self.follow_map.get(userId,set())
        candidates=followees | {userId}
        for person in candidates:
            if person in self.tweet_map and len(self.tweet_map[person]) > 0:
                index = len(self.tweet_map[person]) - 1    
                time, tweetId = self.tweet_map[person][index]
                heappush(heap, (-time, tweetId, person, index - 1))
            

        result = []
        while heap and len(result) < 10:
            negtime, tweetId, person, index = heappop(heap)
            result.append(tweetId)

            if index >= 0:    
                time, next_tweetId = self.tweet_map[person][index]
                heappush(heap, (-time, next_tweetId, person, index - 1))

        return result
       

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_map:
            self.follow_map[followerId]=set()
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            self.follow_map[followerId].discard(followeeId)
        
