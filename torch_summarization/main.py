import sys,os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--do_pre",default='False',type=str)  #是否需要进行preprocess操作
parser.add_argument("--segment_sentence_src",default='False',type=str)  #如进行preprocess操作，是否对source进行分句
parser.add_argument("--segment_sentence_tgt",default='False',type=str)  #如进行preprocess操作，是否对target进行分句

args = parser.parse_args()
arg_dict=args.__dict__

do_pre=arg_dict['do_pre']
segment_sentence_src=arg_dict['segment_sentence_src']
segment_sentence_tgt=arg_dict['segment_sentence_tgt']

from torch_summarization.preprocess import text_segmentate

# 1. 预处理
dummy_document=[{'src':"日前，方舟子发文直指林志颖旗下爱碧丽推销假保健品，引起哗然。调查发现，爱碧丽没有自己的生产加工厂。其胶原蛋白饮品无核心研发，全部代工生产。号称有“逆生长”功效的爱碧丽“梦幻奇迹限量组”售价高达1080元，实际成本仅为每瓶4元！",
                'tgt':'林志颖公司疑涉虚假营销无厂房无研发'},
                {'src':"韩方应对路径可以概括为：企业道歉担责；政府公正不护短；民间祈福关怀。他们深知形象的重要，竭力呵护企业品牌和国家形象。正如有评论，韩国“政府+企业+民众”三位一体式呵护韩国国家形象的“苦心经营”，的确有值得我们借鉴之处。",
                'tgt':'从韩亚航空事故看其应对路径'}]
processed_document=[]
for sample in dummy_document:
    if isinstance(sample['src'],list):
        source=sample['src']
    elif isinstance(sample['src'],str):
        source=[sample['src']]
    else:
        raise Exception('src的值必须为str或由str组成的list')
    if isinstance(sample['tgt'],list):
        target=sample['tgt']
    elif isinstance(sample['tgt'],str):
        target=[sample['tgt']]
    else:
        raise Exception('tgt的值必须为str或由str组成的list')
    
    if do_pre=='True':
        #分句
        if segment_sentence_src=='True':
            newsource=[]
            newsource.extend([text_segmentate(x) for x in source])
            source=newsource
        if segment_sentence_tgt=='True':
            newtarget=[]
            newtarget.extend([text_segmentate(x) for x in target])
            target=newtarget

    processed_document.append({'src':source,'tgt':target})
print(processed_document)


    



# 2. tokenize

# 3. embedding（如果直接使用预训练transformer模型建模的话就不需要，因为预训练模型本身就会训练embedding层）
# 如果直接使用传统的文本表征方式也将划分在本部分：①word2vec（使用gensim） ②sklearn.feature_extraction.text ③其他自定义的文本特征

# 4. 模型构建和运算
## 4.1 无监督
## 4.2 有监督
## 4.2.1 训练、验证、调参
## 4.2.2 推理

# 5. 模型的结果评估