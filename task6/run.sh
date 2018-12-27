OUTPUT_DIR=/user/s1891388/assignment/task6
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
 -D mapreduce.job.name=s1891388_task6 \
 -D mapred.reduce.tasks=1 \
 -input /data/large/imdb/title.ratings.tsv\
 -output $OUTPUT_DIR \
 -mapper mapper.py \
 -reducer reducer.py \
 -combiner combiner.py\
 -file reducer.py\
 -file mapper.py\
 -file combiner.py\


hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
cat $OUTPUT_FILE
