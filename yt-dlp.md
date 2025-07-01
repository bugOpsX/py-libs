# YOUTUBE VIDEOS IN ALL QUALITIES 😲

It gets very frustrating when you *desperately* need a good YouTube downloader but can't find anything reliable 😩

Well guess what? We've got you covered!  
This tool works like a charm, supports **any quality**, and is totally free & open-source. Let’s go! 👇

---

##  Use `yt-dlp` - A Powerful Python Tool

- yt-dlp is a **command-line tool** to download YouTube videos in any quality  
- Works on **Windows, macOS, Linux**  
- Supports **video + audio merging**, **playlists**, **audio-only**, and more

---

## Follow These Steps and BOOM 💥

### 1. Download **FFmpeg**  
Required to merge video + audio properly.

- Get it from: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
- Download the “**essentials zip**”
- Extract to:  `C:\ffmpeg`
- Then add `C:\ffmpeg\bin` to your **System PATH**

### 2. Install yt-dlp
Open terminal and run:
```bash
pip install yt-dlp
```

### 3. Download Command for Video 📽️
Use this in terminal:
```
yt-dlp -f "bestvideo[height<=720]+bestaudio/best[height<=720]" <video_url>

```
- **Note :** To change quality, just replace **720** with:
144, 360, 480, 1080, 1440, 2160, 4320...

### 4. Audio Only 🔉
Use this in terminal:
```
yt-dlp -f bestaudio <YouTube-link>

```

### 5. Playlist ⏯️
Use this in terminal:
```
yt-dlp -f "bestvideo+bestaudio" <playlist-link>

```
---

### HOW IT WORKS 🤔
- YouTube streams video & audio separately (especially for HD)
- yt-dlp downloads both streams
- It uses ffmpeg in background to merge into a single .mp4
Final output is saved with the video title in your current folder.

## 🌟 GIVE IT A STAR
👉 Just click the **Star** button at the top-right of this page!

 
