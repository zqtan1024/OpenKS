# from openks.loaders import loader_config, SourceType, FileType, Loader
from openks.models import OpenKSModel

# 列出已加载模型
OpenKSModel.list_modules()

# 算法模型选择配置
args = {
        "--stvgbert": True
        # "--device": 'cpu'
    }
platform = 'PyTorch'
executor = 'STVGBert'
model = 'pytorch-SpatioTemporalVisualGrounding'
print("根据配置，使用 {} 框架，{} 执行器训练 {} 模型。".format(platform, executor, model))
print("-----------------------------------------------")
# 模型训练
executor = OpenKSModel.get_module(platform, executor)

text_ner = executor(args=args)
text_ner.run(mode="train")
print("-----------------------------------------------")
