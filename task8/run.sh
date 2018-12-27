OUTPUT_DIR=/user/s1891388/assignment/task8
TEMP_DIR=/user/s1891388/assignment/temp
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR $TEMP_DIR

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
 -D mapreduce.job.name=s1891388_task8 \
 -input /data/large/imdb/title.basics.tsv\
 -input /data/large/imdb/title.ratings.tsv\
 -output $TEMP_DIR \
 -mapper mapper.py \
 -reducer reducer.py \
 -file reducer.py\
 -file mapper.py\

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
-D mapreduce.job.name=s1891388_task8_2 \
-input $TEMP_DIR \
-output $OUTPUT_DIR \
-mapper mapper2.py \
-reducer reducer2.py \
-file mapper2.py \
-file reducer2.py 


hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
cat $OUTPUT_FILE
