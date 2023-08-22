from abc import abstractmethod
from pytube import YouTube, Stream
import re
import argparse
from pathlib import Path


def parse_txt(filename: str) -> set:
    with open(filename) as file:
        urls = [line[:-1] for line in file]
    return urls


#     title = re.sub(r"[^a-zA-Z0-9а-яА-Я\s_()-]+", "", title)
def generate_filename(title: str) -> str:
    title = re.sub(r"[^А-Яа-яA-Za-z0-9\s(),_-]+", "", title)
    return title + ".mp4"


class StreamGetter:
    @abstractmethod
    def get_stream(self, yt: YouTube):
        pass


class VideoGetter(StreamGetter):
    def get_stream(self, yt: YouTube) -> Stream:
        return yt.streams.get_highest_resolution()


class MusicGetter(StreamGetter):
    def get_stream(self, yt: YouTube) -> Stream:
        return yt.streams.filter(only_audio=True).first()


def download(yt_stream: Stream, output_path: str, filename: str):
    yt_stream.download(output_path=output_path, filename=filename)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--filename", type=str, required=False, default="video.txt"
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        required=False,
        default="E:\code\\additional\youtube-downloader\\video",
    )
    parser.add_argument("-m", "--music", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.music == True:
        stream_getter = MusicGetter()
    else:
        stream_getter = VideoGetter()

    urls = parse_txt(args.filename)
    print(urls)
    for i, url in enumerate(urls):
        print(i)
        yt = YouTube(url, use_oauth=True)
        new_filename = generate_filename(yt.title)
        path = Path(args.path + "\\" + new_filename)
        print(new_filename)
        if path.is_file():
            continue
        download(
            stream_getter.get_stream(yt),
            output_path=args.path,
            filename=generate_filename(yt.title),
        )
