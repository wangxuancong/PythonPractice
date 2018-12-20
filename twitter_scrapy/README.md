##  Overview

This project gets data from [Twitter](https://twitter.com/). The data include the user's tweets, self-information, friends list and followers list of the user and the favorite tweets of the user. Plus, this project can also get the followers information, but rate limit problems arise.

##  Get start

This project use twitter api to get data from Twitter and we give a default developer account to get the permission of using api.

You may over the wall ,then use ***sudo isof -i -P*** to check out your proxy port and fix it in constant.py

default parameters:

```
consumer_key = 'DAg0TYh9D8lYObJbYKmYdZhZL'
consumer_secret = 'E52C5xeDZYEu1V1dpqHf6ZylBaBT73wbFccWGDyDMtVwJEl24F'
access_token = '1058184258387271680-9xXH1jUXTBbw6LEiLTeP5hK9yrvmFU'
access_secret = 'oSxUhLAFZJjcHOwAbjNMiNU5Oz6U0OGGr9b8Yg67NtRLf'
```

- You'd better to get your own dev-account, it is convenient for your management. Apply for one in https://developer.twitter.com/. Get your own permission and reset the parameters.
- set up the`id_list.txt`, add the twitter IDs to get data

- run `twitteruser.py`/`twittermessage.py`/`twitterfavorite.py`, corresponding data will be saved in data cache.

##  Data information

###  Tweets (Messages)

We get target user's history tweets by [`([*id/user_id/screen_name*][, *since_id*][, *max_id*][, *count*][, *page*]`](http://docs.tweepy.org/en/v3.5.0/api.html#API.user_timeline). In our data we have:

| Attribute  | Type   | Description                                                  |
| ---------- | :----- | ------------------------------------------------------------ |
| id_str     | String | The string representation of the unique identifier for this Tweet. |
| created_at | String | UTC time when this Tweet was created.                        |
| text       | String | The actual UTF-8 text of the status update.                  |

format: < created_at, id_str, text >

###  Users

We get information related to target user by [`API.get_user`(*id/user_id/screen_name*)](http://docs.tweepy.org/en/v3.5.0/api.html#API.get_user), [`API.friends_ids(*id/screen_name/user_id*[, *cursor*])`](http://docs.tweepy.org/en/v3.5.0/api.html#API.friends_ids) and [`API.followers_ids(*id/screen_name/user_id*)`](http://docs.tweepy.org/en/v3.5.0/api.html#API.followers_ids). Data include:

####  User's information

The target user's self-information.

| Attribute   | Type   | Description                                                  |
| ----------- | ------ | ------------------------------------------------------------ |
| id_str      | String | The string representation of the unique identifier for this User. |
| screen_name | String | The screen name, handle, or alias that this user identifies themselves with. |
| created_at  | String | The UTC datetime that the user account was created on Twitter. |
| location    | String | *Nullable* . The user-defined location for this account’s profile. |
| description | String | *Nullable* . The user-defined UTF-8 string describing their account. |

format: < id_str, screen_name, created_at, location, description >

####  Follower list & Friend list

The target user's follower and friend list.

| Attribute | Type             | Description                                |
| --------- | ---------------- | ------------------------------------------ |
| id        | List of integers | Followers' or friends' ids, saved as list. |

format: < id >

###  Favorites

The favorite tweets of the target user.

| Attribute  | Type   | Description                                                  |
| ---------- | :----- | ------------------------------------------------------------ |
| id_str     | String | The string representation of the unique identifier for this Tweet. |
| created_at | String | UTC time when this Tweet was created.                        |
| text       | String | The actual UTF-8 text of the status update.                  |

format: < id_str, created_at, text >

To extend attributes of data above, refer to https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json.

##  Tips

- For more functions of tweepy, refer to http://docs.tweepy.org/en/v3.5.0/.

- When the project hits the limit of response, official Twitter api will throw a rate limit and a 15 minutes suspension is needed before restart. Relative docs can be checked in [Rate Limits](https://developer.twitter.com/en/docs/basics/rate-limits) and [Rate Limiting](https://developer.twitter.com/en/docs/basics/rate-limiting). Further optimization should be considered to cope with this issue. (multi-ip/ human-like operation)