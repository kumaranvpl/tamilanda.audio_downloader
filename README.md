# tamilanda.audio_downloader
A small utility to download all FLAC songs from given album 

# Why I developed it
FLAC has higher bitrate than mp3. 
And for tamil songs, hd.tamilanda.audio site provides FLAC songs ripped from good source.
But they don't provide a way to download all songs in an album at once.
I don't want to waste time by downloading each file and moving it into a directory.
So I developed this tool to save few minutes of my time.

# How to download
1. Get url for an album(example: http://hd.tamilanda.audio/index.php?dir=Music_Directors_Hits/Anirudh_Ravichander/Velaikkaran_(2017)&p=0&sort=0)
2. Decide in which directory you want these album to download(Default: current directory)
3. Create a virtual environment and install all the requirements
4. Run 'python main.py album_url'

# Examples
1. python main.py "http://hd.tamilanda.audio/index.php?dir=Music_Directors_Hits/Anirudh_Ravichander/Velaikkaran_(2017)&p=0&sort=0"
2. python main.py "http://hd.tamilanda.audio/index.php?dir=Music_Directors_Hits/Anirudh_Ravichander/Velaikkaran_(2017)&p=0&sort=0" "/home/kumaran/Music"

# Features
1. Downloads all songs of an album to separate directory
2. Downloads to given location
3. Can show progress for each song download
4. Auto resume feature. If download fails just rerun the program. It will skip already downloaded files and resumes the failed ones. Thanks to wget for this.

# ToDo
1. Download by giving just the album name instead of whole album url
