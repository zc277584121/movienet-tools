import os
import traceback
from filter_movie import get_min_intersection_list, Trailer


def download_movies_with_all_attr(movienet_path, download_folder='./'):
    min_intersection = get_min_intersection_list(movienet_path)
    trailer_json_path = os.path.join(movienet_path, 'trailer.urls.unique30K.v1.json')
    trailer = Trailer(trailer_json_path)
    imdb2youtube_dict = trailer.get_imdb2youtube_dict()
    all_download_folder_files = ''.join(os.listdir(download_folder))
    for imdb_id in min_intersection:
        try:
            youtube_id = imdb2youtube_dict[imdb_id]
            print('youtube_id =', youtube_id)
            if youtube_id in all_download_folder_files:
                print('********Already downloaded********')
                continue
            file_pattern = "'" + os.path.join(download_folder, '%(title)s-%(id)s.%(ext)s') + "'"
            os.system('youtube-dl https://www.youtube.com/watch?v={} --output {} --external-downloader aria2c --external-downloader-args "-x 16  -k 1M"'.format(youtube_id, file_pattern))
            print('finish one movie')
        except:
            traceback.print_exc()


if __name__ == '__main__':
    download_movies_with_all_attr(movienet_path='/Users/zilliz/dataset/movienet', download_folder='/Users/zilliz/dataset/movienet/trailers')
