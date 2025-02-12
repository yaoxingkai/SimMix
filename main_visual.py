from dig.auggraph.method.SMixup import mixup_visual
import numpy as np
import torch
from torch.nn import functional as F

device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device("cpu")


GMNET_conf = {"nlayers": 6, "nhidden": 256, "bs": 256, "lr": 0.001, "epochs": 500}
# SupCon_conf = {"bs": 1024, "lr": 0.001, "epochs": 50}
# model = mixup_visual.smixup(data_root_path="dataset/", dataset="IMDBB", GMNET_conf = GMNET_conf, SupCon_conf=SupCon_conf)
# model.train_test(batch_size=256, cls_model="GIN", cls_nlayers=4, cls_hidden=32, cls_dropout=0.5, cls_lr=0.001, cls_epochs=300, alpha1=1, alpha2=1, ckpt_path="ckpt_path/IMDBB/GIN")


# SupCon_conf = {"bs": 1024, "lr": 0.01, "epochs": 500}
# model = mixup_visual.smixup(data_root_path="dataset/", dataset="PROTEINS", GMNET_conf = GMNET_conf, SupCon_conf=SupCon_conf)
# model.train_test(batch_size=256, cls_model="GIN", cls_nlayers=4, cls_hidden=32, cls_dropout=0.1, cls_lr=0.001, cls_epochs=300, alpha1=1, alpha2=1, ckpt_path="ckpt_path/PROTEINS")


SupCon_conf = {"bs": 1024, "lr": 0.01, "epochs": 500}
model = mixup_visual.smixup(data_root_path="dataset/", dataset="NCI1", GMNET_conf = GMNET_conf, SupCon_conf=SupCon_conf)
model.train_test(batch_size=256, cls_model="GIN", cls_nlayers=4, cls_hidden=32, cls_dropout=0.1, cls_lr=0.001, cls_epochs=500, alpha1=1, alpha2=1, ckpt_path="ckpt_path/NCI1")


# SupCon_conf = {"bs": 64, "lr": 0.01, "epochs": 500}
# model = mixup_visual.smixup(data_root_path="dataset/", dataset="REDDITB", GMNET_conf = GMNET_conf, SupCon_conf=SupCon_conf)
# model.train_test(batch_size=16, cls_model="GIN", cls_nlayers=4, cls_hidden=32, cls_dropout=0.1, cls_lr=0.01, cls_epochs=500, alpha1=1, alpha2=1, ckpt_path="ckpt_path/REDDITB")


# SupCon_conf = {"bs": 1024, "lr": 0.01, "epochs": 500}
# model = mixup_visual.smixup(data_root_path="dataset/", dataset="IMDBM", GMNET_conf = GMNET_conf, SupCon_conf=SupCon_conf)
# model.train_test(batch_size=256, cls_model="GIN", cls_nlayers=4, cls_hidden=32, cls_dropout=0.1, cls_lr=0.001, cls_epochs=300, alpha1=1, alpha2=1, ckpt_path="ckpt_path/IMDBM")


# SupCon_conf = {"bs": 512, "lr": 0.01, "epochs": 500}
# model = mixup_visual.smixup(data_root_path="dataset/", dataset="REDDITM5", GMNET_conf = GMNET_conf, SupCon_conf=SupCon_conf)
# model.train_test(batch_size=16, cls_model="GIN", cls_nlayers=4, cls_hidden=32, cls_dropout=0.5, cls_lr=0.01, cls_epochs=500, alpha1=1, alpha2=1, ckpt_path="ckpt_path/REDDITM5/GIN")
 