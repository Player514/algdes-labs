None: 
- Remove the red nodes, do BFS

Some: 
- Use flow
- Set black -> black = inf
- Set red -> any = 1

Many:
- NP-hard
- Brute force if N < 5? 6? 7? 
- Basically give up

Few: 
- Some approach, red_1 -> any = 1. red_2 -> any = 2
- 

Alternate: 
- Dynamic programming? 
- OPT = take-next OR do-not-take-next if next == alterning or do-not-take-next == alternating
- Cache the path from node x, y in cache[x][y] 

