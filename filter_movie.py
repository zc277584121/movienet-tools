import json
import os

from utils import print_line, intersection, union


class Trailer:
    def __init__(self, json_path):
        self.trailer_dict_list = _read_file_to_dict(json_path)
        self.imdb_id_list = []

    def get_imdb_id_list(self):
        for trailer_dict in self.trailer_dict_list:
            self.imdb_id_list.append(trailer_dict['imdb_id'])
        return self.imdb_id_list

    def get_imdb2youtube_dict(self):
        res_dict = {}
        for trailer_id_dict in self.trailer_dict_list:
            imdb_id = trailer_id_dict['imdb_id']
            youtube_id = trailer_id_dict['youtube_id']
            res_dict[imdb_id] = youtube_id
        return res_dict


class VideoInfo:
    def __init__(self, json_path):
        self.video_info_dict = _read_file_to_dict(json_path)

    def get_all_mv_ids(self):
        return list(self.video_info_dict.keys())


class Poster4M:
    def __init__(self, json_path):
        self.post4m_dict = _read_file_to_dict(json_path)

    def get_all_mv_ids(self):
        all_mv_list = []
        for rm_value in self.post4m_dict.values():
            all_mv_list += (rm_value['movie'])
        return all_mv_list


def get_mv_ids_from_folder(folder_path):
    """
    Get all movie id in a given path
    """
    all_json_files = os.listdir(folder_path)
    all_movie_id_list = [json_file.split('.')[0] for json_file in all_json_files]
    return all_movie_id_list


def get_mv_ids_from_txt(txt_path):
    """
    Get all movie id in a given txt file
    """
    with open(txt_path, 'r') as f:
        all_movie_id_list = f.readlines()
        all_movie_id_list = [mv_id.strip() for mv_id in all_movie_id_list]
    return all_movie_id_list


def get_mv_ids_dict_from_json(json_path):
    """
    Get all movie id split by 'train', 'val', 'test', 'full' etc. in a given json file
    """
    return _read_file_to_dict(json_path)


def _read_file_to_dict(json_path):
    with open(json_path, 'r') as f:
        all_movie_id_list = f.readlines()
        split_dict = json.loads(''.join(all_movie_id_list))
    return split_dict


def get_min_intersection_list(movienet_path):
    """
    Get the minimum intersection trailer list which contains all the attributes.
    """

    def print_intersect_union(list1, list2):
        print_line()
        print('len of intersection =',
              len(intersection(list1, list2)))
        print('len of union =',
              len(union(list1, list2)))
        print(list2[:5])
        print('len of list1 = ', len(list1))
        print('len of list2 = ', len(list2))

    # Annotation
    annotation_path = os.path.join(movienet_path, 'annotation')
    all_annotation_movie_id_list = get_mv_ids_from_folder(annotation_path)
    print('len(all_annotation_movie_id_list) =', len(all_annotation_movie_id_list))
    print_line()

    # Meta
    meta_path = os.path.join(movienet_path, 'meta')
    all_subtitle_movie_id_list = get_mv_ids_from_folder(meta_path)
    print('len(all_subtitle_movie_id_list) =', len(all_subtitle_movie_id_list))
    print_line()

    # Movie per-shot keyframes

    # Movie List
    mv_list_path = os.path.join(movienet_path, 'list.v1.txt')
    all_mv_list_movie_id_list = get_mv_ids_from_txt(mv_list_path)
    print('len(all_mv_list_movie_id_list) =', len(all_mv_list_movie_id_list))
    print_line()

    # Movie1K train/val/test split
    mv_split_path = os.path.join(movienet_path, 'movie1K.split.v1.json')
    all_mv_split_movie_id_dict = get_mv_ids_dict_from_json(mv_split_path)
    print('all_mv_split_movie_id_dict.keys() =', all_mv_split_movie_id_dict.keys())
    for split_name, split_movie_id_list in all_mv_split_movie_id_dict.items():
        print('len of {}'.format(split_name), len(split_movie_id_list))
    print_line()

    # Poster4M
    post4m = Poster4M(os.path.join(movienet_path, 'poster4M.img_meta.v1.json'))
    post4m_id_list = post4m.get_all_mv_ids()
    print('len(post4m_id_list) =', len(post4m_id_list))
    post4m_id_set = set(post4m_id_list)
    print('len(post4m_id_set) =', len(post4m_id_set))

    post4m_id_set_list = list(post4m_id_set)
    print_line()

    # Subtitles
    subtitle_path = os.path.join(movienet_path, 'subtitle')
    all_subtitle_movie_id_list = get_mv_ids_from_folder(subtitle_path)
    print('len(all_subtitle_movie_id_list) =', len(all_subtitle_movie_id_list))
    print_line()

    # Script
    script_path = os.path.join(movienet_path, 'script')
    all_script_movie_id_list = get_mv_ids_from_folder(script_path)
    print('len(all_script_movie_id_list) =', len(all_script_movie_id_list))
    print_line()

    # Shot detection result for movie1K
    shot_path = os.path.join(movienet_path, 'shot')
    all_shot_movie_id_list = get_mv_ids_from_folder(shot_path)
    print('len(all_shot_movie_id_list) =', len(all_shot_movie_id_list))
    print_line()

    # Audio feature for movie1K
    # not downloaded yet

    # Place feature for movie1K
    # not downloaded yet

    # Video info for movie1K movies
    video_info = VideoInfo(os.path.join(movienet_path, 'movie1K.video_info.v1.json'))
    video_info_mv_id_list = video_info.get_all_mv_ids()
    print('len(video_info_mv_id_list) =', len(video_info_mv_id_list))
    print_line()

    # Trailer 30K URLs
    trailer_json_path = os.path.join(movienet_path, 'trailer.urls.unique30K.v1.json')
    trailer = Trailer(trailer_json_path)
    trailer_imdb_id_list = trailer.get_imdb_id_list()
    print('len(trailer_imdb_id_list) =', len(trailer_imdb_id_list))
    print_line()

    # --------------------------anlysis--------------------------
    print_line()

    print_intersect_union(all_mv_list_movie_id_list, all_shot_movie_id_list)
    print('list1 = all_mv_list_movie_id_list, list2 = all_shot_movie_id_list')

    print_intersect_union(all_mv_list_movie_id_list, video_info_mv_id_list)
    print('list1 = all_mv_list_movie_id_list, list2 = video_info_mv_id_list')

    print_intersect_union(all_mv_list_movie_id_list, all_annotation_movie_id_list)
    print('list1 = all_mv_list_movie_id_list, list2 = all_annotation_movie_id_list')

    print_intersect_union(all_mv_list_movie_id_list, all_subtitle_movie_id_list)
    print('list1 = all_mv_list_movie_id_list, list2 = all_subtitle_movie_id_list')

    print_intersect_union(all_mv_list_movie_id_list, post4m_id_set_list)
    print('list1 = all_mv_list_movie_id_list, list2 = post4m_id_set_list')

    print_intersect_union(all_mv_list_movie_id_list, trailer_imdb_id_list)
    print('list1 = all_mv_list_movie_id_list, list2 = trailer_imdb_id_list')

    # ------------------------------
    print_line()
    print_line()
    min_intersection = intersection(intersection(all_mv_list_movie_id_list, all_subtitle_movie_id_list),
                                    trailer_imdb_id_list)
    print('len(min_intersection) =', len(min_intersection))
    return min_intersection


if __name__ == '__main__':
    min_intersection = get_min_intersection_list(movienet_path='/Users/zilliz/Downloads')
    print(min_intersection[:10])
