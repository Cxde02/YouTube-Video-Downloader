from pytube import YouTube
from pytube.exceptions import VideoUnavailable

print('---------------------------')
print('|YOU TUBE VIDEO DOWNLOADER|')
print('---------------------------')

def video_480p(link, folder_path):
    yt = YouTube(link)
    video = yt.streams.get_by_resolution('480p')

    # Check if the video stream is available
    if video:
        # Download the video
        print(f"\nStarting to download {video.title}...\n")
        video.download(folder_path)
        print("Downloaded 100%")
        return True
    else:
        print("\nResolution not available for download. Choose another resolution")
        return False

def video_720p(link, folder_path):
    yt = YouTube(link)
    video = yt.streams.get_by_resolution('720p')

    # Check if the video stream is available
    if video:
        # Download the video
        print(f"\nStarting to download {video.title}...\n")
        video.download(folder_path)
        print("Downloaded 100%")
        return True
    else:
        print("\nResolution not available for download. Choose another resolution")
        return False

def yt_video_downloader(link, folder_path):
    try:
        yt = YouTube(link)
        video = yt.streams.get_by_resolution('1080p')
        # video = yt.streams.get_highest_resolution()

        # Check if the video stream is available
        if video:
            # Download the video
            print(f"\nStarting to download {video.title}...\n")
            video.download(folder_path)
            print("Downloaded 100%")
            return True
        else:
            print("\nResolution not available for download. Choose another resolution\n")
            return False
    except VideoUnavailable as e:
        if "age restricted" in str(e):
            print("\nThis video is age-restricted and cannot be downloaded.\n")
        else:
            print("\nVideo is unavailable for download.\n")
        return False

folder_path = 'C:/Users/user/Desktop/videosDownloadedFromPython' #Download directory
link = '' #YT Video link

while True:
    if not link: #Displayed if link is not hardcoded (User forgets to enter link before)
        link = input("Enter the YouTube video link: ")

    print('-------------------------')
    print('| Type 1 for 480p video  |')
    print('| Type 2 for 720p video  |')
    print('| Type 3 for 1080p video |')
    print('| Type 4 to exit         |')
    print('-------------------------')

    choice = int(input('\nEnter your choice: '))

    if choice < 1 or choice > 4:
        print('Invalid Choice! Enter again (1|2|3|4) ')
    elif choice == 1:
        if video_480p(link, folder_path):
            break
    elif choice == 2:
        if video_720p(link, folder_path):
            break
    elif choice == 3:
        if yt_video_downloader(link, folder_path):
            break
    elif choice == 4:
        print('\nExiting Program...')
        break
