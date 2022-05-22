import sys,os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from torch_summarization.preprocess import text_segmentate

print(text_segmentate('一个，完整的句子。',1,'，。'))