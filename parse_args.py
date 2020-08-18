#!/usr/env/bin python3
import argparse
import os
import random


def parse_args():
    parser = argparse.ArgumentParser()
    #生成图片数量
    parser.add_argument('--num_img', type=int, default=20000, help="Number of images to generate")
    #图片中的字符数量
    parser.add_argument('--length', type=int, default=12,
                        help='Chars(chn) or words(eng) in a image. For eng corpus mode, default length is 3')

    parser.add_argument('--clip_max_chars', action='store_true', default=False,
                        help='For training a CRNN model, max number of chars in an image'
                             'should less then the width of last CNN layer.')
    #图片高度，图片宽度
    parser.add_argument('--img_height', type=int, default=32)
    parser.add_argument('--img_width', type=int, default=280,
                        help="If 0, output images will have different width")
    #图片中允许出现的字符
    parser.add_argument('--chars_file', type=str, default='./data/chars/char_bak.txt',
                        help='Chars allowed to be appear in generated images.')

    parser.add_argument('--config_file', type=str, default='./configs/default.yaml',
                        help='Set the parameters when rendering images')
    #字体 chn.txt/eng.txt/zdy.txt
    parser.add_argument('--fonts_list', type=str, default='./data/fonts_list/zdy.txt',
                        help='Fonts file path to use')
    parser.add_argument('--bg_dir', type=str, default='./data/bg',
                        help="Some text images(according to your config in yaml file) will"
                             "use pictures in this folder as background")
    #当corpus_mode是chn或eng时，图片中文字将直接从corpus中的文件中读取
    parser.add_argument('--corpus_dir', type=str, default="./data/corpus",
                        help='When corpus_mode is chn or eng, text on image will randomly selected from corpus.'
                             'Recursively find all txt file in corpus_dir')
    #选random时，按字典字符随机生成。选chn或eng时，按生成的字符序列读取
    parser.add_argument('--corpus_mode', type=str, default='random', choices=['random', 'chn', 'eng', 'list'],
                        help='Different corpus type have different load/get_sample method'
                             'random: random pick chars from chars file'
                             'chn: pick continuous chars from corpus'
                             'eng: pick continuous words from corpus, space is included in label')
    #图片生成目录
    # parser.add_argument('--output_dir', type=str, default='./output', help='Images save dir')    #当前目录
    parser.add_argument('--output_dir', type=str, default='../Train/data/lv_make_image', help='Images save dir')      #ocr训练目录
    #图片生成的文件夹,         **需要选择train/test**
    parser.add_argument('--tag', type=str, default='train', help='output images are saved under output_dir/{tag} dir')   #train/test

    parser.add_argument('--debug', action='store_true', default=False, help="output uncroped image")

    parser.add_argument('--viz', action='store_true', default=False)

    parser.add_argument('--strict', action='store_true', default=False,
                        help="check font supported chars when generating images")

    parser.add_argument('--gpu', action='store_true', default=False, help="use CUDA to generate image")

    parser.add_argument('--num_processes', type=int, default=None,
                        help="Number of processes to generate image. If None, use all cpu cores")

    flags, _ = parser.parse_known_args()
    flags.save_dir = os.path.join(flags.output_dir, flags.tag)

    if os.path.exists(flags.bg_dir):
        num_bg = len(os.listdir(flags.bg_dir))
        flags.num_bg = num_bg

    if not os.path.exists(flags.save_dir):
        os.makedirs(flags.save_dir)

    if flags.num_processes == 1:
        parser.error("num_processes min value is 2")

    return flags


if __name__ == '__main__':
    args = parse_args()
    print(args.corpus_dir)
