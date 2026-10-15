# Lab 4 - VibeCoding: Balloon Pop

Submission by Uditi (PES2UG24CS565).

## Contents

| Item | File |
|---|---|
| Updated code | [`balloon-pop/`](balloon-pop/) |
| Video before changes | [`before_balloon_pop.mp4`](before_balloon_pop.mp4) |
| Video after changes | [`after_balloon_pop.mp4`](after_balloon_pop.mp4) |
| Chat history (PDF) | [`Lab4_Chat_History.pdf`](Lab4_Chat_History.pdf) |
| Chat link | https://claude.ai/share/5a9476c4-ed4a-4f68-84e3-e5d82839292e |

## Videos not playing in the browser?

GitHub can't preview large video files and shows "we can't show files that are this big right now". The files are uploaded fine. To watch them:

1. Click the video file above, then click **Download raw file** (the download icon at the top right of the file page), or use the direct links below.
2. Open the downloaded `.mp4` in any video player.

Direct download links:
- Before: https://github.com/uditiii/05_balloon_pop/raw/refs/heads/main/Lab-4/before_balloon_pop.mp4
- After: https://github.com/uditiii/05_balloon_pop/raw/refs/heads/main/Lab-4/after_balloon_pop.mp4

## What changed

- **Task 1:** fixed click detection in `game/click_detection.py` (compare squared distance to squared radius).
- **Task 2:** three balloon types (normal, bonus, penalty) with their own colors and points.
- **Task 3:** 3 lives; a balloon reaching the bottom costs a life, popping never does.
- **Task 4:** 30-second timed round with a game-over screen and restart (click or press R).

## Run

```
cd balloon-pop
pip install -r requirements.txt
python main.py
```
