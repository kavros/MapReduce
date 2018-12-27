OUTPUT_DIR=/user/s1891388/assignment/task3
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
 -D mapreduce.job.name=s1891388_task3 \
 -D mapred.reduce.tasks=1 \
 -input /data/large/imdb/name.basics.tsv\
 -output $OUTPUT_DIR \
 -mapper mapper.py \
 -combiner reducer.py\
 -reducer reducer.py \
 -file reducer.py\
 -file mapper.py\

hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
cat $OUTPUT_FILE
