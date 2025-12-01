# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

One the one hand, we have three times more space to store data thanks to even distribution. The load on the boat servers is also distributed evenly. On the other hand, we need to query on all of the boats for a specific question^ since we don't know exactly where to search.

## Partitioning by Hour

This approach is good for querying for a specific time interval, so researcher will be absolutely sure that he is getting full measured data. The disadvantage is that one boat can be significantly overloaded then others, for example when most observations occur between midnight and 1am.

## Partitioning by Hash Value

The load on the boat servers is distributed evenly, as it was in the first case. Also, we know exactly where to find specific observation by its hash value. The downside is that for time interval queries we are forced query on all of the boats.
