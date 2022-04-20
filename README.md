This repo is forked from [movienet/movienet-tools](https://github.com/movienet/movienet-tools).

This repo aims to provide some data processing tools for movienet.

# download trailers
## download one video trailer

There are many trailers on the `trailer.urls.unique30K.v1.json` which is downloaded from [movienet](http://movienet.site/#).

To download those trailers, install [youtube-dl](https://youtube-dl.org/) and install [aria2c](https://github.com/aria2/aria2).

```bash
pip install youtube-dl
brew install aria2

youtube-dl https://www.youtube.com/watch?v=[youtube_id] --external-downloader aria2c --external-downloader-args "-x 16  -k 1M"
```
`youtube_id` is in the `trailer.urls.unique30K.v1.json` file.

--external-downloader aria2c //means调用外部下载工具  
--external-downloader-args //means外部下载工具指定参数  
-x 16 //means启用aria2 16个线程，最多就支持16线程  
-K 1M //means指定块的大小  


## download trailers with complete information

There are many attributes in a trailer, which can be download from [movienet](http://movienet.site/#).
For example:
- Annotation (Last updated at 02/08/2020, size: 53MB, after unzip: 881MB)
- Meta (Last updated at 06/08/2020, size: 537MB, after unzip: 2.3GB)
- Movie per-shot keyframes (240P) (Last updated at 29/08/2020, size: 161GB, after unzip: 161GB)
- Movie List (1100) (Last updated at 29/08/2020, size: 10KB) 
- Movie1K train/val/test split (Last updated at 29/08/2020, size: 30KB)
- Poster4M image meta information (Last updated at 02/09/2020, size: 1.3GB, one could download images from the urls provided in the json file.)
- Subtitles (815 files) from movie1K (Last updated at 05/09/2020, size: 29.9MB, after unzip: 84.4MB)
- Script (479 files) from movie1K (Last updated at 05/09/2020, size: 27.9MB, after unzip: 101.8MB)
- Shot detection result for movie1K (Last updated at 05/09/2020, size: 20.9MB, after unzip: 50.7MB)
- Audio feature for movie1K (Last updated at 06/09/2020, size: 89.7GB)
- Place feature for movie1K (Last updated at 06/09/2020, size: 11GB)
- Video info for movie1K movies, including fps, frame_count, etc (Last updated at 09/09/2020, size: 118KB)
- Trailer 30K URLs (Last updated at 17/10/2020, size: 2.155MB)  

To filter the trailers which contain all the attributes information, we need to download all the files from movienet first.

To analyze all of the files downloaded from movienet, we can use the following command:
 
```
python filter_movie.py


len(all_annotation_movie_id_list) = 8918
----------------------------------------------------------------------------------------------------
len(all_meta_movie_id_list) = 375359
----------------------------------------------------------------------------------------------------
len(all_mv_list_movie_id_list) = 1100
----------------------------------------------------------------------------------------------------
all_mv_split_movie_id_dict.keys() = dict_keys(['train', 'val', 'test', 'full'])
len of train 660
len of val 220
len of test 220
len of full 1100
----------------------------------------------------------------------------------------------------
len(post4m_id_list) = 2774499
len(post4m_id_set) = 300435
----------------------------------------------------------------------------------------------------
len(all_subtitle_movie_id_list) = 815
----------------------------------------------------------------------------------------------------
len(all_script_movie_id_list) = 479
----------------------------------------------------------------------------------------------------
len(all_shot_movie_id_list) = 1100
----------------------------------------------------------------------------------------------------
len(video_info_mv_id_list) = 1100
----------------------------------------------------------------------------------------------------
len(trailer_imdb_id_list) = 32753
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
len of intersection = 1100
len of union = 1100
['tt0454876', 'tt0976051', 'tt0116695', 'tt1072748', 'tt0108656']
len of list1 =  1100
len of list2 =  1100
list1 = all_mv_list_movie_id_list, list2 = all_shot_movie_id_list
----------------------------------------------------------------------------------------------------
len of intersection = 1100
len of union = 1100
['tt0032138', 'tt0035423', 'tt0038650', 'tt0045537', 'tt0047396']
len of list1 =  1100
len of list2 =  1100
list1 = all_mv_list_movie_id_list, list2 = video_info_mv_id_list
----------------------------------------------------------------------------------------------------
len of intersection = 1100
len of union = 8918
['tt2167924', 'tt4557064', 'tt2188885', 'tt3196830', 'tt2075378']
len of list1 =  1100
len of list2 =  8918
list1 = all_mv_list_movie_id_list, list2 = all_annotation_movie_id_list
----------------------------------------------------------------------------------------------------
len of intersection = 1100
len of union = 375359
['tt7204834', 'tt1196338', 'tt0265244', 'tt5889280', 'tt7363368']
len of list1 =  1100
len of list2 =  375359
list1 = all_mv_list_movie_id_list, list2 = all_meta_movie_id_list
----------------------------------------------------------------------------------------------------
len of intersection = 815
len of union = 1100
['tt1144884', 'tt0369339', 'tt0477348', 'tt1193138', 'tt1371111']
len of list1 =  1100
len of list2 =  815
list1 = all_mv_list_movie_id_list, list2 = all_subtitle_movie_id_list
----------------------------------------------------------------------------------------------------
len of intersection = 1077
len of union = 300458
['tt7577374', 'tt0893616', 'tt3877166', 'tt5222740', 'tt0709065']
len of list1 =  1100
len of list2 =  300435
list1 = all_mv_list_movie_id_list, list2 = post4m_id_set_list
----------------------------------------------------------------------------------------------------
len of intersection = 993
len of union = 32860
['tt2308606', 'tt2530672', 'tt4881642', 'tt0465203', 'tt2347174']
len of list1 =  1100
len of list2 =  32753
list1 = all_mv_list_movie_id_list, list2 = trailer_imdb_id_list
----------------------------------------------------------------------------------------------------
len of intersection = 479
len of union = 1100
['tt0113101', 'tt0964517', 'tt0118971', 'tt2140373', 'tt0120255']
len of list1 =  1100
len of list2 =  479
list1 = all_mv_list_movie_id_list, list2 = all_script_movie_id_list
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
len(min_intersection) = 434

```
We can observe that the min intersection trailer_imdb_id_list contains 434 trailers.

So we can download the trailers using youtube-dl.

```
python download_movie.py
```



------
The following is the original README.md file from movienet/movienet-tools


-------



**Updates**

[MovieNet Official Website](http://movienet.site/) is online now!

# Introduction
movienet-tools is an open source movie analysis toolbox based on PyTorch.
It's part of [MovieNet](http://movienet.site/) project maintained by MovieNet Team from [MMLab, CUHK](http://mmlab.ie.cuhk.edu.hk).
And it is also one of [OpenMMLab](https://open-mmlab.github.io/index.html) projects.

## Features
- Basic video processing tools.
- Holistic semantic video feature extractors.
- All-in-one movie info web crawler.

## Installation
Please refer to [INSTALL.md](docs/INSTALL.md) for installation and dataset preparation. Pretrained models and dataset are also explanined here.

## Get Started
Please see [movienet-tools documentation](http://docs.movienet.site/movie-toolbox/tools) for the basic usage.

## Acknowledgement
The structure of ``movienet-tools`` follows that of codebased in [openmmlab](https://github.com/open-mmlab).
The part of character detection are modified from [mmdetection](https://github.com/open-mmlab/mmdetection)
and the part of action feature extraction are modified from [mmaction](https://github.com/open-mmlab/mmaction).
Many thanks to these open-source codebases.

## Citation
If you use MovieNet dataset or this toolbox or benchmarks in your research, please cite this project.
```
@inproceedings{huang2020movie,
	title={MovieNet: A Holistic Dataset for Movie Understanding},
	author={Huang, Qingqiu and Xiong, Yu and Rao, Anyi and Wang, Jiaze and Lin, Dahua},
	booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)}, 
	year={2020}
}
```
