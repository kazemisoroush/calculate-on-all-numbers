# Hadoop number calculation project

This project calculates total count, minimum, maximum, sum and sum-squared of input files.

Compile using
```sh
$ mvn install
```

Run the job using
```sh
$ hadoop jar ./target/CalculateAll.jar -r <count> -m <count> dataSet.txt
```
