this repo is fork from [movienet/movienet-tools](https://github.com/movienet/movienet-tools)

this repo aims to provide some data processing tools for movienet.

# download trailers
## download one video trailer

```bash
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
