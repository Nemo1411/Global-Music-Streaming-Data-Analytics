sqlCopy code
-- Count the number of unique users per platform
SELECT
  platform,
  COUNT(DISTINCT user_id) as unique_users
FROM
  music_streaming_data
GROUP BY
  platform;

-- Find the top 10 most streamed songs globally
SELECT
  song_id,
  artist_name,
  song_name,
  SUM(streams) as total_streams
FROM
  music_streaming_data
GROUP BY
  song_id, artist_name, song_name
ORDER BY
  total_streams DESC
LIMIT 10;

-- Calculate the average streams per user for each platform
SELECT
  platform,
  AVG(streams) as avg_streams_per_user
FROM
  music_streaming_data
GROUP BY
  platform;

-- Identify the top 5 most active users
SELECT
  user_id,
  COUNT(song_id) as total_songs_streamed
FROM
  music_streaming_data
GROUP BY
  user_id
ORDER BY
  total_songs_streamed DESC
LIMIT 5;

