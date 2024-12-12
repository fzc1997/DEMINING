import sys
import pysam

# 从标准输入读取和向标准输出写入
bam = pysam.AlignmentFile('-', 'rb')  # 从 stdin 读取 BAM
bam_unique_mis6 = pysam.AlignmentFile('-', "wb", template=bam)  # 向 stdout 写入 BAM

mapq_threshold = 0
n_primary = 0
n_not_xa = 0
n_not_xa_mapq_gt_20 = 0

# 使用缓存提高读取效率
for read in bam.fetch(until_eof=True):
    if read.is_secondary:  # not the primary alignment
        continue
    n_primary += 1
    if read.has_tag('XA'):
        continue
    n_not_xa += 1
    if read.mapping_quality <= mapq_threshold:
        continue
    n_not_xa_mapq_gt_20 += 1
    md_tag = read.get_tag('MD').split()[0]
    if sum(1 for ab in md_tag if ab.islower()) > 6:
        continue
    bam_unique_mis6.write(read)

bam_unique_mis6.close()
bam.close()

sys.stderr.write(f"n_primary: {n_primary}\n")
sys.stderr.write(f"n_not_xa: {n_not_xa}\n")
sys.stderr.write(f"n_not_xa_mapq_gt_20: {n_not_xa_mapq_gt_20}\n")
