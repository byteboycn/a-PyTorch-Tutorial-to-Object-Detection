import utils
from utils import create_data_lists
import torch

if __name__ == '__main__':
    create_data_lists(voc07_path='/Users/nature/AI/dataset/VOC/VOCtrainval_06-Nov-2007/VOC2007',
                      voc07_test_path='/Users/nature/AI/dataset/VOC/VOCtest_06-Nov-2007/VOC2007',
                      voc12_path='/Users/nature/AI/dataset/VOC/VOCtrainval_11-May-2012/VOC2012',
                      output_folder='/Users/nature/AI/dataset/VOC/output')

