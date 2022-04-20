import os

from filter_movie import get_min_intersection_list, Trailer


def download_movies_with_all_attr(movienet_path):
    min_intersection = get_min_intersection_list(movienet_path)
    trailer_json_path = os.path.join(movienet_path, 'trailer.urls.unique30K.v1.json')
    trailer = Trailer(trailer_json_path)
    imdb2youtube_dict = trailer.get_imdb2youtube_dict()
    for imdb_id in min_intersection:
        youtube_id = imdb2youtube_dict[imdb_id]
        print('youtube_id =', youtube_id)
        # todo: download the video by youtube_id


if __name__ == '__main__':
    download_movies_with_all_attr(movienet_path='/Users/zilliz/Downloads/')
