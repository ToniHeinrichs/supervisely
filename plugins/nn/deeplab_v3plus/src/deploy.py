# coding: utf-8

import cv2

import supervisely_lib as sly
from supervisely_lib.nn.hosted.deploy import ModelDeploy
from inference import DeeplabSingleImageApplier


def main():
    model_deploy = ModelDeploy(model_applier_cls=DeeplabSingleImageApplier)
    model_deploy.run()


if __name__ == '__main__':
    cv2.setNumThreads(0)
    sly.main_wrapper('DEEPLAB_SERVICE', main)
