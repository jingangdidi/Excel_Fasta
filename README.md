# Excel_Fasta
Transfer Excel sequence file to Fasta file without whitespace
在将Excel中的残基、基因序列复制为fasta文本序列时，会存在空格，该脚本用于将Excel中的残基、基因序列转为fasta格式文本序列，并去除字符间空格
### 使用
1. 将EF.py与excel文件放在同一路径下
2. 打开终端，输入python EF.py运行脚本，输入Excel文件的名称
3. 在该路径下生成转换的fasta文件。
### Excel中序列格式
使用.xlsx格式，第一行和第二行为表头，不读取，将从第三行开始转换
