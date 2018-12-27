OUTPUT_DIR=/user/s1891388/assignment/task10
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
 -D num.key.fields.for.partition=1\
 -D stream.num.map.output.key.fields=2\
 -D mapreduce.job.name=s1891388_task10 \
 -input /data/large/imdb/name.basics.tsv\
 -input /data/large/imdb/title.basics.tsv\
 -output $OUTPUT_DIR \
 -mapper mapper.py \
 -reducer reducer.py\
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner\
 -file reducer.py\
 -file mapper.py\


hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
cat $OUTPUT_FILE
